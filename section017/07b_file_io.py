# old/risky way
input_file = open('LectureExamples_Fall2024/section017/data_files/plain.txt', 'r')
contents = input_file.read()
print(f'{contents = }')
input_file.close()

# recommended way
with open('LectureExamples_Fall2024/section017/data_files/plain.txt', 'r') as input_file:
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
with open('LectureExamples_Fall2024/section017/data_files/customer.txt', 'w') as output_file:
    output_file.write(str(customer) + '\n')

import json 
with open('LectureExamples_Fall2024/section017/data_files/high_scores.json', 'r') as hs_file:
    high_scores = json.load(hs_file)

for score in high_scores:
    print(f'{score["name"]} had the score {score["score"]}')

with open('LectureExamples_Fall2024/section017/data_files/customer.json', 'w') as cust_file:
    json.dump(cust_file, customer) # need to switch arg order

