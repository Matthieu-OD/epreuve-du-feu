from sys import argv

liste = [int(num) for num in argv[1:]]

def tri(liste):
    """
        Take a list and return the list sorted
    """

    if len(liste) == 0 or len(liste) == 1:
        return liste

    mid_idx = len(liste) // 2;
    mid_num = liste[mid_idx]

    small_num_list = []
    big_num_list = []

    for idx in range(len(liste)):
        num = liste[idx]

        if idx == mid_idx:
            continue

        if num > mid_num:
            big_num_list.append(num)
        else:
            small_num_list.append(num)
    return tri(small_num_list) + [mid_num] + tri(big_num_list)

print(tri(liste))
