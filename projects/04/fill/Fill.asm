// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// Screen max size
@8191
D=A
@screenSize
M=D

// create temp variable to check if pressed key matches current temp if
// don't match move to loop also set fill color in another temp location
(KEYLOOP)
@lastKey
D=A
@KBD

//check if keys don't match and jump out
D=D-M
@FILLSCREEN
D;JNE
@KEYLOOP
0;JMP

// run fill loop
(FILLSCREEN)
@i
M=0
@color
M=0
@KBD
D=M
@PAINT
D;JEQ
@color
M=-1

(PAINT)
@i
D=M
@SCREEN
D=D+A
@currentFill
M=D
@color
D=M
@currentFill
A=M
M=D

//If iterator greater than screensize break loop
@i
M=M+1
D=M
@screenSize
D=D-M
@PAINT
D;JLE

@KEYLOOP
0;JMP