# todo get the user to select a main task to do while playing the game
 
import pygame
import sys
from start.button import Button
from utilities.generic_scene import GenericScene

class StartScene(GenericScene):    

    def create_components(self):
        # Title
        my_font = pygame.font.SysFont('College', 30)
        self.text_surface = my_font.render('Gladiatorial Tasks', False, (0, 0, 0))

        # start button
        start_img = pygame.image.load("start/start_button.png").convert_alpha()
        self.start_button = Button(self.display, self.WIDTH/2-100, self.HEIGHT/2-100, start_img, 0.4)

        # quit button
        quit_img = pygame.image.load("start/quit_button.png").convert_alpha()
        self.quit_button = Button(self.display, self.WIDTH/2-100, self.HEIGHT/2, quit_img, 0.4)

    def game_body_loop(self):
        
        self.display.fill("red")

        self.display.blit(self.text_surface, (self.WIDTH/2-self.text_surface.get_width()/2, 50))

        self.start_button.draw()
        self.quit_button.draw()

        # change game state on click
        if self.start_button.activated:
            self.game_state_object.current_state = "planning"

        # quit game if quit button clicked
        if self.quit_button.activated:
            pygame.quit()
            sys.exit()
