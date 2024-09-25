marks = [50.0, 75.5, 17.0, 81.0, 62.3, 67.0, 72.0, 43.0]
names = ['Paolo', 'Giselle', 'Terry', 'Xi', 'Pauline', 'Hedar', 'Elizabeth', 'Carl']

result = []
for i in range(len(marks)):
    result.append({
        'name': names[i],
        'mark': marks[i]
    })
print(f'{result = }')