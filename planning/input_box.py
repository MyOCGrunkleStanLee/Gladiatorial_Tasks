import pygame


class InputBox:

    def __init__(
        self, screen: pygame.Surface, x_position, y_position, width, length, prompt_text
    ) -> None:
        # these variables typically remain the same throughout runtime
        self.screen = screen
        self.x_position = x_position
        self.y_position = y_position
        self.width = width
        self.length = length

        self.background_box = pygame.Rect((x_position, y_position, width, length))
        self.my_font = pygame.font.SysFont('College', 30)

        # these variables will change during runtime
        self.prompt_text = prompt_text
        self.user_text = ''

    def draw(self) -> None:

        # render background
        pygame.draw.rect(self.screen, (255, 255, 255), self.background_box)

        # render prompt text
        prompt_surface = self.my_font.render(self.prompt_text, False, (0, 0, 0))
        self.screen.blit(prompt_surface, (self.x_position, self.y_position))

        # render user input
        user_surface = self.my_font.render(self.user_text, False, (0, 0, 0))
        self.screen.blit(user_surface, (self.x_position, self.y_position + 40))
