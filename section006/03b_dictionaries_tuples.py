# hacker's corner

x = 1
y = 2

# C++ way
temp = x 
x = y 
y = temp 

# Python way
x,y = y,x 

# coding exercise 1

sentence = 'the quick brown fox jumped over the lazy dog'
# print(f'{sentence[::-1] = }')

words = sentence.split(' ')
# reverse_words = words[::-1]
reverse_words = []
reverse_sentence = ''
for word in words:
    reverse_words.insert(0, word)
    reverse_sentence = word + ' ' + reverse_sentence
print(f'{reverse_words = }')
print(f'{reverse_sentence = }')
reverse_string2 = ' '.join(reverse_words)


# coding exercise 2

email = """Dear Sir or Madam, Your recent transaction is ready to be approved. If this transaction is fraudulent, then click to
cancel the transaction the Purchasing Department or be scammed"""
frequencies = {}
words = email.split(' ')
# print(f'{words = }')
for word in words:
    if word in frequencies.keys():
        frequencies[word] += 1
    else:
        frequencies[word] = 1

# print(f'{frequencies = }')

# coding challenge
names = ['Kevin', 'Luisa', 'Ahmed']
marks = [65.0, 73.5, 81.0]
student_data = []
for i in range(len(names)):
    student = {
        'name': names[i],
        'mark': marks[i]
    }
    student_data.append(student)
# print(f'{student_data = }')