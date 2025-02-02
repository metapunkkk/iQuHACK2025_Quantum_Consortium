import json
import argparse
import numpy as np


def map_loc(loc):
    """
    Map a location list [a,b,c,d] to a single integer index.
    (This example uses a simple linear combination; adjust as needed.)
    """
    return loc[0] + loc[1] + loc[2] + loc[3]


def translate_init(instr):
    """
    Translate an 'init' instruction.
    Uses the init_locs field to set the qubit register size and the initial indices.
    """
    n = len(instr["init_locs"])
    # Compute indices from each location using map_loc.
    indices = [str(loc[3]) for loc in instr["init_locs"]]
    qubits = ", ".join("q[{}]".format(i) for i in range(n))
    lines = [
        "    # Initialization (instruction id {}):".format(instr.get("id", "init")),
        "    q = move.NewQubitRegister({})".format(n),
        "    state = move.Init(qubits=[{}], indices=[{}])".format(qubits, ", ".join(indices))
    ]
    return lines


def translate_1qGate(instr):
    """
    Translate a 1qGate instruction.

    For each location in instr["locs"], which is a list of 4-integer lists:
      - If the second entry (index 1) is greater than 0, the qubit is assumed to already be in the gate zone.
      - If the second entry is 0, then the qubit is in storage and must first be moved to the gate zone.

    The active index for the qubit is taken from the fourth entry (index 3).
    The parameters for the LocalXY gate (x_exponent and axis_phase_exponent)
    are taken from the first two entries of the first list in "params_for_all_qubits".

    The routine groups all qubits that need to be moved and then applies a single LocalXY operation
    on all qubits in the gate zone.
    """
    lines = []
    # Get the gate parameters; default to (1.0, 1.0) if not provided.
    params = instr.get("params_for_all_qubits", [[1.0, 1.0, 0.0]])[0]
    #x_exponent = params[0]
    #axis_phase_exponent = params[1]
    z1t = params[0]
    rxt = params[1]
    z2t = params[2]

    # Lists for qubit indices.
    # "storage_to_gate" collects qubits that are in storage (loc[1] == 0) and need moving.
    # "gate_already" collects qubits already in the gate zone (loc[1] > 0).
    storage_to_gate = []
    gate_already = []

    for loc in instr.get("locs", []):
        # loc is expected to be a list of 4 integers: [entry0, entry1, entry2, entry3]
        active_index = str(loc[3])
        if loc[1] > 0:
            gate_already.append(active_index)
        elif loc[1] == 0:
            storage_to_gate.append(active_index)
        else:
            lines.append("    # Warning: Unexpected location value: {}".format(loc))

    # First, if any qubits are in storage, move them from storage to gate.
    if storage_to_gate:
        storage_to_gate_sorted = sorted(storage_to_gate, key=lambda s: int(s))
        lines.append("    # For qubits in storage (indices {}), move to gate".format(storage_to_gate_sorted))
        lines.append("    state.gate[[{}]] = move.Move(state.storage[[{}]])".format(
            ", ".join(storage_to_gate_sorted), ", ".join(storage_to_gate_sorted)))


    # Now, all qubits should be in the gate zone.
    # Merge the indices (maintaining ascending order).
    all_gate_indices = gate_already + storage_to_gate
    # Sort numerically if desired.
    all_gate_indices_sorted = sorted(all_gate_indices, key=lambda s: int(s))

    #state = move.LocalRz(atom_state=state,phi=0.5,indices=[3])
    if abs(z1t) > 1e-6:
        lines.append("    # Apply LocalRz with phi={} on indices {}".format(float(z1t), all_gate_indices_sorted))
        lines.append("    state = move.LocalRz(atom_state=state,phi={},indices=[{}])". \
                     format(float(z1t), ", ".join(all_gate_indices_sorted)))
    if abs(rxt) > 1e-6:
        lines.append("    # Apply LocalXY with x_exponent={} and axis_phase_exponent={} on indices {}".
                     format(float(rxt),-float(np.pi/2), all_gate_indices_sorted))
        lines.append("    state = move.LocalXY(atom_state=state, x_exponent={}, axis_phase_exponent={}, indices=[{}])". \
                     format(float(rxt),-float(np.pi/2), ", ".join(all_gate_indices_sorted)))
    if abs(z2t) > 1e-6:
        lines.append("    state = move.LocalRz(atom_state=state,phi={},indices=[{}])". \
                     format(float(z2t), ", ".join(all_gate_indices_sorted)))

    return lines

def translate_rydberg(instr):
    """
    Translate a rydberg (two-qubit) gate instruction.
    Here we assume a placeholder mapping to move.GlobalCZ.
    """
    lines = []
    for gate in instr.get("gates", []):
        q0 = gate.get("q0")
        q1 = gate.get("q1")
        lines.append("    # Rydberg gate (id {}): between qubit {} and {}".format(gate.get("id"), q0, q1))
        lines.append("    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q{} and q{}".format(q0, q1))
    return lines


def translate_rearrangeJob(instr):
    """
    For each begin location in instr["begin_locs"]:
      - If its second element (index 1) is > 0, then that qubit is in the gate region,
        and the move is from gate to storage.
      - if its second element is 0, then that qubit is in storage,
        and the move is from storage to gate.

    The fourth element of each location is used as the active index.
    Qubits that move in the same direction are grouped together and moved in a singl move statement.

    Additional sub–instructions (e.g. activate/deactivate) are output as comments.
    """
    lines = []
    lines.append("    # Rearrangement job (id {}):".format(instr.get("id")))

    begin_locs = instr.get("begin_locs", [])
    end_locs = instr.get("end_locs", [])
    if not begin_locs or not end_locs or len(begin_locs) != len(end_locs):
        lines.append("    #  Error: Missing or mismatched begin_locs and end_locs")
        return lines

    # prepare groups for moves:
    storage_to_gate_source = []
    storage_to_gate_dest = []
    gate_to_storage_source = []
    gate_to_storage_dest = []

    # Iterate over each pair of begin/end locations.
    for b_loc, e_loc in zip(begin_locs, end_locs):
        # b_loc[1] determines which zone the qubit starts in:
        #   if 0, then it's in storage (and will be moved to gate);
        #   if > 0, then it's in the gate (and will be moved to storage).
        if b_loc[1] == 0:
            # Qubit is in storage -> moving to gate.
            spacing = 0
            storage_to_gate_source.append(str(b_loc[3]))
            if e_loc[1] > 0 and e_loc[3] > 0:
                spacing = (e_loc[1]*e_loc[3]) + 1
            storage_to_gate_dest.append(str(spacing))
        elif b_loc[1] > 0:
            # Qubit is in gate -> moving to storage.
            spacing = 0
            if b_loc[3] > 0:
                spacing = (b_loc[1]*b_loc[3]) + 1
            gate_to_storage_source.append(str(spacing))
            gate_to_storage_dest.append(str(e_loc[3]))
        else:
            lines.append("    #  Warning: Unexpected begin location value: {}".format(b_loc))

    storage_to_gate_source.sort()
    storage_to_gate_dest.sort()
    gate_to_storage_source.sort()
    gate_to_storage_dest.sort()


    # It is assumed that the indices are already in ascending order.
    # Emit a single move statement for all qubits moving from storage to gate.
    if storage_to_gate_source:
        lines.append("    #  Move (storage -> gate): transferring qubits from {} to {}".
                     format(storage_to_gate_source, storage_to_gate_dest))
        lines.append("    state.gate[[{}]] = move.Move(state.storage[[{}]])  # storage to gate move". \
                     format(", ".join(storage_to_gate_dest), ", ".join(storage_to_gate_source)))

    # Emit a single move statement for all qubits moving from gate to storage.
    if gate_to_storage_source:
        lines.append("    #  Move (gate -> storage): transferring qubits from {} to {}".
                     format(gate_to_storage_source, gate_to_storage_dest))
        lines.append("    state.storage[[{}]] = move.Move(state.gate[[{}]])  # gate to storage move". \
                     format(", ".join(gate_to_storage_dest), ", ".join(gate_to_storage_source)))

    # Process any sub–instructions for additional context (e.g. activate/deactivate steps)
    for sub_inst in instr.get("insts", []):
        typ = sub_inst.get("type")
        if typ == "activate":
            lines.append(
                "    #  Activate: row_id: {}, col_id: {}".format(sub_inst.get("row_id"), sub_inst.get("col_id")))
        elif typ == "deactivate":
            lines.append(
                "    #  Deactivate: row_id: {}, col_id: {}".format(sub_inst.get("row_id"), sub_inst.get("col_id")))
        else:
            lines.append("    #  (Sub-instruction type '{}' not specifically handled)".format(typ))

    return lines


def translate_instruction(instr):
    """
    Dispatch a JSON instruction by its type.
    """
    typ = instr.get("type")
    if typ == "init":
        return translate_init(instr)
    elif typ == "1qGate":
        return translate_1qGate(instr)
    elif typ == "rydberg":
        return translate_rydberg(instr)
    elif typ == "rearrangeJob":
        return translate_rearrangeJob(instr)
    else:
        return ["    # Instruction type '{}' not supported.".format(typ)]


def translate_json(qasm_json):
    """
    Given the loaded JSON (with fields "name", "instructions", etc.),
    generate the Bloqade code as a string.
    """
    lines = []
    # Header: import the Bloqade API.
    lines.append("from bloqade import move")
    lines.append("")
    # Use the JSON "name" field as the function name (or default to main).
    func_name = qasm_json.get("name", "main")
    lines.append("@move.vmove")
    lines.append("def {}():".format(func_name))
    # Process instructions in order.
    for instr in qasm_json.get("instructions", []):
        instr_lines = translate_instruction(instr)
        lines.extend(instr_lines)
        lines.append("")  # add a blank line between instructions
    # Final execution call.
    lines.append("    move.Execute(state)")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Translate QASM JSON to Bloqade code.")
    parser.add_argument("input", help="Input JSON file with QASM instructions")
    parser.add_argument("output", help="Output Python file for Bloqade code")
    args = parser.parse_args()

    # Load the input JSON.
    with open(args.input, "r") as f:
        qasm_json = json.load(f)

    # Translate to Bloqade code.
    output_code = translate_json(qasm_json)

    # Write out the resulting code.
    with open(args.output, "w") as f:
        f.write(output_code)

    print("Generated Bloqade code written to", args.output)


if __name__ == "__main__":
    main()