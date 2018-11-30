from random import randint

c = ["rock","paper","scissors"]

computer = c[randint(0,2)]
player = False

while player == False:
    player = input("rock, paper or scissors?")
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You Lose!, Computer: " + computer + " player: " + player)
        else:
            print("You Win!, Computer: " + computer + " player: " + player)
    elif player == "paper":
        if computer == "scissors":
            print("You Lose!, Computer: " + computer + " player: " + player)
        else:
            print("You Win!, Computer: " + computer + " player: " + player)
    elif player == "scissors":
        if computer == "rock":
            print("You Lose!, Computer: " + computer + " player: " + player)
        else:
            print("You Win!, Computer: " + computer + " player: " + player)
    else:
        print("Not a valid play!")

    player = False
    computer = c[randint(0,2)]
