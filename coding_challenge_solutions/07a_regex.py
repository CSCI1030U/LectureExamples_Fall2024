import re 

def validate_email(string):
    email_fsa = re.compile('^[a-zA-Z_][a-zA-Z0-9_.]*@[a-zA-Z0-9_.]+(\.[a-zA-Z0-9_.]+)*\.(ca|com|gov|net|edu|uk)$')
    result = email_fsa.match(string)
    return result != None

print(f'{validate_email("randy.fortier@ontariotechu.net") = }')
print(f'{validate_email("candy_canes1@sweets.co.uk") = }')
print(f'{validate_email("candy_canes1@sweets.co.uk.") = }')
