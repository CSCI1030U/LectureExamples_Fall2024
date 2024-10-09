class Student:
    def __init__(self, first_name, last_name, sid):
        self.first_name = first_name 
        self.last_name = last_name 
        self.sid = sid 
        self.grades = []
    
    def add_grade(self, new_grade):
        self.grades.append(new_grade)
    
    def __repr__(self) -> str:
        return f'{self.first_name} {self.last_name} ({self.grades})'

    def __gt__(self, other) -> bool:
        return len(self.grades) > len(other.grades)

keri = Student('Keri', 'Laplace', '100000001')
keri.add_grade('A+')
print(f'{keri.grades = }')
print(f'{keri}')
print(str(keri))

ahmed = Student('Ahmed', 'Karoush', '100000002')
ahmed.add_grade('A+')
ahmed.add_grade('A+')
print(f'{keri > ahmed = }')

# coding exercise 1
class Dog:
    def __init__(self, name, mass):
        self.__name = name
        self.__mass = mass 
    
    def __repr__(self):
        return f'Dog: {self.__name} ({self.__mass} kg)'
    
    def __lt__(self, other):
        # if self.__mass < other.__mass:
        #     return True 
        # else:
        #     return False 
        return self.__mass < other.__mass
    
rufus = Dog('Rufus', 3.5)
lady = Dog('Lady', 1.0)
print(f'{rufus = }')
print(f'{lady < rufus = }')
print(f'{rufus < lady = }')
