mark = float(input("Mark (out of 100): "))
if mark < 50.0:
    print('F')
elif mark < 60.0:
    print('D')
elif mark < 70.0:
    print('C')
elif mark < 80.0:
    print('B')
else:
    print('A')