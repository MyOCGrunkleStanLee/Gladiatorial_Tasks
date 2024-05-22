import pygame


class StarterOption:

    def __init__(
        self, screen: pygame.Surface, x_position: int, y_position: int, image: pygame.Surface, emotion_name: str
    ) -> None:
        self.screen = screen
        self.x_position = x_position
        self.y_position = y_position

        self.background_box = pygame.Rect((x_position, y_position, 150, 200))

        # load starter image
        self.image = image

        # create starter name text
        self.my_font = pygame.font.SysFont('College', 30)
        self.emotion_name = emotion_name

        # (optional) create active/hover states
        # below is shamelessly stolen from button.py
        self.activated = False
        self.clicked = False
        self.hover = False
        self.mask = pygame.mask.from_surface(self.image, threshold=0)

    def draw(self):
        pass

        # render background
        pygame.draw.rect(self.screen, (255, 255, 255), self.background_box)

        # render image
        self.screen.blit(self.image, (self.x_position + 25, self.y_position + 75))
        # render text
        text_surface = self.my_font.render(self.emotion_name, False, (0, 0, 0))
        self.screen.blit(text_surface, (self.x_position + 20, self.y_position))
        # conditions for hover states

        # everything below is shamelessly stolen from button.py (yolo)
        self.activated = False

        # get mouse pos
        pos = pygame.mouse.get_pos()

        if self.background_box.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True
            # button is only activated when mouse is released on top of button after left clicking
            if self.clicked and not pygame.mouse.get_pressed()[0]:
                self.activated = True
                self.clicked = False
        else:
            self.clicked = False
