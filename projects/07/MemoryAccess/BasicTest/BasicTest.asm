// Writing push from constant 10
@10
D=A
@SP
A=M
M=D
@SP
M=M+1

// Writing pop to local 0
// go to location to deposit
@LCL
D=M
@0
D=D+A
@R13
M=D
//get top of stack
@SP
AM=M-1
D=M
@R13
A=M
M=D

// Writing push from constant 21
@21
D=A
@SP
A=M
M=D
@SP
M=M+1

// Writing push from constant 22
@22
D=A
@SP
A=M
M=D
@SP
M=M+1

// Writing pop to argument 2
// go to location to deposit
@ARG
D=M
@2
D=D+A
@R13
M=D
//get top of stack
@SP
AM=M-1
D=M
@R13
A=M
M=D

// Writing pop to argument 1
// go to location to deposit
@ARG
D=M
@1
D=D+A
@R13
M=D
//get top of stack
@SP
AM=M-1
D=M
@R13
A=M
M=D

// Writing push from constant 36
@36
D=A
@SP
A=M
M=D
@SP
M=M+1

// Writing pop to this 6
// go to location to deposit
@THIS
D=M
@6
D=D+A
@R13
M=D
//get top of stack
@SP
AM=M-1
D=M
@R13
A=M
M=D

// Writing push from constant 42
@42
D=A
@SP
A=M
M=D
@SP
M=M+1

// Writing push from constant 45
@45
D=A
@SP
A=M
M=D
@SP
M=M+1

// Writing pop to that 5
// go to location to deposit
@THAT
D=M
@5
D=D+A
@R13
M=D
//get top of stack
@SP
AM=M-1
D=M
@R13
A=M
M=D

// Writing pop to that 2
// go to location to deposit
@THAT
D=M
@2
D=D+A
@R13
M=D
//get top of stack
@SP
AM=M-1
D=M
@R13
A=M
M=D

// Writing push from constant 510
@510
D=A
@SP
A=M
M=D
@SP
M=M+1


// Writing pop to temp 6
@SP
AM=M-1
D=M
@11
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

// Writing push from that 5
@THAT
D=M
@5
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

// Writing push from this 6
@THIS
D=M
@6
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// Writing push from this 6
@THIS
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

 // Writing arithmetic command sub
@SP
A=M-1
D=M
A=A-1
M=M-D
D=A+1
@SP
M=D

// Writing push from temp 6
@11
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

