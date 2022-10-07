print("Welcome to the tip calculator!")
bill=float(input("What was the total bill? $"))
tip=int(input ("How much tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill? "))
tip_to_percent = tip / 100
total_tip2 = bill * tip_to_percent
total_bill = bill + total_tip2
split = total_bill / people
final_amount = round(split, 2)
print (f"Each person should pay: ${final_amount}" )
