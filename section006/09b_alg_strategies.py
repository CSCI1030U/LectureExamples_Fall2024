def binary_search(x, a, start, end):
    if start > end: # empty list
        return False 
    
    middle = (start + end) // 2
    if x == a[middle]:
        return True 
    elif x < a[middle]:
        return binary_search(x, a, start, middle - 1)
    else: # x > a[middle]
        return binary_search(x, a, middle + 1, end)

def binary_search_python(x, a):
    if len(a) < 1: # empty list
        return False 
    
    middle = len(a) // 2
    if x == a[middle]:
        return True 
    elif x < a[middle]:
        return binary_search_python(x, a[0:middle])
    else: # x > a[middle]
        return binary_search_python(x, a[middle+1:])

print(f'{binary_search_python(3, [1,2,3,4,5]) = }')
print(f'{binary_search_python(1, [1,2,3,4,5]) = }')
print(f'{binary_search_python(5, [1,2,3,4,5]) = }')
print(f'{binary_search_python(0, [1,2,3,4,5]) = }')
print(f'{binary_search_python(8, [1,2,3,4,5]) = }')

binary_search_python(0, [1,2,3])

# coding exercise 1

def search_dc(values, to_find):
    if len(values) == 0:
        return False 
    
    middle = len(values) // 2
    if to_find == values[middle]:
        return True 
    return search_dc(values[:middle], to_find) or \
        search_dc(values[middle+1:], to_find)

print(f'{search_dc([5,2,4,1,3], 4) = }')
print(f'{search_dc([5,2,4,1,3], 5) = }')
print(f'{search_dc([5,2,4,1,3], 3) = }')
print(f'{search_dc([5,2,4,1,3], 0) = }')
print(f'{search_dc([5,2,4,1,3], 8) = }')
