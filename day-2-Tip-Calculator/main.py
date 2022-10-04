
print("Welcome to tip calculator.")
bill = input("What was the total bill : $")
tip = input("What percentge tip would you like to give? 10,12 or 15 ?")
person = input("How many person to split the bill ?")
value = (int(bill)/ int(person) * ((int(tip)/100) + 1))
new_value = '{:.2f}'.format(value)
print("Each person should pay : $", new_value)
