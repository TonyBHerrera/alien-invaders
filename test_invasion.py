import sys 
import pygame

class YoshiInvasion:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1000, 700))
        pygame.display.set_caption("Yoshi Invasion")

        self.bg_color = (0,0,230)


    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)

            pygame.display.flip()            

if __name__ == '__main__':
    ai = YoshiInvasion()
    ai.run_game()