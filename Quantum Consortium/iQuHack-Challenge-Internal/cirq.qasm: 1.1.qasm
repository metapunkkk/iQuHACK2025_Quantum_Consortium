// Generated from Cirq v1.4.1

OPENQASM 2.0;
include "qelib1.inc";


// Qubits: [q_0, q_1, q_2]
qreg q[3];


cz q[0],q[1];
u3(pi*1.5,0,0) q[1];
cz q[1],q[2];
u3(pi*0.5,0,0) q[1];
