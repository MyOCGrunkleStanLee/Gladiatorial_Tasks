import pygame
from combat.player import PlayerEmotion
from combat.enemies import EnemyEmotion
from start.button import Button

from typing import List



class CombatUI:
    def __init__(self, display, players: List[PlayerEmotion], enemies: List[EnemyEmotion]):
        # get the player and enemy from list from somewhere else
        
        self.player = players[0]
        self.enemy = enemies[0]
        self.display = display
        self.current_phase = "idle"
        self.background_img = pygame.image.load("Assets/CombatScreen.png").convert_alpha()
        self.create_components()

        # important for combat
        self.selected_attack = None
        self.data = None


    def create_components(self):
        self.font = pygame.font.Font(None, 36)

        # overlay
        self.overlay_img = pygame.image.load("Assets/CombatMoveOverlay.png")
        x_overlay, y_overlay = 838 , 405
        self.overlay_rect = self.overlay_img.get_rect(topleft=(x_overlay, y_overlay))

        # get rects for each attack
        self.attack_rects = [pygame.Rect(x_overlay, y_overlay, 211, 70),
                 pygame.Rect(x_overlay+221, y_overlay, 211, 70),
                 pygame.Rect(x_overlay, y_overlay+80, 211, 70),
                 pygame.Rect(x_overlay+221, y_overlay+80, 211, 70)]

        # buttons for move menu
        img = pygame.image.load("Assets/TransparentForMoveButton.png")
        self.move_buttons = [Button(self.display, self.attack_rects[0].x, self.attack_rects[0].y, img, 1, positioning="topleft"),
                        Button(self.display, self.attack_rects[1].x, self.attack_rects[1].y, img, 1, positioning="topleft"),
                        Button(self.display, self.attack_rects[2].x, self.attack_rects[2].y, img, 1, positioning="topleft"),
                        Button(self.display, self.attack_rects[3].x, self.attack_rects[3].y, img, 1, positioning="topleft")]
        
        # attack button
        attack_button_image = pygame.image.load("Assets/NextButton.png").convert_alpha()
        self.attack_button = Button(self.display, 800, 450, attack_button_image, 1)
        self.back_button = Button(self.display, 800, 550, attack_button_image, 1)



    def update(self):
        # draw bg
        finished = False
        self.display.blit(self.background_img, (0, 0))
        match self.current_phase:
            case "idle":
                self.idle()
            case "select_attack":
                self.select_attack(self.player.learned_moves)
            case "start_attack":
                print("heehehehheh")
                finished = self.start_attack()
        print(finished)
        return finished


    def idle(self):
        # activate the player button
        self.player.button_activated = True

        if self.player.button.hover:
            # TODO set hover overlay
            # self.player.button.set_new_image()
            pass

        if self.player.button.activated:
            # change state, open menu
            self.player.button_activated = False
            self.current_phase = "select_attack"
        
        
        # draw player and enemy
        self.draw_emotions()


    def select_attack(self, attacks):
        # if a move button is selected save in selected_attack
        for i, button in enumerate(self.move_buttons):
            if button.activated:
                if i < len(attacks):
                    self.selected_attack = attacks[i]
                    print(self.selected_attack.name)
                else:
                    # todo play no no noise here
                    print("index out of range")


        # select enemy if an attack is selected
        if self.selected_attack != None:
            self.enemy.button_activated = True

            if self.enemy.button.hover:
                # TODO hover animation
                pass

            if self.enemy.button.activated:
                # store data about attack
                print("enemy button clicked")
                self.player.target = self.enemy
                self.player.attack = self.selected_attack
                self.current_state = "start_attack"
                

        # draw stuff
        self.draw_emotions()
        self.draw_attack_overlay(attacks)

    def start_attack(self):
        print("jey")
        finished = False
        if self.attack_button.activated:
            self.attack_button.activated = False
            self.data = [self.player.attack, self.player.target]
            print("going forward")
            return True

        if self.back_button.activated:
            self.back_button.activated = False
            print("undoing")
            return False

        # draw stuff
        self.draw_emotions()
        self.attack_button.draw(self.display)
        self.back_button.draw(self.display)

        return finished

    
    def reset_ui(self):
        # TODO has to be called somewhere in combat before a new attack cycle begins
        self.selected_attack = None
        self.current_phase = "idle"
        


    def draw_attack_overlay(self, attacks):
        # overlay
        self.display.blit(self.overlay_img, self.overlay_rect)
        # attack text
        for attack_str, rect in zip(attacks, self.attack_rects):
            text_surface = self.font.render(attack_str.name, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=rect.center)
            self.display.blit(text_surface, text_rect)
        # buttons
        for i, button in enumerate(self.move_buttons):
            button.draw(self.display)


    def draw_emotions(self):
        # only print emotions when they are alive
        if self.player.motivation > 0:
            self.player.draw(self.display)
        if self.enemy.motivation > 0:
            self.enemy.draw(self.display)


