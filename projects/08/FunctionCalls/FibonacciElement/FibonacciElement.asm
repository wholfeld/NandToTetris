//init function
@256
D=A
@SP
M=D
// push return address
// Writing push from constant 256
@256
D=A
@SP
A=M
M=D
@SP
M=M+1


// Save LCL of the calling function
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// Save ARG of the calling function
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// Save THIS of the calling function
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// Save THAT of the calling function
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// Repostion ARG for current args
@SP
D=M
@5
D=D-A
@ARG
M=D
// Reposition LCL
@SP
D=M
@LCL
M=D
// Writing push from constant 4
@4
D=A
@SP
A=M
M=D
@SP
M=M+1

// Calling function Main.fibonacci0
// push return address
// Writing push from constant Main.fibonacci0$return_address
@Main.fibonacci0$return_address
D=A
@SP
A=M
M=D
@SP
M=M+1


// Save LCL of the calling function
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// Save ARG of the calling function
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// Save THIS of the calling function
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// Save THAT of the calling function
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// Repostion ARG for current args
@SP
D=M
@6
D=D-A
@ARG
M=D
// Reposition LCL
@SP
D=M
@LCL
M=D
// Transfer control
@Main.fibonacci
0;JMP
//return label
(Main.fibonacci0$return_address)
// create label WHILE
(WHILE)

// goto WHILE
@WHILE
0;JMP

// function Main.fibonacci with 0 locals
(Main.fibonacci)
@0
D=A
@R13
M=D
(Main.fibonacci$setup_locals)
@R13
MD=M-1
@Main.fibonacci$locals_done
D;JLT
// Writing push from constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1


@Main.fibonacci$setup_locals
D;JMP
(Main.fibonacci$locals_done)
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

 // Writing comparative command lt
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@JUMPTRUE0
D;JLT
@SP
A=M
M=0
@END0
0;JMP
(JUMPTRUE0)
@SP
A=M
M=-1
(END0)
@SP
M=M+1

// if goto IF_TRUE
@SP
AM=M-1
D=M
@IF_TRUE
D;JNE

// goto IF_FALSE
@IF_FALSE
0;JMP

// create label IF_TRUE
(IF_TRUE)

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
// create label IF_FALSE
(IF_FALSE)

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

// Calling function Main.fibonacci1
// push return address
// Writing push from constant Main.fibonacci1$return_address
@Main.fibonacci1$return_address
D=A
@SP
A=M
M=D
@SP
M=M+1


// Save LCL of the calling function
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// Save ARG of the calling function
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// Save THIS of the calling function
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// Save THAT of the calling function
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// Repostion ARG for current args
@SP
D=M
@6
D=D-A
@ARG
M=D
// Reposition LCL
@SP
D=M
@LCL
M=D
// Transfer control
@Main.fibonacci
0;JMP
//return label
(Main.fibonacci1$return_address)
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

// Calling function Main.fibonacci2
// push return address
// Writing push from constant Main.fibonacci2$return_address
@Main.fibonacci2$return_address
D=A
@SP
A=M
M=D
@SP
M=M+1


// Save LCL of the calling function
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// Save ARG of the calling function
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// Save THIS of the calling function
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// Save THAT of the calling function
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// Repostion ARG for current args
@SP
D=M
@6
D=D-A
@ARG
M=D
// Reposition LCL
@SP
D=M
@LCL
M=D
// Transfer control
@Main.fibonacci
0;JMP
//return label
(Main.fibonacci2$return_address)
 // Writing arithmetic command add
@SP
A=M-1
D=M
A=A-1
M=M+D
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
