#Imports needed for aim trainer
import pygame
import math
import random
import time
import constants
from cursor import My_Cursor
from calculations import calculations
from button import Button
import leaderboard
import stretches_with_sens

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)
def run(sens):
    clicked = []
    functions = []
    values = []
    run = True
    targets = []
    clock = pygame.time.Clock()
    c = My_Cursor(sens)
    k = -1
    l = 0
    record_values = False

    targets_pressed = 0
    clicks = 0
    misses = 0
    start_time = time.time()
    
    pygame.time.set_timer(constants.TARGET_EVENT, constants.TARGET_INCREMENT)
    for x in range(1):
                x = random.randint(constants.TARGET_PADDING, constants.WIDTH - constants.TARGET_PADDING)
                y = random.randint(
                constants.TARGET_PADDING + constants.TOP_BAR_HEIGHT, constants.HEIGHT - constants.TARGET_PADDING)
                target = Target(x, y)
                targets.append(target)
    while run:
        clock.tick(60)
        click = False
        mouse_pos = (c.rect.x, c.rect.y)
        elapsed_time = time.time() - start_time
               

        if elapsed_time >= 30.0:
                end_screen(constants.WIN, elapsed_time, targets_pressed, clicks, clicked, functions,sens,misses)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    break

            if event.type == constants.TARGET_EVENT:
                x = random.randint(constants.TARGET_PADDING, constants.WIDTH - constants.TARGET_PADDING)
                y = random.randint(
                    constants.TARGET_PADDING + constants.TOP_BAR_HEIGHT, constants.HEIGHT - constants.TARGET_PADDING)
                target = Target(x, y)
                targets.append(target)

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1

        for target in targets:
            target.update()


            if click and target.collide(*mouse_pos):
                targets.remove(target)
                
                if record_values:
                    functions.append(values)
                    values = []
                record_values = True
                clicked.append((target.x, target.y))
                k += 1
                
                targets_pressed += 1
                x = random.randint(constants.TARGET_PADDING, constants.WIDTH - constants.TARGET_PADDING)
                y = random.randint(
                constants.TARGET_PADDING + constants.TOP_BAR_HEIGHT, constants.HEIGHT - constants.TARGET_PADDING)
                target = Target(x, y)
                targets.append(target)
            elif click and not(target.collide(*mouse_pos)):
                misses += 1
                print(misses)
                
        
        if record_values:
            values.append(mouse_pos)
            l += 1
            
            
        draw(constants.WIN, targets)
        draw_top_bar(constants.WIN, elapsed_time, targets_pressed, misses)
        c.update()
        c.draw()
        pygame.display.update()

    pygame.quit()
    

class Target:
    MAX_SIZE = 50
    GROWTH_RATE = 0
    COLOR = "red"
    SECOND_COLOR = "white"

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 49.9
        self.grow = True

    def update(self):
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False

        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size)
        pygame.draw.circle(win, self.SECOND_COLOR,
                           (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(win, self.SECOND_COLOR,
                           (self.x, self.y), self.size * 0.4)

    def collide(self, x, y):
        dis = math.sqrt((x - self.x)**2 + (y - self.y)**2)
        return dis <= self.size

def draw(win, targets):
    win.fill(constants.BG_COLOR)

    for target in targets:
        target.draw(win)

def format_time(secs):
    milli = math.floor(int(secs * 1000 % 1000) / 100)
    seconds = int(round(secs % 60, 1))
    minutes = int(secs // 60)

    return f"{minutes:02d}:{seconds:02d}.{milli}"


def draw_top_bar(win, elapsed_time, targets_pressed, misses):
    
    pygame.draw.rect(win, "grey", (0, 0, constants.WIDTH, constants.TOP_BAR_HEIGHT))
    time_label = constants.LABEL_FONT.render(
        f"Time: {format_time(elapsed_time)}", 1, "black")
    score = (targets_pressed * 20) - (misses * 5)

    speed = round(targets_pressed / elapsed_time, 1)
    speed_label = constants.LABEL_FONT.render(f"Speed: {speed} t/s", 1, "black")

    hits_label = constants.LABEL_FONT.render(f"Hits: {targets_pressed}", 1, "black")

    score_label = constants.LABEL_FONT.render(f"Score: {score}", 1, "black")

    win.blit(time_label, (5, 5))
    win.blit(speed_label, (400, 5))
    win.blit(hits_label, (750, 5))
    win.blit(score_label, (1050,5))


def end_screen(win, elapsed_time, targets_pressed, clicks, clicked, functions, sens, misses):
    c = My_Cursor(sens)
    BUT_SIZE_1 = (142, 75)
    BUT_SIZE_2 = (0, 75)
    BUT_SIZE_3 = (45, 75)
    SURF_LOC = (((constants.WIDTH // 3) * 2 + 2, constants.HEIGHT // 2))
    SURF_LOC_2 = (((constants.WIDTH - 1100), constants.HEIGHT // 2))
    SURF_LOC_3 = (((constants.WIDTH - 750), constants.HEIGHT // 2))

    next_button = Button(
        image = pygame.image.load("assets/Next.png"), pos = (SURF_LOC[0] + (BUT_SIZE_1[0] * 2) + (BUT_SIZE_1[0] // 2), constants.HEIGHT - BUT_SIZE_1[1] + (BUT_SIZE_1[1] // 2)),
        text_input = "NEXT", font = get_font(30), base_color = "#d7fcd4", hovering_color = "White"
        )

    play_again_button = Button(
        image = pygame.image.load("assets/Play_Again.png"), pos = (SURF_LOC_2[0] + (BUT_SIZE_2[0] * 2) + (BUT_SIZE_2[0] // 2), constants.HEIGHT - BUT_SIZE_2[1] + (BUT_SIZE_2[1] // 2)),
        text_input = "Play Again", font = get_font(30), base_color = "#d7fcd4", hovering_color = "White"
        )
    
    save_button = Button(
        image = pygame.image.load("assets/Test.png"), pos = (SURF_LOC_3[0] + (BUT_SIZE_3[0] * 2) + (BUT_SIZE_3[0] // 2), constants.HEIGHT - BUT_SIZE_3[1] + (BUT_SIZE_3[1] // 2)),
        text_input = "Save", font = get_font(30), base_color = "#d7fcd4", hovering_color = "White"
        )

    running = True
    while running:
        constants.SCREEN.fill(constants.BG_COLOR)
        cursor_pos = (c.rect.x, c.rect.y)

        time_label = constants.LABEL_FONT.render(
            f"Time: {format_time(elapsed_time)}", 1, "white")

        speed = round(targets_pressed / elapsed_time, 1)
        speed_label = constants.LABEL_FONT.render(f"Speed: {speed} t/s", 1, "white")

        hits_label = constants.LABEL_FONT.render(f"Hits: {targets_pressed}", 1, "white")
        try:
            accuracy = round(targets_pressed / clicks * 100, 1)
        except:
            accuracy = 0
        accuracy_label = constants.LABEL_FONT.render(f"Accuracy: {accuracy}%", 1, "white")

        deviance_label = constants.LABEL_FONT.render(f"Deviance: {calculations(clicked, functions)}", 1, "white")

        win.blit(time_label, (get_middle(time_label), 100))
        win.blit(speed_label, (get_middle(speed_label), 200))
        win.blit(hits_label, (get_middle(hits_label), 300))
        win.blit(accuracy_label, (get_middle(accuracy_label), 400))
        win.blit(deviance_label, (get_middle(deviance_label), 500))
        for button in [next_button, play_again_button, save_button]:
            button.changeColor(cursor_pos)
            button.update(constants.SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_button.checkForInput(cursor_pos):
                    stretches_with_sens.stretches_main(sens)
                if play_again_button.checkForInput(cursor_pos):
                    run(sens)
                if save_button.checkForInput(cursor_pos):
                    print(f"misses: {misses}, hits: {targets_pressed}")
                    leaderboard.save_and_display_leaderboard(win, targets_pressed, misses, accuracy, sens)
                    
        c.draw()
        c.update()
        pygame.display.update()

def get_middle(surface):
    return constants.WIDTH / 2 - surface.get_width()/2


if __name__ == '__main__':
    run(1)
 
