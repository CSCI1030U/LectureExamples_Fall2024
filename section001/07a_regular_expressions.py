r"""
.. - any 2 characters
a|b - either an 'a' or a 'b'
(a|b) - either an 'a' or a 'b'
(a|b)* - 0 or more a's or b's
(a|b*) - 1 'a' or 0 or more b's
ab - 1 a and then 1 b
(a|b)(a|b) - 1 a or b, then 1 more a or b
\(.*\) - a left bracket, then 0 or more characters (any), then a right bracket
(a|b|c|d|e|f|g|...|y|z) - any lowercase letters
a+ - 1 or more a's
aa* - 1 or more a's
a?bb - either 1 a or no a's, then 2 b's
(a|b)? - an optional a or b
(a|b){3} - exactly 3 a's or b's
(a|b){1,3} - between 1 and 3 a's or b's
(a|b){3,} - 3 or more a's or b's
[0-9] - any single digit
\d - any single digit
[aeiou] - any lowercase vowel
[a-z] - any lowercase letter
[a-zA-Z] - any letter (uppercase or lowercase)
[^a-z] - any character other than a lowercase letter
[^aeiou] - any character other than a lowercase vowel
[.,;:?!] - any punctuation character
[.,;:?!]+ - any 1 or more punctuation characters
"""
import re 

variable_regex = '[a-zA-Z_]\\w*'
variable_fsm = re.compile(variable_regex)

print(f'{variable_fsm.match("avg_price2") = }')
print(f'{variable_fsm.match("max_cost=") = }')
print(f'{variable_fsm.match("2num_sum") = }')
print(f'{variable_fsm.search(" avg_price < 18.0:") = }')
print(f'{variable_fsm.findall("avg_price max_value midterm_avg") = }')

sentence = 'the quick, brown, fox; jumped over - the lazy dog.'
separator = re.compile(r'[,;\-.:!? ]+')
words = re.split(separator, sentence)
print(f'{words = }')

even_num_binary_regex = '([01]{2})*'
even_num_binary_fsm = re.compile(even_num_binary_regex)
if even_num_binary_fsm.match('001101'):
    print(f'It is a match')

# coding exercise 

# eight_or_sixteen_regex = '[01]{8}|[01]{16}'
eight_or_sixteen_regex = '^[01]{8}([01]{8})?$' # exact match with ^ and $
# eight_or_sixteen_regex = '[01]{8,16}' # incorrect
eight_or_sixteen_fsm = re.compile(eight_or_sixteen_regex)
print(f'{eight_or_sixteen_fsm.search("00111010") = }')
print(f'{eight_or_sixteen_fsm.search("0011101011110000") = }')
print(f'{eight_or_sixteen_fsm.search("001110101100") = }') # no
print(f'{eight_or_sixteen_fsm.search("My number is 01011010") = }') # no
print(f'{eight_or_sixteen_fsm.search("01011010 is the best!") = }') # no

