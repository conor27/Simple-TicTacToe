import os
import time
import random

def tictactoe():
    topLeft = "1"
    topCenter = "2"
    topRight = "3"
    midLeft = "4"
    midCenter = "5"
    midRight = "6"
    bottomLeft = "7"
    bottomCenter = "8"
    bottomRight = "9"

    itemList = [topLeft, topCenter, topRight, midLeft, midCenter, midRight, bottomLeft, bottomCenter, bottomRight]

    def punchX(boardSpotX):
        itemList[boardSpotX] = "X"

    def punchO(boardSpotO):
        itemList[boardSpotO] = "O"

    # looks for any potential threats on the board.
    def threatCheck(gameBoard):

        ## Horizontal threat check
        if gameBoard[0] == "O" and gameBoard[1] == "O":
            return 2
        elif gameBoard[0] == "O" and gameBoard[2] == "O":
            return 1
        elif gameBoard[1] == "O" and gameBoard[2] == "O":
            return 0
        elif gameBoard[3] == "O" and gameBoard[4] == "O":
            return 5
        elif gameBoard[3] == "O" and gameBoard[5] == "O":
            return 4
        elif gameBoard[4] == "O" and gameBoard[5] == "O":
            return 3
        elif gameBoard[6] == "O" and gameBoard[7] == "O":
            return 9
        elif gameBoard[6] == "O" and gameBoard[8] == "O":
            return 7
        elif gameBoard[7] == "O" and gameBoard[8] == "O":
            return 6

        ## vertical threat check
        elif gameBoard[0] == "O" and gameBoard[3] == "O":
            return 6
        elif gameBoard[0] == "O" and gameBoard[6] == "O":
            return 3
        elif gameBoard[3] == "O" and gameBoard[6] == "O":
            return 0
        elif gameBoard[1] == "O" and gameBoard[4] == "O":
            return 7
        elif gameBoard[1] == "O" and gameBoard[7] == "O":
            return 4
        elif gameBoard[4] == "O" and gameBoard[7] == "O":
            return 1
        elif gameBoard[2] == "O" and gameBoard[5] == "O":
            return 8
        elif gameBoard[2] == "O" and gameBoard[8] == "O":
            return 5
        elif gameBoard[5] == "O" and gameBoard[8] == "O":
            return 2

        # diagonal line checks
        elif gameBoard[0] == "O" and gameBoard[4] == "O" and gameBoard[8] != "X":
            return 8
        elif gameBoard[0] == "O" and gameBoard[8] == "O" and gameBoard[4] != "X":
            return 4
        elif gameBoard[4] == "O" and gameBoard[8] == "O" and gameBoard[0] != "X":
            return 0
        elif gameBoard[6] == "O" and gameBoard[4] == "O" and gameBoard[2] != "X":
            return 2
        elif gameBoard[6] == "O" and gameBoard[2] == "O" and gameBoard[4] != "X":
            return 4
        elif gameBoard[4] == "O" and gameBoard[2] == "O" and gameBoard[0] != "X":
            return 6
        else:
            return 10

    # This function takes the item list as an arguement and returns the index number of the next square
    def nextMove(board):

        #starts by checking to see if the opponent has any threats

        if threatCheck(itemList) != 10:
            return threatCheck(itemList)

        # ## Horizontal threat check
        # if itemList[0] == "O" and itemList[1] == "O":
        #     return 2
        # elif itemList[0] == "O" and itemList[2] == "O":
        #     return 1
        # elif itemList[1] == "O" and itemList[2] == "O":
        #     return 0
        # elif itemList[3] == "O" and itemList[4] == "O":
        #     return 5
        # elif itemList[3] == "O" and itemList[5] == "O":
        #     return 4
        # elif itemList[4] == "O" and itemList[5] == "O":
        #     return 3
        # elif itemList[6] == "O" and itemList[7] == "O":
        #     return 9
        # elif itemList[6] == "O" and itemList[8] == "O":
        #     return 7
        # elif itemList[7] == "O" and itemList[8] == "O":
        #     return 6
        #
        # ## vertical threat check
        # elif itemList[0] == "O" and itemList[3] == "O":
        #     return 6
        # elif itemList[0] == "O" and itemList[6] == "O":
        #     return 3
        # elif itemList[3] == "O" and itemList[6] == "O":
        #     return 0
        # elif itemList[1] == "O" and itemList[4] == "O":
        #     return 7
        # elif itemList[1] == "O" and itemList[7] == "O":
        #     return 4
        # elif itemList[4] == "O" and itemList[7] == "O":
        #     return 1
        # elif itemList[2] == "O" and itemList[5] == "O":
        #     return 8
        # elif itemList[2] == "O" and itemList[8] == "O":
        #     return 5
        # elif itemList[5] == "O" and itemList[8] == "O":
        #     return 2
        #
        # # diagonal line checks
        # elif itemList[0] == "O" and itemList[4] == "O":
        #     return 8
        # elif itemList[0] == "O" and itemList[8] == "O":
        #     return 4
        # elif itemList[4] == "O" and itemList[8] == "O":
        #     return 0
        # elif itemList[6] == "O" and itemList[4] == "O":
        #     return 2
        # elif itemList[6] == "O" and itemList[2] == "O":
        #     return 4
        # elif itemList[4] == "O" and itemList[2] == "O":
        #     return 6

        # takes middle spot if it's not taken yet
        elif itemList[4] != "X":
            return 4

        #takes a random space if there is no better option
        else:
            moveValid = False
            while moveValid != True:
                randomSpace = random.randrange(0,8)
                print(randomSpace)
                if itemList[randomSpace] != "X" and itemList[randomSpace] != "O":
                    return randomSpace

    def printboard():
        print(" "+itemList[0]+" | "+itemList[1]+" | "+itemList[2]+" ")
        print("-----------")
        print(" "+itemList[3]+" | " +itemList[4]+" | "+itemList[5]+" ")
        print("-----------")
        print(" "+itemList[6]+" | "+itemList[7]+" | "+itemList[8]+" ")


    def wannaplay():
        print("Do you wanna play tic tac toe?")
        while True:
            answer = input()
            if answer == "yes":
                print("Great!")
                return "go"
            else:
                print("Awe:( Are you sure?")
                print("Do you want to play tic tac toe?")


    if wannaplay() == "go":
        print("Okay you go first, choose a square on the board")
        printboard()
        firstMove = input()
        for i in range(9):
            if int(firstMove)-1 == i:
                itemList[i] = "O"
        printboard()
        print("Good move! My turn...")
        time.sleep(2)

        if itemList[4] != "O":
            itemList[4] = "X"

        # if the middle isn't free a random square is chosen.
        else:
            valid = False
            while valid != True:
                cpuFirstMove = random.randrange(0, 8)
                if cpuFirstMove != 4:
                    valid = True

            itemList[cpuFirstMove] = "X"
        printboard()

        print("Okay, you again. Choose a space")

        # verifies that loop works
        while True:
            secondMove = input()
            if itemList[int(secondMove)-1] != "X" or itemList[int(secondMove)-1] != "O":
                break
            else:
                print("Sorry, that isn't a valid ")

        # loops to the item and updates it in the list
        for i in range(9):
            if int(secondMove)-1 == i:
                itemList[int(secondMove)-1] = "O"

        printboard()

        print("Nice! Me again...")
        time.sleep(2)
        itemList[nextMove(itemList)] = "X"

        printboard()

        print("Okay, your turn. Choose a spot!")

        # ensures validity of move three, then updates board
        userMoveThree = False
        while userMoveThree != True:
            moveThree = int(input())
            if str(moveThree) == itemList[moveThree-1]:
                userMoveThree = True
                punchO(moveThree-1)
            else:
                print("Sorry, looks like that isn't a valid option! Try again:)")
        printboard()

        print("Hmmm good move! Okay, I'm up!")
        time.sleep(2)








tictactoe()