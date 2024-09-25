def sum_all(values):
    total = 0.0
    for val in values:
        total += val 
    return total 

result = sum_all([1,2,3,4,5])
print(f'{result = }')

# coding exercise 1

def get_class_average(marks):
    # marks[0] = 0.0 # demonstrate pass by ref
    return sum(marks) / len(marks)

midterm_marks = [57.0, 62.5, 68.0, 74.0, 55.0, 71.0, 94.5, 47.5]
midterm_average = get_class_average(midterm_marks)
print(f'{midterm_marks = }')
print(f'{midterm_average = }') # 66.1875

# hacker's corner

two_to_the_8 = (lambda x,y: x ** y)(2,8)
print(f'{two_to_the_8 = }')