#
#   Salvatore Campisi
#
#   A Star Pathfinding
#
#   February 2020, AA 19/20
#   Artificial Intelligence Laboratory
#

import math

def get_row_col_from_id(id, rows, cols):
    new_cols = math.ceil(cols/2)

    r = math.floor((id-1) /new_cols) * 2
    c = ((id-1) % new_cols) * 2

    return (r,c)

def get_lines_from_file(pathname):
    f = open(pathname, "r")
    f.seek(0)
    lines_list = f.readlines()

    return lines_list

def get_grid_size(pathname):
    lines_list = get_lines_from_file(pathname)
    first_line = lines_list[0]
    split_list = first_line.split()

    rows = int(split_list[0])
    cols = int(split_list[1])

    rows = rows + (rows - 1)
    cols = cols + (cols -1)

    return (rows, cols)

def get_list_of_free_cells(pathname):
    rows, cols = get_grid_size(pathname)

    lines_list = get_lines_from_file(pathname)
    lines_list.pop(0)

    free_cells = []

    for line in lines_list:
        split_list = line.split()

        first_id = int(split_list[0])
        second_id = int(split_list[1])

        r1, c1 = get_row_col_from_id(first_id, rows, cols)
        r2, c2 = get_row_col_from_id(second_id, rows, cols)

        if(r1 < r2): r3 = r2 - 1
        elif(r1 > r2): r3 = r1 - 1
        else: r3 = r1

        if(c1 < c2): c3 = c2 - 1
        elif(c1 > c2): c3 = c1 - 1
        else: c3 = c1

        free_cells.append( (r1, c1) )
        free_cells.append( (r2, c2) )
        free_cells.append( (r3, c3) )

    return free_cells

def create_grid(pathname):
    rows, cols = get_grid_size(pathname)
    grid = []

    for r in range(rows):
        grid.append([])
        for c in range(cols):
            grid[r].append(1)

    free_cells = get_list_of_free_cells(pathname)

    for cell in free_cells:
        r = cell[0]
        c = cell[1]

        grid[r][c] = 0

    return grid


if __name__ == "__main__":
    my_grid = create_grid("../data/lab_c.txt")
    print(my_grid)
