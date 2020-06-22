import os
import time
import random

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

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

    endIndexList = [2, 5, 8]

    def punchX(boardSpotX):
        itemList[boardSpotX] = "X"

    def punchO(boardSpotO):
        itemList[boardSpotO] = "O"

    # looks for any potential threats on the board.
    def threatCheck(gameBoard, letterOfThreat):

        letterOfThreat = letterOfThreat.upper()

        if letterOfThreat == "O":
            otherLetter = "X"
        else:
            otherLetter = "O"

        ## Horizontal threat check
        if gameBoard[0] == letterOfThreat and gameBoard[1] == letterOfThreat and gameBoard[2] != otherLetter:
            return 2
        elif gameBoard[0] == letterOfThreat and gameBoard[2] == letterOfThreat and gameBoard[1] != otherLetter:
            return 1
        elif gameBoard[1] == letterOfThreat and gameBoard[2] == letterOfThreat and gameBoard[0] != otherLetter:
            return 0
        elif gameBoard[3] == letterOfThreat and gameBoard[4] == letterOfThreat and gameBoard[5] != otherLetter:
            return 5
        elif gameBoard[3] == letterOfThreat and gameBoard[5] == letterOfThreat and gameBoard[4] != otherLetter:
            return 4
        elif gameBoard[4] == letterOfThreat and gameBoard[5] == letterOfThreat and gameBoard[3] != otherLetter:
            return 3
        elif gameBoard[6] == letterOfThreat and gameBoard[7] == letterOfThreat and gameBoard[9] != otherLetter:
            return 9
        elif gameBoard[6] == letterOfThreat and gameBoard[8] == letterOfThreat and gameBoard[8] != otherLetter:
            return 7
        elif gameBoard[7] == letterOfThreat and gameBoard[8] == letterOfThreat and gameBoard[6] != otherLetter:
            return 6

        ## vertical threat check
        elif gameBoard[0] == letterOfThreat and gameBoard[3] == letterOfThreat and gameBoard[6] != otherLetter:
            return 6
        elif gameBoard[0] == letterOfThreat and gameBoard[6] == letterOfThreat and gameBoard[3] != otherLetter:
            return 3
        elif gameBoard[3] == letterOfThreat and gameBoard[6] == letterOfThreat and gameBoard[0] != otherLetter:
            return 0
        elif gameBoard[1] == letterOfThreat and gameBoard[4] == letterOfThreat and gameBoard[7] != otherLetter:
            return 7
        elif gameBoard[1] == letterOfThreat and gameBoard[7] == letterOfThreat and gameBoard[4] != otherLetter:
            return 4
        elif gameBoard[4] == letterOfThreat and gameBoard[7] == letterOfThreat and gameBoard[1] != otherLetter:
            return 1
        elif gameBoard[2] == letterOfThreat and gameBoard[5] == letterOfThreat and gameBoard[8] != otherLetter:
            return 8
        elif gameBoard[2] == letterOfThreat and gameBoard[8] == letterOfThreat and gameBoard[5] != otherLetter:
            return 5
        elif gameBoard[5] == letterOfThreat and gameBoard[8] == letterOfThreat and gameBoard[2] != otherLetter:
            return 2

        # diagonal line checks
        elif gameBoard[0] == letterOfThreat and gameBoard[4] == letterOfThreat and gameBoard[8] != otherLetter:
            return 8
        elif gameBoard[0] == letterOfThreat and gameBoard[8] == letterOfThreat and gameBoard[4] != otherLetter:
            return 4
        elif gameBoard[4] == letterOfThreat and gameBoard[8] == letterOfThreat and gameBoard[0] != otherLetter:
            return 0
        elif gameBoard[6] == letterOfThreat and gameBoard[4] == letterOfThreat and gameBoard[2] != otherLetter:
            return 2
        elif gameBoard[6] == letterOfThreat and gameBoard[2] == letterOfThreat and gameBoard[4] != otherLetter:
            return 4
        elif gameBoard[4] == letterOfThreat and gameBoard[2] == letterOfThreat and gameBoard[0] != otherLetter:
            return 6
        else:
            return 10

    # This function takes the item list as an argument and returns the index number of the next square
    def nextMove(board):

        #starts by checking to see if the opponent has any threats

        if threatCheck(itemList, "O") != 10:
            return threatCheck(itemList, "O")

        # takes middle spot if it's not taken yet
        elif itemList[4] != "X":
            return 4

        #takes a random space if there is no better option
        else:
            moveValid = False
            while moveValid != True:
                randomSpace = random.randrange(0,8)
                # print(randomSpace)
                if itemList[randomSpace] != "X" and itemList[randomSpace] != "O":
                    return randomSpace

    def printSpace(number):
        if itemList[number] == str(number+1) and number in endIndexList:
            print(itemList[number] + " ")
        elif itemList[number] == str(number+1):
            print(itemList[number], end=" ")
        elif itemList[number] != str(number+1) and number in endIndexList:
            print(color.BOLD + itemList[number] + color.END + " ")
        else:
            print(color.BOLD + itemList[number] + color.END, end=" ")

    # old version of the function that doesn't integrate bolding
    # def printboard():
    #     print(" "+itemList[0]+" | "+itemList[1]+" | "+itemList[2]+" ")
    #     print("-----------")
    #     print(" "+itemList[3]+" | " +itemList[4]+" | "+itemList[5]+" ")
    #     print("-----------")
    #     print(" "+itemList[6]+" | "+itemList[7]+" | "+itemList[8]+" ")
    #     print()

    def printboard():
        print("", end=" ")
        printSpace(0)
        print("|", end=" ")
        printSpace(1)
        print("|", end=" ")
        printSpace(2)

        print("-----------")

        print("", end=" ")
        printSpace(3)
        print("|", end=" ")
        printSpace(4)
        print("|", end=" ")
        printSpace(5)

        print("-----------")

        print("", end=" ")
        printSpace(6)
        print("|", end=" ")
        printSpace(7)
        print("|", end=" ")
        printSpace(8)

        print()

    def wannaplay():
        print("Do you wanna play tic tac toe?")
        while True:
            answer = input()
            if answer.lower() == "yes":
                print("Great! I'll be X, and you'll be O")
                time.sleep(2)
                return True
            else:
                print("Awe:( Are you sure?")
                time.sleep(2)
                print("Do you want to play tic tac toe?")


    if wannaplay() == True:
        print("Okay you go first, choose a square on the board")
        printboard()
        firstMove = input()
        for i in range(9):
            if int(firstMove)-1 == i:
                itemList[i] = "O"
        printboard()
        print("Good move! My turn...")
        time.sleep(2)

        # takes the middle square if user didn't take it
        if itemList[4] != "O":
            itemList[4] = "X"

        # if the middle isn't free a random square is chosen.
        else:
            valid = False
            while valid != True:
                cpuFirstMove = random.randrange(0, 8)
                if cpuFirstMove != 4:
                    itemList[cpuFirstMove] = "X"
                    valid = True

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

        # third move by user, this could be a win so look out for that first
        # After win check, threat check, and then random move.
        if threatCheck(itemList, "X") != 10:
            punchX(threatCheck(itemList, "X"))
            "I win! Better luck next time, Bucko."

        elif threatCheck(itemList, "O") != 10:
            punchX(threatCheck(itemList, "O"))
            "Huhuhu. Stopped ya!"

        else:
            print("Not seeing any ways to win for either of us this time...")
            time.sleep(2)
            valid = False
            while valid != True:
                cpuThirdMove = random.randrange(0,8)
                if itemList[cpuThirdMove] != "X" and itemList[cpuThirdMove] != "O":
                    valid = True
                    punchX(cpuThirdMove)

        printboard()
        print("We're really in the thick of it now. Your move.")






tictactoe()