my_dict = {'orange': None,
           'red': 'красный',
           'green': None,
           'yellow': 'желтый',
           'black': None}
result = {k: v for k, v in my_dict.items() if v is not None}
print(result)