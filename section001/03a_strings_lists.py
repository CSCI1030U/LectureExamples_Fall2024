email = """Dear Ms. Johnson,

This letter is to apply for....

Regards,
Carla
"""
print(f'{email = }')

name = 'Carla Rodriguez'
print(f'{name[0] = }')
# name[4] = 'o'
# print(f'{name = }')

print(f'{name[::-1]}')

# coding exercise 1

full_name = 'Eren Yeager'
for i in range(len(full_name)):
    if full_name[i] == ' ':
        space_index = i 
print(f'{space_index = } {full_name[space_index] = }')

first_name = full_name[0:space_index]
print(f'{first_name = }')

last_name = full_name[space_index + 1:]
print(f'{last_name = }')


names = ['Indu', 'Simba', 'Randy', 'Pablo', 'Inigo', 'Simba']
names.remove('Simba')
print(f'{names = }')

# coding exercise 2

marks = [52.0, 65.0, 71.5, 80.75, 90.0, 35.0]
print(f'{sum(marks) / len(marks) = }')

sum = 0.0
length = 0
for mark in marks:
    sum += mark 
    length += 1
print(f'{sum / length = }')