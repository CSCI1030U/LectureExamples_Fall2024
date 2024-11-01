names = ['Barb', 'Kumar', 'Aleishia']

try:
    print(f'{names[3] = }')
except IndexError as error:
    print('Index [3] doesn\'t exist')

print('All done printing the 4th name')

class InsufficientFundsException(Exception):
    pass 

def buy_product(price, account_balance):
    if price > account_balance:
        raise InsufficientFundsException(f'You cannot afford ${price}.')
    account_balance -= price 
    print(f'{account_balance = }')

account_balance = 100.0
try:
    buy_product(150.0, account_balance)
except InsufficientFundsException as error:
    print('That costs too much, sorry!')

# coding exercise 1

class NoZeroAllowed(Exception):
    pass

def print_reciprocals(values):
    for n in values:
        # if n == 0:
        #     raise NoZeroAllowed('You cannot 1/0')
        try:
            print(f'{1/n = }')
        except ZeroDivisionError as error:
            print('Cannot calculate 1/0')

print_reciprocals([5,4,3,2,1,0])