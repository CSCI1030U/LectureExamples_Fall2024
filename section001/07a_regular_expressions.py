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

even_num_binary = '([01]{2})*'
