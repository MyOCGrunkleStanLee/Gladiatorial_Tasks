import pygame
from utilities.game_state_object import GameStateObject

class GenericScene:
    """
    A generic scene class that has a game_loop_body method.
    """

    def __init__(self, display: pygame.Surface, game_state_object: GameStateObject) -> None:
        """Initializes the object with a PyGame surface to render and data from the game session"""
        self.display = display
        self.game_state_object = game_state_object

    def game_body_loop(self) -> None:
        pass