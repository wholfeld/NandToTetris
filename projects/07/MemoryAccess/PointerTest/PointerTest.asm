// Writing push from constant 3030
@3030
D=A
@SP
A=M
M=D
@SP
M=M+1
// Writing pop to pointer 0

// Writing push from constant 3040
@3040
D=A
@SP
A=M
M=D
@SP
M=M+1
// Writing pop to pointer 1

// Writing push from constant 32
@32
D=A
@SP
A=M
M=D
@SP
M=M+1
// Writing pop to this 2

// Writing push from constant 46
@46
D=A
@SP
A=M
M=D
@SP
M=M+1
// Writing pop to that 6

// Writing push from pointer 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// Writing push from pointer 1
@1
D=A
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
// Writing push from this 2
@2
D=A
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
// Writing push from that 6
@6
D=A
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
