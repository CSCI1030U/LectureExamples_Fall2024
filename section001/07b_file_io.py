# file = open('section001/data_files/plain.txt', 'r')
with open('section001/data_files/plain.txt', 'r') as in_file:
    # contents = file.read()
    for line in in_file:
        print(f'{line = }')
    # file.read(1)
    # file.readline()
# file.close()
# print(f'{contents = }')

product = {
    'brand': 'Apple',
    'model': 'iPhone 13',
    'price': 1800.00,
    'flash': 128,
    'ram': 16
}
with open('section001/data_files/product.txt', 'w') as out_file:
    out_file.write(str(product))

shopping_cart = [
    {'product-id': 17723, 'quantity': 10},
    {'product-id': 53682, 'quantity': 1},
    {'product-id': 32704, 'quantity': 1},
    {'product-id': 8110, 'quantity': 2},
]
import json

with open('section001/data_files/shopping_cart.json', 'w') as cart_out:
    json.dump(shopping_cart, cart_out)

with open('section001/data_files/shopping_cart.json', 'r') as cart_in:
    sc = json.load(cart_in)

print(f'{sc = }')
print(f'{sc[1] = }')
print(f'{sc[1]['product-id'] = }')

# coding exercise 1

sids = ['100000000', '100000001', '100000002', '100000003', '100000004', '100000005', '100000006', '100000007', '100000008', '100000009']
marks = [52.0, 48.5, 54.25, 61.5, 64.0, 77.75, 29.0, 91.25, 68.25, 59.75]
with open('section001/data_files/marks.csv', 'w') as marks_out:
    for i in range(len(sids)):
        marks_out.write(f'{sids[i]},{marks[i]}\n')

midterms = []
with open('section001/data_files/marks.csv', 'r') as marks_in:
    for line in marks_in:
        data = line.split(',')
        student = {
            'student-id': int(data[0]),
            'midterm-mark': float(data[1])
        }
        midterms.append(student)
print(f'{midterms = }')
