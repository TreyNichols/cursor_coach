#Imports needed for aim trainer
import pygame
import math
import random
import time
import constants
from cursor import My_Cursor

def run(sens):
    run = True
    targets = []
    clock = pygame.time.Clock()
    c = My_Cursor(sens)

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
               

        if elapsed_time >= 60.0:
                end_screen(constants.WIN, elapsed_time, targets_pressed, clicks)
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

            if target.size <= 0:
                targets.remove(target)
                misses += 1

            if click and target.collide(*mouse_pos):
                targets.remove(target)
                targets_pressed += 1
                x = random.randint(constants.TARGET_PADDING, constants.WIDTH - constants.TARGET_PADDING)
                y = random.randint(
                constants.TARGET_PADDING + constants.TOP_BAR_HEIGHT, constants.HEIGHT - constants.TARGET_PADDING)
                target = Target(x, y)
                targets.append(target)
            
            if click and not(target.collide(*mouse_pos)):
                misses += 1
            

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

    speed = round(targets_pressed / elapsed_time, 1)
    speed_label = constants.LABEL_FONT.render(f"Speed: {speed} t/s", 1, "black")

    hits_label = constants.LABEL_FONT.render(f"Hits: {targets_pressed}", 1, "black")

    score_label = constants.LABEL_FONT.render(f"Score: {(targets_pressed * 20) - (misses * 5)}", 1, "black")

    win.blit(time_label, (5, 5))
    win.blit(speed_label, (400, 5))
    win.blit(hits_label, (750, 5))
    win.blit(score_label, (1050,5))


def end_screen(win, elapsed_time, targets_pressed, clicks):
    win.fill(constants.BG_COLOR)
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

    win.blit(time_label, (get_middle(time_label), 100))
    win.blit(speed_label, (get_middle(speed_label), 200))
    win.blit(hits_label, (get_middle(hits_label), 300))
    win.blit(accuracy_label, (get_middle(accuracy_label), 400))

    pygame.display.update()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                quit()


def get_middle(surface):
    return constants.WIDTH / 2 - surface.get_width()/2