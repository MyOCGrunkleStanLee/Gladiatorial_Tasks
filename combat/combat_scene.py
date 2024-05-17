import pygame
from utilities.generic_scene import GenericScene
from combat.combat import Combat


class CombatScene(GenericScene):

    def create_components(self):
        self.combat = Combat(self.player_info)
        self.combat.generate_enemies()
        self.combat.phase = "select_attack"

    def game_body_loop(self) -> None:
        self.display.fill("yellow")

        # Title
        my_font = pygame.font.SysFont('College', 30)
        text_surface = my_font.render('Combat!', False, (0, 0, 0))
        self.display.blit(text_surface, (self.WIDTH/2-text_surface.get_width()/2, 50))

        if self.combat.phase == "select_attack":
            # todo generate a button to let the user select 1 of 4? attacks
            for enemy in self.combat.enemies:
                self.combat.select_enemy_attack(enemy)

            print(self.combat.enemies[0].attack)
            self.combat.phase = "select_target"

            # todo remove the generated button when the user selects it
        if self.combat.phase == "select_target":
            # todo generate a (clear) button over enemy sprites to allow them to select the enemy
            # todo generate a back button to change which attack the player wants to use
            for enemy in self.combat.enemies:
                self.combat.select_enemy_target(enemy, self.combat.emotions)
            print(self.combat.enemies[0].target)
            # todo remove the button after the enemy has been selected
            self.combat.phase = "process_attack"

        if self.combat.phase == "process_attack":
            # todo add an attack order queue if we decide to add speed as a mechanic
            # for emotion in self.combat.emotions:
                # self.combat.process_attack(emotion.attack, emotion.target)
            for enemy in self.combat.enemies:
                self.combat.process_attack(enemy.attack, enemy.target)
            self.combat.phase = "show_animation"

        if self.combat.phase == "show_animation":
            self.combat.phase = "clean_up"

        if self.combat.phase == "clean_up":
            # todo check if any emotions or enemies have ran out of health and remove them
            # todo check if the player is out of emotions or if the enemy is defeated
            self.combat.phase = "end"
            pass

        if self.combat.phase == "end":
            self.game_state_object.current_state = "do_it_irl"
