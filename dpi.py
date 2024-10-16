import mouse
import pygame
#import main
SCREEN = pygame.display.set_mode((1280, 720))
pygame.mouse.set_visible(False)
cursor_img_rect = cursor_img.get_rect()

while True:
    SCREEN.fill("black")
    # in your main loop update the position every frame and blit the image    
    cursor_img_rect.center = pygame.mouse.get_pos()  # update position 
    SCREEN.blit(cursor_img, cursor_img_rect) # draw the cursor
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    pygame.display.update()