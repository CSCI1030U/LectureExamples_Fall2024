result1 =  (17 + ((2 + 3) - 8))
# ([2 * {12 / 6}] + 8)
# ())(

class EmptyStackError(Exception):
    pass

class Stack:
    def __init__(self):
        self.elements = []
        self.top_index = 0
    
    def is_empty(self):
        return len(self.elements) == 0
    
    def push(self, new_element):
        self.elements.append(new_element)
        self.top_index += 1
    
    def top(self):
        if self.is_empty():
            raise EmptyStackError('No elements on stack to top')
        return self.elements[-1]

    def pop(self):
        if self.is_empty():
            raise EmptyStackError('No elements on stack to pop')
        self.top_index -= 1
        return self.elements.pop()  

    def __repr__(self):
        return str(self.elements)

stack = Stack()
print(f'{stack.is_empty() = }')
stack.push('AAA')
stack.push('BBB')
stack.push('CCC')
print(f'{stack = }')
print(f'{stack.is_empty() = }')
print(f'{stack.top() = }')
print(f'{stack.pop() = }')
print(f'{stack.pop() = }')
print(f'{stack.pop() = }')
try:
    print(f'{stack.pop() = }')
except EmptyStackError as error:
    print('Cannot pop an element from an empty stack')

