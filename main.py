#Variables
boardState = [[0,0,0], 
              [0,0,0], 
              [0,0,0]]
turns = 0

#Defining displaying the board
def displayBoard():
  boardStateStr = str(boardState[0])+'\n'+str(boardState[1])+'\n'+str(boardState[2])
  print(boardStateStr)

#Defining players turns
def play(player):
  row = int(input('Player '+str(player)+' please input your row value (0,1,2): '))
  column = int(input('Player '+str(player)+' please input your column value (0,1,2): '))
  if boardState[row][column] != 0:
    print('This square is already taken please select another square.')
    play(player)
  else:
    boardState[row][column] = player
    displayBoard()

#Checking for winner
def checkWin(playe):
  #Column calculating
  column1 = []
  for row in boardState:
    column1.append(row[0])  
  column2 = []
  for row in boardState:
    column2.append(row[1]) 
  column3 = []
  for row in boardState:
    column3.append(row[2])
  #Diagonal Check
  diagonal1 = [int(boardState[0][0]),int(boardState[1][1]),int(boardState[2][2])]
  diagonal2 = [int(boardState[0][2]),int(boardState[1][1]),int(boardState[2][0])]
  #Horizontal victory
  if boardState[0] == [int(playe),int(playe),int(playe)] or boardState[1] == [int(playe),int(playe),int(playe)] or boardState[2] == [int(playe),int(playe),int(playe)]:
    won = 1
    while won == 1:
      print('Player '+str(playe)+' has won!')
  #Vertical victory
  elif column1 == [int(playe),int(playe),int(playe)] or column2 == [int(playe),int(playe),int(playe)] or column3 == [int(playe),int(playe),int(playe)]:
    won = 1
    while won:
      print('Player '+str(playe)+' has won!')
  #Diagonal win
  elif diagonal1 == [int(playe),int(playe),int(playe)] or diagonal2 == [int(playe),int(playe),int(playe)]:
    won = 1
    while won:
      print('Player '+str(playe)+' has won!')

#Game loop
displayBoard()
for turn in range (0,4):
  checkWin(2)
  play(1)
  if turn != 4: 
    checkWin(1)
    play(2) 