import pygame

import Colors

class Grid():

    def __init__(self, window_width, window_height, grid_size):
        side_size = self.__side_size_from_grid_size(grid_size)

        # Cell parameters:
        self.cell_width = side_size
        self.cell_height = side_size
        self.cell_border = 1

        # Calculating the number of columns and rows from window's width and height:
        self.grid_rows = window_height // (self.cell_height + self.cell_border)
        self.grid_cols = window_width // (self.cell_width + self.cell_border)

        # The two-dimensional array rappresenting the grid:
        self.grid = []
        self.__initialize_grid()

    def __side_size_from_grid_size(self, cmd):
        if(cmd == "L"):
            side_size = 63
        elif(cmd == "M"):
            side_size = 31
        elif(cmd == "S"):
            side_size = 15
        else:
            side_size = 15

        return side_size

    def __initialize_grid(self):
        for r in range(self.grid_rows):
            self.grid.append([])
            for c in range(self.grid_cols):
                self.grid[r].append(0)

    def __cell_from_coords(self, x, y):
        # Mapping to (x,y) window's coordinates to the corrispondent grid cell:
        r = y // (self.cell_height + self.cell_border)
        c = x // (self.cell_width + self.cell_border)

        return (r,c)

    def set_cell(self, x, y, cmd):
        r,c = self.__cell_from_coords(x,y)

        if(cmd == "WHITE"):
            self.grid[r][c] = 0
        elif(cmd == "BLACK"):
            self.grid[r][c] = -1
        elif(cmd == "GRAY"):
            self.grid[r][c] = -2
        elif(cmd == "WALL"):
            self.grid[r][c] = -3
        else:
            print("[Grid] Invalid Command")

    def draw(self, pygame_screen):
        for r in range(self.grid_rows):
            for c in range(self.grid_cols):

                if(self.grid[r][c] == 0):
                    tmp_color = Colors.WHITE
                elif(self.grid[r][c] == -1):
                    tmp_color = Colors.BLACK
                elif(self.grid[r][c] == -2):
                    tmp_color = Colors.GRAY
                elif(self.grid[r][c] == -3):
                    tmp_color = Colors.WALL

                tmp_x = (self.cell_width + self.cell_border) * c
                tmp_y = (self.cell_height + self.cell_border) * r

                pygame.draw.rect(pygame_screen, tmp_color, [tmp_x, tmp_y, self.cell_width, self.cell_height])
