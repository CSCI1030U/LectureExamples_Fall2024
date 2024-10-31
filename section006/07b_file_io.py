with open('section006/data_files/plain.txt', 'r') as text_file:
    # contents = text_file.readlines()
    for line in text_file:
        print(f'{line[:-1] = }')
    # print(f'{text_file = }') 
# print(f'{contents = }') 

esports_user = {
    'user-id': 1234,
    'games': ['Dead by Daylight', 'Fortnite'],
    'league': 'Elite',
    'rank': 1
}
with open('section006/data_files/esports.txt', 'w') as esports_file:
    esports_file.write(str(esports_user) + '\n')

import json 

with open('section006/data_files/marks.json', 'r') as marks_file:
    marks = json.load(marks_file)

print(f'{marks = }')
print(f'{marks[1] = }')
print(f'{marks[1]["sid"] = }')

with open('section006/data_files/esports.json', 'w') as esports_out:
    json.dump(esports_user, esports_out)

sids = ['100000000', '100000001', '100000002', '100000003', '100000004', '100000005', '100000006', '100000007', '100000008', '100000009']
midterm_marks = [52.0, 48.5, 54.25, 61.5, 64.0, 77.75, 29.0, 91.25, 68.25, 59.75]
# 100000000,52.0
# 100000001,48.5
# ...etc...

# coding exercise 1
with open('section006/data_files/grade_output.csv', 'w') as grades_out:
    for i in range(len(sids)):
        grades_out.write(f'{sids[i]},{midterm_marks[i]}\n')

# coding exercise 2
student_marks = []
with open('section006/data_files/grade_output.csv', 'r') as grades_in:
    for line in grades_in:
        data = line.split(',')
        new_student = {
            'student-id': data[0],
            'midterm-mark': float(data[1])
        }
        student_marks.append(new_student)

print(f'{student_marks = }')
