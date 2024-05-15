import pygame
from utilities.generic_scene import GenericScene

class PlanningScene(GenericScene):

    def game_body_loop(self) -> None:
        self.display.fill("blue")