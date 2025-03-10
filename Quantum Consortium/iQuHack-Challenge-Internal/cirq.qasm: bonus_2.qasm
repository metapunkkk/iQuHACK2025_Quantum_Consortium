// Generated from Cirq v1.4.1

OPENQASM 2.0;
include "qelib1.inc";


// Qubits: [q_0, q_1, q_2, q_3, q_4, q_5, q_6, q_7, q_8, q_9, q_10, q_11, q_12, q_13, q_14, q_15, q_16]
qreg q[17];


u3(pi*1.5,0,0) q[0];
u3(pi*1.5,0,0) q[5];
u3(pi*1.5,0,0) q[11];
u3(pi*0.5,0,0) q[12];
u3(pi*0.5,0,0) q[10];
u3(pi*0.5,0,0) q[7];
u3(pi*0.5,0,0) q[9];
u3(pi*0.5,0,0) q[6];
u3(pi*0.5,0,0) q[14];
u3(pi*0.5,0,0) q[4];
u3(pi*0.5,0,0) q[1];
u3(pi*0.5,0,0) q[16];
u3(pi*0.5,0,0) q[13];
cz q[0],q[3];
cz q[5],q[8];
cz q[11],q[15];
cz q[4],q[7];
cz q[6],q[9];
cz q[10],q[14];
u3(pi*0.5,0,0) q[11];
u3(pi*0.5,0,0) q[15];
u3(pi*0.5,0,0) q[5];
cz q[0],q[2];
u3(pi*1.0,0,0) q[10];
u3(pi*0.5,pi*1.0,0) q[7];
u3(pi*0.5,pi*1.0,0) q[9];
u3(pi*1.5,0,0) q[8];
u3(pi*0.5,pi*1.0,0) q[14];
u3(pi*1.5,0,0) q[3];
u3(pi*1.0,0,0) q[6];
u3(pi*1.0,0,0) q[4];
cz q[12],q[15];
u3(pi*0.5,0,0) q[0];
u3(pi*1.5,0,0) q[11];
u3(pi*1.5,0,0) q[5];
cz q[1],q[4];
cz q[3],q[6];
cz q[8],q[10];
u3(pi*1.0,0,0) q[12];
u3(pi*0.5,pi*1.0,0) q[15];
cz q[5],q[7];
cz q[11],q[14];
u3(pi*1,0,0) q[8];
u3(pi*0.5,0,0) q[3];
u3(pi*1.5,0,0) q[1];
u3(pi*0.5,0,0) q[4];
cz q[10],q[13];
u3(pi*1,0,0) q[11];
u3(pi*1,0,0) q[5];
cz q[6],q[8];
cz q[14],q[16];
u3(0,pi*0.5,pi*0.5) q[10];
u3(pi*0.5,0,0) q[7];
u3(pi*0.5,pi*1.0,pi*1.0) q[13];
cz q[2],q[5];
cz q[9],q[11];
u3(pi*0.5,pi*1.0,pi*1.0) q[8];
u3(0,pi*0.5,pi*0.5) q[14];
u3(0,pi*0.5,pi*0.5) q[6];
cz q[7],q[10];
cz q[13],q[16];
u3(pi*0.5,0,pi*1.0) q[9];
u3(pi*0.5,0,pi*1.0) q[2];
cz q[1],q[5];
cz q[8],q[11];
u3(pi*0.5,0,0) q[10];
u3(pi*0.5,pi*1.0,pi*1.0) q[16];
u3(pi*1.5,0,0) q[7];
u3(0,pi*0.5,pi*0.5) q[13];
cz q[2],q[6];
cz q[9],q[12];
u3(pi*0.5,pi*1.0,pi*1.0) q[11];
u3(0,pi*0.5,pi*0.5) q[8];
u3(0,pi*0.5,pi*0.5) q[1];
u3(pi*0.5,pi*1.0,pi*1.0) q[5];
u3(pi*0.5,0,0) q[12];
u3(pi*1.5,0,0) q[9];
u3(pi*1.5,0,0) q[2];
u3(pi*0.5,0,0) q[6];
