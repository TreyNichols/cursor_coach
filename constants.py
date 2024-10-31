import pygame
pygame.init()

CURSOR_SIZE = 32

WIDTH, HEIGHT = 1280, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
TARGET_INCREMENT = 99999999
TARGET_EVENT = pygame.USEREVENT
TARGET_PADDING = 30
BG_COLOR = (116, 148, 236)
LIVES = 3
TOP_BAR_HEIGHT = 50
LABEL_FONT = pygame.font.Font("assets/font.ttf", 24)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BG = pygame.image.load("assets/Background.png")

from pygame.locals import (
    QUIT, KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN
    )