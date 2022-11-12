list = []
num = int(input('How many numbers: '))

for n in range(num):
    numbers = int(input('Enter number '))
    list.append(numbers)
e= max(list)+ min(list)
print(e)
