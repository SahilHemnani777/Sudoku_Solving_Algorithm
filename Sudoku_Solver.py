#!/usr/bin/env python3
"""Shebang line (for LINUX)"""
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
"""Function to Print Board in Sudoku style"""
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

print_board(board)

"""Function to find the index of empty box in the puzzle"""
def find_empty(bo):
    for i in range(leb(bo)):
        for j in range(len(bo[o])):
            if bo[i][j]==0:
                return (i,j) #row,coloum
