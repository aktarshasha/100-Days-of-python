print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120 :
    print("you can ride")
    age = int(input("What is your age? "))
    if age <= 12:
        bill =5
        print("child tickets are $5")
    elif age <= 18:
        bill =7
        print("teenagers tickets are $7")
    elif age <= 21:
        bill =10
        print("adult tickets are $10")
    elif age >= 45 and age<= 55 :
        print("adult tickets are $0")
        wants = input("do you want photos Y or N. ")
    if wants == "Y" :
       actual_bill = bill+3
       print(f"you have to pay ${actual_bill}")
else :
    print("you are not allowed")
