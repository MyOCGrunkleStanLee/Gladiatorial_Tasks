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


        # TODO give CombatUI a player and enemy list
        self.ui = CombatUI(self.display, [], [])
        self.ui_finished = False
        self.ui.draw_emotions()
        self.combat.phase = "select_attack"


    def game_body_loop(self) -> None:

        if not self.ui_finished:
            self.ui_finished = self.ui.update()
        else:
            # TODO do calculation stuff, also logic for win/loose condition, your code for this is below, commented it for clarification

            # after calculating reset ui so cycle can continue (assuming that no win/loose condition)
            self.ui.reset_ui()
            self.ui_finished = False

        if self.combat.phase == "select_attack":
            for emotion in self.combat.emotions:
                data = self.ui.select_attack(emotion.learned_moves)
                if data is not None:
                    emotion.attack, emotion.target = data
                    self.combat.phase = "confirm_attack"

            for enemy in self.combat.enemies:
                self.combat.select_enemy_attack(enemy)
                self.combat.select_enemy_target(enemy, self.combat.emotions)

            if self.combat.emotions[0].attack is not None:
                self.combat.phase = "confirm_attack"

        if self.combat.phase == "confirm_attack":
            if self.ui.start_attack() is True:
                self.combat.phase = "process_attack"
            else:
                self.combat.phase = "select_attack"

        if self.combat.phase == "process_attack":
            print("WE ARE NOW PROCESSING THE ATTACKS")
            # todo add an attack order queue if we decide to add speed as a mechanic
            for emotion in self.combat.emotions:
                if emotion.motivation > 0:
                    self.combat.process_attack(emotion)

            for enemy in self.combat.enemies:
                if enemy.motivation > 0:
                    self.combat.process_attack(enemy)
            self.combat.phase = "show_animation"

        if self.combat.phase == "show_animation":
            self.combat.phase = "clean_up"

        if self.combat.phase == "clean_up":
            for emotion in self.combat.emotions:
                if emotion.motivation <= 0:
                    self.combat.clean_emotion(emotion)

            for enemy in self.combat.enemies:
                if enemy.motivation <= 0:
                    self.combat.clean_enemies(enemy)

            if len(self.combat.emotions) == 0:
                self.combat.phase = "loss"

            elif len(self.combat.enemies) == 0:
                self.combat.phase == "win"

            else:
                self.combat.phase = "select_attack"

            # todo check if any emotions or enemies have ran out of health and remove them
            # todo check if the player is out of emotions or if the enemy is defeated

        if self.combat.phase == "win":
            # todo display a you won screen and give experience
            self.game_state_object.current_state = "do_it_irl"

        if self.combat.phase == "loss":
            # todo display a you lose screen and have the player try again or maybe move on anyways?
            self.game_state_object.current_state = "select_starter"
