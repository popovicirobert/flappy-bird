
import pygame

class Bird:

    def __init__(self, screen):
        self.screen = screen
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = pygame.display.get_surface().get_size()

        self.GROUND_HEIGHT = 37

        self.BIRD_WIDTH = 50
        self.BIRD_HEIGHT = 36

        self.INITIAL_X = self.SCREEN_WIDTH / 2
        self.INITIAL_Y = self.SCREEN_HEIGHT / 2

        self.initialize_bird_position()

        self.decrease_y = 0
        self.gravity = 0.25
        self.time_since_last_jump = 0

        self.pendle_position = 0
        self.pendle_delta_y = list([-1] * 10 + [1] * 20 + [-1] * 10)

        self.passed_pipes = {}


    def initialize_bird_position(self):
        self.bird_image = pygame.image.load(r'images/bird_day.png')
        self.bird_rect = pygame.Rect(0, 0, self.BIRD_WIDTH, self.BIRD_HEIGHT)
        self.bird_rect.center = self.screen.get_rect().center

    def jump(self):
        self.time_since_last_jump = 0
        self.decrease_y = 8

    def out_of_bounds(self):
        if self.bird_rect.y >= self.SCREEN_HEIGHT - self.BIRD_HEIGHT - self.GROUND_HEIGHT:
            return True
        return False

    def killed(self, sliding_background):
        for pipe in sliding_background.pipes:
            if self.bird_rect.colliderect(pipe.rect_up) or \
                    self.bird_rect.colliderect(pipe.rect_down):
                return True

            if self.bird_rect.x > pipe.rect_down.x + pipe.PIPE_WIDTH:
                self.passed_pipes[pipe.pipe_index] = True

        return self.out_of_bounds()

    def update_bird_position(self):
        increase_y = self.time_since_last_jump * self.gravity
        delta_y = increase_y - self.decrease_y * (self.decrease_y - 1) / 2

        self.bird_rect.y += delta_y
        self.bird_rect.y = max(0, self.bird_rect.y)
        self.bird_rect.y = min(self.SCREEN_HEIGHT - self.BIRD_HEIGHT - self.GROUND_HEIGHT,
                               self.bird_rect.y)

        self.time_since_last_jump += 1
        self.decrease_y = max(self.decrease_y - 1, 0)


    def show_bird(self):
        self.screen.blit(self.bird_image, self.bird_rect)

    def pendle(self):
        self.bird_rect.y += self.pendle_delta_y[self.pendle_position]
        self.pendle_position = (self.pendle_position + 1) % len(self.pendle_delta_y)

    def get_score(self):
        return len(self.passed_pipes)


