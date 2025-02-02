// Generated from Cirq v1.4.1

OPENQASM 2.0;
include "qelib1.inc";


// Qubits: [q_0, q_1, q_2]
qreg q[3];


u3(pi*1.5,pi*1.1432833079,pi*0.8567166921) q[1];
u3(pi*0.5,0,0) q[2];
u3(pi*0.5,pi*1.7289037684,pi*0.2710962316) q[0];
cz q[1],q[2];
u3(pi*0.25,pi*1.6432833079,pi*0.3567166921) q[1];
cz q[1],q[2];
u3(pi*1,pi*1.625,pi*0.375) q[2];
u3(pi*0.8567166921,pi*0.5,pi*1.3567166921) q[1];
cz q[0],q[2];
u3(pi*1.875,pi*1.2289037684,pi*0.7710962316) q[0];
cz q[0],q[2];
u3(pi*0.9184003476,pi*0.3105034208,pi*0.7710962316) q[0];
u3(0,pi*1.625,pi*0.5) q[2];
cz q[0],q[1];
u3(pi*0.25,pi*1.3105034208,pi*0.6894965792) q[0];
cz q[0],q[1];
u3(pi*0.1894965792,pi*0.5,pi*0.6894965792) q[0];
u3(0,pi*1.75,pi*0.5) q[1];
