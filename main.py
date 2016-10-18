import pygame
from interaction import interaction
from yo_buttons import Button
from vision import *
from game import Game

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 200)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
PURPLE = (255, 0, 255)
ORANGE = (255, 155, 0)
BRIGHT_GREEN = (0, 255, 0)
BRIGHT_BLUE = (0, 0, 255)
BRIGHT_RED = (255, 0, 0)

pygame.init()

screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()
FPS = 20
total_frames = 0

game = Game()

while True:

    screen.fill((120,120,120))

    Game.update(screen)
    interaction(screen)

    pygame.display.set_caption("Hax Free Pokemon")
    pygame.display.flip()
    clock.tick(FPS)
    total_frames += 1
