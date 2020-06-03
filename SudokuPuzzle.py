import random
from sys import argv

random.seed(51800785)

def createLatinSquare(n):
	square = []
	for i in range(n):
		square.append(random.sample(range(n), n))
	
	while (square[0][0] == square[1][0] or square[0][0] == square[2][0] or square[1][0] == square[2][0] or square[0][1] == square[1][1] or square[0][1] == square[2][1] or square[1][1] == square[2][1] or square[0][2] == square[1][2] or square[0][2] == square[2][2] or square[1][2] == square[2][2]):
		square[0] = random.sample(range(n), n)
		square[1] = random.sample(range(n), n)
		square[2] = random.sample(range(n), n)

	return square


def swapRows(t):
	t[1], t[9] = t[9], t[1]
	t[4], t[12] = t[12], t[4]
	t[7], t[15] = t[15], t[7]

	t[2], t[18] = t[18], t[2]
	t[5], t[21] = t[21], t[5]
	t[8], t[24] = t[24], t[8]

	t[11], t[19] = t[19], t[11]
	t[14], t[22] = t[22], t[14]
	t[17], t[25] = t[25], t[17]

	return t


def diggingSudokuHole(t):
	for i in range(9):
		pos_2 = random.randint(0, 2)
		pos_3 = random.randint(0, 2)
		
		while (t[i][pos_2][pos_3] == 0):
			pos_2 = random.randint(0, 2)
			pos_3 = random.randint(0, 2)		
		
		t[i][pos_2][pos_3] = 0
	
	return t


# Input arguments
script, first, second = argv


# create Latin Squares
square_1 = createLatinSquare(3)
square_2 = createLatinSquare(3)
square_3 = createLatinSquare(3)

square_4 = createLatinSquare(3)
square_5 = createLatinSquare(3)
square_6 = createLatinSquare(3)

square_7 = createLatinSquare(3)
square_8 = createLatinSquare(3)
square_9 = createLatinSquare(3)

latinSquaresTable = [square_1, square_2, square_3, square_4, square_5, square_6, square_7, square_8, square_9]


# Convert to base 10
randomNum = [i for i in range(9)]
random.shuffle(randomNum)

randomSquaresPosition = [latinSquaresTable[randomNum[j]] for j in range(9)]

randomPick = random.randint(0, 8)

tempTable = []
Table = []

for k in latinSquaresTable[randomPick]:
	for m in k:
	    pos = 0
	    for n in randomSquaresPosition[pos]:
	        for o in n:
	            if (m == 0):
	                o = o + 0 * 3 + 1
	                tempTable.append(o)

	            if (m == 1):
	                o = o + 1 * 3 + 1
	                tempTable.append(o)

	            if (m == 2):
	                o = o + 2 * 3 + 1
	                tempTable.append(o)

	        Table.append(tempTable)
	        tempTable = []

	    pos += 1


# Swap 2 - 4, 3 - 7, 6 - 8 rows
swapRows(Table)


# Digging holes
temp_1 = [Table[0], Table[1], Table[2]]
temp_2 = [Table[3], Table[4], Table[5]]
temp_3 = [Table[6], Table[7], Table[8]]

temp_4 = [Table[9], Table[10], Table[11]]
temp_5 = [Table[12], Table[13], Table[14]]
temp_6 = [Table[15], Table[16], Table[17]]

temp_7 = [Table[18], Table[19], Table[20]]
temp_8 = [Table[21], Table[22], Table[23]]
temp_9 = [Table[24], Table[25], Table[26]]

digTable = [temp_1, temp_2, temp_3, temp_4, temp_5, temp_6, temp_7, temp_8, temp_9]
	
if (first == "9"):
	diggingSudokuHole(digTable)

elif (first == "18"):
	diggingSudokuHole(digTable)

	diggingSudokuHole(digTable)

elif (first == "27"):
	diggingSudokuHole(digTable)

	diggingSudokuHole(digTable)

	diggingSudokuHole(digTable)

elif (first == "36"):
	diggingSudokuHole(digTable)

	diggingSudokuHole(digTable)
	
	diggingSudokuHole(digTable)
	
	diggingSudokuHole(digTable)

elif (first == "45"):
	diggingSudokuHole(digTable)

	diggingSudokuHole(digTable)
	
	diggingSudokuHole(digTable)
	
	diggingSudokuHole(digTable)

	diggingSudokuHole(digTable)
	
elif (first == "54"):
	diggingSudokuHole(digTable)

	diggingSudokuHole(digTable)
	
	diggingSudokuHole(digTable)
	
	diggingSudokuHole(digTable)

	diggingSudokuHole(digTable)
	
	diggingSudokuHole(digTable)


# Display Sudoku table
block_1 = [Table[0], Table[3], Table[6]]
block_2 = [Table[1], Table[4], Table[7]]
block_3 = [Table[2], Table[5], Table[8]]

block_4 = [Table[9], Table[12], Table[15]]
block_5 = [Table[10], Table[13], Table[16]]
block_6 = [Table[11], Table[14], Table[17]]

block_7 = [Table[18], Table[21], Table[24]]
block_8 = [Table[19], Table[22], Table[25]]
block_9 = [Table[20], Table[23], Table[26]]

finalTable = [block_1, block_2, block_3, block_4, block_5, block_6, block_7, block_8, block_9]

sudokuTable = []
for i in range(len(finalTable)):
	for j in range(3):
		for k in range(3):
			sudokuTable.append(finalTable[i][j][k])


resultTable = []
t = []
for i in range(len(sudokuTable)):
	t.append(sudokuTable[i])

	if (i == 8):
		resultTable.append(t)
		t = []

	elif (i == 17):
		resultTable.append(t)
		t = []

	elif (i == 26):
		resultTable.append(t)
		t = []

	elif (i == 35):
		resultTable.append(t)
		t = []

	elif (i == 44):
		resultTable.append(t)
		t = []

	elif (i == 53):
		resultTable.append(t)
		t = []

	elif (i == 62):
		resultTable.append(t)
		t = []

	elif (i == 71):
		resultTable.append(t)
		t = []

	elif (i == 80):
		resultTable.append(t)
		t = []		

print("\n-----> Sudoku Table <------")
for i in resultTable:
	print(i) 


# Write result to output file
lineNumbers = len(str(9))
with open(second, "w") as f:
	for line in resultTable:
		f.write(", ".join(f"{k or '0':{lineNumbers}}" for k in line) + "\n")

f.close()

print("\n--> Your result has been saved to " + second + "...")
