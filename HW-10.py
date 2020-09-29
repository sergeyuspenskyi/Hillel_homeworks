n = int(input('Put a number: '))
list_1 = ['a', 'b', 'c']
result = []
for i in range(1, n + 1):
    for elem in list_1:
        result.append(elem + str(i))
print(result)
