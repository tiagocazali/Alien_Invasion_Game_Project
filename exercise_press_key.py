from os import name
import sys
import pygame

class Test_Pygame:
    """This is only a Extra Exercise! It os NOT part of Alien Game!

        This exercise is:
        Make a Pygame file that creates an empty screen. In the event loop,
        print the event.key attribute whenever a pygame.KEYDOWN event is detected. 
        Run program and press various keys to see how Pygame responds
    """

    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("It is just a TEST flie!")
        self.font = pygame.font.Font(None, 36)
        self.key_text = ""


    def main(self):

        while True:
            self.check_events()
            self.update_screen()
            self.clock.tick(60)  # limits FPS to 60



    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
    
    def check_keydown_events(self, event):
        print(event.key)
        if event.key == pygame.K_q:
            sys.exit()
        else:
            self.key_text = pygame.key.name(event.key)
            
        
    def update_screen(self):
        self.screen.fill((40, 160, 200))
        text_surface = self.font.render(f"Tecla pressionada: {self.key_text}", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(400, 300))
        self.screen.blit(text_surface, text_rect)
        pygame.display.flip()



if __name__ == "__main__":
    test = Test_Pygame()
    test.main()


