import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

actions = [rock, paper, scissors]
your_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 For Scissors.\n'))
computer_choice = random.randint(0,2)
print(your_choice, computer_choice)
print(f"Your choice is:\n{actions[your_choice]}\nComputer choice is:\n{actions[computer_choice]}")
if your_choice == computer_choice:
  print("Nobody wins")
elif (your_choice == 0) & (computer_choice == 2):
    print("You win!!!")
elif (computer_choice == 0) & (your_choice == 2):
    print("You lose!!!")
elif your_choice > computer_choice:
  print("You win!!!")
else:
  print("You lose!!!")
