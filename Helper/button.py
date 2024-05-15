import pygame


class Button():
    def __init__(self, screen, x, y, image, scale):
        self.screen = screen
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        self.clicked = False

        # get mouse pos
        pos = pygame.mouse.get_pos()

        # check if button is clicked
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True

        self.screen.blit(self.image, (self.rect.x, self.rect.y))


         