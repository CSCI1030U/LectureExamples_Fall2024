def binary_search(x, a, start, end):
    if start > end:
        return False 
    
    middle = (start + end) // 2

    if x == a[middle]:
        return True 
    elif x < a[middle]:
        return binary_search(x, a, start, middle - 1)
    else: # x > a[middle]
        return binary_search(x, a, middle + 1, end)

print(f'{binary_search(3, [1,2,3,4,5], 0, len([1,2,3,4,5])-1) = }') 
print(f'{binary_search(1, [1,2,3,4,5], 0, len([1,2,3,4,5])-1) = }') 
print(f'{binary_search(5, [1,2,3,4,5], 0, len([1,2,3,4,5])-1) = }') 
print(f'{binary_search(0, [1,2,3,4,5], 0, len([1,2,3,4,5])-1) = }') 
print(f'{binary_search(8, [1,2,3,4,5], 0, len([1,2,3,4,5])-1) = }') 

def binary_search2(values, to_find):
    if len(values) < 1:
        return False 
    
    middle = len(values) // 2

    if to_find == values[middle]:
        return True 
    elif to_find < values[middle]:
        return binary_search2(values[0:middle - 1], to_find)
    else: # to_find > values[middle]
        return binary_search2(values[middle + 1:], to_find)

print(f'{binary_search2([1,2,3,4,5], 3) = }') 
print(f'{binary_search2([1,2,3,4,5], 1) = }')
print(f'{binary_search2([1,2,3,4,5], 5) = }')
print(f'{binary_search2([1,2,3,4,5], 0) = }')
print(f'{binary_search2([1,2,3,4,5], 8) = }')

# coding exercise 1

def search_dc(values, to_find):
    if len(values) == 0:
        return False 
    
    middle = len(values) // 2
    if to_find == values[middle]:
        return True 

    first_half = values[0:middle]
    second_half = values[middle+1:]

    return search_dc(first_half, to_find) or search_dc(second_half, to_find)

print(f'{search_dc([4,3,2,5,1], 3) = }') 
print(f'{search_dc([4,3,2,5,1], 1) = }')
print(f'{search_dc([4,3,2,5,1], 5) = }')
print(f'{search_dc([4,3,2,5,1], 0) = }')
print(f'{search_dc([4,3,2,5,1], 8) = }')
