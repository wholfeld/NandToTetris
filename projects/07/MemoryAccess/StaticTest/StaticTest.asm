// Writing push from constant 111
@111
D=A
@SP
A=M
M=D
@SP
M=M+1

// Writing push from constant 333
@333
D=A
@SP
A=M
M=D
@SP
M=M+1

// Writing push from constant 888
@888
D=A
@SP
A=M
M=D
@SP
M=M+1

// Writing pop to static 8
@SP
AM=M-1
D=M
@24
M=D

// Writing pop to static 3
@SP
AM=M-1
D=M
@19
M=D

// Writing pop to static 1
@SP
AM=M-1
D=M
@17
M=D

// Writing push from static 3
@19
D=M
@SP
A=M
M=D
@SP
M=M+1

// Writing push from static 1
@17
D=M
@SP
A=M
M=D
@SP
M=M+1

 // Writing arithmetic command sub
@SP
A=M-1
D=M
A=A-1
M=M-D
D=A+1
@SP
M=D

// Writing push from static 8
@24
D=M
@SP
A=M
M=D
@SP
M=M+1

 // Writing arithmetic command add
@SP
A=M-1
D=M
A=A-1
M=M+D
D=A+1
@SP
M=D

