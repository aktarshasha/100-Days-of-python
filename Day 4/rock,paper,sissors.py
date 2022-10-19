rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''




choice=input("What do you choose? Type 0 for Rock,1 for paper,2 for scissors ")

print("you choose")
if choice == '0':
 print(rock)
elif choice == '1':
 print(paper)
elif choice == '2':
 print(scissors)

print("computer choose")

import random
c_choice= random.randint(0, 2)

if c_choice == 0:
 print(rock)
elif c_choice == 1:
 print(paper)
elif c_choice == 2:
 print(scissors)

if choice<'0'or choice>='3':
    print("invalid input")
elif choice=='0' and c_choice==2:
    print("you win!")
elif choice=='1' and c_choice==0:
    print("you win!")
elif choice=='2' and c_choice==1:
    print("you win!")
elif choice=='2' and c_choice==0:
    print("you loose!")
elif choice=='0' and c_choice==1:
    print("you loose!")
elif choice=='1' and c_choice==2:
    print("you loose!")
elif choice==c_choice:
    print("its a draw")
    
