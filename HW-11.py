import random
result = [random.randint(1, 10) for i in range(10)]
result = list(set(result))
for i in sorted(result, reverse=True):
    print(i, i * '*', sep='. ')
