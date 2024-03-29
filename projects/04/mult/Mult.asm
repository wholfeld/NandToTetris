// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
// Zero out R2
@R2
M=D

(LOOP)
// Check if multiplier is 0
@R1
D=M
// If 0 jump to end
@END
D;JEQ
// Subract 1 from multiplier
@R1
M=D-1
// Take multiplicand and add it to R2
@R0
D=M
@R2
M=D+M
// Repeat
@LOOP
0;JMP

(END)
@END
0;JMP