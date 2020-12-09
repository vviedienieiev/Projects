print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
doors = input("You see 2 doors. Left and right. Which one will you choose?(L/R)\n")
if doors.lower() != "l":
  print("Fall into a hole.\nGame Over!!!")
else:
  island = input("You exited the house and stay near the beach. You need to get to the island in the middle of the lake. You can smiw or wait for the boat. What will you do?(S\W)\n")
  if island.lower() != "w":
    print("You died from piranhas.\nGame over!!!")
  else:
    three_doors = input("Now you see 3 doors. Red, blue and yellow. Which one are you going to choose?(R\B\Y)\n")
    if three_doors.lower() == "r":
      print("Burned by fire.\nGame over!!!")
    if three_doors.lower() == "b":
      print("Eaten by beasts.\nGame over!!!")
    if three_doors.lower() == "y":
      print("You win!!!")
    else:
      print("Game over!!!")
