def forever(message):
    print(message)
    forever(message)

# forever('hello') # infinite recursion

def repeat_n_times(n, message):
    if n < 1:
        return 
    
    print(f'{n = } {message = }')

    repeat_n_times(n - 1, message)

repeat_n_times(3, 'hello')

# coding exercise 1

def fib(n):
    if n == 0 or n == 1:
        return n 
    
    return fib(n - 1) + fib(n - 2)

print(f'{fib(0) = }')
print(f'{fib(1) = }')
print(f'{fib(2) = }')
print(f'{fib(3) = }')
print(f'{fib(4) = }')
print(f'{fib(5) = }')
print(f'{fib(6) = }')
# print(f'{fib(60) = }') # yikes!
