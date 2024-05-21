import pygame


class Button():
    def __init__(self, screen, x, y, image, scale, positioning="center"):
        self.screen = screen
        self.x = x
        self.y = y
        self.scale = scale
        self.positioning = positioning
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.init_rect()
        self.mask = pygame.mask.from_surface(self.image, threshold=0)
        self.clicked = False
        self.activated = False
        self.hover = False

    def draw(self):
        self.activated = False

        # get mouse pos
        pos = pygame.mouse.get_pos()

        # check if button is clicked
        if self.rect.collidepoint(pos):
            # Convert mouse position to relative position within the button
            relative_x, relative_y = pos[0] - self.rect.left, pos[1] - self.rect.top
            if self.mask.get_at((relative_x, relative_y)):
                self.hover = True
                if pygame.mouse.get_pressed()[0] and self.clicked == False:
                    self.clicked = True
                # button is only activated when mouse is released on top of button after left clicking
                if self.clicked and not pygame.mouse.get_pressed()[0]:
                    self.activated = True
                    self.clicked = False
            else:
                self.hover = False
                self.clicked = False
        else:
            self.clicked = False
            self.hover = False

        self.screen.blit(self.image, self.rect)

    def set_new_image(self, image):
        # use only for new images that are the same shape as the last image!

        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * self.scale), int(height * self.scale)))
        self.rect = self.image.get_rect(center=self.rect.center)
        #self.mask = pygame.mask.from_surface(self.image)

    
    def init_rect(self):
        if self.positioning=="center":
            return self.image.get_rect(center=(self.x, self.y))
        elif self.positioning == "topleft":
            return self.image.get_rect(topleft=(self.x, self.y)) 
        elif self.positioning == "bottomleft":
            return self.image.get_rect(bottomleft=(self.x, self.y)) 
