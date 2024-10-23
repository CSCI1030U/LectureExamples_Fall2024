coding_challenge = 'x+y+x'
class_exercise = 'a{3,}\d{2}\w'

'''
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
