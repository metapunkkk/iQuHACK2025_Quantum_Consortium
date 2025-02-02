from bloqade import move
from kirin.passes import aggressive
from iquhack_scoring import MoveScorer
from math import pi



@move.vmove
def bonus1():
    # Initialization (instruction id 0):
    q = move.NewQubitRegister(17)
    state = move.Init(qubits=[q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9], q[10], q[11], q[12], q[13], q[14], q[15], q[16]], indices=[1, 3, 8, 2, 4, 5, 7, 11, 10, 12, 9, 6, 0, 15, 14, 13, 16])

    # For qubits in storage (indices ['0', '1', '2', '3', '4', '5', '6', '7', '9', '10', '11', '12', '13', '14', '15', '16']), move to gate
    state.gate[[0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16]] = move.Move(state.storage[[0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16]])
    # Apply LocalRz with phi=4.71238898038469 on indices ['0', '1', '2', '3', '4', '5', '6', '7', '9', '10', '11', '12', '13', '14', '15', '16']
    state = move.LocalRz(atom_state=state,phi=4.71238898038469,indices=[0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16])

    # Rearrangement job (id 2):
    #  Move (storage -> gate): transferring qubits from ['8', '9'] to ['5', '9']
    state.gate[[5, 9]] = move.Move(state.storage[[8, 9]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0, 1]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1]

    # Rydberg gate (id 0): between qubit 2 and 10
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q2 and q10

    # Apply LocalRz with phi=3.141592653589793 on indices ['4', '4']
    state = move.LocalRz(atom_state=state,phi=3.141592653589793,indices=[4, 4])
    # Apply LocalXY with x_exponent=1.5707963267948966 and axis_phase_exponent=-1.5707963267948966 on indices ['4', '4']
    state = move.LocalXY(atom_state=state, x_exponent=1.5707963267948966, axis_phase_exponent=-1.5707963267948966, indices=[4, 4])
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[4, 4])

    # Rearrangement job (id 5):
    #  Move (gate -> storage): transferring qubits from ['9'] to ['8']
    state.storage[[8]] = move.Move(state.gate[[9]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 6):
    #  Move (storage -> gate): transferring qubits from ['12'] to ['9']
    state.gate[[9]] = move.Move(state.storage[[12]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 1): between qubit 2 and 9
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q2 and q9

    # Apply LocalXY with x_exponent=1.5707963267948966 and axis_phase_exponent=-1.5707963267948966 on indices ['4', '4']
    state = move.LocalXY(atom_state=state, x_exponent=1.5707963267948966, axis_phase_exponent=-1.5707963267948966, indices=[4, 4])
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[4, 4])

    # Rearrangement job (id 9):
    #  Move (gate -> storage): transferring qubits from ['9'] to ['9']
    state.storage[[9]] = move.Move(state.gate[[9]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 10):
    #  Move (storage -> gate): transferring qubits from ['10'] to ['9']
    state.gate[[9]] = move.Move(state.storage[[10]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 2): between qubit 2 and 8
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q2 and q8

    # Apply LocalXY with x_exponent=1.5707963267948966 and axis_phase_exponent=-1.5707963267948966 on indices ['4', '4']
    state = move.LocalXY(atom_state=state, x_exponent=1.5707963267948966, axis_phase_exponent=-1.5707963267948966, indices=[4, 4])
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[4, 4])

    # Rearrangement job (id 13):
    #  Move (gate -> storage): transferring qubits from ['9'] to ['10']
    state.storage[[10]] = move.Move(state.gate[[9]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 14):
    #  Move (storage -> gate): transferring qubits from ['5'] to ['9']
    state.gate[[9]] = move.Move(state.storage[[5]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 3): between qubit 2 and 5
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q2 and q5

    # Apply LocalRz with phi=1.5707963267948966 on indices ['4']
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[4])
    state = move.LocalRz(atom_state=state,phi=3.141592653589793,indices=[4])

    # Rearrangement job (id 17):
    #  Move (gate -> storage): transferring qubits from ['9'] to ['5']
    state.storage[[5]] = move.Move(state.gate[[9]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 18):
    #  Move (storage -> gate): transferring qubits from ['4'] to ['9']
    state.gate[[9]] = move.Move(state.storage[[4]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 4): between qubit 2 and 4
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q2 and q4

    state = move.LocalRz(atom_state=state,phi=3.141592653589793,indices=[4, 4])

    # Rearrangement job (id 21):
    #  Move (gate -> storage): transferring qubits from ['9'] to ['4']
    state.storage[[4]] = move.Move(state.gate[[9]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 22):
    #  Move (storage -> gate): transferring qubits from ['3', '4', '7'] to ['2', '3', '9']
    state.gate[[2, 3, 9]] = move.Move(state.storage[[3, 4, 7]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0, 1, 2]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1, 2]

    # Rydberg gate (id 5): between qubit 2 and 6
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q2 and q6
    # Rydberg gate (id 6): between qubit 1 and 4
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q1 and q4

    # Apply LocalRz with phi=1.5707963267948966 on indices ['1', '4', '4']
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[1, 4, 4])
    # Apply LocalXY with x_exponent=3.141592653589793 and axis_phase_exponent=-1.5707963267948966 on indices ['1', '4', '4']
    state = move.LocalXY(atom_state=state, x_exponent=3.141592653589793, axis_phase_exponent=-1.5707963267948966, indices=[1, 4, 4])

    # Rearrangement job (id 25):
    #  Move (gate -> storage): transferring qubits from ['3', '5', '9'] to ['12', '4', '7']
    state.storage[[12, 4, 7]] = move.Move(state.gate[[3, 5, 9]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [1, 0, 2]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1, 2]

    # Rearrangement job (id 26):
    #  Move (storage -> gate): transferring qubits from ['2', '4', '5'] to ['3', '3', '5']
    state.gate[[3, 3, 5]] = move.Move(state.storage[[2, 4, 5]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0, 1, 2]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1, 2]

    # Rydberg gate (id 7): between qubit 1 and 3
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q1 and q3
    # Rydberg gate (id 9): between qubit 4 and 5
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q4 and q5

    # Apply LocalRz with phi=1.5707963267948966 on indices ['1', '1', '2', '2']
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[1, 1, 2, 2])
    # Apply LocalXY with x_exponent=3.141592653589793 and axis_phase_exponent=-1.5707963267948966 on indices ['1', '1', '2', '2']
    state = move.LocalXY(atom_state=state, x_exponent=3.141592653589793, axis_phase_exponent=-1.5707963267948966, indices=[1, 1, 2, 2])

    # Rearrangement job (id 29):
    #  Move (gate -> storage): transferring qubits from ['2', '3'] to ['2', '4']
    state.storage[[2, 4]] = move.Move(state.gate[[2, 3]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0, 1]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1]

    # Rearrangement job (id 30):
    #  Move (storage -> gate): transferring qubits from ['1', '12'] to ['2', '3']
    state.gate[[2, 3]] = move.Move(state.storage[[1, 12]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0, 1]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1]

    # Rydberg gate (id 8): between qubit 0 and 3
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q3
    # Rydberg gate (id 11): between qubit 5 and 6
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q5 and q6

    # Apply LocalRz with phi=1.5707963267948966 on indices ['1']
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[1])

    # Rearrangement job (id 33):
    #  Move (gate -> storage): transferring qubits from ['2', '5'] to ['1', '5']
    state.storage[[1, 5]] = move.Move(state.gate[[2, 5]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0, 1]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1]

    # Rearrangement job (id 34):
    #  Move (storage -> gate): transferring qubits from ['11', '4'] to ['2', '5']
    state.gate[[2, 5]] = move.Move(state.storage[[11, 4]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0, 1]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1]

    # Rydberg gate (id 10): between qubit 3 and 4
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q3 and q4
    # Rydberg gate (id 12): between qubit 6 and 7
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q6 and q7

    # Apply LocalRz with phi=1.5707963267948966 on indices ['1', '1', '2', '2']
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[1, 1, 2, 2])
    state = move.LocalRz(atom_state=state,phi=3.141592653589793,indices=[1, 1, 2, 2])

    # Rearrangement job (id 37):
    #  Move (gate -> storage): transferring qubits from ['2', '3', '5'] to ['11', '3', '4']
    state.storage[[11, 3, 4]] = move.Move(state.gate[[2, 3, 5]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0, 1, 2]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1, 2]

    # Rearrangement job (id 38):
    #  Move (storage -> gate): transferring qubits from ['6'] to ['2']
    state.gate[[2]] = move.Move(state.storage[[6]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 13): between qubit 3 and 11
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q3 and q11

    # Apply LocalRz with phi=3.141592653589793 on indices ['1', '1']
    state = move.LocalRz(atom_state=state,phi=3.141592653589793,indices=[1, 1])

    # Rearrangement job (id 41):
    #  Move (gate -> storage): transferring qubits from ['3'] to ['6']
    state.storage[[6]] = move.Move(state.gate[[3]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 42):
    #  Move (storage -> gate): transferring qubits from ['3'] to ['3']
    state.gate[[3]] = move.Move(state.storage[[3]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 14): between qubit 4 and 11
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q4 and q11

    # Apply LocalRz with phi=1.5707963267948966 on indices ['1']
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[1])

    # Rearrangement job (id 45):
    #  Move (gate -> storage): transferring qubits from ['3'] to ['3']
    state.storage[[3]] = move.Move(state.gate[[3]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 46):
    #  Move (storage -> gate): transferring qubits from ['5'] to ['3']
    state.gate[[3]] = move.Move(state.storage[[5]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 15): between qubit 5 and 11
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q5 and q11

    # Apply LocalRz with phi=1.5707963267948966 on indices ['1']
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[1])

    # Rearrangement job (id 49):
    #  Move (gate -> storage): transferring qubits from ['3'] to ['5']
    state.storage[[5]] = move.Move(state.gate[[3]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 50):
    #  Move (storage -> gate): transferring qubits from ['4'] to ['3']
    state.gate[[3]] = move.Move(state.storage[[4]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 16): between qubit 6 and 11
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q6 and q11

    # Apply LocalRz with phi=1.5707963267948966 on indices ['1']
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[1])

    # Rearrangement job (id 53):
    #  Move (gate -> storage): transferring qubits from ['3'] to ['4']
    state.storage[[4]] = move.Move(state.gate[[3]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 54):
    #  Move (storage -> gate): transferring qubits from ['10'] to ['3']
    state.gate[[3]] = move.Move(state.storage[[10]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 17): between qubit 8 and 11
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q8 and q11

    # Apply LocalRz with phi=3.141592653589793 on indices ['1']
    state = move.LocalRz(atom_state=state,phi=3.141592653589793,indices=[1])

    # Rearrangement job (id 57):
    #  Move (gate -> storage): transferring qubits from ['3'] to ['10']
    state.storage[[10]] = move.Move(state.gate[[3]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 58):
    #  Move (storage -> gate): transferring qubits from ['10', '14', '9'] to ['13', '3', '7']
    state.gate[[13, 3, 7]] = move.Move(state.storage[[10, 14, 9]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [1, 0, 2]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1, 2]

    # Rydberg gate (id 18): between qubit 9 and 11
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q9 and q11
    # Rydberg gate (id 20): between qubit 8 and 14
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q8 and q14

    # Apply LocalRz with phi=3.141592653589793 on indices ['6', '6']
    state = move.LocalRz(atom_state=state,phi=3.141592653589793,indices=[6, 6])

    # Rearrangement job (id 61):
    #  Move (gate -> storage): transferring qubits from ['3', '7'] to ['12', '9']
    state.storage[[12, 9]] = move.Move(state.gate[[3, 7]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [1, 0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1]

    # Rearrangement job (id 62):
    #  Move (storage -> gate): transferring qubits from ['8', '9'] to ['3', '7']
    state.gate[[3, 7]] = move.Move(state.storage[[8, 9]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [1, 0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1]

    # Rydberg gate (id 19): between qubit 10 and 11
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q10 and q11
    # Rydberg gate (id 21): between qubit 9 and 14
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q9 and q14

    # Apply LocalRz with phi=3.141592653589793 on indices ['6']
    state = move.LocalRz(atom_state=state,phi=3.141592653589793,indices=[6])

    # Rearrangement job (id 65):
    #  Move (gate -> storage): transferring qubits from ['3', '7'] to ['14', '8']
    state.storage[[14, 8]] = move.Move(state.gate[[3, 7]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [1, 0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1]

    # Rearrangement job (id 66):
    #  Move (gate -> storage): transferring qubits from ['2'] to ['9']
    state.storage[[9]] = move.Move(state.gate[[2]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 67):
    #  Move (storage -> gate): transferring qubits from ['13', '14', '15'] to ['11', '6', '7']
    state.gate[[11, 6, 7]] = move.Move(state.storage[[13, 14, 15]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [1, 2, 0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1, 2]

    # Rydberg gate (id 22): between qubit 13 and 14
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q13 and q14
    # Rydberg gate (id 23): between qubit 9 and 15
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q9 and q15

    # Apply LocalRz with phi=3.141592653589793 on indices ['5', '5', '6', '6']
    state = move.LocalRz(atom_state=state,phi=3.141592653589793,indices=[5, 5, 6, 6])

    # Rearrangement job (id 70):
    #  Move (gate -> storage): transferring qubits from ['11', '13'] to ['10', '13']
    state.storage[[10, 13]] = move.Move(state.gate[[11, 13]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0, 1]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1]

    # Rearrangement job (id 71):
    #  Move (storage -> gate): transferring qubits from ['16', '8'] to ['11', '13']
    state.gate[[11, 13]] = move.Move(state.storage[[16, 8]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [1, 0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1]

    # Rydberg gate (id 24): between qubit 10 and 15
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q10 and q15
    # Rydberg gate (id 26): between qubit 13 and 16
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q13 and q16

    # Apply LocalRz with phi=1.5707963267948966 on indices ['5', '6', '6']
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[5, 6, 6])

    # Rearrangement job (id 74):
    #  Move (gate -> storage): transferring qubits from ['11', '13', '7'] to ['14', '15', '8']
    state.storage[[14, 15, 8]] = move.Move(state.gate[[11, 13, 7]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [2, 0, 1]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1, 2]

    # Rearrangement job (id 75):
    #  Move (storage -> gate): transferring qubits from ['13'] to ['11']
    state.gate[[11]] = move.Move(state.storage[[13]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 25): between qubit 14 and 15
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q14 and q15

    # Apply LocalRz with phi=4.71238898038469 on indices ['5']
    state = move.LocalRz(atom_state=state,phi=4.71238898038469,indices=[5])

    # Rearrangement job (id 78):
    #  Move (gate -> storage): transferring qubits from ['6'] to ['13']
    state.storage[[13]] = move.Move(state.gate[[6]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 79):
    #  Move (storage -> gate): transferring qubits from ['15'] to ['6']
    state.gate[[6]] = move.Move(state.storage[[15]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 27): between qubit 14 and 16
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q14 and q16

    # Apply LocalRz with phi=1.5707963267948966 on indices ['5']
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[5])

    # Rearrangement job (id 82):
    #  Move (gate -> storage): transferring qubits from ['11'] to ['15']
    state.storage[[15]] = move.Move(state.gate[[11]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 83):
    #  Move (storage -> gate): transferring qubits from ['13'] to ['11']
    state.gate[[11]] = move.Move(state.storage[[13]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 28): between qubit 15 and 16
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q15 and q16

    # Apply LocalRz with phi=1.5707963267948966 on indices ['5']
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[5])

    # Rearrangement job (id 86):
    #  Move (gate -> storage): transferring qubits from ['11'] to ['13']
    state.storage[[13]] = move.Move(state.gate[[11]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 87):
    #  Move (gate -> storage): transferring qubits from ['6'] to ['16']
    state.storage[[16]] = move.Move(state.gate[[6]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    move.Execute(state)

expected_qasm = """OPENQASM 2.0;
include "qelib1.inc";


// Qubits: [q(0), q(1), q(2), q(3), q(4), q(5), q(6), q(7), q(8), q(9), q(10), q(11), q(12), q(13), q(14), q(15), q(16)]
qreg q[17];


h q[3];
h q[4];
h q[6];
h q[11];
h q[12];
h q[14];
h q[15];
h q[16];
cx q[2],q[10];
cx q[2],q[9];
cx q[2],q[8];
cx q[2],q[5];
cx q[4],q[2];
cx q[4],q[1];
cx q[6],q[2];
cx q[4],q[5];
cx q[3],q[1];
cx q[3],q[0];
cx q[6],q[5];
cx q[3],q[4];
cx q[6],q[7];
cx q[11],q[3];
cx q[11],q[4];
cx q[11],q[5];
cx q[11],q[6];
cx q[11],q[8];
cx q[11],q[9];
cx q[14],q[8];
cx q[11],q[10];
cx q[14],q[9];
cx q[14],q[13];
cx q[15],q[9];
cx q[15],q[10];
cx q[16],q[13];
cx q[15],q[14];
cx q[16],q[14];
cx q[16],q[15];
"""

aggressive.Fold(move.vmove)(bonus1)
MoveScorer(bonus1, expected_qasm=expected_qasm).animate()
print(MoveScorer(bonus1, expected_qasm=expected_qasm).score())