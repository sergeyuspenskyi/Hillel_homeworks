from operator import itemgetter
with open('input.txt', 'r') as poem:
    poem = poem.read().title()
    bad_chars = ['-', ',', '.', ':']
    poem = ''.join((filter(lambda i: i not in bad_chars, poem)))
    poem = poem.strip().split()
    words_dict = dict()
    for word in poem:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    final_dict = sorted(words_dict.items(), key=itemgetter(1), reverse=True)
    print('Amount of words: ', len(poem))
    print('Frequency: ', '\n'.join(f'{k}: {v}' for k, v in final_dict), sep='\n')
