from bloqade import move
from kirin.passes import aggressive
from iquhack_scoring import MoveScorer
from math import pi



@move.vmove
def problem_2_cirq():
    # Initialization (instruction id 0):
    q = move.NewQubitRegister(3)
    state = move.Init(qubits=[q[0], q[1], q[2]], indices=[3, 1, 0])

    # For qubits in storage (indices ['3', '1', '0']), move to gate
    state.gate[[3, 1, 0]] = move.Move(state.storage[[3, 1, 0]])
    # Apply LocalRz with phi=1.5707963267948966 on indices ['0', '1', '3']
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[0, 1, 3])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=5.431511377569149 on indices ['0', '1', '3']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=5.431511377569149, indices=[0, 1, 3])
    state = move.LocalRz(atom_state=state,phi=0.8516739296104372,indices=[0, 1, 3])

    # Rearrangement job (id 2):
    #  Move (storage -> gate): transferring qubits from ['0', '1'] to ['0', '0']
    state.gate[[0, 0]] = move.Move(state.storage[[0, 1]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [1, 0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1]

    # Rydberg gate (id 0): between qubit 1 and 2
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q1 and q2

    # Apply LocalRz with phi=0.7853981633974483 on indices ['0']
    state = move.LocalRz(atom_state=state,phi=0.7853981633974483,indices=[0])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=5.162526767865374 on indices ['0']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=5.162526767865374, indices=[0])
    state = move.LocalRz(atom_state=state,phi=1.1206585393142123,indices=[0])

    # Rydberg gate (id 1): between qubit 1 and 2
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q1 and q2

    # Apply LocalRz with phi=2.6914548661091087 on indices ['0', '0']
    state = move.LocalRz(atom_state=state,phi=2.6914548661091087,indices=[0, 0])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=1.5707963267948966 on indices ['0', '0']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=1.5707963267948966, indices=[0, 0])
    state = move.LocalRz(atom_state=state,phi=4.262251192904006,indices=[0, 0])

    # Rearrangement job (id 7):
    #  Move (gate -> storage): transferring qubits from ['0'] to ['2']
    state.storage[[2]] = move.Move(state.gate[[0]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 8):
    #  Move (storage -> gate): transferring qubits from ['3'] to ['0']
    state.gate[[0]] = move.Move(state.storage[[3]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 2): between qubit 0 and 2
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q2

    # Apply LocalRz with phi=5.890486225480862 on indices ['0']
    state = move.LocalRz(atom_state=state,phi=5.890486225480862,indices=[0])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=3.8607150507742523 on indices ['0']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=3.8607150507742523, indices=[0])
    state = move.LocalRz(atom_state=state,phi=2.4224702564053335,indices=[0])

    # Rydberg gate (id 3): between qubit 0 and 2
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q2

    # Apply LocalRz with phi=2.8852397850744724 on indices ['0', '0']
    state = move.LocalRz(atom_state=state,phi=2.8852397850744724,indices=[0, 0])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=0.9754752656997802 on indices ['0', '0']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=0.9754752656997802, indices=[0, 0])
    state = move.LocalRz(atom_state=state,phi=2.4224702564053335,indices=[0, 0])

    # Rearrangement job (id 13):
    #  Move (gate -> storage): transferring qubits from ['0'] to ['0']
    state.storage[[0]] = move.Move(state.gate[[0]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 14):
    #  Move (storage -> gate): transferring qubits from ['2'] to ['0']
    state.gate[[0]] = move.Move(state.storage[[2]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 4): between qubit 0 and 1
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q1

    # Apply LocalRz with phi=0.7853981633974483 on indices ['0']
    state = move.LocalRz(atom_state=state,phi=0.7853981633974483,indices=[0])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=4.117067919289573 on indices ['0']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=4.117067919289573, indices=[0])
    state = move.LocalRz(atom_state=state,phi=2.166117387890013,indices=[0])

    # Rydberg gate (id 5): between qubit 0 and 1
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q1

    # Apply LocalRz with phi=0.5953210610951164 on indices ['0', '0']
    state = move.LocalRz(atom_state=state,phi=0.5953210610951164,indices=[0, 0])
    # Apply LocalXY with x_exponent=-1.5707963267948966 and axis_phase_exponent=1.5707963267948966 on indices ['0', '0']
    state = move.LocalXY(atom_state=state, x_exponent=-1.5707963267948966, axis_phase_exponent=1.5707963267948966, indices=[0, 0])
    state = move.LocalRz(atom_state=state,phi=2.166117387890013,indices=[0, 0])

    # Rearrangement job (id 19):
    #  Move (gate -> storage): transferring qubits from ['0', '0'] to ['1', '2']
    state.storage[[1, 2]] = move.Move(state.gate[[0, 0]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [1, 0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1]

    move.Execute(state)

expected_qasm = """OPENQASM 2.0;
include "qelib1.inc";


// Qubits: [q(0), q(1), q(2)]
qreg q[3];


h q[2];

// Operation: CRz(0.5π)(q(1), q(2))
cx q[1],q[2];
u3(0,pi*1.25,pi*0.5) q[2];
cx q[1],q[2];
u3(0,pi*1.75,pi*0.5) q[2];

// Operation: CRz(0.25π)(q(0), q(2))
cx q[0],q[2];
u3(0,pi*1.375,pi*0.5) q[2];
cx q[0],q[2];
u3(0,pi*1.625,pi*0.5) q[2];

h q[1];

// Operation: CRz(0.5π)(q(0), q(1))
cx q[0],q[1];
u3(0,pi*1.25,pi*0.5) q[1];
cx q[0],q[1];
u3(0,pi*1.75,pi*0.5) q[1];

h q[0];

"""

aggressive.Fold(move.vmove)(problem_2_cirq)
MoveScorer(problem_2_cirq, expected_qasm=expected_qasm).animate()
print(MoveScorer(problem_2_cirq, expected_qasm=expected_qasm).score())