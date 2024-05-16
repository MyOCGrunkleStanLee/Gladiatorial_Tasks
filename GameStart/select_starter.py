import pygame
from start.button import Button
from utilities.generic_scene import GenericScene
from utilities.player_info import Player
import combat.emotions
class SelectStarterScene(GenericScene):
    def game_body_loop(self):
        self.display.fill("green")
        # add a button
        start_img = pygame.image.load("start/start_button.png").convert_alpha()
        starter_button = Button(self.display, 500, 500, start_img, 0.4)
        starter_button.draw()

        # change game state on click
        if starter_button.clicked:
            self.player_info.add_emotion(combat.emotions.happiness)
            self.game_state_object.current_state = "combat"
