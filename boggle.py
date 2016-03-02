from random import choice
from string import ascii_uppercase
import logging
import bogglefunction

logging.basicConfig(level=logging.INFO)


# Defining the Grid
def get_grid():
    # put a random letter in each position in the grid
    return {(x, y): choice(ascii_uppercase)
            for x in range(X)
            for y in range(Y)}

#end of get_grid



# neigbour positions
def get_neighbours():
    # create empty neighbours dictionary
    neighbours = {}

    # for each position in grid find neighbouring 8 positions
    for position in grid:
        x, y = position

        # positions of the neighbours
        positions = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y),
                     (x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x - 1, y)]

        # check that the position is on the grid and add it to the neighbours dictionary
        neighbours[position] = [p
                                for p in positions
                                if 0 <= p[0] < X
                                and 0 <= p[1] < Y]

    return neighbours
#end of get_neigbours



#create potential words
def path_to_word(path):
    return ''.join([grid[p] for p in path])



#the dictionary
def get_dictionary():
    stems, dictionary = set(), set()


    with open('dic.txt') as f:
        for word in f:
            word = word.strip().upper()
            dictionary.add(word)

            for i in range(len(word)):
                stems.add(word[:i+1])
        return dictionary, stems





#search function
def search(path):
    word = path_to_word(path)
    logging.debug('%s: %s' % (path, path_to_word(path)))

    #break if word not in stems
    if word not in stems:
        return

    #check word in dictionary
    if word in dictionary:
        paths.append(path)

    #for the next position in neightbours
    for next_pos in neighbours[path[-1]]:
        # the position is not in the path already search the next position
        if next_pos not in path:
            search(path + [next_pos])
        else:
            logging.debug('%s: skipping %s because in path' % (path, grid[next_pos]))
#end of search function


#end of functions





# set grid size
size = X, Y = 4, 4

# create empthy path
paths = []

# create the grid
grid = get_grid()

# get the neighbours positions
neighbours = get_neighbours()

#set the dictionary and stems
dictionary, stems = get_dictionary()



#search the position in the grid
for position in grid:
    logging.info('searching %s' % str(position))
    search([position])



#Print the Game Board
s= ''
for y in range(Y):
    for x in range(X):
        s += grid[x,y] + ''
    s += '\n'
print s



#print the different words found
print [path_to_word(p) for p in paths]


