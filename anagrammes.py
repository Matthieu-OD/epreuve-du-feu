from sys import argv

def anagrammes(word, file):
    res = []

     list_word = list(word)
     list_word.sort()

     file_of_words = open(file, 'r')

     for anagrammes in file_of_words:
         list_anagrammes = list(anagrames)
         
