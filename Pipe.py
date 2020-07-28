import pygame
from pygame.locals import *
from random import randint

class Pipe:
    def __init__(self, window):
        self.window = window
        self.bottom_image = pygame.image.load('assets/pipe.png')
        self.top_image = pygame.transform.flip(self.bottom_image, False, True)
        self.height = self.bottom_image.get_height()
        self.width = self.bottom_image.get_width()
        self.gap = 120
        self.center = randint(125, self.window.get_height()-175)
        self.bottom_pos = (self.window.get_width() + 20, self.center + (self.gap // 2))
        self.top_pos = (self.window.get_width() + 20, (self.center - (self.gap // 2) - self.height))
    
    def move(self, speed):
        self.bottom_pos = (self.bottom_pos[0] - speed, self.bottom_pos[1])
        self.top_pos = (self.top_pos[0] - speed, self.top_pos[1])
    
    def draw(self):
        self.window.blit(self.bottom_image, self.bottom_pos)
        self.window.blit(self.top_image, self.top_pos)
    
    def at_edge(self):
        return self.bottom_pos[0] + self.width <= 0
    
    def rect(self):
        bottom_rect = self.bottom_image.get_rect(topleft=(self.bottom_pos[0], self.center + self.gap // 2))
        top_rect = self.top_image.get_rect(bottomleft=(self.top_pos[0], self.center - self.gap // 2))
        return (bottom_rect, top_rect)
    
    def get_center(self):
        x = self.bottom_pos[0]
        y = self.center
        return (x, y)
        