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
            a[i+1] = a[i]
            i = i - 1
        a[i+1] = key

values = [5,4,3,2,1]
print(f'before sort: {values = }')
insert_sort(values)
print(f'after sort: {values = }')

# coding exercise 1

def mirror_insert_sort(a):
    for j in range(len(a) - 2, -1, -1):
        key = a[j]

        i = j + 1
        while i < len(a) and a[i] < key:
            a[i - 1] = a[i]
            i = i + 1
        a[i - 1] = key

values = [5,4,3,2,1]
print(f'before sort: {values = }')
mirror_insert_sort(values)
print(f'after sort: {values = }')

# coding exercise 2

def sequential_search(values, to_find):
    num_ops = 0
    for i in range(len(values)):
        num_ops += 1
        if values[i] == to_find:
            return num_ops, True
    return num_ops, False

for n in range(100, 10000, 1000):
    ops, result = sequential_search(range(n), -1)
    print(f'{n:08d}:{'*' * (ops//1000)}')
