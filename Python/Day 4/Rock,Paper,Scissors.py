Rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
Paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
Scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
my_signs=[Rock,Paper,Scissors]
print("what do you choose?")
my_move=input('''           Type 'R' for Rock'
          Type 'P' for Paper
          Type 'S' for Scissors 
          :''').upper()
print("My Move")
if my_move=="R":
    print(Rock)
elif my_move=="P":
     print(Paper)
elif my_move=="S":
        print(Scissors)

import random

print("Computer's Move")
move=[Rock, Paper, Scissors]

computer_move=(random.choice(move))
print(computer_move)

if computer_move==Rock and my_move=="R":
    print("Tie")
elif computer_move==Paper and my_move=="P":
    print("Tie")
elif computer_move==Scissors and my_move=="S":
    print("Tie")
elif computer_move==Rock and my_move=="S":
    print("You loose.")
elif computer_move==Rock and my_move=="P":
    print("You Won")
elif computer_move==Scissors and my_move=="P":
    print("You loose.")
elif computer_move==Scissors and my_move=="R":
    print("You Won") 
elif computer_move==Paper and my_move=="R":
    print("You loose.")
elif computer_move==Paper and my_move=="S":
    print("You Won")
else:
    print("invalid move")

