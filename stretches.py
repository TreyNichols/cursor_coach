import pygame, sys
from cursor import My_Cursor
# from main import (main_menu, get_font)
from get_font import get_font
from button import Button
from constants import *
from blit_text import blit_text
def stretches_main():
    c = My_Cursor()
    
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
        inst = "Please select where you feel any pain or discomfort"
        SURF_LOC = [200, 550]
        blit_text(SCREEN, inst, (SURF_LOC[0] + 10, SURF_LOC[1] + 50), get_font(25))
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
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(cursor_pos):
                    return
                if wrist_button.checkForInput(cursor_pos):
                    Wrist_Stretch()
                if thumb_button.checkForInput(cursor_pos):
                    Thumb_Stretch()
                if palm_button.checkForInput(cursor_pos):
                    Palm_Stretch()
                if finger_button.checkForInput(cursor_pos):
                    Finger_Stretch()
                if forearm_button.checkForInput(cursor_pos):
                    Forearm_Stretch()

                    
        
        
        c.update()
        c.draw()
        pygame.display.update()


def Wrist_Stretch():
    c = My_Cursor()

    back_button = Button(
        image = pygame.image.load("assets/Back.png"), pos = (142 // 2, HEIGHT - 75 + (75 // 2)),
        text_input = "BACK", font = get_font(30), base_color = "#d7fcd4", hovering_color = "White"
        )
    wrist_stretch = Button(
        image = pygame.transform.scale_by(pygame.image.load("assets/wrist_flex_1.png"), .6), pos = (650, 100),
        text_input = "1. Put elbow on flat surface and push wrist down", font = get_font(20), base_color = "green", hovering_color = "green"
        )
    wrist_stretch_2 = Button(
        image = pygame.transform.scale_by(pygame.image.load("assets/wrist_flex_2.png"), .6), pos = (650, 400),
        text_input = "2. Put elbow on flat surface and push wrist up", font = get_font(20), base_color = "green", hovering_color = "green"
        )
    while True:
        SCREEN.fill('white')
        cursor_pos = (c.rect.x, c.rect.y)
        inst = "Please follow the step by step guide, holding each stretch for 30 seconds, repeating 2-3 times."
        SURF_LOC = [200, 500]
        blit_text(SCREEN, inst, (SURF_LOC[0] + 10, SURF_LOC[1] + 50), get_font(25)) 


        for button in [back_button, wrist_stretch, wrist_stretch_2]:
            button.changeColor(cursor_pos)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(cursor_pos):
                    return
        
        c.update()
        c.draw()
        pygame.display.update()

def Thumb_Stretch():
    c = My_Cursor()

    back_button = Button(
        image = pygame.image.load("assets/Back.png"), pos = (142 // 2, HEIGHT - 75 + (75 // 2)),
        text_input = "BACK", font = get_font(30), base_color = "#d7fcd4", hovering_color = "White"
        )
    thumb_wrist_stretch = Button(
        image = pygame.transform.scale_by(pygame.image.load("assets/side_wrist.png"), 1.25), pos = (600, 200),
        text_input = "1. Tuck thumb and gently flex down", font = get_font(20), base_color = "green", hovering_color = "green"
        )
    while True:
        SCREEN.fill('white')
        cursor_pos = (c.rect.x, c.rect.y)
        inst = "Gently tuck in your thumb into your fist, and flex your wrist downwards gently. Hold it for 1-2 seconds, repeating 10 times"
        SURF_LOC = [200, 500]
        blit_text(SCREEN, inst, (SURF_LOC[0] - 100, SURF_LOC[1] - 100), get_font(25))
        for button in [back_button, thumb_wrist_stretch]:
            button.changeColor(cursor_pos)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(cursor_pos):
                    return
        
        c.update()
        c.draw()
        pygame.display.update()

def Palm_Stretch():
    c = My_Cursor()

    back_button = Button(
        image = pygame.image.load("assets/Back.png"), pos = (142 // 2, HEIGHT - 75 + (75 // 2)),
        text_input = "BACK", font = get_font(30), base_color = "#d7fcd4", hovering_color = "White"
        )
    closed_fist = Button(
        image = pygame.transform.scale_by(pygame.image.load("assets/closed_fist.png"), 1.15), pos = (150, 100),
        text_input = "1. Closed Fist", font = get_font(20), base_color = "green", hovering_color = "green"
        )
    open_palm = Button(
        image = pygame.transform.scale_by(pygame.image.load("assets/open_palm.png"), 1.15), pos = (450, 100),
        text_input = "2. Open Palm", font = get_font(20), base_color = "green", hovering_color = "green"
        ) 
    closed_palm = Button(
        image = pygame.transform.scale_by(pygame.image.load("assets/closed_palm.png"), 1.15), pos = (750, 100),
        text_input = "3. Closed Palm", font = get_font(20), base_color = "green", hovering_color = "green"
        ) 
    open_palm_2 = Button(
        image = pygame.transform.scale_by(pygame.image.load("assets/open_palm.png"), 1.15), pos = (1050, 100),
        text_input = "4. Open Palm", font = get_font(20), base_color = "green", hovering_color = "green"
        )
    table_fist = Button(
        image = pygame.transform.scale_by(pygame.image.load("assets/table_fist.png"), 1.35), pos = (150, 300),
        text_input = "5. Table Fist", font = get_font(20), base_color = "green", hovering_color = "green"
        )
    claw_fist = Button(
        image = pygame.transform.scale_by(pygame.image.load("assets/tiger_fist.png"), 1.15), pos = (450, 330),
        text_input = "6. Claw", font = get_font(20), base_color = "green", hovering_color = "green"
        )
    half_fist = Button(
        image = pygame.transform.scale_by(pygame.image.load("assets/half_fist.png"), 1.15), pos = (750, 330),
        text_input = "7. Half Fist", font = get_font(20), base_color = "green", hovering_color = "green"
        )
    closed_fist_2 = Button(
        image = pygame.transform.scale_by(pygame.image.load("assets/closed_fist.png"), 1.15), pos = (1050, 330),
        text_input = "8. Closed Fist", font = get_font(20), base_color = "green", hovering_color = "green"
        )
    


    while True:
        SCREEN.fill('white')
        cursor_pos = (c.rect.x, c.rect.y)
        inst = "Please follow the step by step guide, holding each stretch for 5 seconds, repeating 3-4 times."
        SURF_LOC = [200, 500]
        blit_text(SCREEN, inst, (SURF_LOC[0] + 10, SURF_LOC[1] + 50), get_font(25)) 
        for button in [back_button, closed_fist, open_palm, closed_palm, open_palm_2, table_fist, claw_fist, half_fist, closed_fist_2]:
            button.changeColor(cursor_pos)
            button.update(SCREEN)

       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(cursor_pos):
                    return
        
        c.update()
        c.draw()
        pygame.display.update()

def Finger_Stretch():
    c = My_Cursor()

    back_button = Button(
        image = pygame.image.load("assets/Back.png"), pos = (142 // 2, HEIGHT - 75 + (75 // 2)),
        text_input = "BACK", font = get_font(30), base_color = "#d7fcd4", hovering_color = "White"
        )
    finger_flex_up = Button(
        image = pygame.transform.scale_by(pygame.image.load("assets/finger_flex_up.png"), 1.15), pos = (350, 200),
        text_input = "1. Flex Each finger upward", font = get_font(20), base_color = "green", hovering_color = "green"
        )
    finger_flex_down = Button(
        image = pygame.transform.scale_by(pygame.image.load("assets/finger_flex_down.png"), 1.15), pos = (950, 200),
        text_input = "2. Flex Each finger downward", font = get_font(20), base_color = "green", hovering_color = "green"
        )
    while True:
        SCREEN.fill('white')
        cursor_pos = (c.rect.x, c.rect.y)
        inst = "Please follow the step by step guide, hold each finger besides the one you are stretching in the opposite direction. Hold for 3 seconds, then move onto the next finger. Repeat 2 times"
        SURF_LOC = [150, 350]
        blit_text(SCREEN, inst, (SURF_LOC[0] + 10, SURF_LOC[1] + 20), get_font(25)) 
        for button in [back_button, finger_flex_up, finger_flex_down]:
            button.changeColor(cursor_pos)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(cursor_pos):
                    return
        
        c.update()
        c.draw()
        pygame.display.update()

def Forearm_Stretch():
    c = My_Cursor()

    back_button = Button(
        image = pygame.image.load("assets/Back.png"), pos = (142 // 2, HEIGHT - 75 + (75 // 2)),
        text_input = "BACK", font = get_font(30), base_color = "#d7fcd4", hovering_color = "White"
        )
    wrist_stretch_up = Button(
        image = pygame.transform.scale_by(pygame.image.load("assets/wrist_flex_up.png"), .8), pos = (350, 150),
        text_input = "1. Flex Wrist Upward", font = get_font(20), base_color = "green", hovering_color = "green"
        )
    
    wrist_stretch_down = Button(
        image = pygame.transform.scale_by(pygame.image.load("assets/wrist_flex_down.png"), .8), pos = (950, 150),
        text_input = "2. Flex Wrist Downward", font = get_font(20), base_color = "green", hovering_color = "green"
        )
    while True:
        SCREEN.fill('white')
        cursor_pos = (c.rect.x, c.rect.y)
        inst = "Please follow the step by step guide, holding each stretch for 30 seconds, repeating 2-3 times."
        SURF_LOC = [200, 500]
        blit_text(SCREEN, inst, (SURF_LOC[0] + 10, SURF_LOC[1] + 50), get_font(25)) 
        for button in [back_button, wrist_stretch_up, wrist_stretch_down]:
            button.changeColor(cursor_pos)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(cursor_pos):
                    return
        
        c.update()
        c.draw()
        pygame.display.update()



if __name__ == '__main__':
    stretches_main()
    