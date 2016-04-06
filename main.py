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


def find_letter_coordinates(letter, list_of_valid_coordinates_of_the_previous_letter_in_the_word=None):
    coordinate_store = []
    # Given a letter return a list of all the coordinates that contain that letter
    for row in range(4):
        for column in range(4):
            if grid[row][column] == letter:
                coordinate_store.append([row, column])
    if list_of_valid_coordinates_of_the_previous_letter_in_the_word is None:
        return coordinate_store
    else:
        for coordinate in coordinate_store:
            coord_is_valid = False
            for one_of_the_valid_coordinates_of_the_previous_letter_in_the_word in list_of_valid_coordinates_of_the_previous_letter_in_the_word:
                if is_next_letter_valid(one_of_the_valid_coordinates_of_the_previous_letter_in_the_word, coordinate):
                    coord_is_valid = True
            if coord_is_valid is False:
                coordinate_store.remove(coordinate)
        return coordinate_store


def is_word_on_board(word):
    index = 0
    coordinates = find_letter_coordinates(user_word[index])
    while len(coordinates) > 0:
        if index == len(word) -1:
            return True
        index += 1
        coordinates = find_letter_coordinates(user_word[index], coordinates)
    return False


def print_grid(grid):
    for row in grid:
        print(' '.join(row))

def is_word_in_word_list(word):
    for valid_word in open("word_list.txt"):
        if word.rstrip() == valid_word.rstrip():
            return True
    return False

def is_word_valid(word):
    if len(word) <= 2:
        return False
    if is_word_in_word_list(word) is False:
        return False
    if is_word_on_board(word) is False:
        return False
    return True

def word_score(word):
    if len(word) == 3 or len(word) == 4:
        return 1
    elif len(word) == 5:
        return 2
    elif len(word) == 6:
        return 3
    elif len(word) == 7:
        return 5
    elif len(word) >= 8:
        return 11
    else:
        return 0

# Create coords lists for each letter
# Function needed that is passed two lists of coordinates, returns the lists minus any that aren't valid with each other
# Function to iterate through the word
grid = create_grid(dice)
print_grid(grid)

score = 0
for _ in range(5):
    user_word = input('Enter a word: ')
    if is_word_valid(user_word):
        score += word_score(user_word)
        print ("Correct. New score: ", str(score))
    else:
        print ("Invalid word")
