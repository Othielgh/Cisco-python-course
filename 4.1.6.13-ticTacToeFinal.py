from random import randrange
board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]
numberOfMoves = 1               # computer already has done a move
human = 'O'
computer = 'X'
winner = False

def displayBoard(board):
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   '+ board[0][0] +   '   |   ' + board[0][1] +'   |   ' + board[0][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   '+ board[1][0] +   '   |   ' + board[1][1] +'   |   ' + board[1][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   '+ board[2][0] +   '   |   ' + board[2][1] +'   |   ' + board[2][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')


def enterMove(board):

    move = int(input('enter your move: '))

    if move < 1 or move > 9:
        print('Please enter a valid number')
        return enterMove(board)
    elif str(move) not in board[0] and str(move) not in board[1] and str(move) not in board[2]:
        print('This position is already taken, please try again!')
        return enterMove(board)
    elif move == 1:
        board[0][0] = 'O'
    elif move == 2:
        board[0][1] = 'O'
    elif move == 3:
        board[0][2] = 'O'
    elif move == 4:
        board[1][0] = 'O'
    elif move == 5:
        board[1][1] = 'O'
    elif move == 6:
        board[1][2] = 'O'
    elif move == 7:
        board[2][0] = 'O'
    elif move == 8:
        board[2][1] = 'O'
    elif move == 9:
        board[2][2] = 'O'
    
   
#
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#

def makeListOfFreeFields(board):
    
    freeSquares = []
    
    for row in range(0, 3):
        for column in range(0, 3):
            if board[row][column] == 'O' or board[row][column] == 'X':
                pass
            else:
                freeSquares.append(([row],[column]))
    if freeSquares == board:
        print("it's a tie!")            
            
            
def victoryFor(board, sign):

    #print('Checking if ', sign, "has won.")
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:   #row1
        #print(sign, 'has won the game!')
        return True
    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:   #row2
        #print(sign, 'has won the game!')
        return True
    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:   #row3
       # print(sign, 'has won the game!')
        return True
    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:   #column1
        #print(sign, 'has won the game!')
        return True
    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:   #column2
        #print(sign, 'has won the game!')
        return True
    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:   #column3
        #print(sign, 'has won the game!')
        return True
    elif board[0][0] == sign and board[1][2] == sign and board[2][2] == sign:   #diagonal left to right
       # print(sign, 'has won the game!')
        return True
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:   #diagonal right to left
        #print(sign, 'has won the game!')
        return True
    else:
        return False
       # print(sign, 'has not won yet!')

#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#

def drawMove(board):
    
    while True:

        compMove = randrange(10)
        
        if str(compMove) not in board[0] and str(compMove) not in board[1] and str(compMove) not in board[2]:
            return drawMove(board)
        elif compMove == 1:
            board[0][0] = 'X'
        elif compMove == 2:
            board[0][1] = 'X'
        elif compMove == 3:
            board[0][2] = 'X'
        elif compMove == 4:
            board[1][0] = 'X'
        elif compMove == 5:
            board[1][1] = 'X'
        elif compMove == 6:
            board[1][2] = 'X'
        elif compMove == 7:
            board[2][0] = 'X'
        elif compMove == 8:
            board[2][1] = 'X'
        elif compMove == 9:
            board[2][2] = 'X'
        break


while numberOfMoves < 9:

    displayBoard(board)
    enterMove(board)
    numberOfMoves += 1

    if victoryFor(board, human) == True:
        displayBoard(board)
        print('You have won the game!')
        break
    else:
        makeListOfFreeFields(board)
    

    drawMove(board)
    numberOfMoves += 1

    if victoryFor(board, computer) == True:
        displayBoard(board)
        print('The computer has won the game!')
        break
    else:
        makeListOfFreeFields(board)
   # victoryFor(board, human)
    #victoryFor(board, computer)
    
else:
    displayBoard(board)
    print("It's a tie")

print('Game closed')


## EOF