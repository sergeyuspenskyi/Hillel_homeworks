range_years = range(2000, 2050)
result = [i for i in range_years if i % 4 == 0 or i % 400 == 0]
print(' '.join(map(str, result)))