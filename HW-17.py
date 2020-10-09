my_dict = {'red': 'красный',
           'blue': 'синий',
           'yellow': 'желтый'}
result = {v: k for k, v in my_dict.items()}
print(result)