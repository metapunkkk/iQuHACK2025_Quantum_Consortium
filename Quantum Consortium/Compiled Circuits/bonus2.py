from bloqade import move
from kirin.passes import aggressive
from iquhack_scoring import MoveScorer
from math import pi



@move.vmove
def bonus2():
    # Initialization (instruction id 0):
    q = move.NewQubitRegister(17)
    state = move.Init(qubits=[q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9], q[10], q[11], q[12], q[13], q[14], q[15], q[16]], indices=[16, 14, 13, 15, 11, 12, 9, 10, 8, 5, 6, 4, 0, 7, 3, 1, 2])

    # For qubits in storage (indices ['0', '2', '3', '4', '5', '6', '7', '9', '10', '11', '12', '14', '16']), move to gate
    state.gate[[0, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 16]] = move.Move(state.storage[[0, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 16]])
    # Apply LocalRz with phi=4.71238898038469 on indices ['0', '2', '3', '4', '5', '6', '7', '9', '10', '11', '12', '14', '16']
    state = move.LocalRz(atom_state=state,phi=4.71238898038469,indices=[0, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 16])

    # Rearrangement job (id 2):
    #  Move (storage -> gate): transferring qubits from ['1', '10', '11', '15', '16', '3', '5', '8'] to ['13', '17', '2', '3', '5', '6', '7', '9']
    state.gate[[13, 17, 2, 3, 5, 6, 7, 9]] = move.Move(state.storage[[1, 10, 11, 15, 16, 3, 5, 8]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [7, 6, 5, 4, 3, 2, 1, 0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1, 2, 3, 4, 5, 6, 7]

    # Rearrangement job (id 3):
    #  Move (storage -> gate): transferring qubits from ['12', '4', '6', '9'] to ['11', '3', '5', '9']
    state.gate[[11, 3, 5, 9]] = move.Move(state.storage[[12, 4, 6, 9]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [1, 0, 3, 2]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1, 2, 3]

    # Rydberg gate (id 0): between qubit 0 and 3
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q3
    # Rydberg gate (id 2): between qubit 4 and 7
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q4 and q7
    # Rydberg gate (id 4): between qubit 5 and 8
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q5 and q8
    # Rydberg gate (id 8): between qubit 6 and 9
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q6 and q9
    # Rydberg gate (id 10): between qubit 10 and 14
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q10 and q14
    # Rydberg gate (id 16): between qubit 11 and 15
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q11 and q15

    # Apply LocalRz with phi=4.71238898038469 on indices ['1', '2', '2', '4', '4', '5', '6', '6', '8']
    state = move.LocalRz(atom_state=state,phi=4.71238898038469,indices=[1, 2, 2, 4, 4, 5, 6, 6, 8])

    # Rearrangement job (id 6):
    #  Move (gate -> storage): transferring qubits from ['2', '3', '5', '6', '7', '9'] to ['1', '10', '12', '16', '4', '8']
    state.storage[[1, 10, 12, 16, 4, 8]] = move.Move(state.gate[[2, 3, 5, 6, 7, 9]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [5, 4, 3, 2, 1, 0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1, 2, 3, 4, 5]

    # Rearrangement job (id 7):
    #  Move (storage -> gate): transferring qubits from ['0', '1', '10', '12', '13', '4'] to ['0', '0', '2', '3', '6', '9']
    state.gate[[0, 0, 2, 3, 6, 9]] = move.Move(state.storage[[0, 1, 10, 12, 13, 4]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [5, 4, 3, 0, 2, 1]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1, 2, 3, 4, 5]

    # Rearrangement job (id 8):
    #  Move (storage -> gate): transferring qubits from ['14'] to ['7']
    state.gate[[7]] = move.Move(state.storage[[14]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 9):
    #  Move (storage -> gate): transferring qubits from ['16'] to ['5']
    state.gate[[5]] = move.Move(state.storage[[16]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 1): between qubit 0 and 2
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q2
    # Rydberg gate (id 3): between qubit 1 and 4
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q1 and q4
    # Rydberg gate (id 5): between qubit 5 and 7
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q5 and q7
    # Rydberg gate (id 9): between qubit 3 and 6
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q3 and q6
    # Rydberg gate (id 11): between qubit 8 and 10
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q8 and q10
    # Rydberg gate (id 17): between qubit 11 and 14
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q11 and q14
    # Rydberg gate (id 18): between qubit 12 and 15
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q12 and q15

    # Apply LocalRz with phi=1.5707963267948966 on indices ['0', '0', '1', '2', '4', '5', '5', '6', '6', '8']
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[0, 0, 1, 2, 4, 5, 5, 6, 6, 8])

    # Rearrangement job (id 12):
    #  Move (gate -> storage): transferring qubits from ['0', '0', '11', '13', '17', '2', '3', '5', '6', '7'] to ['0', '1', '10', '11', '12', '13', '16', '3', '4', '9']
    state.storage[[0, 1, 10, 11, 12, 13, 16, 3, 4, 9]] = move.Move(state.gate[[0, 0, 11, 13, 17, 2, 3, 5, 6, 7]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [9, 7, 4, 8, 6, 5, 3, 0, 2, 1]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Rearrangement job (id 13):
    #  Move (storage -> gate): transferring qubits from ['11', '7'] to ['17', '3']
    state.gate[[17, 3]] = move.Move(state.storage[[11, 7]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0, 1]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1]

    # Rearrangement job (id 14):
    #  Move (storage -> gate): transferring qubits from ['2', '3', '4'] to ['4', '5', '7']
    state.gate[[4, 5, 7]] = move.Move(state.storage[[2, 3, 4]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [2, 0, 1]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1, 2]

    # Rearrangement job (id 15):
    #  Move (storage -> gate): transferring qubits from ['8'] to ['2']
    state.gate[[2]] = move.Move(state.storage[[8]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 6): between qubit 2 and 5
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q2 and q5
    # Rydberg gate (id 12): between qubit 10 and 13
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q10 and q13
    # Rydberg gate (id 14): between qubit 6 and 8
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q6 and q8
    # Rydberg gate (id 19): between qubit 9 and 11
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q9 and q11
    # Rydberg gate (id 22): between qubit 14 and 16
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q14 and q16

    # Apply LocalRz with phi=1.5707963267948966 on indices ['1', '2', '2', '3', '4', '4', '8']
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[1, 2, 2, 3, 4, 4, 8])
    state = move.LocalRz(atom_state=state,phi=3.141592653589793,indices=[1, 2, 2, 3, 4, 4, 8])

    # Rearrangement job (id 18):
    #  Move (gate -> storage): transferring qubits from ['2', '3', '5', '7', '9'] to ['15', '2', '4', '6', '8']
    state.storage[[15, 2, 4, 6, 8]] = move.Move(state.gate[[2, 3, 5, 7, 9]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [4, 3, 0, 1, 2]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1, 2, 3, 4]

    # Rearrangement job (id 19):
    #  Move (storage -> gate): transferring qubits from ['0', '10', '12', '2', '8'] to ['0', '0', '2', '3', '9']
    state.gate[[0, 0, 2, 3, 9]] = move.Move(state.storage[[0, 10, 12, 2, 8]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [4, 3, 2, 1, 0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1, 2, 3, 4]

    # Rearrangement job (id 20):
    #  Move (storage -> gate): transferring qubits from ['15', '4'] to ['5', '7']
    state.gate[[5, 7]] = move.Move(state.storage[[15, 4]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [1, 0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1]

    # Rydberg gate (id 7): between qubit 1 and 5
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q1 and q5
    # Rydberg gate (id 13): between qubit 7 and 10
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q7 and q10
    # Rydberg gate (id 15): between qubit 2 and 6
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q2 and q6
    # Rydberg gate (id 20): between qubit 8 and 11
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q8 and q11
    # Rydberg gate (id 21): between qubit 9 and 12
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q9 and q12
    # Rydberg gate (id 23): between qubit 13 and 16
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q13 and q16

    # Apply LocalXY with x_exponent=1.5707963267948966 and axis_phase_exponent=-1.5707963267948966 on indices ['0', '0', '1', '1', '2', '2', '3', '3', '4', '4', '8', '8']
    state = move.LocalXY(atom_state=state, x_exponent=1.5707963267948966, axis_phase_exponent=-1.5707963267948966, indices=[0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 8, 8])
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 8, 8])

    # Rearrangement job (id 23):
    #  Move (gate -> storage): transferring qubits from ['0', '0', '17', '2', '3', '3', '5', '9'] to ['0', '12', '15', '17', '2', '3', '4', '5']
    state.storage[[0, 12, 15, 17, 2, 3, 4, 5]] = move.Move(state.gate[[0, 0, 17, 2, 3, 3, 5, 9]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [6, 7, 4, 2, 1, 5, 3, 0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1, 2, 3, 4, 5, 6, 7]

    # Rearrangement job (id 24):
    #  Move (gate -> storage): transferring qubits from ['4', '5', '7', '9'] to ['10', '11', '7', '8']
    state.storage[[10, 11, 7, 8]] = move.Move(state.gate[[4, 5, 7, 9]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0, 2, 1, 3]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1, 2, 3]

    move.Execute(state)

expected_qasm = """OPENQASM 2.0;
include "qelib1.inc";


// Qubits: [q(0, 4), q(1, 1), q(1, 3), q(1, 5), q(2, 0), q(2, 2), q(2, 4), q(3, 1), q(3, 3), q(3, 5), q(4, 2), q(4, 4), q(4, 6), q(5, 1), q(5, 3), q(5, 5), q(6, 2)]
qreg q[17];


h q[4];
h q[10];
h q[6];
h q[12];
cx q[4],q[7];
cx q[6],q[9];
cx q[10],q[14];
cx q[3],q[0];
cx q[8],q[5];
cx q[15],q[11];
cx q[4],q[1];
cx q[6],q[3];
cx q[10],q[8];
cx q[2],q[0];
cx q[7],q[5];
cx q[14],q[11];
cx q[6],q[8];
cx q[10],q[13];
cx q[12],q[15];
cx q[2],q[5];
cx q[9],q[11];
cx q[14],q[16];
cx q[6],q[2];
cx q[10],q[7];
cx q[12],q[9];
cx q[1],q[5];
cx q[8],q[11];
cx q[13],q[16];
h q[4];
h q[10];
h q[6];
h q[12];
"""

aggressive.Fold(move.vmove)(bonus2)
MoveScorer(bonus2, expected_qasm=expected_qasm).animate()
print(MoveScorer(bonus2, expected_qasm=expected_qasm).score())