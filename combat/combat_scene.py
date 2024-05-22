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
            # enemy actions
            for enemy in self.combat.enemies:
                self.combat.select_enemy_attack(enemy)
                self.combat.select_enemy_target(enemy, self.combat.emotions)

            # this is to build the speeed queue the way I did it is a bit janky, but it should work
            attack_queue = {}
            speed_queue = []
            for emotion in self.combat.emotions + self.combat.enemies:
                attack_queue[emotion.speed] = emotion
                speed_queue.append(emotion.speed)
            speed_queue.sort()

            print("WE ARE NOW PROCESSING THE ATTACKS")
            # todo add an attack order queue if we decide to add speed as a mechanic
            for speed_value in speed_queue:
                # grab the actual emotion based off the speed value
                emotion = attack_queue.get(speed_value)
                # if their health is greater than 0 we process their attack
                if emotion.motivation >= 0:
                    self.combat.process_attack(emotion)

                # if their target hp hits 0 we remove them
                if emotion.target.motivation <= 0:
                    if emotion.enemy:
                        self.combat.clean_enemies(emotion)
                    else:
                        self.combat.clean_emotion(emotion)

            #print("player health: " + str(self.combat.emotions[0].motivation))
            #print("enemy health: " + str(self.combat.enemies[0].motivation))

            # after calculating reset ui so cycle can continue (assuming that no win/loose condition)
            self.ui.reset_ui()
            self.ui_finished = False

            if len(self.combat.emotions) == 0:
                print("YOU LOSE")
                # todo display a you lose screen and have the player try again or maybe move on anyways?
                self.game_state_object.current_state = "select_starter"

            elif len(self.combat.enemies) == 0:
                print("YOU WIN")
                # todo display a you won screen and give experience
                self.game_state_object.current_state = "do_it_irl"
