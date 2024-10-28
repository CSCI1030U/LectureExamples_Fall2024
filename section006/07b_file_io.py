with open('section006/data_files/plain.txt', 'r') as text_file:
    # contents = text_file.readlines()
    for line in text_file:
        print(f'{line[:-1] = }')
    # print(f'{text_file = }') 
# print(f'{contents = }') 
