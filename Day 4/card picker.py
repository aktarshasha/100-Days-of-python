# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

#finding length
n=len(names_string)
import random
#randamaisation
choice = random.randint(1, n-1)

person_who_pays =names[choice]

print(f"{person_who_pays}is going to buy the meal today!")
