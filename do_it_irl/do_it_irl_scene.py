import pygame
from utilities.game_state_object import GameStateObject
from utilities.generic_scene import GenericScene
from utilities.player_info import Player
from do_it_irl.timer import Timer
from start.button import Button

class DoItIRLScene(GenericScene):

    def __init__(self, display: pygame.Surface, game_state_object: GameStateObject, player_info: Player = None) -> None:
        super().__init__(display, game_state_object, player_info)
        # this dict contains the the amount of seconds for each task
        self.tasks_time = {1: {1: 60, 2: 6, 3: 60, 4: 60, 5: 60},
                           2: {1: 60, 2: 60, 3: 60, 4: 60, 5: 60}, 
                           3: {1: 60, 2: 60, 3: 60, 4: 60, 5: 60}}
        self.task_time_fixed = 300

        # this needs to be set before the game loop starts
        # --> change/increment task after each combat
        # maybe this should be int for simpler increments? 
        self.task = self.player_info.current_task

        self.timer = None
        self.instruction_image = None
        self.initialized = False

        self.font = pygame.font.SysFont(None, 50)


    def create_components(self) -> None:
        #-------------------------------------------------#
        # position of components
        self.start_button_pos = (self.WIDTH//2-100, 200)
        self.finish_button_pos = (self.WIDTH//2+100, 200)
        self.instruction_pos = (self.WIDTH/2, 350)
        self.timer_pos = (self.WIDTH//2, 70)
        #-------------------------------------------------#

        # start button
        start_img = pygame.image.load("Assets/StartButton.png").convert_alpha()
        self.starter_button = Button(self.display, self.start_button_pos[0], 
                                     self.start_button_pos[1], start_img, 0.8)
        # finish button
        finish_img = pygame.image.load("Assets/FinishedButton.png").convert_alpha()
        self.finish_button = Button(self.display, self.finish_button_pos[0], 
                                    self.finish_button_pos[1], finish_img, 0.8)


    def game_body_loop(self) -> None:
        # init task and timer once
        if not self.initialized:
            self.initialize()
            self.initialized = True
        
        # start timer
        if self.starter_button.activated:
            self.timer.start()

        # if timer runs out, go to combat
        if self.timer.done:
            self.game_state_object.current_state = "task_scene"
        
        # finish task   
        if self.finish_button.activated:
            self.timer.activated = False
            if self.player_info.current_task == 5:
                self.game_state_object.current_state = "task_complete"
            else: 
                print(self.player_info.current_task)
                self.player_info.tasks_state[self.player_info.current_project][self.player_info.current_task] = 1
                self.player_info.current_task += 1
                self.game_state_object.current_state = "task_scene"
        
        # create the instruction image based on the taskid
        task_to_display = self.player_info.selected_tasks[self.player_info.current_task-1]
        text_surface = self.font.render(task_to_display, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(self.instruction_pos[0], self.instruction_pos[1]))
        

        self.draw()
        self.display.blit(text_surface, text_rect)
        

    def initialize(self):
        # set the task id
        self.task = self.player_info.current_task
        # set up timer
        self.timer = Timer(self.task_time_fixed, self.timer_pos, 70)
        #self.timer = Timer(self.task_parameters[self.task], self.timer_pos, 70)


    def draw(self):
        self.display.fill("green")
        #self.display.blit(self.instruction_image, self.instruction_image_rect)
        self.timer.draw(self.display)
        self.starter_button.draw(self.display)
        self.finish_button.draw(self.display)