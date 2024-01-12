board=[" " for i in range(9)]
print(board)
def print_board():
    pos=0
    row1,row2,row3="","",""
    for i in board:
        
        if pos<3:
            row1=row1+"| |"
            pos=pos+1
            
        elif pos<6:
            
            row2=row2+"| |"
            pos=pos+1
            
        else:
            
            row3=row3+"| |"
            pos=pos+1
    #row1="|{}|{}|{}|".format(board[0],board[1],board[2])
    #row2="|{}|{}|{}|".format(board[3],board[4],board[5])
    #row3="|{}|{}|{}|".format(board[6],board[7],board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

print_board()
