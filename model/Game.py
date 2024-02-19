import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
from utils import get_screen_dimensions

from model.Player import Player

class Game:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Game, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        pass


# IMAGE FUNCTIONS ---------------------------
    def flip(sprites):
        return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

    def load_sprite_sheets(dir1, dir2, width, height, direction = False):
        path = join("assets", dir1, dir2)

        # images = [f in f in listdir(path) if isfile(join(path, f))]
        all_sprites = {}

        # for image in images:
            # pass


    BG_COLOR = (255, 255, 255)
    WIDTH, HEIGHT = [int(0.6 * x) for x in get_screen_dimensions()]
    FPS = 60
    PLAYER_VEL = 5
    GRAVITY = 1


    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.init()
    pygame.display.set_caption("Platformer")


    def get_background(self, name):
        image = pygame.image.load(join("assets", "Background", name))
        _, _, width, height = image.get_rect()
        tiles = []

        for i in range(self.WIDTH // width + 1):
            for j in range(self.HEIGHT // height + 1):
                pos = (i * width, j * height)
                tiles.append(pos)

        return tiles, image


    def draw(self, WINDOW, background, bg_image, player):
        for tile in background:
            WINDOW.blit(bg_image, tile)

        player.draw()

        pygame.display.update()


    def handle_move(self, player):
        keys = pygame.key.get_pressed()

        player.x_vel = 0
        if keys[pygame.K_LEFT]:
            player.move_left(self.PLAYER_VEL)
        if keys[pygame.K_RIGHT]:
            player.move_right(self.PLAYER_VEL)


    def start(self):
        clock = pygame.time.Clock()
        background, bg_image = self.get_background("Blue.png")

        player = Player(100, 100, 50, 50, window = self.WINDOW, fps = self.FPS, gravity = self.GRAVITY)

        running = True
        while running:
            clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break

            player.loop()
            self.handle_move(player)
            self.draw(self.WINDOW, background, bg_image, player)

        pygame.quit()
        quit()

