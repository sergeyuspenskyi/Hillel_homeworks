start = int(input('Начальный год: '))
end = int(input('Конечный год: '))
if start >= end:
    print('Просчет невозможен. Конечный год должен быть больше начального')
result = [i for i in range(start, end) if i % 4 == 0 or i % 400 == 0]
print(' '.join(map(str, result)))