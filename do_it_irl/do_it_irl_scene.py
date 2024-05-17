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
        self.task_parameters: dict[str, int] = {
            "task1": 60,
            "task2": 60,
            "task3": 60,
            "task4": 60,
            "task5": 60,
        }

        # this needs to be set before the game loop starts
        # --> change/increment task after each combat
        # maybe this should be int for simpler increments? 
        self.task = ""

        self.timer = None
        self.instruction_image = None
        self.initialized = False

    def create_components(self) -> None:
        # start button
        start_img = pygame.image.load("do_it_irl/assets/start_button.png").convert_alpha()
        self.starter_button = Button(self.display, self.WIDTH//2-100, 200, start_img, 0.8)
        # finish button
        finish_img = pygame.image.load("do_it_irl/assets/finish_button.png").convert_alpha()
        self.finish_button = Button(self.display, self.WIDTH//2+100, 200, finish_img, 0.8)

    def game_body_loop(self) -> None:
        # init task and timer once
        if not self.initialized:
            self.initialize()
            self.initialized = True

        if self.starter_button.activated:
            self.timer.start()
            

        instruction_image_path = "do_it_irl/assets/" + self.task + "-instruction.png"
        self.instruction_image = pygame.image.load(instruction_image_path)
        self.instruction_image_rect = self.instruction_image.get_rect(center=(self.WIDTH/2, 400))

        self.draw()
        

    def initialize(self):
        # set the task id
        self.task = self.player_info.task
        # set up timer
        self.timer = Timer(self.task_parameters[self.task], (self.WIDTH//2, 70), 70)

    def draw(self):
        self.display.fill("violet")
        self.display.blit(self.instruction_image, self.instruction_image_rect)
        self.timer.draw(self.display)
        self.starter_button.draw()
        self.finish_button.draw()