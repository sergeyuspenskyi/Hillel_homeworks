import random
import collections
list_1 = []
for i in range(15):
    list_1.append(random.randint(0, 10))
print('Изначальный список:', list_1)
buffer = collections.Counter(list_1)
result = [[y] * j for y, j in buffer.items()]
print('Группированный список c дубликатами', result)
