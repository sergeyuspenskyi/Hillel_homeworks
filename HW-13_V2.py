set_1 = set()
for number in range(5):
    inp = input('Put int or float number: ')
    try:
        data = int(inp)
    except ValueError:
        data = float(inp)
    set_1.add(data)
min_num = set_1.pop()
max_num = min_num
for i in set_1:
    if min_num > i:
        min_num = i
    if max_num < i:
        max_num = i
print('Min num = ', min_num)
print('Max num = ', max_num)
