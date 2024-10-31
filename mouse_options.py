import mouse, pygame, sys
from cursor import My_Cursor
from constants import *
from button import Button
from get_font import get_font
from blit_text import *
from aim_trainer_game import run as game

def mouse_options():
    """Displays Mouse Options Screen"""
    sens = 1.0
    value = 1.0
    SURF_LOC = (((WIDTH // 3) * 2 + 2, HEIGHT // 2))
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    # Initializes cursor
    c = My_Cursor()
    my_surface = pygame.surface.Surface((WIDTH // 3, HEIGHT // 2))
    
    # The buttons along the bottom. Size is 142 x 75
    BUT_SIZE_1 = (142, 75)
    
    back_button = Button(
        image = pygame.image.load("assets/Back.png"), pos = (SURF_LOC[0] + (BUT_SIZE_1[0] // 2), HEIGHT - BUT_SIZE_1[1] + (BUT_SIZE_1[1] // 2)),
        text_input = "BACK", font = get_font(30), base_color = "#d7fcd4", hovering_color = "White"
        )
    
    test_button = Button(
        image = pygame.image.load("assets/Test.png"), pos = (SURF_LOC[0] + BUT_SIZE_1[0] + (BUT_SIZE_1[0] // 2), HEIGHT - BUT_SIZE_1[1] + (BUT_SIZE_1[1] // 2)),
        text_input = "TEST", font = get_font(30), base_color = "#d7fcd4", hovering_color = "White"
        )
    
    next_button = Button(
        image = pygame.image.load("assets/Next.png"), pos = (SURF_LOC[0] + (BUT_SIZE_1[0] * 2) + (BUT_SIZE_1[0] // 2), HEIGHT - BUT_SIZE_1[1] + (BUT_SIZE_1[1] // 2)),
        text_input = "NEXT", font = get_font(30), base_color = "#d7fcd4", hovering_color = "White"
        )
    
    # The + and - buttons are 75 x 75
    BUT_SIZE_2 = 75
    
    plus_button = Button(
        image = pygame.image.load("assets/plus_minus.png"), pos = (SURF_LOC[0] + BUT_SIZE_1[0] * 1.5 + (BUT_SIZE_2) , HEIGHT - (75 * 2) + (75 // 2)),
        text_input = "+", font = get_font(30), base_color = "#d7fcd4", hovering_color = "White"
        )
    
    minus_button = Button(
        image = pygame.image.load("assets/plus_minus.png"), pos = (SURF_LOC[0] + BUT_SIZE_1[0] * 1.5 - (BUT_SIZE_2) , HEIGHT - (75 * 2) + (75 // 2)),
        text_input = "-", font = get_font(30), base_color = "#d7fcd4", hovering_color = "White"
        )
    
    num_disp = pygame.surface.Surface((BUT_SIZE_2, BUT_SIZE_2))
    DISP_LOC = (SURF_LOC[0] + BUT_SIZE_1[0] + (BUT_SIZE_2 // 2) - 3 , HEIGHT - (75 * 2))
    
    
    
    while True:
        SCREEN.fill("white")
        my_surface.fill("gray")
        SCREEN.blit(my_surface, SURF_LOC)
        cursor_pos = (c.rect.x, c.rect.y)
        num_disp.fill("white")
        SCREEN.blit(num_disp, DISP_LOC)
        
        text = get_font(25).render(str(value), True, "black")
        SCREEN.blit(text, (DISP_LOC[0] + 1, DISP_LOC[1] + (BUT_SIZE_2 // 3)))
        
        inst = "Please change your sensitivity until you are comfortable with the speed"
        
        title = get_font(30).render("MOUSE OPTIONS", True, "black")
        
        SCREEN.blit(title, (SURF_LOC[0] + 20, SURF_LOC[1] + 5))
        blit_text(SCREEN, inst, (SURF_LOC[0] + 10, SURF_LOC[1] + 50), get_font(25))
        
        
        for button in [back_button, test_button, next_button, minus_button, plus_button]:
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
                if plus_button.checkForInput(cursor_pos):
                    value = round(value + 0.1, 1)
                if minus_button.checkForInput(cursor_pos):
                    value = round(value - 0.1, 1)    
                if test_button.checkForInput(cursor_pos):
                    c.sensitivity = value
                if next_button.checkForInput(cursor_pos):
                    # Put next thing here
                    game(sens)
        
        # Updates cursor and screen
        c.update()
        c.draw()            
        pygame.display.update()

if __name__ == '__main__':        
    mouse_options()