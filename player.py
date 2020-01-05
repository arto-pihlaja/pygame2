import pygame
class Player():

    def __init__(self, x, y, width, height, colour, id):
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.rect = (x, y, width, height)
        self.speed = 4

    def draw(self, win):
        pygame.draw.rect(win, self.colour, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed   

        self.update()         
    
    def update(self):            
        self.rect = (self.x, self.y, self.width, self.height)

