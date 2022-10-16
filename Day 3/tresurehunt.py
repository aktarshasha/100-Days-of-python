print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
crossroad= input ("you approuch a crossroad. 'right' or 'left'\n ").lower()
if crossroad == "left" :
    print("proceed")
    forest= input("u arrived at a nearby forest type 'go' to enter and 'wait' to wait\n" ).lower()
    if forest== "go" :
       print ("level 2 complete. proceed")
       castle= input("u have arrived a castle unharmed. you have 3 door in frount of you 'red' 'yellow' and 'blue'.choose one\n").lower()
       if castle == "blue" :
         print("gelchinav ra pukesh")
       elif castle =="yellow":
         print("chii po raww")
       elif castle =="red":
           print("lanjodkaa")
       else:
           print("pikinav tee")
    else :
       print("game over!! you raped by a monster")
else :
    print("game over!! you stepped into a hole")
