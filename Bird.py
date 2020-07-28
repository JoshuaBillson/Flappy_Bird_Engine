import pygame
from pygame.locals import *

class Bird():
    def __init__(self, window):
        self.image = pygame.image.load('assets/Bird.png')
        self.window = window
        self.pos = [75, (self.window.get_height() // 2) - (self.image.get_height() // 2)]
        self.velocity = 0
        self.jump_force = 14

    def jump(self):
        self.velocity -= self.jump_force
        if self.velocity <= -17:
            self.velocity = -17
    
    def fall(self, acceleration):
        if self.velocity <= 15:
            self.velocity += acceleration
    
    def move(self):
        self.pos[1] = self.pos[1] + self.velocity
    
    def draw(self):
        self.window.blit(self.image, self.pos)
    
    def hit_edge(self, ground_height):
        return self.pos[1] <= 0 or self.pos[1] >= (ground_height - self.image.get_height())
    
    def collision(self, pipe_rect):
        bird_rect = self.image.get_rect(topleft = (self.pos))
        return bird_rect.colliderect(pipe_rect)
    
    def get_position(self):
        return self.pos
    
    def get_velocity(self):
        return self.velocity