#!/usr/bin/env python3
#Shebang line (for LINUX)
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],      #This is a unsolved Sudoku board
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


#Function to Backtrack and solve the board [Main function]

def solve(bo):
    #basecase
    find=find_empty(bo)
    if not find: #if there are  no empty boxses (base case of recursion)
        return True
    else:
        row, col=find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col]=i

            if solve(board):
                return True

            bo[row][col]=0
    return False


#Function to check if the number we pass is valid or not
#return True if the number is valid
#return Flase if the number is not valid"""

def valid(bo, num, pos):
    #check Rows
    for i in range(len(bo[0])):
        if bo[pos[0]][i]==num and i!=pos[1]:
            return False
    #check coloum
    for i in range(len(bo[0])):
        if bo[i][pos[1]]==num and i!=pos[0]:
            return False
    #check box(3x3)
    box_x=pos[1]//3
    box_y=pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):    #itterating through rows
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j]==num and (i, j)!=pos:
                return False
    return True


#Function to Print Board in Sudoku style

def print_board(bo):
    for i in range(len(bo)):
        if i%3==0 and i!=0:
            print("------------------------")
        for j in range(len(bo[0])):
            if j%3==0 and j!=0:
                print(" | ", end="")
            if j==8:
                print(str(bo[i][j]))
            else:
                print(str(bo[i][j]) + " ", end="")
print("Unsolved SUDOKU")
print_board(board)

#Function to find the index of empty box in the puzzle

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j]==0:
                return (i,j) #row,coloum
    return None

solve(board)
print("___________________________")
print("                           ")
print("Solved SUDOKU")
print(print_board(board))
