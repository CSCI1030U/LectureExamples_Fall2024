coding_challenge = 'x+y+x'
class_exercise = 'a{3,}\d{2}\w'

r'''
.. - any 2 characters
a|b - a or b
(a|b)(a|b) - any two a's or b's
(a|b)* - 0 or more a's or b's
(a|b)+ - 1 or more a's or b's
(a|b+) - either a single a or 1 or more b's
a?b+ - an optional a, followed by 1 or more b's 
(a|b){7} - exactly 7 a's or b's
(a|b){7,} - 7 or more a's or b's
(a|b){2,7} - between 2 and 7 a's or b's
(a|b|c|d|e|f|....|z) - any lowercase letter
[abcdefghijklmnopqrstuvwxyz] - any lowercase letter
[a-z] - any lowercase letter
[aeiou] - any lowercase vowel
[.!?;:,] - any punctuation
[^aeiou] - any character other than lower vowel
\d - any single digit 
'''

import re 

challenge_fsm = re.compile('x+y+x')
challenge_result = challenge_fsm.match('xxxyyx')

print(f'{challenge_result = }')

message = 'Hi\\there.\nHow are you doing?\'\t'

price_regex = r'\$\d+(\.\d\d)?' # $100, $99.99
price_fsm = re.compile(price_regex)
amazon_review = 'I bought this for  back in 2023...'
price_result = price_fsm.search(amazon_review)

if price_result:
    print(f'{price_result.start() = }')
    print(f'{price_result.end() = }')
    print(f'{price_result.group() = }')
else:
    print('No price found')

name_fsm = re.compile(r'[A-Z][a-z]*')
name_result = name_fsm.findall('J Jonah Jamieson')
print(f'{name_result = }')

sentence = 'this quick, brown, fox jumped; over the lazy dog'
punct_fsm = re.compile(r'[.,:;?!" ]+')
words = re.split(punct_fsm, sentence)
print(f'{words = }')

# coding exercise 1

binary_fsm = re.compile(r'^[01]{8}([01]{8})?$')
print(f'{binary_fsm.search("01101100") = }')
print(f'{binary_fsm.search("0110110011110000") = }')
print(f'{binary_fsm.search("01101100110") = }')
print(f'{binary_fsm.search("01101100 is the number") = }')
print(f'{binary_fsm.search("here it is: 01101100") = }')
