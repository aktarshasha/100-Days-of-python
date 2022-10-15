# own code 2
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

height2 = float(height)
weight2 = float (weight)
result = (weight2 / (height2 * height2))
result = round(result)
if result <= 18.5 :
 print(f"Your BMI is {result}, you are underweight.")
elif result <= 25 :
        print(f"Your BMI is {result}, you have a normal weight.")
elif result <= 30 :
        print(f"Your BMI is {result}, you are slightly overweight.")
elif result <= 35 :
        print(f"Your BMI is {result}, you are obese.")
elif result >= 40 :
        print (f"Your BMI is {result}, you are clinically obese.")
