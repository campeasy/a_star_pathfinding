#
#   Salvatore Campisi
#
#   A Star Pathfinding
#
#   February 2020, AA 19/20
#   Artificial Intelligence Laboratory
#

import pygame
import random

import Colors

class Grid():

    def __init__(self, window_width, window_height, grid_size, specific_grid):
        size = self.__cell_size_from_grid_size(grid_size)

        # Single Cell parameters:
        self.cell_width = size
        self.cell_height = size
        self.cell_border = 1

        # Calculating the number of columns and rows of the Grid from window's width and height:
        self.grid_rows = window_height // (self.cell_height + self.cell_border)
        self.grid_cols = window_width // (self.cell_width + self.cell_border)

        # The two-dimensional array rappresenting the Grid:
        self.grid = specific_grid

        # If the structure is empty, initialize it:
        if(not (self.grid)):
            self.__initialize_grid()

        self.goal_r = 0
        self.goal_c = 0

    def __cell_size_from_grid_size(self, cmd):
        if(cmd == "L"):
            size = 63
        elif(cmd == "M"):
            size = 31
        elif(cmd == "S"):
            size = 15
        else:
            size = 15

        return size

    def __initialize_grid(self):
        # Initializing the Grid:
        for r in range(self.grid_rows):
            self.grid.append([])
            for c in range(self.grid_cols):
                self.grid[r].append(0)

    def __cell_from_coords(self, x, y):
        # Mapping to (x,y) window's coordinates to the corrispondent Grid's cell:
        r = y // (self.cell_height + self.cell_border)
        c = x // (self.cell_width + self.cell_border)

        return (r,c)

    def __set_goal(self, r, c):
        # Delete old Goal from Grid:
        self.grid[self.goal_r][self.goal_c] = 0

        # Write new Goal on the Grid:
        self.goal_r = r
        self.goal_c = c
        self.grid[self.goal_r][self.goal_c] = 2

    def __is_goal(self, r, c):
        return (r == self.goal_r and c == self.goal_c)

    def get_dim(self):
        return (self.grid_rows, self.grid_cols)

    def get_goal(self):
        return (self.goal_r, self.goal_c)

    def get(self):
        return self.grid

    def clean(self):
        # Resetting the Grid:
        for r in range(self.grid_rows):
            for c in range(self.grid_cols):
                self.grid[r][c] = 0

    def random(self):
        # Generating Random Map:
        prev_type = 0
        for r in range(self.grid_rows):
            for c in range(self.grid_cols):
                # Setting the probs based on the previous cell type:
                if(prev_type == 0):
                    prob_land = 94
                    prob_tree = 3
                    prob_water = 3
                elif(prev_type == -1):
                    prob_land = 42
                    prob_tree = 53
                    prob_water = 5
                elif(prev_type == -2):
                    prob_land = 42
                    prob_tree = 5
                    prob_water = 53

                # Setting the new cell type:
                tmp_random = random.randint(0,100)
                if(tmp_random <= prob_land):
                    cell_type = 0
                elif(tmp_random > prob_land and tmp_random <= prob_land+prob_tree):
                    cell_type = -1
                else:
                    cell_type = -2

                self.grid[r][c] = cell_type
                prev_type = cell_type

        # Setting Random Goal:
        random_goal_r = random.randint(0, self.grid_rows-1)
        random_goal_c = random.randint(0, self.grid_cols-1)
        self.__set_goal(random_goal_r, random_goal_c)

    def set_cell(self, x, y, cmd):
        r,c = self.__cell_from_coords(x,y)

        if(not self.__is_goal(r,c)):
            if(cmd == "LAND"):
                self.grid[r][c] = 0
            elif(cmd == "TREE"):
                self.grid[r][c] = -1
            elif(cmd == "WATER"):
                self.grid[r][c] = -2

        if(cmd == "GOAL"):
            self.__set_goal(r,c)

    def clean_path(self):
        for r in range(self.grid_rows):
            for c in range(self.grid_cols):
                if(self.grid[r][c] == 4):
                    self.grid[r][c] = 0

    def set_path(self, path):
        if(path == False):
            self.grid[self.goal_r][self.goal_c] = 3
            return

        for node in path:
            r = node[0]
            c = node[1]
            self.grid[r][c] = 4
        self.grid[r][c] = 2

    def draw(self, pygame_screen):
        for r in range(self.grid_rows):
            for c in range(self.grid_cols):

                if(self.grid[r][c] == 0):
                    tmp_color = Colors.LAND
                elif(self.grid[r][c] == -1):
                    tmp_color = Colors.TREE
                elif(self.grid[r][c] == -2):
                    tmp_color = Colors.WATER
                elif(self.grid[r][c] == 2):
                    tmp_color = Colors.GOAL
                elif(self.grid[r][c] == 3):
                    tmp_color = Colors.GOAL_NOPATH
                elif(self.grid[r][c] == 4):
                    tmp_color = Colors.PATH
                else:
                    tmp_color = Colors.BLACK

                tmp_x = (self.cell_width + self.cell_border) * c
                tmp_y = (self.cell_height + self.cell_border) * r

                pygame.draw.rect(pygame_screen, tmp_color, [tmp_x, tmp_y, self.cell_width, self.cell_height])
