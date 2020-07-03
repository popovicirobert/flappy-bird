
import pygame

class Title:

    def __init__(self, screen, image_path, WIDTH, HEIGHT, y):
        self.screen = screen

        self.SCREEN_WIDTH = pygame.display.get_surface().get_size()[0]

        self.TITLE_WIDTH = WIDTH
        self.TITLE_HEIGHT = HEIGHT

        self.title_image = pygame.image.load(image_path)

        self.title_rect = pygame.Rect(0, 0, self.TITLE_WIDTH, self.TITLE_HEIGHT)
        self.title_rect.centerx = self.SCREEN_WIDTH // 2
        self.title_rect.y = y

    def show(self):
        self.screen.blit(self.title_image, self.title_rect)