print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120 :
    print("you can ride")
    age = int(input("What is your age? "))
    if age <= 12:
        print("pay $5")
    elif age <= 18:
        print("pay $7")
    elif age <= 21:
        print("pay $10")
else :
    print("you are not allowed")
