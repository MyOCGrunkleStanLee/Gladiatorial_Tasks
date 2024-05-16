import pygame
from utilities.generic_scene import GenericScene

class CombatScene(GenericScene):

    def initialize_combat(self):
        pass


    def game_body_loop(self) -> None:
        self.display.fill("yellow")

        # Title
        my_font = pygame.font.SysFont('College', 30)
        text_surface = my_font.render('Combat!', False, (0, 0, 0))
        self.display.blit(text_surface, (self.WIDTH/2-text_surface.get_width()/2, 50))

        #print(self.player_info.emotions[0].name)


