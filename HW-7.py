import random
field = [[''] * 3, [''] * 3, [''] * 3]

for i in range(4):
    x_coord = random.randint(0, 2)
    y_coord = random.randint(0, 2)
    while field[x_coord][y_coord] != '':
        x_coord = random.randint(0, 2)
        y_coord = random.randint(0, 2)

    field[x_coord][y_coord] = 'x|'

for i in range(3):
    for j in range(3):
        if field[i][j] == '':
            field[i][j] = 'o|'

print('Результат игры:')
print(''.join(field[0]))
print(''.join(field[1]))
print(''.join(field[2]))

winner = False
for i in range(3):
    if field[i][0] == field[i][1] == field[i][2] or field[0][i] == field[1][i] == field[2][i]:
        winner = True
if field[0][0] == field[1][1] == field[2][2] or field[0][2] == field[1][1] == field[2][0]:
    winner = True
if winner:
    print('В игре есть победитель')
else:
    print('Игра закончилась в ничью')
