from sys import argv

def anagrammes(word, file):
    res = []

    list_word = list(word)
    list_word.sort()

    file_of_words = open(file, 'r')

    for anagramme in file_of_words:
        list_anagrammes = list(anagramme[:len(anagramme)-1])
        list_anagrammes.sort()

        if list_anagrammes == list_word:
            res.append(anagramme[:len(anagramme)-1])

    file_of_words.close()
         
    return res

print(anagrammes(argv[1], argv[2]))
