from iquhack_scoring import MoveScorer
from bloqade import move
from kirin.passes import aggressive
import math

# Solution to Circuit 1.1

pi = math.pi

@move.vmove
def main():
    q = move.NewQubitRegister(3)

    state = move.Init(qubits=[q[0],q[1],q[2]], indices=[0,1,3])
    state.gate[[0,1,3]] = move.Move(state.storage[[0,1,3]])
    state = move.GlobalCZ(atom_state=state)
    state.gate[[2]] = move.Move(state.gate[[1]])
    state = move.LocalXY(atom_state=state,
                         x_exponent=0.5 * pi,
                         axis_phase_exponent=0.5 * pi, 
                         indices=[2])
    state = move.GlobalCZ(atom_state=state)
    state = move.LocalXY(atom_state=state,
                         x_exponent=-0.5 * pi,
                         axis_phase_exponent=0.5 * pi,
                        indices=[2])
    move.Execute(state)

expected_qasm = """
// Generated from Cirq v1.4.1

OPENQASM 2.0;
include "qelib1.inc";


// Qubits: [q(0), q(1), q(2)]
qreg q[3];


cz q[0],q[1];
cx q[2],q[1];
"""

aggressive.Fold(move.vmove)(main)

scorer = MoveScorer(main, expected_qasm)
score = scorer.score()
print(score)