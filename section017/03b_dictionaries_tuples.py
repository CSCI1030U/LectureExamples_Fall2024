# hacker's corner

x = 5
y = 10

# C++ way
temp = x 
x = y 
y = temp 

# Python
x,y = y,x 

email = '''
Dear sir or madam we received your fund transfer request of $10,000. this will automatically complete in 3 days if you want to cancel, please reply to this message within 2 days thank you for your business the Accounting Department
'''
words = email.split(' ')
# print(f'{words = }')

frequency = {}
for word in words:
    if word in frequency.keys():
        frequency[word] += 1
    else:
        frequency[word] = 1

print(f'{frequency = }')
