import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
from utils import get_screen_dimensions

from model.Player import Player

# GLOBAL VARIABLES --------------------------------
BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT = [int(0.6 * x) for x in get_screen_dimensions()]
FPS = 60
PLAYER_VEL = 5

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.init()
pygame.display.set_caption("Platformer")


def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image


def draw(WINDOW, background, bg_image, player):
    for tile in background:
        WINDOW.blit(bg_image, tile)

    player.draw()

    pygame.display.update()


def handle_move(player):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    if keys[pygame.K_LEFT]:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT]:
        player.move_right(PLAYER_VEL)


def main(WINDOW):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")

    player = Player(100, 100, 50, 50, WINDOW, FPS)

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        player.loop()
        handle_move(player)
        draw(WINDOW, background, bg_image, player)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(WINDOW)
