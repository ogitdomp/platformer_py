import pygame

class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)

    def __init__(self, x, y, width, height, **game_variables):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0

        self.fall_count = 0

        self.fps = game_variables.get('fps')
        self.window = game_variables.get('window')
        self.gravity = game_variables.get('gravity')
        
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self):
        self.y_vel += min(1, (self.fall_count / self.fps) * self.gravity)
        self.move(self.x_vel, self.y_vel)

        self.fall_count += 1

    def draw(self):
        pygame.draw.rect(self.window, self.COLOR, self.rect)