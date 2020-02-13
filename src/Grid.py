import pygame

import Colors

class Grid():

    def __init__(self, window_width, window_height, grid_size):
        size = self.__cell_size_from_grid_size(grid_size)

        # Single Cell parameters:
        self.cell_width = size
        self.cell_height = size
        self.cell_border = 1

        # Calculating the number of columns and rows of the Grid from window's width and height:
        self.grid_rows = window_height // (self.cell_height + self.cell_border)
        self.grid_cols = window_width // (self.cell_width + self.cell_border)

        # The two-dimensional array rappresenting the Grid:
        self.grid = []
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
        self.grid[self.goal_r][self.goal_c] = 1

    def __is_goal(self, r, c):
        return (r == self.goal_r and c == self.goal_c)

    def get_grid(self):
        return self.grid

    def reset(self):
        # Resetting the Grid:
        for r in range(self.grid_rows):
            for c in range(self.grid_cols):
                self.grid[r][c] = 0

    def set_cell(self, x, y, cmd):
        r,c = self.__cell_from_coords(x,y)

        if(not self.__is_goal(r,c)):
            if(cmd == "TERRAIN"):
                if(r == self.goal_r and c == self.goal_c): return
                self.grid[r][c] = 0
            elif(cmd == "TREE"):
                self.grid[r][c] = -1
            elif(cmd == "WATER"):
                self.grid[r][c] = -2

        if(cmd == "GOAL"):
            self.__set_goal(r,c)

    def draw(self, pygame_screen):
        for r in range(self.grid_rows):
            for c in range(self.grid_cols):

                if(self.grid[r][c] == 0):
                    tmp_color = Colors.TERRAIN
                elif(self.grid[r][c] == -1):
                    tmp_color = Colors.TREE
                elif(self.grid[r][c] == -2):
                    tmp_color = Colors.WATER
                elif(self.grid[r][c] == 1):
                    tmp_color = Colors.GOAL

                tmp_x = (self.cell_width + self.cell_border) * c
                tmp_y = (self.cell_height + self.cell_border) * r

                pygame.draw.rect(pygame_screen, tmp_color, [tmp_x, tmp_y, self.cell_width, self.cell_height])
