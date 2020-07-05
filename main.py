
import pygame
import sys, platform
from bird import Bird
from sliding_background import SlidingBackground
from title import Title
from button import Button
from image_button import ImageButton
from scoreboard import ScoreBoard

class FlappyBird:

    def __init__(self):
        self.system = platform.system()

        pygame.init()
        pygame.display.set_caption('Flappy Bird')

        self.FPS = 55

        self.SCREEN_WIDTH = 1000
        self.SCREEN_HEIGHT = 563
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        self.sliding_background = SlidingBackground(self.screen)

        if self.system == 'Linux':
            self.flappy_bird_title = Title(self.screen, r'images/title2.0.png', 466, 137, 50)
        else:
            self.flappy_bird_title = Title(self.screen, r'images\title2.0.png', 466, 137, 50)

        if self.system == 'Linux':
            self.game_over_title = Title(self.screen, r'images/game_over2.0.png', 383, 90, 50)
        else:
            self.game_over_title = Title(self.screen, r'images\game_over2.0.png', 383, 90, 50)

        if self.system == 'Linux':
            self.start_image_button = ImageButton(self.screen, r'images/start_button3.0.png', 183, 109, 400)
        else:
            self.start_image_button = ImageButton(self.screen, r'images\start_button3.0.png', 183, 109, 400)

        self.scoreboard = ScoreBoard(self.screen)

        self.retry_button = Button(self.screen, 425, 'Retry')

        self.bird = Bird(self.screen)

        # True until reset in pressed
        self.game_active = False

        # True until obstacle was hit
        self.game_lost = False

        self.score = 0
        self.create_best_score_file()
        self.get_best_score()


    def create_best_score_file(self):
        fd = open('best_score.txt', 'a')
        fd.close()

    def get_best_score(self):
        with open('best_score.txt', 'r') as fd:
            self.best_score = fd.readline()

        if not self.best_score:
            self.best_score = 0
            with open('best_score.txt', 'w') as fd:
                fd.write('0')

        self.best_score = int(self.best_score)

    def replace_best_score(self, score):
        if score > self.best_score:
            self.best_score = score
            with open('best_score.txt', 'w') as fd:
                fd.write(str(self.best_score))


    def mouse_over(self, rect):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if rect.collidepoint(mouse_x, mouse_y):
            return True
        return False

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                if self.game_active == False:
                    if self.mouse_over(self.start_image_button.rect):
                        self.bird.jump()
                        self.game_active = True
                        self.sliding_background.__init__(self.screen)
                else:
                    if self.game_lost == False:
                        self.bird.jump()
                    elif self.mouse_over(self.retry_button.button_rect):
                        self.game_active = False
                        self.game_lost = False
                        self.bird.__init__(self.screen)
                        self.score = 0


        if self.game_active == True and self.bird.killed(self.sliding_background):
            self.game_lost = True
            self.sliding_background.pipes.empty()

            self.score = self.bird.get_score()
            self.replace_best_score(self.score)


    def update_screen(self):
        self.sliding_background.show(self.game_lost, self.game_active)

        if self.game_active == False and self.game_lost == False:
            self.start_image_button.show()
            self.flappy_bird_title.show()
            self.bird.pendle()

        elif self.game_active == True and self.game_lost == False:
            self.bird.update_bird_position()

        else: # obstacle was hit
            self.game_over_title.show()
            self.scoreboard.show(self.score, self.best_score)
            self.retry_button.show()

        if not(self.game_active == True and self.game_lost == True):
            self.bird.show_bird()

        pygame.display.update()

    def start(self):

        self.clock = pygame.time.Clock()

        while True:
            self.clock.tick(self.FPS)
            self.get_events()
            self.update_screen()



if __name__ == '__main__':
    flappy_bird = FlappyBird()
    flappy_bird.start()