import pygame
from start.button import Button
from utilities.generic_scene import GenericScene



class TaskComplete(GenericScene):
    
    def create_components(self):
        start_img = pygame.image.load("Assets/FinishedButton.png").convert_alpha()
        self.starter_button = Button(self.display, self.WIDTH/2, 400, start_img, 0.8)

        
        self.bg = pygame.image.load("Assets/TaskCompleteScreen.png")

    def game_body_loop(self):
        self.display.blit(self.bg, (0,0))

    

        self.starter_button.draw(self.display)

        # change game state on click
        if self.starter_button.activated:
            self.game_state_object.current_state = "select_task"