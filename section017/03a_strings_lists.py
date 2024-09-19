email = """Dear Ms. Wellington,

This letter is to...

Randy"""

'''
Comment line 1
Comment line2
'''

name = 'Keanu Reeves'
print(f'{name[0] = }')
print(f'{name[2] = }')
print(f'{name[-1] = }')
print(f'{name[0:5] = }')
print(f'{name[::] = }')
print(f'{name[::-1] = }')

# coding exercise 1

full_name = 'Paul McCartney'
for index in range(len(full_name)):
    if full_name[index] == ' ':
        space_index = index 
print(f'{index = }')
print(f'{space_index = }')

first_name = full_name[0:space_index]
print(f'{first_name = }')
last_name = full_name[space_index + 1:]
print(f'{last_name = }')

midterm_marks = [52.0, 71.5, 65.0, 90.0, 71.25, 50.0, 44.0, 62.5, 65.0]
print(f'{midterm_marks[-1] = }')
print(f'{midterm_marks[2:7] = }')
print(f'{midterm_marks[::-1] = }')
midterm_marks[5] = 55.0
midterm_marks.append(100.0)
midterm_marks.insert(0, 35.0)
print(f'{midterm_marks = }')
midterm_marks.remove(65.0)
print(f'{midterm_marks = }')
midterm_marks.pop(0)
midterm_marks.pop()
print(f'{midterm_marks = }')

# coding exercise 2
midterm_marks = [52.0, 71.5, 65.0, 90.0, 71.25, 50.0, 44.0, 62.5, 65.0]
print(f'{sum(midterm_marks) / len(midterm_marks) = }')

sum = 0.0
count = 0
for mark in midterm_marks:
    sum += mark 
    count += 1
print(f'{sum / count = }')


