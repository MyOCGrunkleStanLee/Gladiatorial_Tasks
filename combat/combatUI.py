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


    def create_components(self):
        self.font = pygame.font.Font(None, 36)

        # overlay
        self.overlay_img = pygame.image.load("Assets/CombatMoveOverlay.png")
        self.x_overlay, self.y_overlay = 838 , 405
        self.overlay_rect = self.overlay_img.get_rect(topleft=(self.x_overlay, self.y_overlay))

        # get rects for each attack
        self.attack_rects = [pygame.Rect(self.x_overlay, self.y_overlay, 211, 70),
                 pygame.Rect(self.x_overlay+221, self.y_overlay, 211, 70),
                 pygame.Rect(self.x_overlay, self.y_overlay+80, 211, 70),
                 pygame.Rect(self.x_overlay+221, self.y_overlay+80, 211, 70)]

        # buttons for move menu
        self.move_button_image = pygame.image.load("Assets/TransparentForMoveButton.png")
        self.move_buttons = [Button(self.display, self.attack_rects[0].x, self.attack_rects[0].y, self.move_button_image, 1, positioning="topleft"),
                        Button(self.display, self.attack_rects[1].x, self.attack_rects[1].y, self.move_button_image, 1, positioning="topleft"),
                        Button(self.display, self.attack_rects[2].x, self.attack_rects[2].y, self.move_button_image, 1, positioning="topleft"),
                        Button(self.display, self.attack_rects[3].x, self.attack_rects[3].y, self.move_button_image, 1, positioning="topleft")]
        
        # attack button
        attack_button_image = pygame.image.load("Assets/FightOverlayScreen.png").convert_alpha()
        back_button_image = pygame.image.load("Assets/BackButton.png").convert_alpha()
        self.attack_button = Button(self.display, self.x_overlay+5, self.y_overlay+10, attack_button_image, 1, positioning="topleft")
        self.back_button = Button(self.display, 780, 490, back_button_image, 1)

        self.move_hover = pygame.image.load("Assets/CombatMoveDarkOverlay.png")
        self.currently_hovering = [False, False, False, False]



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
                finished = self.start_attack()
                if finished == "undo":
                    self.selected_attack = None
                    self.current_phase = "select_attack"
        return finished


    def idle(self):
        # activate the player button
        self.player.button_activated = True

        if self.player.button.hover:
            pass
            

        if self.player.button.clicked:
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
                    self.selected_attack = "unvalid"
            if button.hover and not self.currently_hovering[i]:
                button.set_new_image(self.move_hover)
                self.currently_hovering[i] = True
            if not button.hover and self.currently_hovering[i]:
                button.set_new_image(self.move_button_image)
                self.currently_hovering[i] = False

        if self.selected_attack == "unvalid":
            font = pygame.font.SysFont(None, 20)
            text_surface = font.render("Pick a move!", True, (255, 255, 255))
            text_rect = text_surface.get_rect(topleft=(self.x_overlay, self.y_overlay-30))
            self.display.blit(text_surface, text_rect)

        # select enemy if an attack is selected
        if self.selected_attack != None and self.selected_attack != "unvalid":
            self.enemy.button_activated = True

            if self.enemy.button.hover:
                pass
                #self.player.button.set_new_image(self.move_hover)
            

            if self.enemy.button.activated:
                # store data about attack
                self.current_phase = "start_attack"
                print("enemy button clicked")
                self.player.target = self.enemy
                self.player.attack = self.selected_attack

        # draw stuff
        self.draw_emotions()
        self.draw_attack_overlay(attacks)

    def start_attack(self):
        finished = False
        if self.attack_button.activated:
            self.attack_button.activated = False
            print("going forward")
            return True

        if self.back_button.activated:
            self.back_button.activated = False
            print("undoing")
            return "undo"

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
        print(self.player.motivation)
        if self.player.motivation > 0:
            self.player.draw(self.display)
        if self.enemy.motivation > 0:
            self.enemy.draw(self.display)


