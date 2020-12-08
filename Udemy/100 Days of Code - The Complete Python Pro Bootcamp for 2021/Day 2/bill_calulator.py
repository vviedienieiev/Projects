bill = float(input("Plese tell me what is the sum in your bill?\n"))
num_persons = int(input("How many person are going to pay?\n"))
tips = int(input("What is the amount of tips?\n"))

bill_per_person = round(bill*(1+tips/100)/num_persons,2)

print(f"Each person should pay {bill_per_person} USD")
