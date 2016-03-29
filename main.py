import random

cube_one = ['a', 'a', 'e', 'e', 'g', 'n']
cube_two = ['a', 'b', 'b', 'j', 'o', 'o']
cube_three = ['a', 'c', 'h', 'o', 'p', 's']
cube_four = ['a', 'f', 'f', 'k', 'p', 's']
cube_five = ['b', 'm', 'u', 'e', 'z', 'b']
cube_six = ['i', 'c', 'u', 'j', 'c', 'c']
cube_seven = ['d', 'k', 'j', 'a', 'd', 'd']
cube_eight = ['a', 'y', 'e', 'e', 'v', 'b']
cube_nine = ['s', 'u', 'w', 'e', 'c', 'n']
cube_ten = ['d', 'n', 'e', 'e', 'x', 'n']
cube_eleven = ['a', 'a', 'e', 'w', 'g', 'n']
cube_twelve = ['a', 'a', 'x', 'e', 'g', 'n']
cube_thirteen = ['l', 'y', 'e', 'o', 'o', 'n']
cube_fourteen = ['q', 'w', 'f', 'y', 'p', 'n']
cube_fifteen = ['a', 's', 'w', 'a', 'g', 'n']
cube_sixteen = ['a', 't', 'y', 'u', 'i', 'n']

game_letters = []

random.shuffle(cube_one)
random.shuffle(cube_two)
random.shuffle(cube_three)
random.shuffle(cube_four)
random.shuffle(cube_five)
random.shuffle(cube_six)
random.shuffle(cube_seven)
random.shuffle(cube_eight)
random.shuffle(cube_nine)
random.shuffle(cube_ten)
random.shuffle(cube_eleven)
random.shuffle(cube_twelve)
random.shuffle(cube_thirteen)
random.shuffle(cube_fourteen)
random.shuffle(cube_fifteen)
random.shuffle(cube_sixteen)


game_letters.append(cube_one[0])
game_letters.append(cube_two[0])
game_letters.append(cube_three[0])
game_letters.append(cube_four[0])
game_letters.append(cube_five[0])
game_letters.append(cube_six[0])
game_letters.append(cube_seven[0])
game_letters.append(cube_eight[0])
game_letters.append(cube_nine[0])
game_letters.append(cube_ten[0])
game_letters.append(cube_eleven[0])
game_letters.append(cube_twelve[0])
game_letters.append(cube_thirteen[0])
game_letters.append(cube_fourteen[0])
game_letters.append(cube_fifteen[0])
game_letters.append(cube_sixteen[0])

print(game_letters)
word_one = raw_input('Enter a word: ')
word_split = list(word_one)
print(word_split)
if (word_split[0] in game_letters):
    fl = game_letters.index(word_split[0])
    print (fl)
elif (word_split[0] not in game_letters):
    print ('letter not found')
