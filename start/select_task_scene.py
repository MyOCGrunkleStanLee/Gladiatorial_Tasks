import pygame
import sys
from start.button import Button
from utilities.game_state_object import GameStateObject
from utilities.generic_scene import GenericScene
from utilities.player_info import Player

class SelectTaskScene(GenericScene): 

    def __init__(self, display: pygame.Surface, game_state_object: GameStateObject, player_info: Player = None) -> None:
        self.background_img = pygame.image.load("start/ChooseTaskScreen.png").convert_alpha()
        self.icon_button_list = []
        self.finished_tasks = []
        
        super().__init__(display, game_state_object, player_info)
        

    def create_components(self):
        # different states for big icon buttons
        self.big_icon_transparent = pygame.image.load("start/transparent_big_icon.png").convert_alpha()
        self.big_icon_hover = pygame.image.load("Assets/LargeGoldSquare.png").convert_alpha()
        self.big_icon_golden = pygame.image.load("Assets/LargeGoldSquare.png").convert_alpha()

        self.small_icon_golden = pygame.image.load("Assets/SmallGoldSquare.png").convert_alpha()

        # exercise button 
        self.exercise_button = Button(self.display, 163, 175, self.big_icon_transparent, 0.83, positioning="topleft")
        
        self.currently_hovering = False


    def game_body_loop(self):
        # set different overlays for hover and not hover
        if self.exercise_button.hover and not self.currently_hovering:
            self.exercise_button.set_new_image(self.big_icon_hover)
            self.currently_hovering = True
        elif not self.exercise_button.hover and self.currently_hovering:
            self.exercise_button.set_new_image(self.big_icon_transparent)
            self.currently_hovering = False

        if self.exercise_button.activated:
            self.game_state_object.current_state = "planning"

        # draw
        self.display.blit(self.background_img, (0, 0))
        self.exercise_button.draw()
        
        # golden overlay
        self.mark_finished_tasks()

    
    def mark_finished_tasks(self):
        # draw small overlays
        icon_x_coords = [337, 460, 593, 728, 884]
        y_coords = [197, 320, 433]
        for project, tasks in self.player_info.tasks_state.items():
            for task, finished in tasks.items():
                if finished:
                    # calculate x y
                    x = icon_x_coords[task-1]
                    y = y_coords[project-1]
                    rect = self.small_icon_golden.get_rect(topleft=(x, y))
                    self.display.blit(self.small_icon_golden, rect)

        # draw big overlays only if tasks are done
        icon_x_coords = [163, 1036]
        y_coords = [175, 303, 417]
        finished_projects = self.player_info.get_finished_projects()
        for project in finished_projects:
            for i in range(2):
                x = icon_x_coords[i]
                y = y_coords[project-1]
                rect = self.small_icon_golden.get_rect(topleft=(x, y))
                self.display.blit(self.big_icon_golden, rect)

        
