import pygame
from utilities.game_state_object import GameStateObject
from utilities.generic_scene import GenericScene
from utilities.player_info import Player
from do_it_irl.timer import Timer

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

    def game_body_loop(self) -> None:
        # init task and timer once
        if not self.initialized:
            self.initialize()
            self.initialized = True

        # todo: start button and finished button

        instruction_image_path = "do_it_irl/assets/" + self.task + "-instruction.png"
        self.instruction_image = pygame.image.load(instruction_image_path)

        self.draw()
        

    def initialize(self):
        self.task = self.player_info.task
        self.timer = Timer(self.task_parameters[self.task], (604-40, 40), 70)
        self.timer.start()

    def draw(self):
        self.display.fill("violet")
        self.display.blit(self.instruction_image, (604-100, 200))
        self.timer.draw(self.display)