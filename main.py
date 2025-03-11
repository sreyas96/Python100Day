bill = 0
print("Welcome to Python Pizza Deliveries!")

size = input("What size of pizza do you want? S, M, or L: ").lower()
if size == "s":
    bill = bill + 15
elif size =="m":
    bill = bill + 20
elif size == "l":
    bill = bill + 25
else:
    print("Invalid size")

pepperroni = input("Do you wnat pepperroni? Y or N: ").lower()
if pepperroni == "y":
    bill = bill + 2

extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
if extra_cheese == "y":
    bill = bill + 3

print (f"Your final bill is: {bill}")


