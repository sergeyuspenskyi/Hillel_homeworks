my_set = {1221, 12.21, -343, 'word', (22, 21, 12)}
# Вариант 1
result = list(my_set)
print(result[0])
print(result[1])
print(result[2])
print(result[3])
print(result[4])

# Вариант 2
for i in my_set:
    print(i)
