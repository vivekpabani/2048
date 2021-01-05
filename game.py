#!/usr/bin/env python


"""
Problem Definition :

https://www.codeeval.com/open_challenges/194/

TWENTY FORTY EIGHT

"""

__author__ = 'vivek'

import random


def update_matrix(matrix, direction, length, score):

    dir_list = [('UP', (0, 0)),
                ('DOWN', (2, 2)),
                ('RIGHT', (3, 1)),
                ('LEFT', (1, 3))]

    dir_dict = dict(dir_list)

    rotate_data = dir_dict[direction]

    for i in range(rotate_data[0]):
        matrix = rotate_matrix(matrix, length)

    matrix, updated, score = move(matrix, length, score)

    for j in range(rotate_data[1]):
        matrix = rotate_matrix(matrix, length)

    return matrix, updated, score


def rotate_matrix(matrix, length):

    new_matrix = [[0 for i in range(length)] for j in range(length)]

    for i in range(length):
        for j in range(length):
            new_matrix[i][j] = matrix[length - j - 1][i]

    return new_matrix


def move(matrix, length, score):

    updated = 0

    for i in range(0, length):
        stop = -1
        current = 1

        while current < length:
            temp_current = current
            temp = current - 1

            while temp > stop and matrix[temp_current][i] != 0:
                if matrix[temp][i] == 0:
                    matrix[temp][i] = matrix[temp_current][i]
                    matrix[temp_current][i] = 0
                    temp = temp - 1
                    temp_current = temp_current - 1
                    updated = 1
                elif matrix[temp][i] == matrix[temp_current][i]:
                    matrix[temp][i] = matrix[temp][i] * 2
                    score = score + matrix[temp][i]
                    matrix[temp_current][i] = 0
                    stop = temp
                    updated = 1
                else:
                    stop = temp_current - 1
                    temp = stop

            current += 1

    return matrix, updated, score


def print_matrix(matrix):
    """
    Prints the table data provided in list of lists format, where each list is a row.
    """
    col_width = [max(len(str(x)) for x in col) for col in zip(*matrix)]
    lines = ['-'*(i + 2) + '-' for i in col_width]
    dash_line = ''.join(lines)

    print(dash_line)

    for index, line in enumerate(matrix):
        table_row = ""
        for i, x in enumerate(line):
            table_row += "{:{}}".format(x, col_width[i]) + " | "

        print("| " + table_row)

        print(dash_line)


def initiate_matrix(length):

    matrix = [[0 for i in range(length)] for j in range(length)]

    choice_list = [2, 4]

    for k in range(2):
        i = random.choice(range(length))
        j = random.choice(range(length))
        matrix[i][j] = random.choice(choice_list)

    return matrix


def fill_in_matrix(matrix, length):

    found = 0

    while found == 0:

        i = random.choice(range(length))
        j = random.choice(range(length))

        if matrix[i][j] == 0:
            matrix[i][j] = 2
            found = 1

    return matrix


def main():

    choice_dict = dict([('U', 'UP'), ('D', 'DOWN'), ('L', 'LEFT'), ('R', 'RIGHT')])
    quit_list = ['q', 'Q', 'quit', 'Quit']

    length = 4
    score = 0
    matrix = initiate_matrix(length)

    while True:

        print("\nScore: ", score)

        print_matrix(matrix)

        ch = input("Enter Choice [U, D, L, R]:  ")

        if ch in quit_list:
            break
        try:
            direction = choice_dict[str.upper(ch)]
            matrix, updated, score = update_matrix(matrix, direction, length, score)
            if updated:
                matrix = fill_in_matrix(matrix, length)
            else:
                print("No Update.")
        except KeyError:
            print("Please Choose From Given Options [U, D, L, R].")

    print("Final Score: ", score)
    print("Good Bye!")


if __name__ == '__main__':
    main()
