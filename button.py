
import pygame
import platform
from colors import Colors

class Button:

    def __init__(self, screen, y, message,
                 button_color = Colors.RED_ORANGE,
                 text_color = Colors.WHITE,
                 highlight_color = Colors.ORANGE,
                 font = '',
                 width = 150, height = 50):

        self.system = platform.system()

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        if not font:
            if self.system == 'Linux':
                font = pygame.font.Font(r'fonts/flappybirdy-font/flappybirdy.ttf', 48)
            else:
                font = pygame.font.Font(r'fonts\flappybirdy-font\flappybirdy.ttf', 48)

        self.font = font

        self.button_rect = pygame.Rect(0, 0, width, height)
        self.button_rect.centerx = self.screen_rect.centerx
        self.button_rect.y = y

        self.initial_button_color = button_color
        self.button_color = button_color
        self.text_color = text_color
        self.highlight_color = highlight_color

        self.prepare_message(message)


    def prepare_message(self, message):
        self.message_image = self.font.render(message, True, self.text_color)
        self.message_rect = self.message_image.get_rect()
        self.message_rect.center = self.button_rect.center

    def show(self):
        self.highlight_button()
        pygame.draw.rect(self.screen, Colors.WHITE, self.button_rect, 10)
        self.screen.fill(self.button_color, self.button_rect)
        self.screen.blit(self.message_image, self.message_rect)

    def highlight_button(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mouse_x, mouse_y):
            self.button_color = self.highlight_color
        else:
            self.button_color = self.initial_button_color
