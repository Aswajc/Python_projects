import random

rock = "rock"
paper = "paper"
scissor = "scissor"

choice1 = input("what do you choose? 0 for Rock ,1 for paper or 2 for scissor")
choice2 = random.randint(0,2)
print(f"you chose {rock}")
print(f"you chose ")

if choice1 == choice2 :
    print("its a tie..play again")
#.................