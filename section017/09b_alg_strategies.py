def binary_search(to_find, elements, start, end):
    if start > end: # base case - empty list
        return False 
    
    middle = (start + end) // 2
    if to_find == elements[middle]:
        return True
    elif to_find < elements[middle]:
        return binary_search(to_find, elements, start, middle - 1) # A
    else: # to_find > elements[middle]
        return binary_search(to_find, elements, middle + 1, end) # B
    
print(f'{binary_search(3, [1,2,3,4,5], 0, len([1,2,3,4,5]) - 1) = }')
print(f'{binary_search(1, [1,2,3,4,5], 0, len([1,2,3,4,5]) - 1) = }')
print(f'{binary_search(5, [1,2,3,4,5], 0, len([1,2,3,4,5]) - 1) = }')
print(f'{binary_search(4, [1,2,3,4,5], 0, len([1,2,3,4,5]) - 1) = }')
print(f'{binary_search(0, [1,2,3,4,5], 0, len([1,2,3,4,5]) - 1) = }')
print(f'{binary_search(8, [1,2,3,4,5], 0, len([1,2,3,4,5]) - 1) = }')

def binary_search2(to_find, elements):
    if len(elements) == 0:
        return False 
    
    middle = len(elements) // 2
    if to_find == elements[middle]:
        return True 
    elif to_find < elements[middle]:
        return binary_search2(to_find, elements[:middle])
    else: # to_find > elements[middle]
        return binary_search2(to_find, elements[middle + 1:])

print(f'{binary_search2(3, [1,2,3,4,5]) = }')
print(f'{binary_search2(1, [1,2,3,4,5]) = }')
print(f'{binary_search2(5, [1,2,3,4,5]) = }')
print(f'{binary_search2(4, [1,2,3,4,5]) = }')
print(f'{binary_search2(0, [1,2,3,4,5]) = }')
print(f'{binary_search2(8, [1,2,3,4,5]) = }')

# coding exercise 1

def search_dc(to_find, elements):
    if len(elements) == 0:
        return False 
    
    middle = len(elements) // 2
    if to_find == elements[middle]:
        return True
    return search_dc(to_find, elements[:middle]) or \
        search_dc(to_find, elements[middle + 1:])

print(f'{search_dc(3, [2,5,4,3,1]) = }')
print(f'{search_dc(1, [2,5,4,3,1]) = }')
print(f'{search_dc(5, [2,5,4,3,1]) = }')
print(f'{search_dc(4, [2,5,4,3,1]) = }')
print(f'{search_dc(0, [2,5,4,3,1]) = }')
print(f'{search_dc(8, [2,5,4,3,1]) = }')
