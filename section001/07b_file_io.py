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

