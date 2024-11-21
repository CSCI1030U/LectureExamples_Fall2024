class NotOldEnoughError(Exception):
    pass

age = int(input('What is your age? '))
if age < 18:
    raise NotOldEnoughError('You need to be 18 or older to vote')
