import random

rows = 3
columns = 3
positions = [1,2,3,4,5,6,7,8,9]
board = [[1,2,3], [4,5,6], [7,8,9]]

def printBoard():
  for x in range(rows):
    print("\n-----------")
    print("|", end="")
    for y in range(columns):
      print("", board[x][y], end=" |")
  print("\n-----------")

def editBoard(num, edit):
  num -= 1
  if(num == 0):
    board[0][0] = edit
  elif(num == 1):
    board[0][1] = edit
  elif(num == 2):
    board[0][2] = edit
  elif(num == 3):
    board[1][0] = edit
  elif(num == 4):
    board[1][1] = edit
  elif(num == 5):
    board[1][2] = edit
  elif(num == 6):
    board[2][0] = edit
  elif(num == 7):
    board[2][1] = edit
  elif(num == 8):
    board[2][2] = edit

def checkIfWon(board):
  if(board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X'):
    print("X has won!")
    return "X"
  elif(board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O'):
    print("O has won!")
    return "O"
  elif(board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X'):
    print("X has won!")
    return "X"
  elif(board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O'):
    print("O has won!")
    return "O"
  elif(board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X'):
    print("X has won!")
    return "X"
  elif(board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O'):
    print("O has won!")
    return "O"
  ### Y axis
  if(board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X'):
    print("X has won!")
    return "X"
  elif(board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O'):
    print("O has won!")
    return "O"
  elif(board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X'):
    print("X has won!")
    return "X"
  elif(board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O'):
    print("O has won!")
    return "O"
  elif(board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X'):
    print("X has won!")
    return "X"
  elif(board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O'):
    print("O has won!")
    return "O"
  ### Cross wins
  elif(board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X'):
    print("X has won!")
    return "X"
  elif(board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O'):
    print("O has won!")  
    return "O"
  elif(board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X'):
    print("X has won!")  
    return "X"
  elif(board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):
    print("O has won!") 
    return "O" 
  else:
    return "N"

exit = False
editCount = 0

while(exit == False):
  if(editCount % 2 == 0):
    printBoard()
    move = int(input("\nChoose a position 1-9: "))
    if(move >= 1 or move <= 9):
      editBoard(move, 'X')
      positions.remove(move)
    else:
      print("Invalid move.")
    editCount += 1

  else:
    while(True):
      compMove = random.choice(positions)
      print("\nComputer's move: ", compMove)
      if(compMove in positions):
        editBoard(compMove, 'O')
        positions.remove(compMove)
        editCount += 1
        break
  
    winner = checkIfWon(board)
    if(winner != "N"):
        print("\nGame over!")
        break
