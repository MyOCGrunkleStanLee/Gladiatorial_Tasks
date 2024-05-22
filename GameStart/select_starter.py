import pygame
from start.button import Button
from utilities.generic_scene import GenericScene
from utilities.player_info import Player
from GameStart.starter_option import StarterOption
import combat.emotions
from combat.emotions import Emotion


class SelectStarterScene(GenericScene):

    def create_components(self):
        self.background_img = pygame.image.load(
            "Assets/ChooseEmotionsScreen.png"
        ).convert_alpha()

        start_img = pygame.image.load("Assets/StartButton.png").convert_alpha()
        self.starter_button = Button(self.display, self.WIDTH / 2, 500, start_img, 0.4)


        self.emotion_object = Emotion("Happiness", "Assets/HappyDog.png")

        self.starter_option = StarterOption(
            self.display, 50, 130, self.emotion_object
        )

        self.selected_starter: Emotion = None

    def game_body_loop(self):

        self.display.blit(self.background_img, (0, 0))

        self.starter_button.draw(self.display)
        self.starter_option.draw()

        if self.starter_option.activated:
            # print(f"Selected {self.starter_option.emotion_name}")
            self.selected_starter = self.starter_option.emotion

        # change game state on click
        if self.starter_button.activated:
          # temp
          combat.player.happiness.reset()   
          self.player_info.add_emotion(combat.player.happiness)
          self.game_state_object.current_state = "combat"
          