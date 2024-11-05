names = ['Carla', 'Susanne', 'Ahmed', 'Wil']

try:
    print(f'{names[4] = }')
except IndexError as error:
    print('No such name at that index!')
except Exception as error:
    print('Something else happened!')

print('After the error')

def print_names(names, indexes):
    for index in indexes:
        print(names[index])

# print_names(['Carla', 'Susanne', 'Ahmed', 'Wil'], [0, 2, 4])

class InsufficientFundsError(Exception):
    pass

def pay_bill(account_balance, bill_amount):
    if bill_amount > account_balance:
        raise InsufficientFundsError('Account balance too low to pay this bill.')

    return account_balance - bill_amount

try:
    new_balance = pay_bill(100.0, 160.0)
    print(f'{new_balance = }')
except InsufficientFundsError as error:
    print(f'Error while paying bill: {error}')
    # quit() # if you still want the application to stop - e.g. catastrophic error

print('After paying the bill')

# coding exercise 1

class InvalidReciprocalError(Exception):
    pass

# custom error - no handling
# def print_reciprocals(values):
#     for n in values:
#         if n == 0:
#             raise InvalidReciprocalError('Cannot calculate 1/0')
#         print(f'{1/n = }')

# handling the error
def print_reciprocals(values):
    for n in values:
        try:
            print(f'{1/n = }')
        except ZeroDivisionError as error:
            print('Cannot calculate 1/0.')

print_reciprocals([0,1,2,3,4,5])
