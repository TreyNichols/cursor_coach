import pygame, sys
from button import Button
import math
import time
import random
import constants
import aim_trainer_game as aim
from mouse_options import mouse_options
from cursor import My_Cursor
from stretches import stretches_main

pygame.init()
pygame.display.set_caption("Cursor Coach")
c = My_Cursor()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    mouse_options() 
    
def stretches():
    stretches_main()

def main_menu():
    while True:
        constants.SCREEN.blit(constants.BG, (0, 0))

        MENU_MOUSE_POS = (c.rect.x, c.rect.y)

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="START", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        STRETCHES_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="STRETCHES", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(60), base_color="#d7fcd4", hovering_color="White")

        constants.SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, STRETCHES_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(constants.SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if STRETCHES_BUTTON.checkForInput(MENU_MOUSE_POS):
                    stretches()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        c.draw()
        c.update()
        pygame.display.update()
        

if __name__ == '__main__':
    main_menu()