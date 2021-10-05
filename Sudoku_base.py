#Base version of Sudoku, runned in Cmd Line

board = [
    [0,0,9,8,0,7,1,0,0],
    [0,0,0,0,3,1,7,0,0],
    [2,1,0,0,0,6,0,0,3],
    [3,7,2,0,0,0,0,0,9],
    [0,6,0,0,2,0,0,3,0],
    [4,0,0,0,0,0,2,1,8],
    [7,0,0,3,0,0,0,2,6],
    [0,0,6,1,8,0,0,0,0],
    [0,0,3,7,0,4,9,0,0]
]

#Solves the board by using the backtrack algorithm
def solve(bo):
    #If the board is full it means it's solved and finishes the loop
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    #Checks every slot, and updates the board with the first valid value
    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            #The function calls itself to see if now the board is complete
            if solve(bo):
                return True
            #If the number is not valid, sets it to 0 and backtrack to the previous slot
            bo[row][col] = 0
    
    return False

#Checks if every slot in the grid is valid or not
def valid(bo, num, pos):
    #Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    #Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    #Check boxex, which are calculated by dividing the
    #position of target slot by 3 (since the boxes are 3*3)
    #e.g: the 8 at position [0][3] which means it's in the box at coords [0][1]
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    #Loops through all the items in a box (9)
    #In order to find the element in target box we need to multiply 
    #the box value by 3.
    #e.g: the 1 at [0][6] is in box [0][2], so by *3 we get that it
    #is at coords [0][6].
    #The +3 is to loop vertically.
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True

def print_board(bo):
    #prints the board separators
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

#Finds empty (value 0) slots
#Return None if there are no 0, meaning the table is solved
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) #row, col
    return None 

print_board(board)
solve(board)
print("                      ")
print_board(board)

 