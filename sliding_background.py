
import pygame
from pygame.sprite import Group
from pipe import Pipe
from random import randint
from colors import Colors

class SlidingBackground:

    def __init__(self, screen):
        self.screen = screen
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = pygame.display.get_surface().get_size()

        self.background_image = pygame.image.load(r'images\background_medium.png')
        self.speed = 5

        self.split_line = 0

        self.PIPE_PERIOD = 1000

        self.pipes = Group()
        self.last_time = pygame.time.get_ticks() + self.PIPE_PERIOD

        self.PIPE_TYPES = 3
        self.pipe_index = 0

        self.GROUND = 37


    def show(self, game_lost, game_active):
        # x coordinate of split line between the two backgrounds
        self.split_line -= self.speed * (game_lost == False)
        if self.split_line < 0:
            self.split_line += self.SCREEN_WIDTH

        self.screen.blit(self.background_image, (self.split_line - self.SCREEN_WIDTH, 0))
        self.screen.blit(self.background_image, (self.split_line, 0))

        if game_active == True and game_lost == False:
            self.add_pipe()
            self.show_pipes()

        self.screen.fill(Colors.GROUND_OCRE, (0, self.SCREEN_HEIGHT - self.GROUND,
                                              self.SCREEN_WIDTH, self.GROUND))
        self.screen.fill(Colors.BLACK, (0, self.SCREEN_HEIGHT - self.GROUND,
                                        self.SCREEN_WIDTH, 1))

    def add_pipe(self):
        current_time = pygame.time.get_ticks()
        if current_time >= self.last_time + self.PIPE_PERIOD:

            self.pipes.add(Pipe(self.screen, self.speed,
                                randint(0, self.PIPE_TYPES - 1),
                                self.pipe_index))

            self.last_time = current_time
            self.pipe_index += 1


    def show_pipes(self):
        self.remove_pipes()
        for pipe in self.pipes:
            pipe.show()

    def remove_pipes(self):
        for pipe in self.pipes.copy():
            if pipe.rect_down.x <= -pipe.PIPE_WIDTH:
                self.pipes.remove(pipe)







