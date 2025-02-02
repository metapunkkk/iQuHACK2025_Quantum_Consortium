from bloqade import move
from kirin.passes import aggressive
from iquhack_scoring import MoveScorer
from math import pi



@move.vmove
def problem4():
    # Initialization (instruction id 0):
    q = move.NewQubitRegister(9)
    state = move.Init(qubits=[q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8]], indices=[2, 3, 1, 6, 7, 8, 4, 5, 0])

    # For qubits in storage (indices ['3', '1', '6', '7', '8', '4', '5', '0']), move to gate
    state.gate[[3, 1, 6, 7, 8, 4, 5, 0]] = move.Move(state.storage[[3, 1, 6, 7, 8, 4, 5, 0]])
    # Apply LocalRz with phi=1.5707963267948966 on indices ['0', '1', '3', '4', '5', '6', '7', '8']
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[0, 1, 3, 4, 5, 6, 7, 8])

    # Rearrangement job (id 2):
    #  Move (storage -> gate): transferring qubits from ['2', '6'] to ['3', '5']
    state.gate[[3, 5]] = move.Move(state.storage[[2, 6]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0, 1]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1]

    # Rydberg gate (id 0): between qubit 0 and 3
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q3

    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=1.5707963267948966 on indices ['2']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=1.5707963267948966, indices=[2])
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[2])

    # Rearrangement job (id 5):
    #  Move (gate -> storage): transferring qubits from ['3'] to ['6']
    state.storage[[6]] = move.Move(state.gate[[3]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 6):
    #  Move (storage -> gate): transferring qubits from ['4', '6', '7'] to ['2', '3', '3']
    state.gate[[2, 3, 3]] = move.Move(state.storage[[4, 6, 7]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [1, 2, 0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1, 2]

    # Rydberg gate (id 1): between qubit 3 and 4
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q3 and q4
    # Rydberg gate (id 3): between qubit 0 and 6
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q6

    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=1.5707963267948966 on indices ['1', '1', '2', '2']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=1.5707963267948966, indices=[1, 1, 2, 2])
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[1, 1, 2, 2])

    # Rearrangement job (id 9):
    #  Move (gate -> storage): transferring qubits from ['2', '3'] to ['2', '4']
    state.storage[[2, 4]] = move.Move(state.gate[[2, 3]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [1, 0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1]

    # Rearrangement job (id 10):
    #  Move (storage -> gate): transferring qubits from ['2', '3', '8'] to ['0', '2', '3']
    state.gate[[0, 2, 3]] = move.Move(state.storage[[2, 3, 8]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [1, 2, 0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1, 2]

    # Rearrangement job (id 11):
    #  Move (storage -> gate): transferring qubits from ['5'] to ['0']
    state.gate[[0]] = move.Move(state.storage[[5]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 2): between qubit 3 and 5
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q3 and q5
    # Rydberg gate (id 4): between qubit 0 and 1
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q1
    # Rydberg gate (id 6): between qubit 6 and 7
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q6 and q7

    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=1.5707963267948966 on indices ['0', '0', '1', '1', '2', '2']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=1.5707963267948966, indices=[0, 0, 1, 1, 2, 2])
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[0, 0, 1, 1, 2, 2])

    # Rearrangement job (id 14):
    #  Move (gate -> storage): transferring qubits from ['0', '2', '3', '5'] to ['2', '3', '5', '6']
    state.storage[[2, 3, 5, 6]] = move.Move(state.gate[[0, 2, 3, 5]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [1, 3, 2, 0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1, 2, 3]

    # Rearrangement job (id 15):
    #  Move (storage -> gate): transferring qubits from ['0', '1'] to ['0', '2']
    state.gate[[0, 2]] = move.Move(state.storage[[0, 1]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0, 1]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1]

    # Rydberg gate (id 5): between qubit 0 and 2
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q2
    # Rydberg gate (id 7): between qubit 6 and 8
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q6 and q8

    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=1.5707963267948966 on indices ['0', '0', '1', '1']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=1.5707963267948966, indices=[0, 0, 1, 1])
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[0, 0, 1, 1])

    # Rearrangement job (id 18):
    #  Move (gate -> storage): transferring qubits from ['0', '0', '3'] to ['0', '1', '7']
    state.storage[[0, 1, 7]] = move.Move(state.gate[[0, 0, 3]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [2, 1, 0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1, 2]

    # Rearrangement job (id 19):
    #  Move (gate -> storage): transferring qubits from ['2'] to ['8']
    state.storage[[8]] = move.Move(state.gate[[2]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    move.Execute(state)

expected_qasm = """OPENQASM 2.0;
include "qelib1.inc";


// Qubits: [q(0), q(1), q(2), q(3), q(4), q(5), q(6), q(7), q(8)]
qreg q[9];


cx q[0],q[3];
cx q[0],q[6];
h q[3];
h q[0];
h q[6];
cx q[3],q[4];
cx q[0],q[1];
cx q[6],q[7];
cx q[3],q[5];
cx q[0],q[2];
cx q[6],q[8];
"""

aggressive.Fold(move.vmove)(problem4)
MoveScorer(problem4, expected_qasm=expected_qasm).animate()
print(MoveScorer(problem4, expected_qasm=expected_qasm).score())