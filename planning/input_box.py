import pygame


class InputBox:

    def __init__(self, screen, x_position, y_position, width, length) -> None:
        self.screen = screen
        self.x_position = x_position
        self.y_position = y_position
        self.width = width
        self.length = length

        self.background_box = pygame.Rect((x_position, y_position, width, length))

    def draw(self) -> None:
        pygame.draw.rect(self.screen, (255, 255, 255), self.background_box)
