import math
from bloqade import move
from kirin.passes import aggressive
from iquhack_scoring import MoveScorer

pi = math.pi

@move.vmove
def u3_gate(state: move.core.AtomState, theta: float, phi: float, lam: float, index: int) -> move.core.AtomState:
    # Move the qubit from storage to gate zone
    state.gate[[index]] = move.Move(state.storage[[index]])
    # Apply Rz(phi)
    state = move.LocalRz(state, phi, indices=[index])
    # Apply LocalXY with exponent theta and fixed axis_phase_exponent=0.5
    state = move.LocalXY(state, theta, 0.5, indices=[index])
    # Apply Rz(lam)
    state = move.LocalRz(state, lam, indices=[index])
    # Move the qubit back to storage
    state.storage[[index]] = move.Move(state.gate[[index]])
    return state

@move.vmove
def cz_gate(state: move.core.AtomState, q1: int, q2: int) -> move.core.AtomState:
    # Move both qubits into the gate zone
    state.gate[[q1, q2]] = move.Move(state.storage[[q1, q2]])
    # Apply GlobalCZ
    state = move.GlobalCZ(state)
    # Move them back to storage
    state.storage[[q1, q2]] = move.Move(state.gate[[q1, q2]])
    return state

@move.vmove
def main():

    q = move.NewQubitRegister(7)
    state = move.Init(
        qubits=[q[0], q[1], q[2], q[3], q[4], q[5], q[6]],
        indices=[0, 1, 2, 3, 4, 5, 6]
    )
    # --- Apply u3 Gates ---
    state = u3_gate(state, 1.5*pi, 0.0, 0.0, 5)              # u3(pi*1.5,0,0) q[5];
    state = u3_gate(state, 0.5*pi, 0.0, 0.0, 0)              # u3(pi*0.5,0,0) q[0];
    state = u3_gate(state, 0.5*pi, 0.0, 0.0, 3)              # u3(pi*0.5,0,0) q[3];
    state = u3_gate(state, 0.5*pi, 0.0, 0.0, 1)              # u3(pi*0.5,0,0) q[1];
    state = u3_gate(state, 0.5*pi, 0.0, 0.0, 2)              # u3(pi*0.5,0,0) q[2];
    state = u3_gate(state, 0.5*pi, 0.0, 0.0, 4)              # u3(pi*0.5,0,0) q[4];
    # --- Apply CZ Gates ---
    state = cz_gate(state, 5, 6)                         # cz q[5],q[6];
    state = cz_gate(state, 0, 1)                         # cz q[0],q[1];
    state = cz_gate(state, 2, 4)                         # cz q[2],q[4];
    # --- u3 Gates ---
    state = u3_gate(state, 1*pi, 0.0, 0.0, 5)               # u3(pi*1,0,0) q[5];
    state = u3_gate(state, 1*pi, 0.5*pi, 1.5*pi, 0)      # u3(pi*1,pi*0.5,pi*1.5) q[0];
    state = u3_gate(state, 1.0*pi, 0.0, 0.0, 2)             # u3(pi*1.0,0,0) q[2];
    state = u3_gate(state, 1.0*pi, 0.0, 0.0, 1)             # u3(pi*1.0,0,0) q[1];
    state = u3_gate(state, 1*pi, 0.5*pi, 1.5*pi, 4)      # u3(pi*1,pi*0.5,pi*1.5) q[4];
    # --- CZ Gates ---
    state = cz_gate(state, 3, 5)                         # cz q[3],q[5];
    state = cz_gate(state, 0, 2)                         # cz q[0],q[2];
    state = cz_gate(state, 4, 6)                         # cz q[4],q[6];
    # --- u3 Gates ---
    state = u3_gate(state, 1.0*pi, 0.0, 0.0, 3)             # u3(pi*1.0,0,0) q[3];
    state = u3_gate(state, 0.0, 0.0, 1.0*pi, 5)             # u3(0,0,pi*1.0) q[5];
    state = u3_gate(state, 0.5*pi, 0.0, 0.0, 0)             # u3(pi*0.5,0,0) q[0];
    state = u3_gate(state, 0.5*pi, 0.0, 0.0, 6)             # u3(pi*0.5,0,0) q[6];
    state = u3_gate(state, 1.0*pi, 0.0, 0.0, 4)               # u3(pi*1,0,0) q[4];
    # --- CZ Gates ---
    state = cz_gate(state, 1, 5)                         # cz q[1],q[5];
    state = cz_gate(state, 2, 6)                         # cz q[2],q[6];
    state = cz_gate(state, 3, 4)                         # cz q[3],q[4];
    # --- u3 Gates ---
    state = u3_gate(state, 1.5*pi, 0.0, 0.0, 0)             # u3(pi*1.5,0,0) q[0];
    state = u3_gate(state, 0.0, 0.5*pi, 0.5*pi, 1)         # u3(0,pi*0.5,pi*0.5) q[1];
    state = u3_gate(state, 0.5*pi, 1.0*pi, 1.0*pi, 5)    # u3(pi*0.5,pi*1.0,pi*1.0) q[5];
    state = u3_gate(state, 0.0, 0.5*pi, 0.5*pi, 3)         # u3(0,pi*0.5,pi*0.5) q[3];
    state = u3_gate(state, 0.0, 0.5*pi, 0.5*pi, 2)         # u3(0,pi*0.5,pi*0.5) q[2];
    state = u3_gate(state, 0.5*pi, 1.0*pi, 1.0*pi, 4)    # u3(pi*0.5,pi*1.0,pi*1.0) q[4];
    # --- CZ Gates ---
    state = cz_gate(state, 1, 6)                         # cz q[1],q[6];
    state = cz_gate(state, 0, 3)                         # cz q[0],q[3];
    # --- u3 Gates ---
    state = u3_gate(state, 0.5*pi, 0.0, 0.0, 0)             # u3(pi*0.5,0,0) q[0];
    state = u3_gate(state, 0.0, 0.5*pi, 0.5*pi, 1)         # u3(0,pi*0.5,pi*0.5) q[1];
    state = u3_gate(state, 0.5*pi, 1.0*pi, 1.0*pi, 6)    # u3(pi*0.5,pi*1.0,pi*1.0) q[6];
    
    move.Execute(state)
    return state

expected_qasm = """OPENQASM 2.0;
include "qelib1.inc";

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

# Aggressively inline all subroutines so that the final QASM is flat.
aggressive.Fold(move.vmove)(main)

# Animate and score the circuit.
MoveScorer(main, expected_qasm=expected_qasm).animate()
print(MoveScorer(main, expected_qasm=expected_qasm).score())