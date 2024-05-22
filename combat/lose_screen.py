import pygame
from start.button import Button
from utilities.generic_scene import GenericScene
from utilities.player_info import Player
from GameStart.starter_option import StarterOption
import combat.emotions


class LoseScreen(GenericScene):

    def create_components(self):
        start_img = pygame.image.load("Assets/NextButton.png").convert_alpha()
        self.next_button = Button(self.display, self.WIDTH / 2, 500, start_img, 2)


    def game_body_loop(self):
        self.bg = pygame.image.load("Assets/BattleLoseScreen.png")
        self.display.blit(self.bg, (0,0))


        self.next_button.draw(self.display)
        # cself.starter_option.draw()


        # change game state on click
        if self.next_button.activated:
          self.game_state_object.current_state = "combat"
          