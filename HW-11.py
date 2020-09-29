import random
list_1 = []
for i in range(5):
    list_1.append(random.randint(1, 10))
dict_1 = {}
for a, b in enumerate(list_1):
    dict_1[a] = b
for k, v in dict(sorted(dict_1.items(), key=lambda item: item[1], reverse=True),).items():
    print(f'{k:}. {v * "*"}')
