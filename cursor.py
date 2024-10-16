import pygame
import mouse
from pygame.locals import (KEYDOWN)
import time

CURSOR_SIZE = 32

sens = 0.5

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

clock = pygame.time.Clock()

class My_Cursor():
    def __init__(self):
        self.spr = pygame.transform.scale(pygame.image.load("assets/target.png"), (CURSOR_SIZE, CURSOR_SIZE))
        self.root = pygame.display.get_surface()
        self.x = SCREEN_WIDTH/2
        self.y = SCREEN_HEIGHT/2
        self.rect = pygame.rect.Rect(self.x, self.y, 32, 32)

    def draw(self):
        self.root.blit(self.spr, (self.x, self.y))
        s = pygame.Surface((CURSOR_SIZE, CURSOR_SIZE))
        self.root.blit(s, (self.rect.x, self.rect.y))
        
    def update(self):
        if (pygame.mouse.get_pos()[0] == 0 or pygame.mouse.get_pos()[0] >= SCREEN_WIDTH-1 or 
                pygame.mouse.get_pos()[1] == 0 or pygame.mouse.get_pos()[1] >= SCREEN_HEIGHT-1):
            mouse.move(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, absolute = True, duration = 0)    
        #pygame.mouse.set_pos((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))        
        (delta_x, delta_y) = pygame.mouse.get_rel()
        self.x += (delta_x * sens)
        #self.x = (pygame.mouse.get_pos()[0] * sens) - (0.5 * CURSOR_SIZE)
        self.y += (delta_y * sens)
        #self.y = (pygame.mouse.get_pos()[1] * sens) - (0.5 * CURSOR_SIZE)
        if self.x < 0:
            self.x = 0
        if self.x > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH
        if self.y < 0:
            self.y = 0
        if self.y >= SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT
        
        
        #time.sleep(.01)    
        pygame.event.clear()
            #clock.tick(30)
            
        
        #pygame.mouse.set_pos((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        
        print(self.x, self.y, delta_x, delta_y, pygame.mouse.get_pos())
    
pygame.init()
#pygame.mouse.set_visible(False)
SCREEN = pygame.display.set_mode((1280, 720))

# Set cursor invisible
# Create cursor in middle of screen
# Force the actual cursor to stay in the middle
# Take amount moved each frame and translate it to the artificial cursor times sensitivity factor x

pygame.event.set_grab(True)
c = My_Cursor()
run = True
pygame.mouse.set_pos((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
c.update()
c.draw()
pygame.display.update()
while run:
    SCREEN.fill("white")
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
        elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEMOTION:
            c.update()
    c.draw()
    pygame.display.update()
#c = pygame.cursors.Cursor()



    