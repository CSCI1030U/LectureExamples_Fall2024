def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n - 1)

print(f'{factorial(0) = }')
print(f'{factorial(1) = }')
print(f'{factorial(2) = }')
print(f'{factorial(3) = }')
print(f'{factorial(4) = }')
print(f'{factorial(5) = }')
print(f'{factorial(6) = }')
