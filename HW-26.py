import string
for letter in list(string.ascii_uppercase):
    with open(f'{letter}.txt', 'w') as file:
        file.write(letter)
