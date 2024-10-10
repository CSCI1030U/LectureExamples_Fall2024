# coding exercise 1

class Pet:
    def __init__(self, name, breed, mass, sex):
        self._name = name
        self._breed = breed 
        self._mass = mass 
        self._sex = sex 

    def speak(self):
        print(f'{self._name}: speaks (?)')

class Dog(Pet):
    def __init__(self, name, breed, mass, sex, barky):
        super().__init__(name, breed, mass, sex)
        self._barky = barky
    
    def speak(self):
        print(f'{self._name}: Woof!')

class Cat(Pet):
    def speak(self):
        print(f'{self._name}: Meow!')

pets = [
    Dog('Rufus', 'Husky', 8.0, 'female', False),
    Cat('Boots', 'Long hair', 3.2, 'male')
]

for pet in pets:
    pet.speak()

# coding exercise 2

class Product:
    def __init__(self, price, description):
        self._price = price 
        self._description = description
    
    def __repr__(self):
        return f'Product: {self._description} (${self._price})'

class Shoe(Product):
    def __init__(self, price, description, brand, size, colour):
        super().__init__(price, description)
        self._brand = brand 
        self._size = size 
        self._colour = colour 

    def __repr__(self):
        return f'Shoe: {self._description} (${self._price}, size: {self._size})'
    
products = [
    Product(19.99, 'A brown belt'),
    Shoe(49.99, 'Dressy black shoes', 'Foot Happy', 8, 'Black')
]
for product in products:
    print(f'{product = }')
