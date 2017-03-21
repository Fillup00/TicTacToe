'''
Jonathan Telep
2/25/2017
Homework assignment 3
CS3560
'''
gameOver = False                                                    #Boolean expression verifying game did not end
p1Wins = 0
p2Wins = 0
def Tic_Tac_Toe():
    board_size = 0
    p1 = ""
    p2 = ""

    

    def get_board_size():
        print("What size board do you wish to play on: ")
        board_size = int(input())
        if board_size > 2 and board_size < 101:
            return board_size
        else:
            print("Board must be a minimum of 3 and maximum of 100 size")
            get_board_size()
    

    def create_board(board_size):
        count = 0
        for i in range(0,board_size):
            for j in range(0,board_size):
                board[i][j] = count
                count += 1
                
        
         
    def print_board():                                                  #prints the board
        #maxSize = board_size * board_size
        count = 0
        for i in range(0,board_size):
            for j in range(0,board_size):
                if count % board_size == 0 and count != 0:
                    print()
                    print(board[i][j], '|', end='')
                    count += 1
                else:
                    print(board[i][j], '|', end='')
                    count += 1

        print()
    


        
    def check_board():                                                                                  #checks to see if a winning combination was found

        #The following two nested for loops check if there is a winner horizontally
        horizCount = 0
        resetCount = 0
        for i in range(0,board_size):
            for j in range(0,board_size):
                if resetCount % board_size != 0:
                    if board[i][j] == "X":
                        horizCount += 1
                        if horizCount == board_size:
                            print("Player 1 Wins! Total Wins", p1Wins)
                            return True
                else:
                    horizCount = 0
           
        horizCount = 0
        resetCount = 0
        for i in range(0,board_size):
            for j in range(0,board_size):
                if resetCount % board_size != 0:
                    if board[i][j] == "Y":
                        horizCount += 1
                        if horizCount == board_size:
                            print("Player 2 Wins! Total Wins", p2Wins)
                            return True
                else:
                    horizCount = 0        

        #The following two nested for loops check if there is a winner horizontally
        horizCount = 0
        resetCount = 0
        for j in range(0,board_size):
            for i in range(0,board_size):
                if resetCount % board_size != 0:
                    if board[i][j] == "X":
                        horizCount += 1
                        if horizCount == board_size:
                            print("Player 1 Wins! Total Wins", p1Wins)
                            return True
                else:
                    vertCount = 0
           
        vertCount = 0
        resetCount = 0
        for j in range(0,board_size):
            for i in range(0,board_size):
                if resetCount % board_size != 0:
                    if board[i][j] == "Y":
                        vertCount += 1
                        if horizCount == board_size:
                            print("Player 2 Wins! Total Wins", p2Wins)
                            return True
                else:
                    vertCount = 0


        
        for i in range(0,board_size):
            for j in range(0,board_size):
                if board[i][j] == "X" or board[i][j] == "O":                                                      #checks for a Cats game
                    count += 1
                    
                if count == maxSize:
                    print("It's a cats game!")
                    return True
            

    def choose_num(playerName):                                                                         #Gets player's move and/or menu options
        incorrect = True
        while incorrect:
            print()
            print(playerName)
            print("Enter the number for the spot you'd like to move to: ")
            spot = input()
            if(spot == "p" or spot == "h" or spot == "s" or spot == "w" or spot == "r" or (int(spot) < board_size * board_size)):
                
                if(spot == "p"):                                                                            #When p is entered prints the board
                    print_board()
                elif(spot == "h"):                                                                          #When h is entered the menu is showed again
                    menu()
                elif(spot == "s"):                                                                          #When s is entered they save the game and ends
                    print("What is the name of the file you'd like to save to: ")
                    fileName = input()
                    file = open(fileName, "w")
                    for x in board:
                        x = str(x)
                        file.write(x)
                        file.write(" ")
                    file.write(p1 + " ")
                    file.write(str(p1Wins) + " ")
                    file.write(p2 + " ")
                    file.write(str(p2Wins) + " ")
                    return spot
                elif(spot == "r"):                                                                          #When r is entered the game is forfeited
                    incorrect = False
                    print("The game was forfeited by", playerName)
                    return spot
                else:
                    spot = int(spot)
                    maxSize = board_size * board_size
                    if spot in range(0, maxSize):                                                                 #Verifies that the spot is on the board
                        incorrect = False
                        return spot
                    else:
                        print("That's not on the board.")
            else:
                print("Entry not valid, please try again")

    def whose_turn():                                                                                   #This function finds whose turn it is if a file is loaded
        xCount = 0
        yCount = 0
        for i in range(0,board_size):
            for j in range(0,board_size):
                if board[i][j] == "X": 
                    xCount += 1
                if board[i][j] == "O":
                    yCount += 1

        if xCount == yCount:
            return True
        else:
            return False
        
    def get_player1(p1):                                                                                #Calls choose_num and then actually makes the move for player1
        move = choose_num(p1)
        if(move != "r" and move != "s"):
            
            if board[move] == "X" or board[move] == "O":
                print("\nChosen spot is occupied. Please try again.")
                get_player1(p1)
            else:
                board[move] = "X"
                return False
        else:                                                                                           #If r or s is called makes sure game ends
            return True
            
    def get_player2(p2):                                                                                #Calls choose_num and then actually makes the move for player2
        move = choose_num(p2)        
        if(move != "r" and move != "s"):
            if board[move] == "X" or board[move] == "O":
                print("\nChosen spot is occupied. Please try again.")
                get_player2(p2)
            else:
                board[move] = "O"
                return False
        else:                                                                                           #If r or s is called makes sure game ends
            return True

    def menu():                                                                                         #Menu function to display options other than a move
        print("\n#############################################################################")
        print("Enter one of the following charactesrs within the parenthesis.")
        print("(You should enter these values when asked to enter a move)")
        print("(p) To view the current state of the game board")
        print("(s) To save the current game")
        print("(r) To resign from the current")
        print("(h) To show this menu again")
        print("#############################################################################\n")

    def play():
        global gameOver
        while not gameOver:                                                         #start of a while loop verifying game is still active
            if(whose_turn()):
                gameOver = get_player1(p1)                                              #Checks if game ended by r or s entered
                if gameOver == True:
                    break
                gameOver = check_board()                                                #Checks if game ended by a winning combination
                if gameOver == True:
                    break
                print()
            else:
                gameOver = get_player2(p2)                                              #Checks if the game ended from an entered r or s option
                if gameOver == True:
                    break
                gameOver = check_board()                                                #Checks if the game ended by a winning combination
                if gameOver == True:
                    break
                print()
        
    if p1Wins == 0 and p2Wins == 0:
        print("Welcome to 4X4 Tic Tac Toe!")                                        #Welcoming display
        if input("Do you have a saved game: (y/n)") == "y":                         #Asks if they wish to resume a saved game
            file = input("Enter the file name for the saved game: ")
            file_input = open(file, "r")
            boardText = file_input.readline()
            
            boardText = boardText.split(" ")
            i=0
            for x in boardText:                                                       #If so fulfill the board with the file's info
                
                if i <= 15:
                    board[i] = x
                    i = i + 1
                elif( i == 16):
                    p1 = x
                    i = i + 1
                elif(i == 17):
                    global p1Wins
                    p1Wins = x
                    i = i + 1
                elif(i == 18):
                    p2 = x
                    i = i + 1
                else:
                    global p2Wins
                    p2Wins = x

                    

            file_input.close()
            menu()
            play()
            
        else:
            board_size = get_board_size()
            board = [[0 for x in range(board_size)] for y in range(board_size)]                    #Game board spaces
            create_board(board_size)
            print_board()
            
            print("Player 1, enter your name: ")
            p1 = input()
            print("Player 2, enter your name: ")
            p2 = input()
            menu()
            play()
            
        
        

    if input("Would you like to play again? (y/n)") == "y":                     #Asks users if they wish to play the game again
        global gameOver
        gameOver = False
        board = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        play()
    else:
        print("Thank you, come again.")


def main():
    Tic_Tac_Toe()                                                               #Calls Tic Tac Toe game to start

if __name__ == '__main__':  
    main()
