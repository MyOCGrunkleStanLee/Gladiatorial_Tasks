import pygame
from start.button import Button
from utilities.generic_scene import GenericScene
from utilities.player_info import Player
import combat.emotions
class SelectStarterScene(GenericScene):

    def __init__(self, display: pygame.Surface, game_state_object, player_info = None) -> None:
        """Initializes the object with a PyGame surface to render and data from the game session"""
        self.display = display
        self.game_state_object = game_state_object
        self.player_info = player_info

        start_img = pygame.image.load("start/start_button.png").convert_alpha()
        self.starter_button = Button(self.display, 500, 500, start_img, 0.4)

    def game_body_loop(self):
        self.display.fill("green")

        self.starter_button.draw()

        # change game state on click
        if self.starter_button.activated:
            self.player_info.add_emotion(combat.emotions.happiness)
            self.game_state_object.current_state = "combat"
