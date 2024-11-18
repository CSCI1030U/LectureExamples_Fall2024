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

# coding exercise 2

def insert_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i]['ratio'] < key['ratio']:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key

def fractional_knapsack(available_items, capacity):
    # 1. calculate the value/weight ratio for each item
    for item in available_items:
        item['ratio'] = item['value'] / item['weight']

    # 2. sort items by ratio
    insert_sort(available_items)
    print(f'{available_items = }')

    # 3. repeatedly choose items in order of highest ratio until full
    chosen_items = []
    for item in available_items:
        if item['weight'] <= capacity:
            chosen_items.append(item)
            capacity -= item['weight']
            if capacity == 0.0:
                return chosen_items
        else: # item['weight'] > capacity
            fraction = capacity / item['weight']
            partial_item = {
                'name': 'Part of ' + item['name'],
                'weight': item['weight'] * fraction,
                'value': item['value'] * fraction,
                'ratio': item['ratio']
            }
            chosen_items.append(partial_item)
            return chosen_items
    return chosen_items
        

items = [
    {'name': 'Stone Statue', 'weight': 75.0, 'value': 2.5},
    {'name': 'Gold Idol', 'weight': 4.5, 'value': 25.0},
    {'name': 'Jewelled Necklace', 'weight': 0.25, 'value': 850.0},
    {'name': 'Gold Bracelet', 'weight': 1.0, 'value': 12.0},
    {'name': 'Wooden Carving', 'weight': 0.5, 'value': 2.0}
]
backpack = fractional_knapsack(items, 5.75)
print(f'{backpack = }')

# coding exercise 3

def fib_dp(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[i - 1] + fibs[i - 2])
    return fibs[n]

print(f'{fib_dp(1) = }')
print(f'{fib_dp(2) = }')
print(f'{fib_dp(3) = }')
print(f'{fib_dp(4) = }')
print(f'{fib_dp(5) = }')
print(f'{fib_dp(60) = }')
print(f'{fib_dp(1000) = }')
