import pygame

class ImageButton:
    def __init__(self, screen, image_path, WIDTH, HEIGHT, y):
        self.screen = screen
        self.SCREEN_WIDTH = pygame.display.get_surface().get_size()[0]

        self.image = pygame.image.load(image_path)

        self.BUTTON_WIDTH = WIDTH
        self.BUTTON_HEIGHT = HEIGHT

        self.rect = pygame.Rect(0, 0, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        self.rect.centerx = self.SCREEN_WIDTH // 2
        self.rect.y = y

    def show(self):
        self.highlight_button()
        self.screen.blit(self.image, self.rect)

    def mouse_over(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_x, mouse_y):
            return True
        return False

    def highlight_button(self):
        if self.mouse_over():
            self.image.set_alpha(128)
        else:
            self.image.set_alpha(255)
