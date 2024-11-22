# [10,8,8,7,4,3,1] 
# [3,8,1,10,8,7,4,9]
''' Example heap:
            11
    9               10
1       7       5       6
'''

'''Example BST:
            11
    6               24
1       7       19       36
array representation: [11, 6, 24, 1, 7, 19, 36]
'''

class BinarySearchTree:
    def __init__(self, values = []):
        self.values = values 

    def _left_child_index(self, index):
        return 2 * index + 1
    
    def _right_child_index(self, index):
        return 2 * index + 2
    
    def _parent_index(self, index):
        return (index - 1) // 2
    
    def _is_valid_index(self, index):
        return (index >= 0 and index < len(self.values))
    
    def search(self, to_find, current=0):
        if not self._is_valid_index(current):
            return False 
        
        if to_find == self.values[current]:
            return True 
        elif to_find < self.values[current]:
            left_index = self._left_child_index(current)
            return self.search(to_find, current = left_index)
        else: # to_find > self.values[current]:
            right_index = self._right_child_index(current)
            return self.search(to_find, current = right_index)


empty_bst = BinarySearchTree()

init_bst = BinarySearchTree(values = [11, 6, 24, 1, 7, 19, 36])
print(f'{init_bst.search(11) = }')
print(f'{init_bst.search(7) = }')
print(f'{init_bst.search(36) = }')
print(f'{init_bst.search(2) = }')
print(f'{init_bst.search(100) = }')
