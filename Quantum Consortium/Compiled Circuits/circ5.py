from bloqade import move
from kirin.passes import aggressive
from iquhack_scoring import MoveScorer
from math import pi



@move.vmove
def problem5():
    # Initialization (instruction id 0):
    q = move.NewQubitRegister(7)
    state = move.Init(qubits=[q[0], q[1], q[2], q[3], q[4], q[5], q[6]], indices=[5, 6, 0, 4, 1, 3, 2])

    # For qubits in storage (indices ['0', '1', '3', '4', '5', '6']), move to gate
    state.gate[[0, 1, 3, 4, 5, 6]] = move.Move(state.storage[[0, 1, 3, 4, 5, 6]])
    # Apply LocalRz with phi=1.5707963267948966 on indices ['0', '1', '3', '4', '5', '6']
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[0, 1, 3, 4, 5, 6])

    # Rearrangement job (id 2):
    #  Move (storage -> gate): transferring qubits from ['0', '1', '2', '3', '5', '6'] to ['0', '0', '2', '3', '3', '5']
    state.gate[[0, 0, 2, 3, 3, 5]] = move.Move(state.storage[[0, 1, 2, 3, 5, 6]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [4, 5, 0, 1, 3, 2]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1, 2, 3, 4, 5]

    # Rydberg gate (id 0): between qubit 0 and 1
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q1
    # Rydberg gate (id 1): between qubit 2 and 4
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q2 and q4
    # Rydberg gate (id 3): between qubit 5 and 6
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q5 and q6

    # Apply LocalRz with phi=3.141592653589793 on indices ['0', '0', '1', '2', '2']
    state = move.LocalRz(atom_state=state,phi=3.141592653589793,indices=[0, 0, 1, 2, 2])
    # Apply LocalXY with x_exponent=1.5707963267948966 and axis_phase_exponent=-1.5707963267948966 on indices ['0', '0', '1', '2', '2']
    state = move.LocalXY(atom_state=state, x_exponent=1.5707963267948966, axis_phase_exponent=-1.5707963267948966, indices=[0, 0, 1, 2, 2])
    state = move.LocalRz(atom_state=state,phi=4.71238898038469,indices=[0, 0, 1, 2, 2])

    # Rearrangement job (id 5):
    #  Move (gate -> storage): transferring qubits from ['0', '2', '5'] to ['0', '2', '5']
    state.storage[[0, 2, 5]] = move.Move(state.gate[[0, 2, 5]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [2, 0, 1]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1, 2]

    # Rearrangement job (id 6):
    #  Move (storage -> gate): transferring qubits from ['0'] to ['5']
    state.gate[[5]] = move.Move(state.storage[[0]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 7):
    #  Move (storage -> gate): transferring qubits from ['2', '4'] to ['0', '2']
    state.gate[[0, 2]] = move.Move(state.storage[[2, 4]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [1, 0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1]

    # Rydberg gate (id 2): between qubit 0 and 2
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q2
    # Rydberg gate (id 4): between qubit 4 and 6
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q4 and q6
    # Rydberg gate (id 5): between qubit 3 and 5
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q3 and q5

    # Apply LocalRz with phi=3.141592653589793 on indices ['0', '0', '1', '1']
    state = move.LocalRz(atom_state=state,phi=3.141592653589793,indices=[0, 0, 1, 1])

    # Rearrangement job (id 10):
    #  Move (gate -> storage): transferring qubits from ['0', '2', '3'] to ['0', '2', '4']
    state.storage[[0, 2, 4]] = move.Move(state.gate[[0, 2, 3]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [2, 1, 0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1, 2]

    # Rearrangement job (id 11):
    #  Move (storage -> gate): transferring qubits from ['2', '5'] to ['0', '2']
    state.gate[[0, 2]] = move.Move(state.storage[[2, 5]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [1, 0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1]

    # Rearrangement job (id 12):
    #  Move (storage -> gate): transferring qubits from ['0'] to ['3']
    state.gate[[3]] = move.Move(state.storage[[0]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 6): between qubit 3 and 4
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q3 and q4
    # Rydberg gate (id 8): between qubit 1 and 5
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q1 and q5
    # Rydberg gate (id 9): between qubit 2 and 6
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q2 and q6

    # Apply LocalXY with x_exponent=1.5707963267948966 and axis_phase_exponent=-1.5707963267948966 on indices ['0', '0', '1', '1', '2']
    state = move.LocalXY(atom_state=state, x_exponent=1.5707963267948966, axis_phase_exponent=-1.5707963267948966, indices=[0, 0, 1, 1, 2])
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[0, 0, 1, 1, 2])

    # Rearrangement job (id 15):
    #  Move (gate -> storage): transferring qubits from ['0', '3', '3', '5'] to ['0', '2', '3', '5']
    state.storage[[0, 2, 3, 5]] = move.Move(state.gate[[0, 3, 3, 5]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [3, 0, 1, 2]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1, 2, 3]

    # Rearrangement job (id 16):
    #  Move (storage -> gate): transferring qubits from ['4'] to ['0']
    state.gate[[0]] = move.Move(state.storage[[4]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 17):
    #  Move (storage -> gate): transferring qubits from ['3'] to ['3']
    state.gate[[3]] = move.Move(state.storage[[3]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 7): between qubit 0 and 3
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q3
    # Rydberg gate (id 10): between qubit 1 and 6
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q1 and q6

    # Apply LocalRz with phi=1.5707963267948966 on indices ['0', '1', '1']
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[0, 1, 1])

    # Rearrangement job (id 20):
    #  Move (gate -> storage): transferring qubits from ['0', '0', '2', '3'] to ['1', '3', '4', '6']
    state.storage[[1, 3, 4, 6]] = move.Move(state.gate[[0, 0, 2, 3]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [1, 2, 0, 3]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1, 2, 3]

    move.Execute(state)

expected_qasm = """OPENQASM 2.0;
include "qelib1.inc";


// Qubits: [q(0), q(1), q(2), q(3), q(4), q(5), q(6)]
qreg q[7];


h q[1];
h q[2];
h q[3];
cx q[6],q[5];
cx q[1],q[0];
cx q[2],q[4];
cx q[3],q[5];
cx q[2],q[0];
cx q[1],q[5];
cx q[6],q[4];
cx q[2],q[6];
cx q[3],q[4];
cx q[3],q[0];
cx q[1],q[6];
"""

aggressive.Fold(move.vmove)(problem5)
MoveScorer(problem5, expected_qasm=expected_qasm).animate()
print(MoveScorer(problem5, expected_qasm=expected_qasm).score())