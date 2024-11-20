avg = (1 + (2 + 3)) / 3
'''
            3
        +
            2
    +
        1
/
    3
'''
# [ 1 | ] ---> [ 2 | ] ---> [ 3 | x ]

# coding exercise 1

class Stack:
    def __init__(self):
        self.__elements = []
    
    def push(self, new_element):
        self.__elements.append(new_element)

    def top(self):
        return self.__elements[-1]
    
    def pop(self):
        return self.__elements.pop()
    
    def is_empty(self):
        return len(self.__elements) == 0
    
    def __repr__(self):
        return str(self.__elements)

stack = Stack()
stack.push('AAA')
stack.push('BBB')
stack.push('CCC')
print(f'{stack.pop() = }')
print(f'{stack.pop() = }')
print(f'{stack.pop() = }')
