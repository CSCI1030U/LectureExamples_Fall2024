class BinarySearchTree:
    def __init__(self, values = []):
        self.values = values 

    def _left_child_index(self, node_index):
        return node_index * 2 + 1
    
    def _right_child_index(self, node_index):
        return node_index * 2 + 2
    
    def _parent_index(self, node_index):
        return (node_index - 1) // 2
    
    def _is_valid_index(self, index):
        return index >= 0 and index < len(self.values)

    def search(self, to_find, current_index = 0):
        if not self._is_valid_index(current_index):
            return False 
        
        if to_find == self.values[current_index]:
            return True 
        elif to_find < self.values[current_index]:
            return self.search(to_find, self._left_child_index(current_index))
        else: # to_find > self.values[current_index]
            return self.search(to_find, self._right_child_index(current_index))
        
    def print(self, index = 0, depth = 0):
        if not self._is_valid_index(index):
            return
        
        # print right sub-tree (recursively)
        self.print(self._right_child_index(index), depth+1)

        # print root node
        print('\t' * depth + str(self.values[index]))

        # print left sub-tree (recursively)
        self.print(self._left_child_index(index), depth+1)

'''
        21
    15
        12
10
        6
    5
        2

[10,5,15,2,6,12,21]
'''

bst1 = BinarySearchTree() # empty
bst2 = BinarySearchTree(values = [10,5,15,2,6,12,21])
print(f'{bst2.search(6) = }')
print(f'{bst2.search(15) = }')
print(f'{bst2.search(21) = }')
print(f'{bst2.search(10) = }')
print(f'{bst2.search(-1) = }')
bst2.print()

'''
                10
        5               15
    2       6       12      21
'''