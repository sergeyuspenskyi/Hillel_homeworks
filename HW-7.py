import random
field = [[], [], []]
for i in range(3):
    field[0].append(random.choice(('x|', 'o|')))
    field[1].append(random.choice(('x|', 'o|')))
    field[2].append(random.choice(('x|', 'o|')))
print('Результат игры:')
print(''.join(field[0]))
print(''.join(field[1]))
print(''.join(field[2]))
if field[0][0] == field[0][1] == field[0][2] or \
        field[1][0] == field[1][1] == field[1][2] or \
        field[2][0] == field[2][1] == field[2][2] or \
        field[0][0] == field[1][0] == field[2][0] or \
        field[0][1] == field[1][1] == field[2][1] or \
        field[0][2] == field[1][2] == field[2][2] or \
        field[0][0] == field[1][1] == field[2][2] or \
        field[0][2] == field[1][1] == field[2][0]:
    print('В игре есть победитель')
else:
    print('Игра закончилась в ничью')
