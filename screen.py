import pygame
from configpy import mainConfig

class screen:
    def __init__(self, config):
        pygame.init()
        self.running = True
        self.tam_x = config['screen']['tam_x']
        self.tam_y = config['screen']['tam_y']
        self.screen = pygame.display.set_mode((self.tam_x,self.tam_y))
        self.base_image = pygame.image.load(config['game']['base_path'])

        pygame.display.set_caption(config['screen']['caption'])

    def in_GameDisplay(self, mat):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT): 
                self.running = False

        self.screen.fill((255,255,255))

        self.screen.blit(self.base_image, (52, 0))
        pygame.display.update()
        
        if not self.running: 
            pygame.quit()

if __name__ == "__main__":
    C = mainConfig()
    C.read_config()

    test = screen(C.config)
    
    while test.running:
        test.in_GameDisplay()