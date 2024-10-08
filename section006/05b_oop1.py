class Student:
    def __init__(self, first_name, last_name, sid):
        self.__first_name = first_name 
        self.__last_name = last_name 
        self.__sid = sid 
        self.__grades = []
        self.__courses = []

    def assign_grade(self, new_grade):
        self.__grades.append(new_grade)

    def get_grades(self):
        return self.__grades

    def get_sid(self):
        return self.__sid
    
    def __str__(self):
        return f'{self.__first_name} {self.__last_name} ({self.__sid})'

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
    
    def __repr__(self):
        return f'{self.__name} ({self.__mass} kg)'

    # less than
    def __lt__(self, other_dog):
        # if self.__mass < other_dog.__mass:
        #     return True
        # else:
        #     return False
        return self.__mass < other_dog.__mass
    

rufus = Dog('Rufus', 2.0)
spike = Dog('Spike', 5.0)

print(f'{rufus = }')
print(f'{str(rufus) = }')
print(f'{rufus < spike = }')
print(f'{spike < rufus = }')
