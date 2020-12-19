MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def select_coffee():
  select_coffee = True
  while select_coffee:
    coffee_choice = input("What would you like? (espresso/latte/cappucino):\n").lower()
    if coffee_choice == "report":
      show_current_state(input("Write password: \n"))
      if input("Do you want to make an order?(Y/N)".lower()) != "y":
        return 0
    elif coffee_choice not in ["espresso", "latte", "cappucino"]:
      wrong_coffee = input("You selected the wrong coffee. Do you want to try again?(Y/N)\n").lower()
      if wrong_coffee != "y":
        return 0
    else:
      print(f"You selected {coffee_choice}.")
      return coffee_choice

def show_current_state(password):
  if password == "qwerty": # very bad choice of password xD
    for key, value in resources.items():
      print(f"{key}: {value}")
  else:
    print("You don't have enough rights")

def check_ingredients(coffee):
  for ingredient in MENU[coffee]["ingredients"]:
    if MENU[coffee]["ingredients"][ingredient] > resources[ingredient]:
      return 0, ingredient
  return 1


def insert_money(coffee):
    print(f"You need to pay ${MENU[coffee]['cost']}. Please insert coins:")
    quarters = int(input("How many quarters?: ")) # 25 cents
    dimes = int(input("How many dimes?: ")) # 10 cents
    nickles = int(input("How many nickles?: ")) # 5 cents
    pennies = int(input("How many pennies?: ")) # 1 cents
    return quarters, dimes, nickles, pennies

def update_machine_status(coffee):
  for ingredient in MENU[coffee]["ingredients"]:
    resources[ingredient] = resources[ingredient]- MENU[coffee]["ingredients"][ingredient]
  resources['money'] = MENU[coffee]["cost"]

def coffee_machine():
  coffee = select_coffee()
  if coffee == 0:
    return 0
  ingredients_status = check_ingredients(coffee)
  if ingredients_status != 1:
    print(f"Not sufficient amount of {ingredients_status[1]}.")
    return 0
  quarters, dimes, nickles, pennies = insert_money(coffee)
  payed_sum = 0.25*quarters+0.1*dimes+0.05*nickles+0.01*pennies
  if payed_sum < MENU[coffee]['cost']:
    print(f"Sorry that's not enough money. Money refunded.")
    return 0
  elif payed_sum > MENU[coffee]['cost']:
    money_change = payed_sum - MENU[coffee]['cost']
    print(f"Here is ${money_change} in change.")
  else:
    money_change = 0
  return 1, coffee


while True:
  coffee_process_status = coffee_machine()
  if coffee_process_status == 0:
    print("Thank you for using our coffee machine!")
    break
  else:
    update_machine_status(coffee_process_status[1])
    print(f"Here is your {coffee_process_status[1]}. Enjoy! ")
    again_choice = input("Do you want to make 1 more order?(Y/N)\n").lower()
    if again_choice !='y':
      break
