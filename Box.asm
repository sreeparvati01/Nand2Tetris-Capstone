// Box.asm (K = 36)
// Box starts at row 36, is 20 rows tall, and is 16 pixels wide (1 word).
// While a key is pressed the box is black; when released it is erased.

(LOOP)
    // Default to white (erase the box).
    @color
    M=0
    @KBD
    D=M
    @DRAW
    D;JEQ

    // A pressed key makes the box black.
    @color
    M=-1

(DRAW)
    // SCREEN + 32 * 36 = 17536 (first word of row 36).
    @17536
    D=A
    @addr
    M=D

    // Draw 20 screen rows.
    @20
    D=A
    @rows
    M=D

(ROWLOOP)
    @color
    D=M
    @addr
    A=M
    M=D         // One 16-pixel word per row.

    // Move to the same word position in the next screen row.
    @32
    D=A
    @addr
    M=D+M

    // Decrement row counter and repeat until all 20 rows are done.
    @rows
    M=M-1
    D=M
    @ROWLOOP
    D;JGT

    @LOOP
    0;JMP
