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
// Writing push from constant 4000
@4000
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

// Writing push from constant 5000
@5000
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

// Calling function Sys.main
// push return address
// Writing push from constant Sys.main$return_address
@Sys.main$return_address
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
// Transfer control
@Sys.main
0;JMP
//return label
(Sys.main$return_address)
// Writing pop to temp 1
@SP
AM=M-1
D=M
@6
M=D

// create label LOOP
(LOOP)

// goto LOOP
@LOOP
0;JMP

// function Sys.main with 5 locals
(Sys.main)
@5
D=A
@R13
M=D
(Sys.main$setup_locals)
@R13
MD=M-1
@Sys.main$locals_done
D;JLT
// Writing push from constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1


@Sys.main$setup_locals
D;JMP
(Sys.main$locals_done)
// Writing push from constant 4001
@4001
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

// Writing push from constant 5001
@5001
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

// Writing push from constant 200
@200
D=A
@SP
A=M
M=D
@SP
M=M+1

// Writing pop to local 1
@LCL
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

// Writing push from constant 40
@40
D=A
@SP
A=M
M=D
@SP
M=M+1

// Writing pop to local 2
@LCL
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

// Writing push from constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1

// Writing pop to local 3
@LCL
D=M
@3
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

// Writing push from constant 123
@123
D=A
@SP
A=M
M=D
@SP
M=M+1

// Calling function Sys.add12
// push return address
// Writing push from constant Sys.add12$return_address
@Sys.add12$return_address
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
@Sys.add12
0;JMP
//return label
(Sys.add12$return_address)
// Writing pop to temp 0
@SP
AM=M-1
D=M
@5
M=D

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

// Writing push from local 2
@LCL
D=M
@2
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// Writing push from local 3
@LCL
D=M
@3
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// Writing push from local 4
@LCL
D=M
@4
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

 // Writing arithmetic command add
@SP
A=M-1
D=M
A=A-1
M=M+D
D=A+1
@SP
M=D

 // Writing arithmetic command add
@SP
A=M-1
D=M
A=A-1
M=M+D
D=A+1
@SP
M=D

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
// function Sys.add12 with 0 locals
(Sys.add12)
@0
D=A
@R13
M=D
(Sys.add12$setup_locals)
@R13
MD=M-1
@Sys.add12$locals_done
D;JLT
// Writing push from constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1


@Sys.add12$setup_locals
D;JMP
(Sys.add12$locals_done)
// Writing push from constant 4002
@4002
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

// Writing push from constant 5002
@5002
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

// Writing push from constant 12
@12
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
