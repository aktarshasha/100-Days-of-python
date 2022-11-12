num=[]
num = input("Input num ").split()

highest_num = 0
for num in num:
  if num > highest_num:
    highest_num = num
smallest_num = 0
for num in num:
    if num < smallest_num:
        smallest_num = num
e= smallest_num + highest_num
print(e)
