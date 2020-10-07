from collections import Counter


def check4duplicates():
    if len(list4check) == len(set(list4check)):
        return False
    else:
        return True


word = input('Put word to check: ')
word_lower = [letter.lower() for letter in word]
list4check = list(word_lower)
result = check4duplicates()
if result:
    print('Word has duplicates. See below:')
    list4check = [item for item, v in Counter(list4check).items() if v > 1]
    print(list4check)
else:
    print('Word has no duplicates')