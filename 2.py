mass = [[g.strip() for g in i.split('	')] for i in open('cars.txt', encoding='utf-8')]
mass.pop(0)

for i in range(1, len(mass)):
    if float(mass[i][-2]) > 70000:
        mass[i][0] = str(round(int(mass[i][0]) - int(mass[i][0]) * 0.12))

print('\n'.join(['  '.join(x) for x in mass]))
