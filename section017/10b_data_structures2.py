'''
[10, 10, 8, 8, 6, 5, 5, 4, 2, 1] # enqueue 10 (linear - O(n)), dequeue 10 (constant - O(1))
[8, 6, 1, 10, 5, 8, 2, 10, 4, 5, 7] # enqueue 7 (constant), dequeue 10 (linear - n)


- height (h) binary tree of n elements is O(log2(n))
    maximum n = 2^h - 1 

- heap implementation of a priority queue is log2(n) for enqueue and dequeue
- example heap:
                15
        11                 9
    5       1           6       2
'''

'''
- example binary search tree:
                6
        2               11
    1       5       9       15

- array representation:
[6, 2, 11, 1, 5, 9, 15]
'''

class BinarySearchTree:
    def __init__(self, values = []):
        self.values = values 
    
    def _left_child(self, index):
        return 2 * index + 1
    
    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index - 1) // 2
    
    def _is_valid_index(self, index):
        return (index >= 0) and (index < len(self.values))
    
    # BST specific
    def search(self, to_find, current = 0):
        if not self._is_valid_index(current):
            return False 
        
        if to_find == self.values[current]:
            return True 
        elif to_find < self.values[current]:
            left_child = self._left_child(current)
            return self.search(to_find, left_child)
        else: # to_find > self.values[current]
            right_child = self._right_child(current)
            return self.search(to_find, right_child)
    
    '''
        15
    11
        9
6
        5
    2
        1
    '''
    def display(self, current = 0, depth = 0):
        # check if this is a valid index
        if not self._is_valid_index(current):
            return

        # print right sub-tree, recursively
        self.display(self._right_child(current), depth + 1)

        # print current node, at the proper indentation
        print('\t' * depth + str(self.values[current]))

        # print left sub-tree, recursively
        self.display(self._left_child(current), depth + 1)


bst_empty = BinarySearchTree()
bst_nonempty = BinarySearchTree(values = [6, 2, 11, 1, 5, 9, 15])
print(f'{bst_nonempty.search(6) = }')
print(f'{bst_nonempty.search(11) = }')
print(f'{bst_nonempty.search(5) = }')
print(f'{bst_nonempty.search(12) = }')
print(f'{bst_nonempty.search(0) = }')
bst_nonempty.display()