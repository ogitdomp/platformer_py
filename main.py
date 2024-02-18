import os, random, math, pygame
from os import listdir
from os.path import isfile, join
from utils import get_screen_dimensions

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

def draw(WINDOW, background, bg_image):
    for tile in background:
        WINDOW.blit(bg_image, tile)
    
    pygame.display.update()

def main(WINDOW):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")

    running = True
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        draw(WINDOW, background, bg_image)
        
    pygame.quit()
    quit()


if __name__ == "__main__":
    main(WINDOW)