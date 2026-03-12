a, b = map(int, input().split())

number = 0 

while True:
    if a % b == 0:
        number += 1
        break 
    number += 1
    a -= number 
print(number)