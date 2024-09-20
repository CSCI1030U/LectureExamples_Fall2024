# coding challenge 03a.1

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
count = 0
sum = 0
for val in values:
    if (val % 2) == 0:
        sum += val 
        count += 1

print(f'{sum/count = }')