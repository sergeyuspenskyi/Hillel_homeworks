import random
list_ = [random.randint(0, 10) for i in range(5)]
print([number for number in list_ if number > list_.index(number)])