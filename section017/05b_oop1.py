class Guitar:
    def __init__(self, num_strings, type):
        self.__num_strings = num_strings
        self.__type = type
    
    def set_type(self, new_type): # setters/mutators
        self.__type = new_type

    def get_num_strings(self):    # getters/accessors
        return self.__num_strings
    
    def tune(self):
        # tune the guitar
        pass

    def __gt__(self, other):
        return self.__num_strings > other.__num_strings
        # if self.__num_strings > other.__num_strings:
        #     return True 
        # else:
        #     return False
    
    def __repr__(self):
        return f'{self.__type} with {self.__num_strings} strings'
    
gibson = Guitar(6, 'Electric')
print(f'{gibson = }')
gibson.set_type('LP Electric')
# print(f'{gibson.__num_strings = }') # private variable
print(f'{gibson.get_num_strings() = }')

taylor = Guitar(12, 'Accoustic')
print(f'{taylor = }')
print(f'{gibson > taylor = }')

class Dog:
    def __init__(self, name, mass):
        self.__name = name 
        self.__mass = mass 
    
    def __repr__(self):
        return f'{self.__name} ({self.__mass} kg)'

    # implement the < operator


rufus = Dog('Rufus', 1.5)
print(f'{rufus = }')
