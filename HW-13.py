set_1 = set()
for number in range(5):
    set_1.add(input('Put int or float number: '))
set_1 = list(set_1)
min_num = set_1[0]
max_num = set_1[0]
for i in set_1:
    if min_num > i:
        min_num = i
    if max_num < i:
        max_num = i
print('Min num = ', min_num)
print('Max num = ', max_num)
