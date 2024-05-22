import pygame
from start.button import Button
from utilities.generic_scene import GenericScene
from utilities.player_info import Player
from GameStart.starter_option import StarterOption
import combat.emotions


class SelectStarterScene(GenericScene):

    def create_components(self):
        start_img = pygame.image.load("start/start_button.png").convert_alpha()
        self.starter_button = Button(self.display, self.WIDTH / 2, 500, start_img, 0.4)

        # Title
        my_font = pygame.font.SysFont('College', 30)
        self.text_surface = my_font.render('Select Starter', False, (0, 0, 0))

        happiness_image = pygame.image.load(
            "Assets/HappyDog.png"
        )
        happiness_image = pygame.transform.scale(happiness_image, (100, 100))
        self.starter_option = StarterOption(
            self.display, 560, 100, happiness_image, "Happiness"
        )

        self.selected_starter = ''

    def game_body_loop(self):
        self.display.fill("green")

        # Title
        self.display.blit(
            self.text_surface, (self.WIDTH / 2 - self.text_surface.get_width() / 2, 50)
        )

        self.starter_button.draw(self.display)
        self.starter_option.draw()

        if self.starter_option.activated:
            # print(f"Selected {self.starter_option.emotion_name}")
            self.selected_starter = self.starter_option.emotion_name

        # change game state on click
        if self.starter_button.activated:
          # temp
          combat.player.happiness.reset()   
          self.player_info.add_emotion(combat.player.happiness)
          self.game_state_object.current_state = "combat"
          