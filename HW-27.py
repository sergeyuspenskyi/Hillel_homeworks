def txt_file_handler(file) -> list:
    """Deletes 'bad' chars from txt. file except words(letters) and converts to list"""
    with open(file, 'r') as poem:
        bad_chars = ['-', ',', '.', ':']
        poem = poem.read().title()
        poem = ''.join((filter(lambda i: i not in bad_chars, poem)))
    return poem.strip().split()


def word_counter(list_) -> list:
    """Counts and sorts words from a list"""
    from operator import itemgetter
    _dict = dict()
    for word in list_:
        if word in _dict:
            _dict[word] = _dict[word] + 1
        else:
            _dict[word] = 1
    return sorted(_dict.items(), key=itemgetter(1), reverse=True)


print('Amount of words: ', len(txt_file_handler('input.txt')))
print('Frequency: ', '\n'.join(f'{k}: {v}' for k, v in word_counter(txt_file_handler('input.txt'))), sep='\n')
