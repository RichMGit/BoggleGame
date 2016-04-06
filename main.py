import random

dice = [
    ['a', 'a', 'e', 'e', 'g', 'n'],
    ['a', 'b', 'b', 'j', 'o', 'o'],
    ['a', 'c', 'h', 'o', 'p', 's'],
    ['a', 'f', 'f', 'k', 'p', 's'],
    ['b', 'm', 'u', 'e', 'z', 'b'],
    ['i', 'c', 'u', 'j', 'c', 'c'],
    ['d', 'k', 'j', 'a', 'd', 'd'],
    ['a', 'y', 'e', 'e', 'v', 'b'],
    ['s', 'u', 'w', 'e', 'c', 'n'],
    ['d', 'n', 'e', 'e', 'x', 'n'],
    ['a', 'a', 'e', 'w', 'g', 'n'],
    ['a', 'a', 'x', 'e', 'g', 'n'],
    ['l', 'y', 'e', 'o', 'o', 'n'],
    ['q', 'w', 'f', 'y', 'p', 'n'],
    ['a', 's', 'w', 'a', 'g', 'n'],
    ['a', 't', 'y', 'u', 'i', 'n']
]


def create_grid(sets_of_dice):
    letters = []
    grid = []
    for die in sets_of_dice:  # die is singular for dice :)
        random.shuffle(die)
    random.shuffle(sets_of_dice)
    for die in dice:
        letters.append(die[0])
    a = 0
    for _ in range(4):  # runs 4 times
        grid.append(letters[a:a+4])
        a += 4
    return grid
# [
#     ['a', 'a', 'e', 'e'],
#     ['a', 'a', 'e', 'e'],
#     ['a', 'a', 'e', 'e'],
#     ['a', 'a', 'e', 'e']
# ]


def is_next_letter_valid(first, second):
    # Each argument is an array eg [0][0]
    # Are the indexes of the two letters within 1 of each other?
    if -1 <= (first[0] - second[0]) <= 1 and -1 <= (first[1] - second[1]) <= 1:
        return True
    else:
        return False


def find_letter_coordinates(letter):
    coordinate_store = []
    # Given a letter return a list of all the coordinates that contain that letter
    for row in range(4):
        for column in range(4):
            if grid[row][column] == letter:
                coordinate_store.append([row, column])
    return coordinate_store


def remove_invalid_coordinates(coordinate_list, neighbour):
    for coordinate in coordinate_list:
        if not is_next_letter_valid(coordinate, neighbour):
            coordinate_list.remove(coordinate)
    return coordinate_list


def print_grid(grid):
    for row in grid:
        print(' '.join(row))


def unknown(user_word):
    for index, letter in enumerate(user_word):
        for s in find_letter_coordinates(user_word[index]):
            if index == len(user_word) - 1:
                return False
            for a in find_letter_coordinates(user_word[index + 1]):
                if is_next_letter_valid(s, a):
                    print(s, a, 'are valid')
                    return True
    return False

grid = create_grid(dice)
print_grid(grid)

if is_next_letter_valid([0, 0], [0, 1]):
    print('This is ok')

user_word = input('Enter a word: ')
print(unknown(user_word))



# for index in len(user_word):
#     for s in find_letter_coordinates(user_word[index]):
#         for a in find_letter_coordinates(user_word[1]):
#             if is_next_letter_valid(s, a):
#                 for p in find_letter_coordinates(user_word[2]):
#                     if is_next_letter_valid(a, p):
#                         return True



# first_letter_coordinates = find_letter_coordinates(user_word[0])
#
#
# print(remove_invalid_coordinates(first_letter_coordinates, [1, 2]))

