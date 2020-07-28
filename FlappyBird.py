import pygame
from pygame.locals import *
from Bird import Bird
from Background import Background
import sys
from random import randint
from time import time
from NeuralNetwork import Network
pygame.init()

# Constants
WINDOW_SIZE = (288, 512)
TITLE = 'Flappy Bird'
FPS = 60
GRAVITY = 1
SPEED = 5

WRITEFROM = 0
WRITETO = 1
GENERATION = 10
SCORES = []

def main():
    pygame.init()
    window = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption(TITLE)
    
    flappy_bird = FlappyBird(window, "AI", '90')
    flappy_bird.play_game()
        
    pygame.quit()

    sys.exit()
        


class FlappyBird:
    def __init__(self, window, player, network):
        '''
        Initialize a FlappyBird object for storing the state of the game and providing a public interface to the player.
        
        Parameters:
          window (pygame.Window): The window object on which we will draw the game.
          player (string): 'HUMAN' for human player or 'AI' for artificial player.
        '''
        self.window = window
        self.clock = pygame.time.Clock()
        self.background = Background(self.window)
        self.bird = Bird(self.window)
        self.ground_height = self.background.get_ground_height()
        self.continue_game = True
        self.score = 0
        self.player = player
        
        if self.player == "AI":
            self.network = Network(network, [self.bird.jump])

    
    def start_level(self):
        timer = 0 
        if self.player == "HUMAN":
            delay = FPS * 3
        elif self.player == "AI":
            delay = 15
        while timer < delay:
            self.draw_frame()
            font = pygame.font.SysFont('Verdana', 80, True)
            surface = font.render(str(3 - (timer // FPS)), True, pygame.Color(255, 255, 255))
            self.window.blit(surface, ((self.window.get_width() // 2) - (surface.get_width() // 2), 150))
            pygame.event.get()
            timer += 1
            pygame.display.update()
            self.clock.tick(FPS)
        self.epoch = time()
    
    
    def play_game(self):
        self.start_level()
        while self.continue_game:
            self.events()
            self.update_state()
            self.draw_frame()
            pygame.display.update()
            self.clock.tick(FPS)  
                
        score = time() - self.epoch
    
    def events(self):
        events = pygame.event.get()
        if self.player == "HUMAN":
            for event in events:
                if event.type == QUIT:
                    self.continue_game = False
                elif event.type == KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[K_SPACE]:
                        self.bird.jump()
        elif self.player == "AI":
            for event in events:
                if event.type == QUIT:
                    self.continue_game = False
            self.feed_data()
            
    def update_state(self):
        self.bird.fall(GRAVITY)
        self.bird.move()
        self.background.move(SPEED)
        self.update_score()      
        if self.bird_collision():
            self.continue_game =  False
        
    def bird_collision(self):
        collision = False
        if self.bird.hit_edge(self.ground_height):
            collision = True
        pipe_rects = self.background.pipe_rects()
        for pipe_rect in pipe_rects:
            bottom_rect = pipe_rect[0]
            top_rect = pipe_rect[1]
            if self.bird.collision(bottom_rect) or self.bird.collision(top_rect):
                collision = True
        return collision
    
    def update_score(self):
        bird_pos = self.bird.get_position()
        pipe_pos = self.background.pipe_rects()[0][0].topright
        if pipe_pos[0] <= bird_pos[0] < pipe_pos[0] + SPEED:
            self.score += 1
    
    def draw_frame(self):
        self.window.fill(pygame.Color((12, 202, 223)))
        self.background.draw()
        self.draw_score()
        self.bird.draw()
        
    def draw_score(self):
        # draws the current score to the display
        # self - a Game object
        offset = 10
        font = pygame.font.SysFont('Verdana', 30, True)
        surface = font.render('Score: ' + str(self.score), True, pygame.Color(255, 255, 255))
        self.window.blit(surface, (offset, offset))
    
    def feed_data(self):
        bird_pos = self.bird.get_position()
        pipe_pos = self.background.get_pipe_pos()
        y_coord = pipe_pos[1] - bird_pos[1]
        dist_to_pipe = abs(pipe_pos[0] - bird_pos[0])
        gap_y_coord = pipe_pos[1]
        y_velocity = self.bird.get_velocity()
        self.network.feed_network([y_coord, dist_to_pipe, gap_y_coord, y_velocity])


if __name__ == "__main__":
    main()