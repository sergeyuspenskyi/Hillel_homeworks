set_1 = set()
for number in range(5):
    set_1.add(input('Put int or float number: '))
min_num = set_1.pop()
max_num = set_1.pop()
for i in set_1:
    if min_num > i:
        min_num = i
    if max_num < i:
        max_num = i
print('Min num = ', min_num)
print('Max num = ', max_num)
