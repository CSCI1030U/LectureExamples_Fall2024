'''
INSERT-SORT(A)
1  for j = 2 to length[A] do
2     key = A[j]
3     i = j-1
4     while i > 0 and A[i] > key do
5        A[i+1] = A[i]
6        i = i-1
7     A[i+1] = key
'''
def insert_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key

# coding exercise 1
def mirror_insert_sort(a):
    for j in range(len(a) - 2, -1, -1):
        key = a[j]
        i = j + 1
        while i < len(a) and a[i] < key:
            a[i - 1] = a[i]
            i = i + 1
        a[i - 1] = key


values = [3,5,1,4,2]
print(f'before sort: {values = }')
mirror_insert_sort(values)
print(f'after sort: {values = }')

# coding exercise 1

def sequential_search(values, to_find):
    num_operations = 0
    for i in range(len(values)):
        num_operations += 1
        if values[i] == to_find:
            return num_operations, True
    return num_operations, False

for n in [10, 100, 1000, 10000]:
    num_ops, result = sequential_search(range(n), -1)
    print(f'{n}:{num_ops}')

for n in range(1000, 10001, 1000):
    num_ops, result = sequential_search(range(n), -1)
    print(f"{n:08d}:{'*' * (num_ops//500)}")
