import pygame
from utilities.generic_scene import GenericScene
from simplified_combat.combat_encounter import CombatEncounter
from simplified_combat.move import Move
from simplified_combat.emotion import Emotion


class CombatScene(GenericScene):

    def create_components(self) -> None:
        happy_moveset = [Move("Happy Attack 1", 2), Move("Happy Attack 2", 4)]
        self.player_party = [Emotion("Happy", 10, happy_moveset)]

        angry_moveset = [Move("Angry Attack 1", 1), Move("Angry Attack 2", 2)]
        self.enemy_party = [Emotion("Angry", 5, angry_moveset)]

        self.combat_encounter = CombatEncounter(self.player_party, self.enemy_party)

        #Title
        my_font = pygame.font.SysFont('College', 30)
        self.text_surface = my_font.render('Combat!!!!', False, (0, 0, 0))

    def game_body_loop(self) -> None:
        self.display.fill("yellow")

        self.display.blit(self.text_surface, (self.WIDTH/2-self.text_surface.get_width()/2, 50))
