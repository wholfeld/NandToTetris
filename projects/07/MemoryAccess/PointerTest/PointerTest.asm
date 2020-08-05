// Writing push from constant 3030
@3030
D=A
@SP
A=M
M=D
@SP
M=M+1

// Writing pop to pointer 0
@SP
AM=M-1
D=M
@3
M=D

// Writing push from constant 3040
@3040
D=A
@SP
A=M
M=D
@SP
M=M+1

// Writing pop to pointer 1
@SP
AM=M-1
D=M
@4
M=D

// Writing push from constant 32
@32
D=A
@SP
A=M
M=D
@SP
M=M+1

// Writing pop to this 2
@THIS
D=M
@2
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

// Writing push from constant 46
@46
D=A
@SP
A=M
M=D
@SP
M=M+1

// Writing pop to that 6
@THAT
D=M
@6
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

// Writing push from pointer 0
@3
D=M
@SP
A=M
M=D
@SP
M=M+1

// Writing push from pointer 1
@4
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

// Writing push from this 2
@THIS
D=M
@2
A=D+A
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

// Writing push from that 6
@THAT
D=M
@6
A=D+A
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

