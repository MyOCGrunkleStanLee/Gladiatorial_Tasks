import pygame
from utilities.game_state_object import GameStateObject
from utilities.generic_scene import GenericScene
from combat.combat import Combat
from combat.player import PlayerEmotion
from combat.enemies import EnemyEmotion
from utilities.player_info import Player
from start.button import Button
from combat.combatUI import CombatUI


class CombatScene(GenericScene):
    def create_components(self):
        self.combat = Combat(self.player_info)
        self.combat.generate_enemies()
        self.combat.phase = "select_attack"

        # TODO give CombatUI a player and enemy list
        self.ui = CombatUI(self.display, [], [])
        self.ui_finished = False


    def game_body_loop(self) -> None:

        if not self.ui_finished:
            self.ui_finished = self.ui.update()
        else:
            # TODO do calculation stuff, also logic for win/loose condition, your code for this is below, commented it for clarification

            # after calculating reset ui so cycle can continue (assuming that no win/loose condition)
            self.ui.reset_ui()
            self.ui_finished = False

        """
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
        """