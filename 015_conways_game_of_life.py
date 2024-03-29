"""
Given a 2D array and a number of generations, compute n timesteps of Conway's Game of Life.

The rules of the game are:

    Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
    Any live cell with more than three live neighbours dies, as if by overcrowding.
    Any live cell with two or three live neighbours lives on to the next generation.
    Any dead cell with exactly three live neighbours becomes a live cell.

Each cell's neighborhood is the 8 cells immediately around it (i.e. Moore Neighborhood). The universe is infinite in
both the x and y dimensions and all cells are initially dead - except for those specified in the arguments. The
return value should be a 2d array cropped around all of the living cells. (If there are no living cells, then return
[[]].)

For illustration purposes, 0 and 1 will be represented as ░░ and ▓▓ blocks respectively (PHP, C: plain black and
white squares). You can take advantage of the htmlize function to get a text representation of the universe, e.g.:"""



from IPython.core.display import display, HTML


def htmlize(array):

    full = "▓▓"
    empty = "░░"

    s = []
    for row in array:
        for cell in row:
            s.append(full if cell else empty)
        s.append('')
    output = ''.join(s)
    display(HTML(output))


def convert_table_to_set(table):

    ni = len(table)
    nj = len(table[0])

    s = set()
    for i in range(ni):
        for j in range(nj):
            if table[i][j]:
                s.add((i, j))

    return s


def convert_set_to_table(s):

    if not s:
        mi = mj = ni = nj = 0
    else:
        min_i = min(map(lambda x: x[0], s))
        min_j = min(map(lambda x: x[1], s))
        max_i = max(map(lambda x: x[0], s))
        max_j = max(map(lambda x: x[1], s))

    range_i = max_i - min_i + 1
    range_j = max_j - min_j + 1

    table = [[False for j in range(range_j)] for i in range(range_i)]

    for (i, j) in s:
        table[i - min_i][j - min_j] = True

    return table



from itertools import product


def get_generation(cells, generations):

    cells = convert_table_to_set(cells)

    for n in range(generations):

        cells_neigh = set()
        cells_new = set()

        for (i, j) in cells:
            for (di, dj) in product((-1, 0, 1), (-1, 0, 1)):
                cells_neigh.add((i + di, j + dj))

        for (i, j) in cells_neigh:
            neighbours = 0
            for (di, dj) in product((-1, 0, 1), (-1, 0, 1)):
                if (i + di, j + dj) in cells and (di, dj) != (0, 0):
                    neighbours += 1

            if neighbours == 3:
                cells_new.add((i, j))
            elif neighbours == 2 and (i, j) in cells:
                cells_new.add((i, j))

        cells = cells_new

    return convert_set_to_table(cells)

start = [[1, 0, 0],
         [0, 1, 1],
         [1, 1, 0]]
end = [[0, 1, 0],
       [0, 0, 1],
       [1, 1, 1]]

output = get_generation(start, 1)
htmlize(output)

