import string
with open('alphabet.txt', 'w') as text:
    number = 1
    for line in list(string.ascii_uppercase):
        text.write(str(number) + ': ' + line + '\n')
        number = number + 1
