def get_total(item_price, quantity, tax_rate):
    print('Let us calculate the total')
    subtotal = item_price * quantity
    return subtotal * (1.0 + tax_rate)

print('Let me first call the function')
result = get_total(9.99, 5, 0.13)
print(f'{result = }')
print('Yep, that was the total!')

# coding exercise 1

def get_class_average(marks):
    return sum(marks) / len(marks)

print(f'{get_class_average([1,2,3,4,5]) = }')
print(f'{get_class_average(marks=[1,2,3,4,5]) = }')
