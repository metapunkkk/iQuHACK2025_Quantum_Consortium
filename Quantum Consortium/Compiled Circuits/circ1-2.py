from bloqade import move
from kirin.passes import aggressive
from iquhack_scoring import MoveScorer
from math import pi



@move.vmove
def problem1part2():
    # Initialization (instruction id 0):
    q = move.NewQubitRegister(3)
    state = move.Init(qubits=[q[0], q[1], q[2]], indices=[2, 1, 0])

    # For qubits in storage (indices ['0', '1', '2']), move to gate
    state.gate[[0, 1, 2]] = move.Move(state.storage[[0, 1, 2]])
    # Apply LocalRz with phi=1.5707963267948966 on indices ['0', '1', '2']
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[0, 1, 2])
    # Apply LocalXY with x_exponent=3.9269908169872414 and axis_phase_exponent=-1.5707963267948966 on indices ['0', '1', '2']
    state = move.LocalXY(atom_state=state, x_exponent=3.9269908169872414, axis_phase_exponent=-1.5707963267948966, indices=[0, 1, 2])
    state = move.LocalRz(atom_state=state,phi=2.356194490192345,indices=[0, 1, 2])

    # Rearrangement job (id 2):
    #  Move (storage -> gate): transferring qubits from ['0', '1'] to ['0', '0']
    state.gate[[0, 0]] = move.Move(state.storage[[0, 1]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [1, 0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1]

    # Rydberg gate (id 0): between qubit 1 and 2
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q1 and q2

    # Apply LocalRz with phi=1.0471975510918778 on indices ['0']
    state = move.LocalRz(atom_state=state,phi=1.0471975510918778,indices=[0])
    # Apply LocalXY with x_exponent=5.605836630753276 and axis_phase_exponent=-1.5707963267948966 on indices ['0']
    state = move.LocalXY(atom_state=state, x_exponent=5.605836630753276, axis_phase_exponent=-1.5707963267948966, indices=[0])
    state = move.LocalRz(atom_state=state,phi=0.67734867642631,indices=[0])

    # Rydberg gate (id 1): between qubit 1 and 2
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q1 and q2

    # Apply LocalRz with phi=1.5707963267948966 on indices ['0', '0']
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[0, 0])
    # Apply LocalXY with x_exponent=1.4627468398237582 and axis_phase_exponent=-1.5707963267948966 on indices ['0', '0']
    state = move.LocalXY(atom_state=state, x_exponent=1.4627468398237582, axis_phase_exponent=-1.5707963267948966, indices=[0, 0])
    state = move.LocalRz(atom_state=state,phi=2.2481450032212065,indices=[0, 0])

    # Rearrangement job (id 7):
    #  Move (gate -> storage): transferring qubits from ['0'] to ['0']
    state.storage[[0]] = move.Move(state.gate[[0]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 8):
    #  Move (storage -> gate): transferring qubits from ['2'] to ['0']
    state.gate[[0]] = move.Move(state.storage[[2]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 2): between qubit 0 and 1
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q1

    # Apply LocalRz with phi=0.7853981633974483 on indices ['0']
    state = move.LocalRz(atom_state=state,phi=0.7853981633974483,indices=[0])
    # Apply LocalXY with x_exponent=4.71238898038469 and axis_phase_exponent=-1.5707963267948966 on indices ['0']
    state = move.LocalXY(atom_state=state, x_exponent=4.71238898038469, axis_phase_exponent=-1.5707963267948966, indices=[0])
    state = move.LocalRz(atom_state=state,phi=0.7853981633974483,indices=[0])

    # Rearrangement job (id 11):
    #  Move (gate -> storage): transferring qubits from ['0'] to ['1']
    state.storage[[1]] = move.Move(state.gate[[0]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 12):
    #  Move (storage -> gate): transferring qubits from ['0'] to ['0']
    state.gate[[0]] = move.Move(state.storage[[0]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 3): between qubit 0 and 2
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q2

    # Apply LocalRz with phi=0.7853981633974483 on indices ['0']
    state = move.LocalRz(atom_state=state,phi=0.7853981633974483,indices=[0])
    # Apply LocalXY with x_exponent=1.5707963267948966 and axis_phase_exponent=-1.5707963267948966 on indices ['0']
    state = move.LocalXY(atom_state=state, x_exponent=1.5707963267948966, axis_phase_exponent=-1.5707963267948966, indices=[0])
    state = move.LocalRz(atom_state=state,phi=4.71238898038469,indices=[0])

    # Rearrangement job (id 15):
    #  Move (gate -> storage): transferring qubits from ['0'] to ['0']
    state.storage[[0]] = move.Move(state.gate[[0]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 16):
    #  Move (storage -> gate): transferring qubits from ['1'] to ['0']
    state.gate[[0]] = move.Move(state.storage[[1]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 4): between qubit 0 and 1
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q1

    # Apply LocalRz with phi=0.7853981633974483 on indices ['0']
    state = move.LocalRz(atom_state=state,phi=0.7853981633974483,indices=[0])
    # Apply LocalXY with x_exponent=1.5707963267948966 and axis_phase_exponent=-1.5707963267948966 on indices ['0']
    state = move.LocalXY(atom_state=state, x_exponent=1.5707963267948966, axis_phase_exponent=-1.5707963267948966, indices=[0])
    state = move.LocalRz(atom_state=state,phi=4.71238898038469,indices=[0])

    # Rearrangement job (id 19):
    #  Move (gate -> storage): transferring qubits from ['0'] to ['1']
    state.storage[[1]] = move.Move(state.gate[[0]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 20):
    #  Move (storage -> gate): transferring qubits from ['0'] to ['0']
    state.gate[[0]] = move.Move(state.storage[[0]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 5): between qubit 0 and 2
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q2

    # Apply LocalRz with phi=1.5707963267948966 on indices ['0', '0']
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[0, 0])

    # Rearrangement job (id 23):
    #  Move (gate -> storage): transferring qubits from ['0'] to ['0']
    state.storage[[0]] = move.Move(state.gate[[0]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 24):
    #  Move (storage -> gate): transferring qubits from ['1'] to ['0']
    state.gate[[0]] = move.Move(state.storage[[1]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 6): between qubit 1 and 2
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q1 and q2

    # Apply LocalRz with phi=3.141592653589793 on indices ['0', '0']
    state = move.LocalRz(atom_state=state,phi=3.141592653589793,indices=[0, 0])

    # Rearrangement job (id 27):
    #  Move (gate -> storage): transferring qubits from ['0', '0'] to ['1', '2']
    state.storage[[1, 2]] = move.Move(state.gate[[0, 0]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0, 1]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1]

    move.Execute(state)

expected_qasm = """OPENQASM 2.0;
include "qelib1.inc";


// Qubits: [q(0), q(1), q(2)]
qreg q[3];


ccx q[0],q[1],q[2];

"""

aggressive.Fold(move.vmove)(problem1part2)
MoveScorer(problem1part2, expected_qasm=expected_qasm).animate()
print(MoveScorer(problem1part2, expected_qasm=expected_qasm).score())