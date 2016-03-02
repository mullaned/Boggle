

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


# Defining the Grid
def get_grid():
    # put a random letter in each position in the grid
    return {(x, y): choice(ascii_uppercase)
            for x in range(X)
            for y in range(Y)}



def path_to_word(path):
    return ''.join([grid[p] for p in path])

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

    #add the current path to the paths list
    #paths.append(path)



    if word not in stems:
        return

    if word in dictionary:
        paths.append(path)
    #for the next position in neightbours
    for next_pos in neighbours[path[-1]]:
        # the position is not in the path already search the next position
        if next_pos not in path:
            search(path + [next_pos])
        else:
            logging.debug('%s: skipping %s because in path' % (path, grid[next_pos]))