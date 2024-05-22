import pygame
from combat.emotions import Emotion


class StarterOption:

    def __init__(
        self, screen: pygame.Surface, x_position: int, y_position: int, emotion: Emotion
    ) -> None:
        pass
        self.screen = screen
        self.x_position = x_position
        self.y_position = y_position
        self.emotion = emotion

        self.emotion_name = emotion.name

        self.emotion_image = pygame.image.load(emotion.image_path)
        self.emotion_image = pygame.transform.scale(self.emotion_image, (100, 100))

        self.my_font = pygame.font.SysFont('College', 48)
        self.transparent_overlay = pygame.image.load(
            "GameStart/choose-emotion-transparent.png"
        )
        self.overlay_collision = self.transparent_overlay.get_rect(
            topleft=(x_position, y_position)
        )

        self.activated = False
        self.clicked = False

    def draw(self):

        # render image
        self.screen.blit(
            self.emotion_image, (self.x_position + 25, self.y_position + 75)
        )
        # render text
        text_surface = self.my_font.render(self.emotion_name, False, (0, 0, 0))
        self.screen.blit(text_surface, (self.x_position + 300, self.y_position + 75))

        # render transparent foreground
        self.screen.blit(self.transparent_overlay, (self.x_position, self.y_position))

        # everything below is shamelessly stolen from button.py (yolo)
        self.activated = False

        # get mouse pos
        pos = pygame.mouse.get_pos()

        if self.overlay_collision.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True
            # button is only activated when mouse is released on top of button after left clicking
            if self.clicked and not pygame.mouse.get_pressed()[0]:
                self.activated = True
                self.clicked = False
        else:
            self.clicked = False
