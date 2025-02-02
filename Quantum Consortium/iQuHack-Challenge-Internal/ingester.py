import numpy as np
import re

def qubit_mapper(json_list, qasm_lists):
    qasm_global_index = 0
    qasm_set = set()
    for x in range(len(qasm_lists)):
        qasm_set.add(x)
    for gate in json_list:
        for qasm_qubit_index,qasm_list in enumerate(qasm_lists):
            if qasm_global_index > qasm_list.length() or gate != qasm_list[qasm_global_index]:
                qasm_set.remove(qasm_qubit_index)
        qasm_global_index += 1
    return qasm_set

def qasm_lists(file_path):
    qubit_gates = {}  # Dictionary to track gates per qubit

    with open(file_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        
        # Ignore comments and metadata
        if line.startswith("//") or line.startswith("OPENQASM") or "qreg" in line or "creg" in line:
            continue

        # Extract gate and qubit(s)
        match = re.match(r"(\w+)\s+(q\[(\d+)\])", line)
        
        if match:
            gate, qubit_label, qubit_index = match.groups()
            qubit_index = int(qubit_index)

            # Append gate to the corresponding qubit list
            if qubit_index not in qubit_gates:
                qubit_gates[qubit_index] = []
            qubit_gates[qubit_index].append(gate)

    # Convert to a 2D array (list of lists, since qubits may have different lengths)
    max_qubit = max(qubit_gates.keys()) if qubit_gates else 0
    qubit_list = [qubit_gates.get(i, []) for i in range(max_qubit + 1)]

    return qubit_list

import cirq
import numpy as np

def u3_to_phased_xpow(theta, phi, lamb):
    """
    Converts a QASM U3(θ, φ, λ) gate to Cirq's PhasedXPowGate and additional Z rotations.
    
    U3(θ, φ, λ) = RZ(φ) * PhasedXPowGate(φ/π, θ/π) * RZ(λ)
    
    Parameters:
    - theta: Rotation angle around the XZ plane.
    - phi: Initial Z rotation.
    - lamb: Final Z rotation.
    
    Returns:
    - List of Cirq gates equivalent to U3(θ, φ, λ).
    """
    # Convert parameters to Cirq's format
    phase_exponent = phi / np.pi
    x_exponent = theta / np.pi
    
    # Create the equivalent Cirq gate sequence
    gates = []
    if phi != 0:
        gates.append(cirq.rz(phi))
    gates.append(cirq.PhasedXPowGate(phase_exponent=phase_exponent, exponent=x_exponent))
    if lamb != 0:
        gates.append(cirq.rz(lamb))
    
    return gates

# Example usage
theta, phi, lamb = np.pi / 3, np.pi / 4, np.pi / 6
gates = u3_to_phased_xpow(theta, phi, lamb)
print(gates)

import cirq
import numpy as np

def u3_to_phasedxpow_rz(theta, phi, lam):
    rz_gate = cirq.rz(phi + lam)
    phased_xpow_gate = cirq.PhasedXPowGate(phase_exponent=0.5, exponent=theta / np.pi)
    return [phased_xpow_gate, rz_gate]

# Example usage
q = cirq.LineQubit(0)
theta, phi, lam = np.pi / 3, np.pi / 4, np.pi / 6
circuit = cirq.Circuit(u3_to_phasedxpow_rz(theta, phi, lam)[0](q), u3_to_phasedxpow_rz(theta, phi, lam)[1](q))
print(circuit)

