print("Welcome to the Tip Calculator\n")
bill = float(input("What was the total bill? "+"$\n"))
tip = float(input("How much tip you want to give? "+"%\n"))
tip_amount = bill * tip / 100
people = int(input("How many people to split the bill? \n"))
splited_bill = (bill + tip_amount) / people
print("tip amount "+"$\n",tip_amount)
print(f"Each person should pay: {splited_bill}"+"$\n")

