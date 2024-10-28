# Imports
import pygame
import mouse
from constants import (SCREEN_WIDTH, SCREEN_HEIGHT, CURSOR_SIZE)

class My_Cursor():
    def __init__(self, sensitivity:float = 1):
        """Creates a custom cursor taking in sensitivity as a parameter"""
        self.spr = pygame.transform.scale(pygame.image.load("assets/target.png"), (CURSOR_SIZE, CURSOR_SIZE))
        self.root = pygame.display.get_surface()
        self.x = SCREEN_WIDTH/2
        self.y = SCREEN_HEIGHT/2
        self.rect = pygame.rect.Rect(self.x + CURSOR_SIZE//2, self.y + CURSOR_SIZE//2, 2, 2)
        self.sensitivity = sensitivity
        
        # Makes the hardware mouse invisible
        pygame.mouse.set_visible(False)
        pygame.mouse.set_pos((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))


    def draw(self):
        self.root.blit(self.spr, (self.x, self.y))
        s = pygame.Surface((2, 2))
        self.root.blit(s, (self.rect.x, self.rect.y))
        
    def update(self):
        # Finds the change in position of the mouse from where it was prior to now
        # and adds that to the cursor position times the sensitivity factor
        (delta_x, delta_y) = pygame.mouse.get_rel()
        self.x += (delta_x * self.sensitivity)
        self.y += (delta_y * self.sensitivity)
        
        
        # Keeps the cursor on the screen
        if self.x < 0 - (CURSOR_SIZE // 2):
            self.x = 0 - (CURSOR_SIZE // 2)
        if self.x > SCREEN_WIDTH - (CURSOR_SIZE // 2):
            self.x = SCREEN_WIDTH - (CURSOR_SIZE // 2)
        if self.y < 0 - (CURSOR_SIZE // 2):
            self.y = 0 - (CURSOR_SIZE // 2)
        if self.y >= SCREEN_HEIGHT - (CURSOR_SIZE // 2):
            self.y = SCREEN_HEIGHT - (CURSOR_SIZE // 2)
        
        self.rect.x = self.x + CURSOR_SIZE//2 - 1
        self.rect.y = self.y + CURSOR_SIZE//2 - 1    
        
        # Moves mouse if it hits the edge
        if (pygame.mouse.get_pos()[0] == 0 or pygame.mouse.get_pos()[0] >= SCREEN_WIDTH-1 or 
                pygame.mouse.get_pos()[1] == 0 or pygame.mouse.get_pos()[1] >= SCREEN_HEIGHT-1):
            mouse.move(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, absolute = True, duration = 0)
        
            
        
        #pygame.mouse.set_pos((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        
        #print(self.x, self.y, delta_x, delta_y, pygame.mouse.get_pos())
    


# Set cursor invisible
# Create cursor in middle of screen
# Force the actual cursor to stay in the middle
# Take amount moved each frame and translate it to the artificial cursor times sensitivity factor x

# Testing:

# from pygame.locals import KEYDOWN
# pygame.init()
# pygame.event.set_grab(True)
# SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# c = My_Cursor(1)
# run = True
# pygame.mouse.set_pos((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
# c.update()
# c.draw()
# pygame.display.update()
# while run:
#     SCREEN.fill("white")
#     for event in pygame.event.get():
#         if event.type == KEYDOWN:
#             # Was it the Escape key? If so, stop the loop.
#             if event.key == K_ESCAPE:
#                 running = False
#         elif event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#         if event.type == pygame.MOUSEMOTION:
#             c.update()
#     c.draw()
#     pygame.display.update()



    