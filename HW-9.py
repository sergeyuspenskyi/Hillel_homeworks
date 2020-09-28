import random
import itertools
list_1 = []
for i in range(random.randint(5, 20)):
    list_1.append([random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)])
print('Initial lists in list: ', list_1)
print('Unpacked list: ', list(itertools.chain(*list_1)))
