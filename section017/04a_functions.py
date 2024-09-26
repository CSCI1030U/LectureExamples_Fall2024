import math 

def distance_between(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

dist = distance_between(x1=0, x2=0, y1=3, y2=4)
print(f'{dist = }') 

def calc_interest(principle=1000.0, interest_rate=0.035) -> float:
    return principle * interest_rate

print(f'{calc_interest(5000, 0.05) = }')
print(f'{calc_interest(principle=5000) = }')
print(f'{calc_interest(interest_rate=0.05) = }')
print(f'{calc_interest() = }')

# coding exercise 1

def get_class_average(marks: list[float]) -> float:
    # return sum(marks) / len(marks)
    total = 0.0
    count = 0
    for mark in marks:
        total += mark 
        count += 1
    return total / count

result = get_class_average([1,2,3,4,5])
print(f'{result = }')
