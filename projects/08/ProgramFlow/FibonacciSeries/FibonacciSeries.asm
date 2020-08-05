// Writing push from argument 1
@ARG
D=M
@1
A=D+A
D=M
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

// Writing push from constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// Writing pop to that 0
@THAT
D=M
@0
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

// Writing push from constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// Writing pop to that 1
@THAT
D=M
@1
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

// Writing push from argument 0
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// Writing push from constant 2
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

// Writing pop to argument 0
@ARG
D=M
@0
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

// create label MAIN_LOOP_START
(MAIN_LOOP_START)

// Writing push from argument 0
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// if goto COMPUTE_ELEMENT
@SP
AM=M-1
D=M
@COMPUTE_ELEMENT
D;JGT

// goto END_PROGRAM
@END_PROGRAM
0;JMP

// create label COMPUTE_ELEMENT
(COMPUTE_ELEMENT)

// Writing push from that 0
@THAT
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// Writing push from that 1
@THAT
D=M
@1
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

// Writing pop to that 2
@THAT
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

// Writing push from pointer 1
@4
D=M
@SP
A=M
M=D
@SP
M=M+1

// Writing push from constant 1
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

// Writing pop to pointer 1
@SP
AM=M-1
D=M
@4
M=D

// Writing push from argument 0
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// Writing push from constant 1
@1
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

// Writing pop to argument 0
@ARG
D=M
@0
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

// goto MAIN_LOOP_START
@MAIN_LOOP_START
0;JMP

// create label END_PROGRAM
(END_PROGRAM)

