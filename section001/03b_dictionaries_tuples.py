# coding exercise 1

sentence = 'the quick brown fox jumped over the lazy dog'

# 1. divide up the string into words (list of words)
words = sentence.split(' ')
print(f'{words = }')

# 2. reverse the list of words
# reverse_words = words[::-1]
reverse_words = []
for word in words:
    reverse_words.insert(0, word)

print(f'{reverse_words = }')

# 3. put the words back into single string/sentence
# reverse_sentence = ' '.join(reverse_words)
reverse_sentence = ''
for word in reverse_words:
    reverse_sentence = reverse_sentence + ' ' + word

print(f'{reverse_sentence[1:] = }')

# hacker's corner

x = 0
y = 10

# C++ way
temp = x
x = y 
y = temp 

# python way
x,y = y,x 

# coding exercise 2

email = '''
Dear sir or madam You have recently made this purchase to us for new TV for $20000.  To cancel this
transaction please reply to this E-mail with your mother's maiden
name this Billing Department
'''
words = email.split(' ')
print(f'{words = }')
freq = {}
for word in words:
    if word in freq.keys():
        freq[word] += 1
    else:
        freq[word] = 1

print(f'{freq = }')