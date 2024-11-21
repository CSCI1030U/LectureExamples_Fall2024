result = (1 + (2 * (3 - 4)))

# (1 + {2 + [3 * 4}]) # bracket mismatch

# int[] scores = new int[]{1,2,3,4,5}
# stack = Stack()

class EmptyStackError(Exception):
    pass

class Stack:
    def __init__(self):
        self.elements = []
        self.top_index = 0

    def push(self, new_element):
        self.elements.append(new_element)
        self.top_index = 1
    
    def pop(self):
        if len(self.elements) == 0:
            raise EmptyStackError('No elements to pop')
        # value_to_pop = self.elements[-1]
        # self.elements.pop()
        # return value_to_pop
        return self.elements.pop()

    def top(self):
        if len(self.elements) == 0:
            raise EmptyStackError('No elements to top')
        return self.elements[-1]
    
    def is_empty(self):
        return len(self.elements) == 0

    def __repr__(self):
        return str(self.elements)

stack = Stack()
print(f'{stack.is_empty() = }')
stack.push('AAA')
stack.push('BBB')
stack.push('CCC')
print(f'{stack.is_empty() = }')
print(f'{stack = }')
print(f'{stack.top() = }')
print(f'{stack.pop() = }')
print(f'{stack.pop() = }')
print(f'{stack.pop() = }')
try:
    print(f'{stack.top() = }')
except EmptyStackError as error:
    print('Invalid operation on an empty stack:', error)
try:
    print(f'{stack.pop() = }')
except EmptyStackError as error:
    print('Invalid operation on an empty stack:', error)

# [10,10,6,4,2,1,1] # sorted:  enqueue is linear, dequeue is constant
# [1,2,6,4,1,10] # unsorted:  enqueue is constant, dequeue is linear
# heap (binary tree)  enqueue is log2(n) and dequeue log2(n)
