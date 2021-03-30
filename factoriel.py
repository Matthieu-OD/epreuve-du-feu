from sys import argv

def factoriel(number):
    if number == 0 or number == 1:
        return 1
    return factoriel(number-1) * number

argument = int(argv[1])
print(factoriel(argument))
