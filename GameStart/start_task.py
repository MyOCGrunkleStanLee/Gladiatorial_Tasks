# todo get the user to select a main task to do while playing the game
 
import pygame
from Helper.button import Button

class TaskTree:
    """
    This is our Task Tree screen
    """
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

    def run(self):
        self.display.fill("red")

        # add a button
        start_img = pygame.image.load("Assets/start_button.png").convert_alpha()
        start_button = Button(self.display, 100, 100, start_img, 0.4)
        start_button.draw()

        # change gamestate on click
        if start_button.clicked:
            self.gameStateManager.set_state("exercise")
