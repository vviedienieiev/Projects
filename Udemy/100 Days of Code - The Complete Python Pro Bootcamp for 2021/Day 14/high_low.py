import art
import game_data
import random
from replit import clear

def first_game(full_list):
  A = random.randint(0, len(full_list)-1)
  while True:
    B = random.randint(0, len(full_list)-1)
    if A != B:
      return A,B

def other_games(A,B, full_list):
  A = B
  while True:
    B = random.randint(0, len(full_list)-1)
    if A != B:
      return A,B


def play(a,b):
  clear()
  print(art.logo)
  print(f"Your score is {score}")
  print("You will compare the following:")
  print(f"{full_list[a]['name']}, {full_list[a]['description']} from {full_list[a]['country']}\n")
  print(art.vs)
  print(f"{full_list[b]['name']}, {full_list[b]['description']} from {full_list[b]['country']}\n")
  choice = input("Who has more follower? Write 'A' or 'B':\n").lower()
  A_followers, B_followers = full_list[a]["follower_count"], full_list[b]["follower_count"]
  if (choice == 'a') & (A_followers > B_followers):
    return True
  elif (choice == 'b') & (B_followers > A_followers):
    return True
  else:
    print(f"{full_list[a]['name']} has {full_list[a]['follower_count']} followers\n{full_list[b]['name']} has {full_list[b]['follower_count']} followers")
    return False


full_list = game_data.data
A,B = first_game(full_list)
score = 0
while play(A,B):
  score += 1
  A,B = other_games(A,B,full_list)
print(f"Your final score is {score}! Try get 6.")
  
