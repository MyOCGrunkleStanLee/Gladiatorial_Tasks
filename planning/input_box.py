import pygame


class InputBox:

    def __init__(
        self, screen: pygame.Surface, x_position, y_position, width, length, prompt_text
    ) -> None:
        self.screen = screen
        self.x_position = x_position
        self.y_position = y_position
        self.width = width
        self.length = length
        self.prompt_text = prompt_text

        self.background_box = pygame.Rect((x_position, y_position, width, length))

        my_font = pygame.font.SysFont('College', 30)

        self.prompt_text = prompt_text
        self.prompt_surface = my_font.render(self.prompt_text, False, (0, 0, 0))

        self.user_text = ''
        self.user_surface = my_font.render(self.user_text, True, (0, 0, 0))

    def draw(self) -> None:
        pygame.draw.rect(self.screen, (255, 255, 255), self.background_box)

        self.screen.blit(self.prompt_surface, (self.x_position, self.y_position))
        self.screen.blit(self.user_surface, (self.x_position, self.y_position + 40))