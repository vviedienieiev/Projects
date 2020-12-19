from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()


while True:
  money_machine.money_received = 0
  coffee = input(f"What would you like? {menu.get_items()}:\n").lower()
  order = menu.find_drink(order_name = coffee)
  if order is not None:
    is_enough_resources = coffee_machine.is_resource_sufficient(order)
    if is_enough_resources:
      is_processed = money_machine.make_payment(order.cost)
      if is_processed:
        coffee_machine.make_coffee(order)
        choice = input("Do you want to make another order?(Y/N):\n").lower()
        if choice != "y":
          break