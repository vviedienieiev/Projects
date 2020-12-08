import time 

print("Hello, dear user!\nI will help you to create a new band name")
print("In order to help you to create band name, i need to know something about you")
city_name = input("Please, tell me where are you from?\n")
pet_name = input("What is the name of your pet?\n")
print("Give me few seconds to generate your band name.")
print("I almsot complete this task.")
time.sleep(3)
print("Here is it!!! Your band name is {} {}\n".format(city_name, pet_name))
