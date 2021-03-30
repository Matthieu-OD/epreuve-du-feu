from sys import argv

def escalier(size):
    """
        Function that takes a number for the height of the stairs
        Returns a stairs made of stars
    """

    res = ""

    for i in range(1, size+1):
        line = " " * (size - i) + "*" * (i)
        if i != size:
            line += "\n"

        res += line

    print(res)

size = int(argv[1])
escalier(size)
