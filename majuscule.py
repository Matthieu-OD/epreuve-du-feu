from sys import argv

def majuscule(string):
    """
        Change one letter to caps every two letters
    """

    res = ""
    toChange = True

    for letter in string:
        value_letter = ord(letter)
        isLetter = 65 <= value_letter and value_letter <= 92 or 96 <= value_letter and value_letter <= 122
        if isLetter:
            if toChange:
                res += chr(ord(letter) - 32)
            else:
                res += letter
            toChange = not toChange
        else:
            res += letter

    print(res)

string = argv[1]
majuscule(string)
