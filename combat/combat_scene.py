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
        print(self.combat.emotions)
        self.ui = None
        self.ui_finished = False

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
            print("player finished")

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
                    try:
                        self.combat.emotions.remove(emotion.target)
                    except ValueError:
                        self.combat.enemies.remove(emotion.target)

            if len(self.combat.emotions) == 0:
                print("YOU LOSE")
                # after calculating reset ui so cycle can continue (assuming that no win/loose condition)
                self.ui.reset_ui()
                self.ui_finished = False
                # todo display a you lose screen and have the player try again or maybe move on anyways?
                self.game_state_object.current_state = "select_starter"

            elif len(self.combat.enemies) == 0:
                print("YOU WIN")
                # after calculating reset ui so cycle can continue (assuming that no win/loose condition)
                self.ui.reset_ui()
                self.ui_finished = False
                # todo display a you won screen and give experience
                self.game_state_object.current_state = "do_it_irl"

            else:
                # after calculating reset ui so cycle can continue (assuming that no win/loose condition)
                self.ui.reset_ui()
                self.ui_finished = False