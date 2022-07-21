import random
from secrets import choice

choices = ["Rock", "Paper", "Scissors"]
computer =random.choice(choices)
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("Rock, Paper, Scissors").capitalize()
    ## Condition of rock, paper amd scissors
    if player == computer:
        print("tie!")
    elif player == "Paper":
        if computer == "Paper":
            print("You Lose!", computer,"covers", player)
            cpu_score+=1
        else:
            print("You win!", player, "smashes", computer)
            player_score+=1
    elif player == "Paper":
            if computer == "Scissors":
                print("You Lose!", computer, "cut", player)
                cpu_score+=1
            else:
                print("You win!", player, "covers", computer)
                player_score+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("You Lose....", computer, "smashes", player )
            cpu_score+=1
    elif player == 'End':
        print("final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"plaer:{player_score}")
        break            
    