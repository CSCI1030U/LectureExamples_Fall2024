def forever(message):
    print(message)
    forever(message)

# forever('hello') # infinite recursion

def repeat_n_times(n, message):
    if n < 1:
        return
    
    print(f'repeat_n_times: {n = } {message = }')

    repeat_n_times(n - 1, message)

    # will happen in reverse order
    # print(f'repeat_n_times: {n = } {message = }')

repeat_n_times(3, 'Hello!')

# coding exercise 1

# 0, 1, 1, 2, 3, 5, 8, 13, ...

def fib(n):
    if n <= 1:
        return n 
    
    return fib(n - 1) + fib(n - 2)

print(f'{fib(2) = }')
print(f'{fib(5) = }')
print(f'{fib(8) = }')
# print(f'{fib(50) = }') # heat death of the universe
