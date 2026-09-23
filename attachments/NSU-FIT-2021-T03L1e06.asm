asect  0x00

# =================================
# INSERT YOUR CODE BELOW
# Executable instructions only
# No dc or ds pseudo-instructions
# Do not include a halt instruction: that has been done already (below)
# ---------------------------------------------------------------------
ldi r0, content
ldi r1, length
ld r1, r1
ldi r2, 0
while 
	cmp r2, r1
	stays lt
	ld r0, r3
	if 
		tst r3
		 is z
			ldi r1, zer
			ld r1, r3
			inc r3
			st r1, r3
		else 
			if
				tst r3
				is lt
					ldi r1, neg
					ld r1, r3
					inc r3
					st r1, r3
				else 
					ldi r1, pos
					ld r1, r3
					inc r3
					st r1, r3
			fi
	fi
ldi r1, length
ld r1, r1
inc r2
inc r0
wend




# =================================
# LEAVE THIS PART OF THE FILE ALONE
# Do not change the next two instructions: they must be the last two
# instructions executed by your program.
    ldi r0, pos  # Loads the start address of your result into r0 for the robot
    halt         # Brings execution to a halt

# =================================
# DATA GOES BELOW
# We have set this up for you, but you will need to test your program by
# compiling and running it several times with different input data values
# (different arrays of numbers)
# ---------------------------------------------------------------------

INPUTS>
length:  dc 10          # the length of the array (between 1 and 10)
content: dc 2, 0, -3, 4, -9, 0, 7, 88, -92, 18
ENDINPUTS>
pos: ds 1 # 1 byte each for the three result values
neg: ds 1
zer: ds 1
end

