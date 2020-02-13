import pygame

import Colors
from Grid import Grid

class Game():

    def __init__(self, window_title, window_width, window_height):
        self.window_title = window_title

        self.window_width = window_width
        self.window_height = window_height
        self.window_size = [self.window_width, self.window_height]

        self.grid = Grid(self.window_width, self.window_height)

    def run(self):
        pygame.init()

        pygame_screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.window_title)

        window_alive = True
        while window_alive:
            # Event Handling:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    window_alive = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x_click = pygame.mouse.get_pos()[0]
                    y_click = pygame.mouse.get_pos()[1]

                    self.grid.set_cell(x_click, y_click, "WALL")

            # Draw on Window:
            pygame_screen.fill(Colors.GRAY)
            self.grid.draw(pygame_screen)

            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    g = Game("Game", 1280, 800)
    g.run()
