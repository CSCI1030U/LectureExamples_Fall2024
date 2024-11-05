# old/risky way
input_file = open('section017/data_files/plain.txt', 'r')
contents = input_file.read()
print(f'{contents = }')
input_file.close()

# recommended way
with open('section017/data_files/plain.txt', 'r') as input_file:
    # contents = input_file.read()
    for line in input_file:
        print(f'{line = }')
# print(f'{contents = }')

# writing to a file
customer = {
    'name': 'Lenny Fortier',
    'customer-since': '2022-05-03',
    'balance': 0.0
}
with open('section017/data_files/customer.txt', 'w') as output_file:
    output_file.write(str(customer) + '\n')

import json 
with open('section017/data_files/high_scores.json', 'r') as hs_file:
    high_scores = json.load(hs_file)

for score in high_scores:
    print(f'{score["name"]} had the score {score["score"]}')

with open('section017/data_files/customer.json', 'w') as cust_file:
    json.dump(customer, cust_file) # need to switch arg order

# coding exercise 1

sids = ['100000000', '100000001', '100000002', '100000003', '100000004', '100000005', '100000006', '100000007', '100000008', '100000009']
midterm_marks = [52.0, 48.5, 54.25, 61.5, 64.0, 77.75, 29.0, 91.25, 68.25, 59.75]

with open('section017/data_files/student_data.csv', 'w') as student_out:
    for i in range(len(sids)):
        student_out.write(f'{sids[i]},{midterm_marks[i]}\n')

# coding exercise 2

student_records = []
with open('section017/data_files/student_data.csv', 'r') as student_in:
    for line in student_in:
        data = line.split(',')
        new_student = {
            'student-id': int(data[0]),
            'midterm-mark': float(data[1])
        }
        student_records.append(new_student)

print(f'{student_records = }')
print(f'{student_records[1] = }')
print(f'{student_records[1]["midterm-mark"] = }')

