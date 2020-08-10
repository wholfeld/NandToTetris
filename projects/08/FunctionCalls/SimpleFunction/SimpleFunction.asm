// function SimpleFunction.test with 2 locals
@2
D=A
@R13
M=D
(SimpleFunction.test$setup_locals)
@R13
MD=M-1
@SimpleFunction.test$locals_done
D;JLT
// Writing push from constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1


@SimpleFunction.test$setup_locals
D;JMP
(SimpleFunction.test$locals_done)
// Writing push from local 0
@LCL
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// Writing push from local 1
@LCL
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

 // Writing single operand not
@SP
A=M-1
M=!M
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

 // Writing arithmetic command add
@SP
A=M-1
D=M
A=A-1
M=M+D
D=A+1
@SP
M=D

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

 // Writing arithmetic command sub
@SP
A=M-1
D=M
A=A-1
M=M-D
D=A+1
@SP
M=D

// writing return
//setup local as frame as R13
@LCL
D=M
@R13
M=D
//put return address in variable
@5
A=D-A
D=M
@R14
M=D
//Reposition the return value for the caller
@SP
A=M-1
D=M
@ARG
A=M
M=D
//Restore SP of the caller
D=A+1
@SP
M=D
//Restore THAT of the caller
@R13
A=M-1
D=M
@THAT
M=D
//Restore THIS of the caller
@R13
D=M
@2
A=D-A
D=M
@THIS
M=D
//Restore ARG of the caller
@R13
D=M
@3
A=D-A
D=M
@ARG
M=D
//Restore LCL of the caller
@R13
D=M
@4
A=D-A
D=M
@LCL
M=D
//Goto return-address (in the caller's code)
@R14
A=M
0;JMP
