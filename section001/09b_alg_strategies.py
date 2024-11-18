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

# coding exercise 2

def insert_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i]['ratio'] < key['ratio']:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key

def knapsack_greedy(items, capacity):
    # 1. calculate the value/weight ratio for each item
    for item in items:
        item['ratio'] = item['value'] / item['weight']

    # 2. sort all items by their ratio
    insert_sort(items)

    # 3. take the items in order of their ratio until at capacity
    backpack = []
    for item in items:
        if item['weight'] < capacity:
            backpack.append(item)
            capacity -= item['weight']
        elif item['weight'] == capacity:
            backpack.append(item)
            capacity -= item['weight']
            return backpack 
        else: # item['weight'] > capacity
            fraction = capacity / item['weight']
            backpack.append({
                'name': item['name'],
                'ratio': item['ratio'],
                'weight': item['weight'] * fraction,
                'value': item['value'] * fraction
            })
            return backpack

available_items = [
    {'name': 'Wooden Sculpture', 'weight': 2.0, 'value': 3.5},
    {'name': 'Silver Earrings', 'weight': 1.0, 'value': 150.0},
    {'name': 'Diamond Necklace', 'weight': 1.0, 'value': 750.0},
    {'name': 'Stone Statue', 'weight': 45.0, 'value': 8.5},
    {'name': 'Gold Bracelet', 'weight': 5.0, 'value': 275.0},
]
backpack = knapsack_greedy(available_items, 8.5)
print(f'{backpack = }')

# coding exercise 3

def fib_dp(n):
    fibs = [0, 1]
    for i in range(2, n + 1):
        ith_fib = fibs[i - 1] + fibs[i - 2]
        fibs.append(ith_fib)
    return fibs[n]

print(f'{fib_dp(1) = }')
print(f'{fib_dp(2) = }')
print(f'{fib_dp(3) = }')
print(f'{fib_dp(4) = }')
print(f'{fib_dp(5) = }')
print(f'{fib_dp(6) = }')
print(f'{fib_dp(100) = }')
