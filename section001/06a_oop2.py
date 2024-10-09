class Pet:
    def __init__(self, name, breed, mass, sex):
        self._name = name 
        self._breed = breed 
        self._mass = mass 
        self._sex = sex  
    
    def speak(self):
        print(f'{self._name} speaks?')

class Dog(Pet):
    def __init__(self, name, breed, mass, sex, noisy):
        super().__init__(name, breed, mass, sex)
        self._noisy = noisy
    
    def speak(self):
        print(f'{self._name}:  Woof!')

class Cat(Pet):
    def speak(self):
        print(f'{self._name}:  Meow!')

pets = [
    Dog('Rufus', 'Husky', 8.0, 'female', True),
    Cat('Boots', 'Long hair', 3.2, 'male')
]
for pet in pets:
    pet.speak()

# coding exercise 2

class Product:
    def __init__(self, price, description):
        self._price = price 
        self._description = description 
    

class Shoe(Product):
    def __init__(self, price, description, brand, size, colour):
        super().__init__(price, description)
        # TODO:  finish this next time 
