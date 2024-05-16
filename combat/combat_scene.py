import pygame
from utilities.generic_scene import GenericScene

class CombatScene(GenericScene):

    def initialize_combat(self):
        pass


    def game_body_loop(self) -> None:
        print(self.player_info.emotions[0].name)


