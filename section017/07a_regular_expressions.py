exercise_regex = 'x+y+x'

r'''
Basic operators:
. - any single character (e.g. 'a' or '\n' or '%')
\. - matches a single '.'
.. - any two characters
ab - an 'a' and then a 'b'
a|b - a single 'a' or a single 'b'
a|b|c|d|e|f|....|y|z - any single lowercase letter
(a|b) - a single 'a' or a single 'b'
b* - 0 or more b's
a|b* - either a single 'a' or 0 or more b's
(a|b)* - 0 or more a's or b's

Extended operators:
[abcdefghijklmnopqrstuvwxyz] - any single lowercase letter
[a-z] - any single lowercase letter
[a-z]* - 0 or more lowercase letters
[a-z]+ - 1 or more lowercase letters
[a-zA-Z] - any single letter (lowercase or uppercase)
[a-zA-Z_\-] - any single letter or underscore or dash
[0-9] - any single digit
[aeiou] - any single lowercase vowel
[0-9][0-9][0-9] - exactly 3 digits
[0-9]{3} - exactly 3 digits
[0-9]{2,5} - 2, 3, 4, or 5 digits (2-5 digits)
[a-z]{6,} - 6 or more lowercase letters
[^0-9] - any character except a digit
[^a-z] - any character except lowercase letters
[^aeiou] - any character except lowercase vowels
\d - any single digit
\w - any single 'word' character - same as [a-zA-Z0-9_]
\s - any 'space' character (including newlines, tabs, non-breaking spaces)
a*|b+ - 0 or more a's or 1 or more b's
[a-z]?[0-9] - an optional lowercase letter, then a single digit
'''
import re

variable_regex = r'[a-zA-Z_]\w*'
variable_fsm = re.compile(variable_regex) # regex -> fsm
print(f'{variable_fsm.match('avg_midterm_mark = 68.25') = }')
print(f'{variable_fsm.match('avg_midterm2_mark = 68.25') = }')
print(f'{variable_fsm.search('1_year_later = 100.0') = }')
variable_result = variable_fsm.search('max_age > 21:')
if variable_result:
    print(f'{variable_result.start() = }')
    print(f'{variable_result.end() = }')
    print(f'{variable_result.group() = }')

phone_regex = r'(1-)?[0-9]{3}-[0-9]{3}-[0-9]{4}'
phone_fsm = re.compile(phone_regex)
print(f'{phone_fsm.match("905-721-8668") = }')
print(f'{phone_fsm.match("1-905-721-8668") = }')
print(f'{phone_fsm.search("9057218668") = }')

# coding exercise 1

# binary_num_regex = '[01]{8}|[01]{16}'
binary_num_regex = '^[01]{8}([01]{8})?$' # ^ - start of string, $ - end of string
binary_num_fsm = re.compile(binary_num_regex)
print(f'{binary_num_fsm.search("1010010111000011") = }')
print(f'{binary_num_fsm.search("11000011") = }')
print(f'{binary_num_fsm.search("010111000011") = }')
print(f'{binary_num_fsm.search("binary: 1010010111000011") = }')
print(f'{binary_num_fsm.search("11000011 is the number") = }')
