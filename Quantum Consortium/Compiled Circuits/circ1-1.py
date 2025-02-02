from bloqade import move
from kirin.passes import aggressive
from iquhack_scoring import MoveScorer
from math import pi



from bloqade import move

@move.vmove
def problem_1part1_cirq():
    # Initialization (instruction id 0):
    q = move.NewQubitRegister(3)
    state = move.Init(qubits=[q[0], q[1], q[2]], indices=[2, 1, 0])

    # Rearrangement job (id 1):
    #  Move (storage -> gate): transferring qubits from ['1', '2'] to ['2', '3']
    state.gate[[2, 3]] = move.Move(state.storage[[1, 2]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [1, 0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1]

    # Rydberg gate (id 0): between qubit 0 and 1
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q0 and q1

    # Apply LocalRz with phi=4.71238898038469 on indices ['1']
    state = move.LocalRz(atom_state=state,phi=4.71238898038469,indices=[1])

    # Rearrangement job (id 4):
    #  Move (gate -> storage): transferring qubits from ['3'] to ['2']
    state.storage[[2]] = move.Move(state.gate[[3]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rearrangement job (id 5):
    #  Move (storage -> gate): transferring qubits from ['0'] to ['3']
    state.gate[[3]] = move.Move(state.storage[[0]])  # storage to gate move
    #  Activate: row_id: [0], col_id: [0]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0]

    # Rydberg gate (id 1): between qubit 1 and 2
    state = move.GlobalCZ(atom_state=state)  # placeholder for rydberg gate between q1 and q2

    # Apply LocalRz with phi=1.5707963267948966 on indices ['1']
    state = move.LocalRz(atom_state=state,phi=1.5707963267948966,indices=[1])

    # Rearrangement job (id 8):
    #  Move (gate -> storage): transferring qubits from ['2', '3'] to ['1', '3']
    state.storage[[1, 3]] = move.Move(state.gate[[2, 3]])  # gate to storage move
    #  Activate: row_id: [0], col_id: [0, 1]
    #  (Sub-instruction type 'move:big' not specifically handled)
    #  Deactivate: row_id: [0], col_id: [0, 1]

    move.Execute(state)

expected_qasm = """OPENQASM 2.0;
include "qelib1.inc";


// Qubits: [q(0), q(1), q(2)]
qreg q[3];


cz q[0],q[1];
cx q[2],q[1];

"""

aggressive.Fold(move.vmove)(problem_1part1_cirq)
MoveScorer(problem_1part1_cirq, expected_qasm=expected_qasm).animate()
print(MoveScorer(problem_1part1_cirq, expected_qasm=expected_qasm).score())