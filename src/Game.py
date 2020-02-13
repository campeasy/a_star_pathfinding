import pygame

import Colors
from Grid import Grid

class Game():

    def __init__(self, window_title, window_width, window_height, grid_size):
        self.window_title = window_title

        # Rounding Window's width and height to the first multiple of 64:
        self.window_width = self.__round_mul(window_width)
        self.window_height = self.__round_mul(window_height)

        self.window_size = [self.window_width, self.window_height]

        self.grid = Grid(self.window_width, self.window_height, grid_size)

    def __round_mul(self, tmp):
        rest = tmp % 64
        gap = 64 - rest
        return tmp+gap

    def run(self):
        pygame.init()

        pygame_screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.window_title)

        window_alive = True
        mouse_is_pressed = False

        while window_alive:
            # Event Handling:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    window_alive = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_is_pressed = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_is_pressed = False

            if(mouse_is_pressed):
                x_click = pygame.mouse.get_pos()[0]
                y_click = pygame.mouse.get_pos()[1]

                self.grid.set_cell(x_click, y_click, "WALL")

            # Draw on Window:
            pygame_screen.fill(Colors.GRAY)
            self.grid.draw(pygame_screen)

            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    g = Game("Game", 1500, 1000, "L")
    g.run()
