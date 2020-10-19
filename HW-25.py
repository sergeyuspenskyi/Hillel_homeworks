import string
with open('alphabet.txt', 'w') as text:
    for number, letter in enumerate(string.ascii_uppercase, start=1):
        text.write(f'{number}: {letter} \n')
