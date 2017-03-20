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
    

    p1 = ""
    p2 = ""
    board = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]                     #Game board spaces
    winning_combinations =(                                             #All possible winning combinations of a 4 by 4 board
        (0,1,2,3),
        (4,5,6,7),
        (8,9,10,11),
        (12,13,14,15),
        (0,4,8,12),
        (1,5,9,13),
        (2,6,10,14),
        (3,7,11,15),
        (3,6,9,12),
        (0,5,10,15)
        )
    
    def print_board():                                                  #prints the board
        print(board[0],'|',board[1],'|',board[2],'|',board[3])
        print("------------------")
        print(board[4],'|',board[5],'|',board[6],'|',board[7])
        print("------------------")
        print(board[8],'|',board[9],'|',board[10],'|',board[11])
        print("------------------")
        print(board[12],'|',board[13],'|',board[14],'|',board[15])
        print("")

        
    def check_board():                                                                                  #checks to see if a winning combination was found
        count = 0
        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] == board[combo[3]] == "X":         #Checks if X's won, returns true
                global p1Wins
                p1Wins = int(p1Wins)
                p1Wins += 1
                print("Player 1 Wins! Total Wins: ", p1Wins)
                return True
            
            if board[combo[0]] == board[combo[1]] == board[combo[2]] == board[combo[3]] == "O":         #Checks if O's won, returns true
                global p2Wins
                p2Wins = int(p2Wins)
                p2Wins += 1
                print("Player 2 Wins! Total Wins: ", p2Wins)
                return True
            
        for i in range(16):
            if board[i] == "X" or board[i] == "O":                                                      #checks for a Cats game
                count += 1
                
            if count == 16:
                print("It's a cats game!")
                return True
            

    def choose_num(playerName):                                                                         #Gets player's move and/or menu options
        incorrect = True
        while incorrect:
            print("")
            print(playerName)
            print("Enter the number for the spot you'd like to move to: ")
            spot = raw_input()
            if(spot == "p" or spot == "h" or spot == "s" or spot == "w" or spot == "r" or spot == "0"  or spot == "1"  or spot == "2"
                or spot == "3"  or spot == "4"  or spot == "5" or spot == "6" or spot == "7" or spot == "8" or spot == "9"
                or spot == "10" or spot == "11" or spot == "12" or spot == "13" or spot == "14" or spot == "15"):
                
                if(spot == "p"):                                                                            #When p is entered prints the board
                    print_board()
                elif(spot == "h"):                                                                          #When h is entered the menu is showed again
                    menu()
                elif(spot == "s"):                                                                          #When s is entered they save the game and ends
                    print("What is the name of the file you'd like to save to: ")
                    fileName = raw_input()
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
                    if spot in range(0,16):                                                                 #Verifies that the spot is on the board
                        incorrect = False
                        return spot
                    else:
                        print("That's not on the board.")
            else:
                print("Entry not valid, please try again")

    def whose_turn():                                                                                   #This function finds whose turn it is if a file is loaded
        xCount = 0
        yCount = 0
        for i in range(16):
            if board[i] == "X": 
                xCount += 1
            if board[i] == "O":
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
        if raw_input("Do you have a saved game: (y/n)") == "y":                         #Asks if they wish to resume a saved game
            file = raw_input("Enter the file name for the saved game: ")
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
            print("Player 1, enter your name: ")
            p1 = raw_input()
            print("Player 2, enter your name: ")
            p2 = raw_input()
            menu()
            play()
            
        
        

    if raw_input("Would you like to play again? (y/n)") == "y":                     #Asks users if they wish to play the game again
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
