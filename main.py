import random

cubes = [
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

for cube in cubes:
    random.shuffle(cube)

random.shuffle(cubes)

game_letters = []

for cube in cubes:
    game_letters.append(cube[0])

grid = []
a = 0
for x in range(4):
    grid.append(game_letters[a:a+4])
    a += 4

print(game_letters)
print(grid)


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

if is_next_letter_valid([0, 0], [0, 1]):
    print('This is ok')

user_word = input('Enter a word: ')

print(find_letter_coordinates(user_word[0]))
print(remove_invalid_coordinates([[1, 1], [2, 2], [4, 4]], [1, 2]))

# word_one = input('Enter a word: ')
# word_split = word_one
# print(word_split)
# if word_split[0] in game_letters:
#     fl = game_letters.index(word_split[0])
#     print(fl)
# elif word_split[0] not in game_letters:
#     print('letter not found')
