import pygame

class Game():

    def __init__(self, window_title, window_width, window_height):
        self.window_title = window_title

        self.window_width = window_width
        self.window_height = window_height
        self.window_size = [window_width, window_height]

        self.colors = {}
        self.__initialize_colors()
    
    def __initialize_colors(self):
        self.colors["black"] = (0,0,0)
        self.colors["white"] = (255,255,255)
        self.colors["gray"] = (127,127,127)

    def run(self):
        pygame.init()

        pygame_screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.window_title)

        window_alive = True
        while window_alive:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    window_alive = False

            pygame_screen.fill(self.colors["gray"])
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    g = Game("Game", 512, 512)
    g.run()
