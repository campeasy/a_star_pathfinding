#
#   Salvatore Campisi
#
#   A Star Pathfinding
#
#   February 2020, AA 19/20
#   Artificial Intelligence Laboratory
#

import sys

import loader
from Game import Game

def check_input(input_list):
    correct_call = "\n[ERROR] correct call:   python main.py WIDTH HEIGHT [S/M/L]\n"

    # Input size check:
    if(len(input_list) < 4):
        print(correct_call)
        return False

    # Width check:
    if(not (input_list[1].isdigit())):
        print(correct_call)
        return False

    # Height check:
    if(not (input_list[2].isdigit())):
        print(correct_call)
        return False

    # Grid size check:
    if(not (input_list[3].isascii())):
        print(correct_call)
        return False

    grid_size = input_list[3]
    if(not (grid_size == "L" or grid_size == "M" or grid_size == "S")):
        print(correct_call)
        return False

    return True

if __name__ == "__main__":
    # The user want to load a specified labyrinth:
    if(len(sys.argv) == 2):
        correct_call = "\n[ERROR] correct call:   python main.py [lab_a/lab_b/lab_c]\n"

        if(sys.argv[1] == "lab_a" or sys.argv[1] == "lab_b" or sys.argv[1] == "lab_c"):
            if(sys.argv[1] == "lab_a"): pathname = "../data/lab_a.txt"
            elif(sys.argv[1] == "lab_b"): pathname = "../data/lab_b.txt"
            else: pathname = "../data/lab_c.txt"

            specific_grid = loader.create_grid(pathname)
            g = Game("a_star_pathfinding", 1535, 959, "M", specific_grid)
            g.run()
        else:
            print(correct_call)
            sys.exit(1)

    # The user want use the draw/random mode:
    else:
        if(not (check_input(sys.argv))):
            sys.exit(1)

        width = int(sys.argv[1])
        height = int(sys.argv[2])
        grid_size = sys.argv[3]

        g = Game("a_star_pathfinding", width, height, grid_size, [])
        g.run()
