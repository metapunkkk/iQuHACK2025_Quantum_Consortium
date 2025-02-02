// Generated from Cirq v1.4.1

OPENQASM 2.0;
include "qelib1.inc";


// Qubits: [q_0, q_1, q_2, q_3, q_4, q_5, q_6, q_7, q_8]
qreg q[9];


u3(pi*1.5,0,0) q[3];
u3(pi*0.5,0,0) q[6];
u3(pi*0.5,0,0) q[4];
u3(pi*0.5,0,0) q[1];
u3(pi*0.5,0,0) q[7];
u3(pi*0.5,0,0) q[5];
u3(pi*0.5,0,0) q[2];
u3(pi*0.5,0,0) q[8];
cz q[0],q[3];
u3(0,pi*0.5,pi*0.5) q[3];
cz q[0],q[6];
u3(pi*0.5,0,0) q[0];
u3(pi*1,pi*0.5,pi*1.5) q[6];
cz q[3],q[4];
u3(0,pi*0.5,pi*0.5) q[3];
u3(pi*0.5,pi*1.0,pi*1.0) q[4];
cz q[0],q[1];
cz q[6],q[7];
cz q[3],q[5];
u3(0,pi*0.5,pi*0.5) q[0];
u3(pi*0.5,pi*1.0,pi*1.0) q[1];
u3(pi*0.5,pi*1.0,pi*1.0) q[7];
u3(0,pi*0.5,pi*0.5) q[6];
u3(0,pi*0.5,pi*0.5) q[3];
u3(pi*0.5,pi*1.0,pi*1.0) q[5];
cz q[0],q[2];
cz q[6],q[8];
u3(0,pi*0.5,pi*0.5) q[0];
u3(pi*0.5,pi*1.0,pi*1.0) q[2];
u3(pi*0.5,pi*1.0,pi*1.0) q[8];
u3(0,pi*0.5,pi*0.5) q[6];
