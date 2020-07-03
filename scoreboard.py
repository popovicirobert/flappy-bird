
import pygame
from colors import Colors

class ScoreBoard:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.SCOREBOARD_Y = 180
        self.SCOREBOARD_WIDTH = 320
        self.SCOREBOARD_HEIGHT = 200

        self.rect = pygame.Rect(0, self.SCOREBOARD_Y, self.SCOREBOARD_WIDTH, self.SCOREBOARD_HEIGHT)
        self.rect.centerx = self.screen_rect.centerx

        self.font = pygame.font.SysFont(None, 48)


    def prepare_score(self, score, best_score):
        self.score_image = self.font.render(f'Score: {score}', True, Colors.WHITE)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.y = self.SCOREBOARD_Y + self.SCOREBOARD_HEIGHT // 4

        self.best_score_image = self.font.render(f'Best Score: {best_score}', True, Colors.WHITE)
        self.best_score_rect = self.best_score_image.get_rect()
        self.best_score_rect.centerx = self.screen_rect.centerx
        self.best_score_rect.y = self.SCOREBOARD_Y + self.SCOREBOARD_HEIGHT // 2

    def show(self, score, best_score):
        pygame.draw.rect(self.screen, Colors.WHITE, self.rect, 10)
        self.screen.fill(Colors.OCRE, self.rect)

        self.prepare_score(score, best_score)

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.best_score_image, self.best_score_rect)