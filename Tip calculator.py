print("Welcome to Tip Calculator!")
# Ask the user for total bill amount.
bill = float(input("What is the total amount of the bill?"))
# Ask for percentage of tip.
tip = int(input("What percentage of tip do you wish to give?")
#Ask for the number in which the bill needs to be splited in.
split = int(input("How many people the amount should be splited in"))
# Caculate the amount each person has to pay.
amount_to_pay = (bill + (bill * tip/100))/split
print(f"Each person has to pay : {amount_to_pay}")
