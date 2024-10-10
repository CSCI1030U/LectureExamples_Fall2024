class Book:
    def __init__(self, title, author, genre, num_pages):
        self.title = title 
        self.author = author 
        self.genre = genre 
        self.num_pages = num_pages 
    
    def read(self):
        print('I learned a thing!')

class Manga(Book):
    def __init__(self, age_rating, title, author, genre, num_pages):
        super().__init__(title, author, genre, num_pages)
        self.age_rating = age_rating 
        
    def translate(self):
        print(f'...English version of {self.title}...')

naruto = Manga(11, 'Naruto', "Naruto's author", 'Action', 120)
print(f'{naruto.author = }')
print(f'{naruto.age_rating = }')
naruto.read()
naruto.translate()

# coding exercise 1
class Pet:
    def __init__(self, name, breed, mass, sex):
        self.name = name 
        self.breed = breed 
        self.mass = mass 
        self.sex = sex 
    
    def speak(self):
        print(f'{self.name} speaks.')

class Dog(Pet):
    def __init__(self, name, breed, mass, sex):
        super().__init__(name, breed, mass, sex)
    
    def speak(self):
        print(f'{self.name}: Woof!')

class Cat(Pet):
    def __init__(self, name, breed, mass, sex):
        super().__init__(name, breed, mass, sex)
    
    def speak(self):
        print(f'{self.name}: Meow!')

pets = [
    Dog('Rufus', 'Husky', 8.0, 'female'),
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

product = Product(19.99, 'Brown belt')
print(f'{product = }')
shoe = Shoe(199.99, 'Air Jordan 1989', 'Nike', 11, 'White')
print(f'{shoe = }')
print(f'{shoe._brand}')
