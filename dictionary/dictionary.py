import csv

def main(f):
    reader = csv.DictReader(f)
    name_langs = ['one', 'two']
    words = {line[name_langs[0]]: line[name_langs[1]] for line in reader}
    words_revers = {line[name_langs[0]]: line[name_langs[1]] for line in reader}
    return words, words_revers

def dictionary(name_file):
    with open(name_file) as f:
        words, words_revers = main(f)

    while True:
        print('Word: ', end='')
        word = input()
        if word in words.keys():
            print(words[word])
        elif word in words_revers.keys():
            print(words_revers[word])
        else:
            print('I do not know this word')


if __name__ == '__main__':
    dictionary('dict.csv')
