#
#   Salvatore Campisi
#
#   A Star Pathfinding
#
#   February 2020, AA 19/20
#   Artificial Intelligence Laboratory
#

import sys

from Game import Game

def check_input(input_list):
    correct_call = "\n[ERROR] correct call:   python main.py WIDTH HEIGHT [S/M/L]\n"

    # Input size check:
    if(len(input_list) < 3):
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
    if(not (check_input(sys.argv))):
        sys.exit(1)

    width = int(sys.argv[1])
    height = int(sys.argv[2])
    grid_size = sys.argv[3]

    g = Game("a_star_pathfinding", width, height, grid_size)
    g.run()
