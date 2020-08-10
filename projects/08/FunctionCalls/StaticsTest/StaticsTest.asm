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
// Writing push from constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1

// Writing push from constant 8
@8
D=A
@SP
A=M
M=D
@SP
M=M+1

// Calling function Class1.set
// push return address
// Writing push from constant Class1.set$return_address
@Class1.set$return_address
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
@7
D=D-A
@ARG
M=D
// Reposition LCL
@SP
D=M
@LCL
M=D
// Transfer control
@Class1.set
0;JMP
//return label
(Class1.set$return_address)
// Writing pop to temp 0
@SP
AM=M-1
D=M
@5
M=D

// Writing push from constant 23
@23
D=A
@SP
A=M
M=D
@SP
M=M+1

// Writing push from constant 15
@15
D=A
@SP
A=M
M=D
@SP
M=M+1

// Calling function Class2.set
// push return address
// Writing push from constant Class2.set$return_address
@Class2.set$return_address
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
@7
D=D-A
@ARG
M=D
// Reposition LCL
@SP
D=M
@LCL
M=D
// Transfer control
@Class2.set
0;JMP
//return label
(Class2.set$return_address)
// Writing pop to temp 0
@SP
AM=M-1
D=M
@5
M=D

// Calling function Class1.get
// push return address
// Writing push from constant Class1.get$return_address
@Class1.get$return_address
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
@Class1.get
0;JMP
//return label
(Class1.get$return_address)
// Calling function Class2.get
// push return address
// Writing push from constant Class2.get$return_address
@Class2.get$return_address
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
@Class2.get
0;JMP
//return label
(Class2.get$return_address)
// create label WHILE
(WHILE)

// goto WHILE
@WHILE
0;JMP

// function Class2.set with 0 locals
(Class2.set)
@0
D=A
@R13
M=D
(Class2.set$setup_locals)
@R13
MD=M-1
@Class2.set$locals_done
D;JLT
// Writing push from constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1


@Class2.set$setup_locals
D;JMP
(Class2.set$locals_done)
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

// Writing pop to static 0
@SP
AM=M-1
D=M
@Class2.0
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

// Writing pop to static 1
@SP
AM=M-1
D=M
@Class2.1
M=D

// Writing push from constant 0
@0
D=A
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
// function Class2.get with 0 locals
(Class2.get)
@0
D=A
@R13
M=D
(Class2.get$setup_locals)
@R13
MD=M-1
@Class2.get$locals_done
D;JLT
// Writing push from constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1


@Class2.get$setup_locals
D;JMP
(Class2.get$locals_done)
// Writing push from static 0
@Class2.0
D=M
@SP
A=M
M=D
@SP
M=M+1

// Writing push from static 1
@Class2.1
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
// function Class1.set with 0 locals
(Class1.set)
@0
D=A
@R13
M=D
(Class1.set$setup_locals)
@R13
MD=M-1
@Class1.set$locals_done
D;JLT
// Writing push from constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1


@Class1.set$setup_locals
D;JMP
(Class1.set$locals_done)
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

// Writing pop to static 0
@SP
AM=M-1
D=M
@Class1.0
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

// Writing pop to static 1
@SP
AM=M-1
D=M
@Class1.1
M=D

// Writing push from constant 0
@0
D=A
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
// function Class1.get with 0 locals
(Class1.get)
@0
D=A
@R13
M=D
(Class1.get$setup_locals)
@R13
MD=M-1
@Class1.get$locals_done
D;JLT
// Writing push from constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1


@Class1.get$setup_locals
D;JMP
(Class1.get$locals_done)
// Writing push from static 0
@Class1.0
D=M
@SP
A=M
M=D
@SP
M=M+1

// Writing push from static 1
@Class1.1
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
