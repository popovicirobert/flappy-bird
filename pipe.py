
import pygame
from pygame.sprite import Sprite
import platform

class Pipe(Sprite):

    def __init__(self, screen, speed, pipe_size, pipe_index):
        self.system = platform.system()

        super(Pipe, self).__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.SCREEN_WIDTH = self.screen_rect.width
        self.SCREEN_HEIGHT = self.screen_rect.height

        self.speed = speed
        self.pipe_size = pipe_size

        self.SPACE = 145

        self.PIPE_Y = [250,
                       325,
                       400]

        self.PIPE_WIDTH = 74
        self.PIPE_HEIGHT = 423

        if self.system == 'Linux':
            self.image_up = pygame.image.load(r'images/pipe_small_up.png')
        else:
            self.image_up = pygame.image.load(r'images\pipe_small_up.png')

        self.rect_up = pygame.Rect(0, 0, self.PIPE_WIDTH, self.PIPE_HEIGHT)
        self.rect_up.x = self.SCREEN_WIDTH
        self.rect_up.bottom = self.PIPE_Y[self.pipe_size] - self.SPACE

        if self.system == 'Linux':
            self.image_down = pygame.image.load(f'images/pipe_small_down.png')
        else:
            self.image_down = pygame.image.load(f'images\pipe_small_down.png')

        self.rect_down = pygame.Rect(0, 0, self.PIPE_WIDTH, self.PIPE_HEIGHT)
        self.rect_down.x = self.SCREEN_WIDTH
        self.rect_down.y = self.PIPE_Y[self.pipe_size]

        self.pipe_index = pipe_index

    def show(self):
        self.rect_up.x -= self.speed
        self.rect_down.x -= self.speed
        self.screen.blit(self.image_up, self.rect_up)
        self.screen.blit(self.image_down, self.rect_down)


