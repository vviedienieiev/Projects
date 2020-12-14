from replit import clear
import art
print(art.logo)
name = input("What is your name?\n")
bid = int(input("What is your bid?\n"))
auction = {name: bid}

other_bidders = True
while other_bidders:
  if input("Is there any other biders?\n").lower() == "yes": 
    name = input("What is other bider`s name?\n")
    bid = int(input("What is other bider`s bid?\n")) 
    auction[name] = bid
  else:
    other_bidders = False

max_val = 0
max_key = 0
for key,value in auction.items():
  if value > max_val:
    max_val = value
    max_key = key 
print(f"The winner is {max_key} with bid ${max_val}")
