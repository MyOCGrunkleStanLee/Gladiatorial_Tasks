# todo get the user to select a main task to do while playing the game
 
import pygame
from start.button import Button
from utilities.generic_scene import GenericScene

class StartScene(GenericScene):    

    def create_components(self):
        start_img = pygame.image.load("start/start_button.png").convert_alpha()
        self.start_button = Button(self.display, 100, 100, start_img, 0.4)

    def game_body_loop(self):
        
        self.display.fill("red")
        # add a button
        self.start_button.draw()

        # change game state on click
        if self.start_button.activated:
            self.game_state_object.current_state = "select_starter"
