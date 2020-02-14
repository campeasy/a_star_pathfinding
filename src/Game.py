import pygame

import Colors
from Grid import Grid

class Game():

    def __init__(self, window_title, window_width, window_height, grid_size):
        self.window_title = window_title

        # Rounding Window's width and height to the first multiple of 64:
        self.window_width = self.__round_mul_64(window_width)
        self.window_height = self.__round_mul_64(window_height)

        self.window_size = [self.window_width, self.window_height]

        self.grid = Grid(self.window_width, self.window_height, grid_size)

    def __round_mul_64(self, tmp):
        rest = tmp % 64
        gap = 64 - rest
        return tmp+gap

    def run(self):
        pygame.init()

        pygame_screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.window_title)

        window_alive = True
        mouse_is_pressed = False
        insert_type = "LAND"

        while window_alive:
            # Event Handling:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    window_alive = False

                # Mouse Handling:
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_is_pressed = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_is_pressed = False

                # Keyboard Handling:
                elif event.type == pygame.KEYDOWN:
                    # Insert Type Keys:
                    if event.key == pygame.K_w:
                        insert_type = "WATER"
                    elif event.key == pygame.K_t:
                        insert_type = "TREE"
                    elif event.key == pygame.K_l:
                        insert_type = "LAND"

                    # Grid Cleaning / Random Generation:
                    elif event.key == pygame.K_c:
                        self.grid.clean()
                    elif event.key == pygame.K_r:
                        self.grid.random()

                    # Setting Goal:
                    elif event.key == pygame.K_g:
                        x_click = pygame.mouse.get_pos()[0]
                        y_click = pygame.mouse.get_pos()[1]
                        self.grid.set_cell(x_click, y_click, "GOAL")

                    # elif event.key == pygame.K_SPACE:

            # Insert Mode:
            if(mouse_is_pressed):
                x_click = pygame.mouse.get_pos()[0]
                y_click = pygame.mouse.get_pos()[1]

                self.grid.set_cell(x_click, y_click, insert_type)

            # Draw on Window:
            pygame_screen.fill(Colors.GRAY)
            self.grid.draw(pygame_screen)

            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    g = Game("A_star_pathfinding", 1800, 1000, "L")
    g.run()
