class Student:
    def __init__(self, first_name, last_name, sid):
        self._first_name = first_name 
        self._last_name = last_name 
        self._sid = sid 
        self._grades = []
        self._courses = []

    def assign_grade(self, new_grade):
        self._grades.append(new_grade)

    def get_grades(self):
        return self._grades

    def get_sid(self):
        return self._sid
    
    def __str__(self):
        return f'{self._first_name} {self._last_name} ({self._sid})'

barb = Student('Barb', 'Jones', '12345')
print(f'{barb._first_name = }') # not recommended
print(f'{barb.get_sid() = }') # this is ok
barb.assign_grade('A+')
print(f'{barb.get_grades() = }')
print(f'{str(barb) = }')

# coding exercise 1

class Dog:
    def __init__(self, name, mass):
        self.__name = name 
        self.__mass = mass 
    
    def __str__(self):
        return f'{self.__name} ({self.__mass})'

    # less than
        
rufus = Dog('Rufus', 2.0)
print(f'{str(rufus) = }')
