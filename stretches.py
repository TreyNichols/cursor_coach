import pygame, sys
from cursor import My_Cursor
# from main import (main_menu, get_font)
from get_font import get_font
from button import Button
from constants import *

def stretches_main():
    c = My_Cursor()
    
    PIC_MIDDLE = HEIGHT // 2
    
    palm_button = Button(
        image = pygame.transform.scale_by(pygame.image.load("assets/palm.png"), .12), pos = (150, PIC_MIDDLE), text_input = "Palm", font = get_font(30), base_color = "black", hovering_color = "green"
        )
    finger_button = Button(
        image = pygame.transform.scale_by(pygame.image.load("assets/fingers.png"), .12), pos = (375, PIC_MIDDLE), text_input = "Fingers", font = get_font(30), base_color = "black", hovering_color = "green"
        )
    wrist_button = Button(
        image = pygame.transform.scale_by(pygame.image.load("assets/wrist.png"), .12), pos = (600, PIC_MIDDLE), text_input = "Wrist", font = get_font(30), base_color = "black", hovering_color = "green"
        )
    forearm_button = Button(
        image = pygame.transform.scale_by(pygame.image.load("assets/forearm.png"), .12), pos = (825, PIC_MIDDLE), text_input = "Forearm", font = get_font(30), base_color = "black", hovering_color = "green"
        )
    thumb_button = Button(
        image = pygame.transform.scale_by(pygame.image.load("assets/thumb.png"), .12), pos = (1050, PIC_MIDDLE), text_input = "Thumb", font = get_font(30), base_color = "black", hovering_color = "green"
        )
    
    back_button = Button(
        image = pygame.image.load("assets/Back.png"), pos = (142 // 2, HEIGHT - 75 + (75 // 2)),
        text_input = "BACK", font = get_font(30), base_color = "#d7fcd4", hovering_color = "White"
        )
    
    while True:
        SCREEN.fill('white')
        cursor_pos = (c.rect.x, c.rect.y)
        
        for button in [palm_button, finger_button, wrist_button, forearm_button, thumb_button, back_button]:
            button.changeColor(cursor_pos)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                
            if event.type == MOUSEBUTTONDOWN:
                if back_button.checkForInput(cursor_pos):
                    return
                #if wrist_button.checkForInput(cursor_pos):
                    
        
        
        c.update()
        c.draw()
        pygame.display.update()





if __name__ == '__main__':
    stretches_main()
    