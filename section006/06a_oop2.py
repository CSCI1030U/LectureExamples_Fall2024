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
