print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $ "))
tip = int(input("How much percent tip would you like to provide? "))
total = (bill * (tip/ 100)) + bill
print(f"Total: ${total}")
split = int(input("how many will split the bill ? "))
print(f"Each person pays $ {round(total/split, 2)}")
