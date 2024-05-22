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

        self.ui = None
        self.ui_finished = False
        self.combat.phase = "select_attack"

        self.initialized = False


    def initialze(self):
        self.ui = CombatUI(self.display, self.combat.emotions, self.combat.enemies)
        self.initialized = True


    def game_body_loop(self) -> None:
        if not self.initialized:
            self.initialze()
            

        if not self.ui_finished:
            self.ui_finished = self.ui.update()
        else:
            data = self.ui.data
            print(data)
            if self.combat.phase == "select_attack":
                # for emotion in self.combat.emotions:
                #    data = self.ui.select_attack(emotion.learned_moves)
                emotion = self.combat.emotions[0]   # for MVP only one emotion
                if data is not None:
                    emotion.attack = data[0]
                    emotion.target = data[1]
                    #emotion.attack, emotion.target = data
                    self.combat.phase = "confirm_attack"

                for enemy in self.combat.enemies:
                    self.combat.select_enemy_attack(enemy)
                    self.combat.select_enemy_target(enemy, self.combat.emotions)

                if self.combat.emotions[0].attack is not None:
                    self.combat.phase = "process_attack"

            # if self.combat.phase == "confirm_attack":     # TODO assuming this is unneccesary?
            #     if self.ui.start_attack() is True:
            #         self.combat.phase = "process_attack"
            #     else:
            #         self.combat.phase = "select_attack"

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

            #print("player health: " + str(self.combat.emotions[0].motivation))
            #print("enemy health: " + str(self.combat.enemies[0].motivation))

            # after calculating reset ui so cycle can continue (assuming that no win/loose condition)
            self.ui.reset_ui()
            self.ui_finished = False

        
