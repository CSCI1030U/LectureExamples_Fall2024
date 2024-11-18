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

# coding exercise 2

def insert_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i]['ratio'] < key['ratio']:
            a[i+1] = a[i]
            i = i - 1
        a[i+1] = key

items = [
    {'name': 'Gold Statue 1', 'value': 6.0, 'weight': 6.0},
    {'name': 'Gold Statue 2', 'value': 5.5, 'weight': 5.0},
    {'name': 'Stone Statue', 'value': 0.5, 'weight': 50.0},
    {'name': 'Jewelled Necklace', 'value': 100.0, 'weight': 0.1}    
]

capacity = 5.1

# 1 calculate value/weight ratios

for i in range(len(items)):
    items[i]['ratio'] = items[i]['value'] / items[i]['weight']

# 2 sort the items by their ratio

insert_sort(items)

treasure = []
for item in items:
    if item['weight'] <= capacity:
        treasure.append(item)
        capacity -= item['weight']
    elif capacity == 0:
        break
    else:
        part_of_item = {
            'name': item['name'],
            'weight': capacity,
            'value': item['value'] * capacity / item['weight']
        }
        treasure.append(part_of_item)
        break

print(f'{treasure = }')

def fib_dp(n):
    fibs = [0,1]
    for i in range(2, n + 1):
        fibs.append(fibs[i - 1] + fibs[i - 2])
    return fibs[n]

print(f'{fib_dp(2) = }')
print(f'{fib_dp(3) = }')
print(f'{fib_dp(4) = }')
print(f'{fib_dp(5) = }')
print(f'{fib_dp(6) = }')
print(f'{fib_dp(100) = }')
