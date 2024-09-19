course = 'CSCI1030U'
print(f'{course[::-1] = }')

full_name = 'Ryan Reynolds'
for i in range(len(full_name)):
    if full_name[i] == ' ':
        space_index = i 
print(f'{space_index = }, {full_name[space_index] = }')

first_name = full_name[0:space_index]
print(f'{first_name = }')

last_name = full_name[space_index + 1:]
print(f'{last_name = }')

names = ['Ryan', 'Bob', 'Randy', 'Gerald', 'Randy']
names.remove('Randy')
names.pop(0)
names.append('Christie')
names.insert(0, 'Esmerelda')
print(f'{names = }')
print(f'{names[1:4] = }')

# coding exercise 
midterm_marks = [55.0, 92.5, 88.25, 65.0, 62.5, 71.0]
print(f'{sum(midterm_marks) / len(midterm_marks) = }')

total = 0.0
count = 0
for mark in midterm_marks:
    total += mark 
    count += 1
print(f'{total / count = }')

# hacker's corner

def is_prime(x):
    return True

result = [x**2 for x in range(100) if is_prime(x)]
print(f'{result = }')