import pygame
from pygame.locals import *
from Pipe import Pipe

class Background:
    def __init__(self, window):
        self.bg = pygame.image.load('assets/bg.png')
        self.ground = pygame.image.load('assets/Ground.png')
        self.window = window
        self.window_width = self.window.get_width()
        self.window_height = self.window.get_height()
        self.ground_height = self.window_height - self.ground.get_height()
        self.ground_pos = [(0, self.ground_height), (self.ground.get_width(), self.ground_height)]
        self.pipes = [Pipe(self.window)]
    
    def draw(self):
        self.window.blit(self.bg, (0, 0)) # draw background
        for pipe in self.pipes: # draw pipes
            pipe.draw()
        for pos in self.ground_pos: # draw ground
            self.window.blit(self.ground, pos)
    
    def move(self, speed):
        if self.ground_pos[0][0] <= -self.ground.get_width():
            self.ground_pos.pop(0)
            self.ground_pos.append((self.ground_pos[0][0] + self.ground.get_width(), self.window_height - self.ground.get_height()))
        if self.pipes[0].at_edge():
            self.pipes.pop(0)
            self.pipes.append(Pipe(self.window))
        for i in range(2):
            self.ground_pos[i] = (self.ground_pos[i][0] - speed, self.ground_pos[i][1])
        for pipe in self.pipes:
            pipe.move(speed)
    
    def get_ground_height(self):
        return self.ground_height
    
    def pipe_rects(self):
        rects = []
        for pipe in self.pipes:
            rects.append(pipe.rect())
        return rects
    
    def get_pipe_pos(self):
        pipe_pos = self.pipes[0].get_center()
        return pipe_pos