from bloqade import move
from kirin.passes import aggressive
from iquhack_scoring import MoveScorer
from math import pi




@move.vmove
def problem3():
    # Initialization (instruction id 0):
    q = move.NewQubitRegister(4)
    state = move.Init(qubits=[q[0], q[1], q[2], q[3]], indices=[0, 1, 2, 4])

    # For qubits in storage (indices ['0', '1', '2', '4']), move to gate
    state.gate[[0, 1, 2, 4]] = move.Move(state.storage[[0, 1, 2, 4]])
    # Apply LocalRz with phi=3.29279232909158 on indices ['0', '1', '2', '4']
    state = move.LocalRz(atom_state=state,phi=3.29279232909158,indices=[0, 1, 2, 4])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=4.71238898038469 on indices ['0', '1', '2', '4']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=4.71238898038469, indices=[0, 1, 2, 4])
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[0, 1, 2, 4])

    # Rearrangement job (id 2):
    #  Move (storage -> gate): transferring qubits from ['0', '1'] to ['0', '0']
    state.gate[[0, 0]] = move.Move(state.storage[[0, 1]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0, 1]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1]

    # Rydberg gate (id 0): between qubit 0 and 1
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q1

    # Apply LocalRz with phi=0.24385486649692603 on indices ['0']
    state = move.LocalRz(atom_state=state,phi=0.24385486649692603,indices=[0])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=4.71238898038469 on indices ['0']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=4.71238898038469, indices=[0])
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[0])

    # Rydberg gate (id 1): between qubit 0 and 1
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q1

    # Apply LocalRz with phi=2.74726631203367 on indices ['0', '0']
    state = move.LocalRz(atom_state=state,phi=2.74726631203367,indices=[0, 0])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=1.5707963267948966 on indices ['0', '0']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=1.5707963267948966, indices=[0, 0])
    state = move.LocalRz(atom_state=state,phi=4.71238898038469,indices=[0, 0])

    # Rearrangement job (id 7):
    #  Move (gate -> storage): transferring qubits from ['0'] to ['0']
    state.storage[[0]] = move.Move(state.gate[[0]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 8):
    #  Move (storage -> gate): transferring qubits from ['4'] to ['0']
    state.gate[[0]] = move.Move(state.storage[[4]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 2): between qubit 0 and 3
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q3

    # Apply LocalRz with phi=0.24385486649692603 on indices ['0']
    state = move.LocalRz(atom_state=state,phi=0.24385486649692603,indices=[0])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=4.71238898038469 on indices ['0']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=4.71238898038469, indices=[0])
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[0])

    # Rydberg gate (id 3): between qubit 0 and 3
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q3

    # Apply LocalRz with phi=2.7194629858281814 on indices ['0', '0']
    state = move.LocalRz(atom_state=state,phi=2.7194629858281814,indices=[0, 0])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=4.71238898038469 on indices ['0', '0']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=4.71238898038469, indices=[0, 0])
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[0, 0])

    # Rearrangement job (id 13):
    #  Move (gate -> storage): transferring qubits from ['0'] to ['1']
    state.storage[[1]] = move.Move(state.gate[[0]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 14):
    #  Move (storage -> gate): transferring qubits from ['2'] to ['0']
    state.gate[[0]] = move.Move(state.storage[[2]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 4): between qubit 0 and 2
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q2

    # Apply LocalRz with phi=0.24385486649692603 on indices ['0']
    state = move.LocalRz(atom_state=state,phi=0.24385486649692603,indices=[0])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=4.71238898038469 on indices ['0']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=4.71238898038469, indices=[0])
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[0])

    # Rydberg gate (id 5): between qubit 0 and 2
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q2

    # Apply LocalRz with phi=0.5930800944593309 on indices ['0', '0']
    state = move.LocalRz(atom_state=state,phi=0.5930800944593309,indices=[0, 0])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=1.0018662234670463 on indices ['0', '0']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=1.0018662234670463, indices=[0, 0])
    state = move.LocalRz(atom_state=state,phi=1.587607902144092,indices=[0, 0])

    # Rearrangement job (id 19):
    #  Move (gate -> storage): transferring qubits from ['0'] to ['2']
    state.storage[[2]] = move.Move(state.gate[[0]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 20):
    #  Move (storage -> gate): transferring qubits from ['0'] to ['0']
    state.gate[[0]] = move.Move(state.storage[[0]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 6): between qubit 1 and 2
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q1 and q2

    # Apply LocalRz with phi=0.24385486649692603 on indices ['0']
    state = move.LocalRz(atom_state=state,phi=0.24385486649692603,indices=[0])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=4.71238898038469 on indices ['0']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=4.71238898038469, indices=[0])
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[0])

    # Rydberg gate (id 7): between qubit 1 and 2
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q1 and q2

    # Apply LocalRz with phi=2.186913544363073 on indices ['0', '0']
    state = move.LocalRz(atom_state=state,phi=2.186913544363073,indices=[0, 0])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=4.71238898038469 on indices ['0', '0']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=4.71238898038469, indices=[0, 0])
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[0, 0])

    # Rearrangement job (id 25):
    #  Move (gate -> storage): transferring qubits from ['0'] to ['0']
    state.storage[[0]] = move.Move(state.gate[[0]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 26):
    #  Move (storage -> gate): transferring qubits from ['1'] to ['0']
    state.gate[[0]] = move.Move(state.storage[[1]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 8): between qubit 1 and 3
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q1 and q3

    # Apply LocalRz with phi=6.03933044068266 on indices ['0']
    state = move.LocalRz(atom_state=state,phi=6.03933044068266,indices=[0])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=4.71238898038469 on indices ['0']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=4.71238898038469, indices=[0])
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[0])

    # Rydberg gate (id 9): between qubit 1 and 3
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q1 and q3

    # Apply LocalRz with phi=1.138175356232792 on indices ['0', '0']
    state = move.LocalRz(atom_state=state,phi=1.138175356232792,indices=[0, 0])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=-1.6255232084538775 on indices ['0', '0']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=-1.6255232084538775, indices=[0, 0])
    state = move.LocalRz(atom_state=state,phi=-0.359386740970844,indices=[0, 0])

    # Rearrangement job (id 31):
    #  Move (gate -> storage): transferring qubits from ['0'] to ['1']
    state.storage[[1]] = move.Move(state.gate[[0]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 32):
    #  Move (storage -> gate): transferring qubits from ['2'] to ['0']
    state.gate[[0]] = move.Move(state.storage[[2]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 33):
    #  Move (storage -> gate): transferring qubits from ['0', '1'] to ['2', '3']
    state.gate[[2, 3]] = move.Move(state.storage[[0, 1]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0, 1]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1]

    # Rydberg gate (id 10): between qubit 0 and 1
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q1
    # Rydberg gate (id 12): between qubit 2 and 3
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q2 and q3

    # Apply LocalRz with phi=5.834191459349553 on indices ['0', '1']
    state = move.LocalRz(atom_state=state,phi=5.834191459349553,indices=[0, 1])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=4.71238898038469 on indices ['0', '1']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=4.71238898038469, indices=[0, 1])
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[0, 1])

    # Rydberg gate (id 11): between qubit 0 and 1
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q1
    # Rydberg gate (id 13): between qubit 2 and 3
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q2 and q3

    # Apply LocalRz with phi=2.9791233689564542 on indices ['0', '0', '1', '1']
    state = move.LocalRz(atom_state=state,phi=2.9791233689564542,indices=[0, 0, 1, 1])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=1.5707963267948966 on indices ['0', '0', '1', '1']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=1.5707963267948966, indices=[0, 0, 1, 1])
    state = move.LocalRz(atom_state=state,phi=4.71238898038469,indices=[0, 0, 1, 1])

    # Rearrangement job (id 38):
    #  Move (gate -> storage): transferring qubits from ['0', '2', '3'] to ['0', '2', '3']
    state.storage[[0, 2, 3]] = move.Move(state.gate[[0, 2, 3]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0, 1, 2]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1, 2]

    # Rearrangement job (id 39):
    #  Move (storage -> gate): transferring qubits from ['3'] to ['0']
    state.gate[[0]] = move.Move(state.storage[[3]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 14): between qubit 0 and 3
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q3

    # Apply LocalRz with phi=0.4489938478300329 on indices ['0']
    state = move.LocalRz(atom_state=state,phi=0.4489938478300329,indices=[0])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=4.71238898038469 on indices ['0']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=4.71238898038469, indices=[0])
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[0])

    # Rydberg gate (id 15): between qubit 0 and 3
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q3

    # Apply LocalRz with phi=1.5438003085341305 on indices ['0', '0']
    state = move.LocalRz(atom_state=state,phi=1.5438003085341305,indices=[0, 0])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=1.5707963267948966 on indices ['0', '0']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=1.5707963267948966, indices=[0, 0])
    state = move.LocalRz(atom_state=state,phi=4.71238898038469,indices=[0, 0])

    # Rearrangement job (id 44):
    #  Move (gate -> storage): transferring qubits from ['0'] to ['1']
    state.storage[[1]] = move.Move(state.gate[[0]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 45):
    #  Move (storage -> gate): transferring qubits from ['2'] to ['0']
    state.gate[[0]] = move.Move(state.storage[[2]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 16): between qubit 0 and 2
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q2

    # Apply LocalRz with phi=0.4489938478300329 on indices ['0']
    state = move.LocalRz(atom_state=state,phi=0.4489938478300329,indices=[0])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=4.71238898038469 on indices ['0']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=4.71238898038469, indices=[0])
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[0])

    # Rydberg gate (id 17): between qubit 0 and 2
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q2

    # Apply LocalRz with phi=1.575559577217865 on indices ['0', '0']
    state = move.LocalRz(atom_state=state,phi=1.575559577217865,indices=[0, 0])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=6.267367446602385 on indices ['0', '0']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=6.267367446602385, indices=[0, 0])
    state = move.LocalRz(atom_state=state,phi=0.29247014196174453,indices=[0, 0])

    # Rearrangement job (id 50):
    #  Move (gate -> storage): transferring qubits from ['0'] to ['2']
    state.storage[[2]] = move.Move(state.gate[[0]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 51):
    #  Move (storage -> gate): transferring qubits from ['0'] to ['0']
    state.gate[[0]] = move.Move(state.storage[[0]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 18): between qubit 1 and 2
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q1 and q2

    # Apply LocalRz with phi=5.834191459349553 on indices ['0']
    state = move.LocalRz(atom_state=state,phi=5.834191459349553,indices=[0])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=4.71238898038469 on indices ['0']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=4.71238898038469, indices=[0])
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[0])

    # Rydberg gate (id 19): between qubit 1 and 2
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q1 and q2

    # Apply LocalRz with phi=2.2092554775190343 on indices ['0', '0']
    state = move.LocalRz(atom_state=state,phi=2.2092554775190343,indices=[0, 0])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=4.71238898038469 on indices ['0', '0']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=4.71238898038469, indices=[0, 0])
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[0, 0])

    # Rearrangement job (id 56):
    #  Move (gate -> storage): transferring qubits from ['0'] to ['0']
    state.storage[[0]] = move.Move(state.gate[[0]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 57):
    #  Move (storage -> gate): transferring qubits from ['1'] to ['0']
    state.gate[[0]] = move.Move(state.storage[[1]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 20): between qubit 1 and 3
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q1 and q3

    # Apply LocalRz with phi=0.4489938478300329 on indices ['0']
    state = move.LocalRz(atom_state=state,phi=0.4489938478300329,indices=[0])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=4.71238898038469 on indices ['0']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=4.71238898038469, indices=[0])
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[0])

    # Rydberg gate (id 21): between qubit 1 and 3
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q1 and q3

    # Apply LocalRz with phi=1.575559577217865 on indices ['0', '0']
    state = move.LocalRz(atom_state=state,phi=1.575559577217865,indices=[0, 0])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=6.267367446602385 on indices ['0', '0']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=6.267367446602385, indices=[0, 0])
    state = move.LocalRz(atom_state=state,phi=0.29247014196174453,indices=[0, 0])

    # Rearrangement job (id 62):
    #  Move (gate -> storage): transferring qubits from ['0'] to ['1']
    state.storage[[1]] = move.Move(state.gate[[0]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 63):
    #  Move (storage -> gate): transferring qubits from ['0'] to ['0']
    state.gate[[0]] = move.Move(state.storage[[0]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 22): between qubit 2 and 3
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q2 and q3

    # Apply LocalRz with phi=5.834191459349553 on indices ['0']
    state = move.LocalRz(atom_state=state,phi=5.834191459349553,indices=[0])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=4.71238898038469 on indices ['0']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=4.71238898038469, indices=[0])
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[0])

    # Rydberg gate (id 23): between qubit 2 and 3
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q2 and q3

    # Apply LocalRz with phi=1.492105089773319 on indices ['0', '0']
    state = move.LocalRz(atom_state=state,phi=1.492105089773319,indices=[0, 0])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=0.2649351269325873 on indices ['0', '0']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=0.2649351269325873, indices=[0, 0])
    state = move.LocalRz(atom_state=state,phi=0.2820170572652836,indices=[0, 0])

    # Rearrangement job (id 68):
    #  Move (gate -> storage): transferring qubits from ['0', '0'] to ['0', '3']
    state.storage[[0, 3]] = move.Move(state.gate[[0, 0]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [1, 0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1]

    move.Execute(state)

expected_qasm = """OPENQASM 2.0;
include "qelib1.inc";


// Qubits: [q(0), q(1), q(2), q(3)]
qreg q[4];


h q[0];
h q[1];
h q[2];
h q[3];

// Gate: CZ**0.15524282950959892
u3(pi*0.5,0,pi*0.25) q[0];
u3(pi*0.5,0,pi*0.75) q[1];
sx q[0];
cx q[0],q[1];
rx(pi*0.4223785852) q[0];
ry(pi*0.5) q[1];
cx q[1],q[0];
sxdg q[1];
s q[1];
cx q[0],q[1];
u3(pi*0.5,pi*0.8276214148,pi*1.0) q[0];
u3(pi*0.5,pi*0.3276214148,pi*1.0) q[1];

// Gate: CZ**0.15524282950959892
u3(pi*0.5,0,pi*0.25) q[0];
u3(pi*0.5,0,pi*0.75) q[3];
sx q[0];
cx q[0],q[3];
rx(pi*0.4223785852) q[0];
ry(pi*0.5) q[3];
cx q[3],q[0];
sxdg q[3];
s q[3];
cx q[0],q[3];
u3(pi*0.5,pi*0.8276214148,pi*1.0) q[0];
u3(pi*0.5,pi*0.3276214148,pi*1.0) q[3];

// Gate: CZ**0.15524282950959892
u3(pi*0.5,0,pi*0.25) q[0];
u3(pi*0.5,0,pi*0.75) q[2];
sx q[0];
cx q[0],q[2];
rx(pi*0.4223785852) q[0];
ry(pi*0.5) q[2];
cx q[2],q[0];
sxdg q[2];
s q[2];
cx q[0],q[2];
u3(pi*0.5,pi*0.8276214148,pi*1.0) q[0];
u3(pi*0.5,pi*0.3276214148,pi*1.0) q[2];

// Gate: CZ**0.15524282950959892
u3(pi*0.5,0,pi*0.25) q[1];
u3(pi*0.5,0,pi*0.75) q[2];
sx q[1];
cx q[1],q[2];
rx(pi*0.4223785852) q[1];
ry(pi*0.5) q[2];
cx q[2],q[1];
sxdg q[2];
s q[2];
cx q[1],q[2];
u3(pi*0.5,pi*0.8276214148,pi*1.0) q[1];
u3(pi*0.5,pi*0.3276214148,pi*1.0) q[2];

rx(pi*0.1766811937) q[0];

// Gate: CZ**0.15524282950959892
u3(pi*0.5,0,pi*0.25) q[1];
u3(pi*0.5,0,pi*0.75) q[3];
sx q[1];
cx q[1],q[3];
rx(pi*0.4223785852) q[1];
ry(pi*0.5) q[3];
cx q[3],q[1];
sxdg q[3];
s q[3];
cx q[1],q[3];
u3(pi*0.5,pi*0.8276214148,pi*1.0) q[1];
u3(pi*0.5,pi*0.3276214148,pi*1.0) q[3];

// Gate: CZ**0.15524282950959892
u3(pi*0.5,0,pi*0.25) q[2];
u3(pi*0.5,0,pi*0.75) q[3];
sx q[2];
cx q[2],q[3];
rx(pi*0.4223785852) q[2];
ry(pi*0.5) q[3];
cx q[3],q[2];
sxdg q[3];
s q[3];
cx q[2],q[3];
u3(pi*0.5,pi*0.8276214148,pi*1.0) q[2];
u3(pi*0.5,pi*0.3276214148,pi*1.0) q[3];

rx(pi*0.1766811937) q[1];
rx(pi*0.1766811937) q[2];
rx(pi*0.1766811937) q[3];

// Gate: CZ**0.2858383611880559
u3(pi*0.5,pi*1.0,pi*0.75) q[0];
u3(pi*0.5,pi*1.0,pi*1.25) q[1];
sx q[0];
cx q[0],q[1];
rx(pi*0.3570808194) q[0];
ry(pi*0.5) q[1];
cx q[1],q[0];
sxdg q[1];
s q[1];
cx q[0],q[1];
u3(pi*0.5,pi*0.3929191806,0) q[0];
u3(pi*0.5,pi*1.8929191806,0) q[1];

// Gate: CZ**0.2858383611880559
u3(pi*0.5,pi*1.0,pi*0.75) q[0];
u3(pi*0.5,pi*1.0,pi*1.25) q[3];
sx q[0];
cx q[0],q[3];
rx(pi*0.3570808194) q[0];
ry(pi*0.5) q[3];
cx q[3],q[0];
sxdg q[3];
s q[3];
cx q[0],q[3];
u3(pi*0.5,pi*0.3929191806,0) q[0];
u3(pi*0.5,pi*1.8929191806,0) q[3];

// Gate: CZ**0.2858383611880559
u3(pi*0.5,pi*1.0,pi*0.75) q[0];
u3(pi*0.5,pi*1.0,pi*1.25) q[2];
sx q[0];
cx q[0],q[2];
rx(pi*0.3570808194) q[0];
ry(pi*0.5) q[2];
cx q[2],q[0];
sxdg q[2];
s q[2];
cx q[0],q[2];
u3(pi*0.5,pi*0.3929191806,0) q[0];
u3(pi*0.5,pi*1.8929191806,0) q[2];

// Gate: CZ**0.2858383611880559
u3(pi*0.5,pi*1.0,pi*0.75) q[1];
u3(pi*0.5,pi*1.0,pi*1.25) q[2];
sx q[1];
cx q[1],q[2];
rx(pi*0.3570808194) q[1];
ry(pi*0.5) q[2];
cx q[2],q[1];
sxdg q[2];
s q[2];
cx q[1],q[2];
u3(pi*0.5,pi*0.3929191806,0) q[1];
u3(pi*0.5,pi*1.8929191806,0) q[2];

rx(pi*0.0931081293) q[0];

// Gate: CZ**0.2858383611880559
u3(pi*0.5,pi*1.0,pi*0.75) q[1];
u3(pi*0.5,pi*1.0,pi*1.25) q[3];
sx q[1];
cx q[1],q[3];
rx(pi*0.3570808194) q[1];
ry(pi*0.5) q[3];
cx q[3],q[1];
sxdg q[3];
s q[3];
cx q[1],q[3];
u3(pi*0.5,pi*0.3929191806,0) q[1];
u3(pi*0.5,pi*1.8929191806,0) q[3];

// Gate: CZ**0.2858383611880559
u3(pi*0.5,pi*1.0,pi*0.75) q[2];
u3(pi*0.5,pi*1.0,pi*1.25) q[3];
sx q[2];
cx q[2],q[3];
rx(pi*0.3570808194) q[2];
ry(pi*0.5) q[3];
cx q[3],q[2];
sxdg q[3];
s q[3];
cx q[2],q[3];
u3(pi*0.5,pi*0.3929191806,0) q[2];
u3(pi*0.5,pi*1.8929191806,0) q[3];

rx(pi*0.0931081293) q[1];
rx(pi*0.0931081293) q[2];
rx(pi*0.0931081293) q[3];

"""

aggressive.Fold(move.vmove)(problem3)
MoveScorer(problem3, expected_qasm=expected_qasm).animate()
print(MoveScorer(problem3, expected_qasm=expected_qasm).score())