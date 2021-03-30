from sys import argv

def create_arg(argv):
    main_rectangle = []
    target = []

    file_rectangle = open(argv[1], "r")

    for x in file_rectangle:
        liste_number = list(x[:len(x)-1])
        main_rectangle.append(liste_number)

    file_rectangle.close()

    file_target = open(argv[2], "r")

    for x in file_target:
        liste_number = list(x[:len(x)-1])
        target.append(liste_number)

    file_target.close()

    return main_rectangle, target


def rectangle(main_rectangle, target):

    # height of the target table and main_rectangle table
    length_target = len(target)
    length_rectangle = len(main_rectangle)

    for line_number, main_line in enumerate(main_rectangle):
        # check if we still can find the target in the rectangle
        if length_rectangle - line_number < length_target:
            break

        is_target_line, coordonates = check_line_match(
            main_line, target[0], line_number)

        if is_target_line:
            check_pass = True
            line_checked = 1
            for test_line in target[1:]:
                main_rectangle_line_to_test = main_rectangle[line_number+line_checked][coordonates[0]-1:coordonates[0]+len(target[0])-1]
                if check_line_match(main_rectangle_line_to_test, test_line)[0]:
                    line_checked += 1
                    continue
                check_pass = False
                break
            if check_pass:
                return coordonates

    return False
        
def check_line_match(main_line, target_line, line_number=0):
    target_line_length = len(target_line)

    for idx, number in enumerate(main_line):
        if number == target_line[0]:

            checked_values = 1
            while checked_values < target_line_length:
                if main_line[idx + checked_values] == target_line[checked_values]:
                    checked_values += 1
                    continue
                break

            if checked_values == target_line_length:
                return True, (idx+1, line_number+1)

    return False, None

main_rectangle, target = create_arg(argv)

print(rectangle(main_rectangle, target))
