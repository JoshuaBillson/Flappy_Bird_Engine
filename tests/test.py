from flappy_bird import game_engine
from sys import exit
from time import sleep
import pygame
pygame.init()

FPS = 30


def main():
    # Set up Window.
    window = pygame.display.set_mode(game_engine.WINDOW_SIZE)
    pygame.display.set_caption("Flappy Bird")

    # Prepare Assets.
    assets = {'bird': '../assets/Bird.png',
              'pipe': '../assets/pipe.png',
              'ground': '../assets/Ground.png',
              'background': '../assets/bg.png'}

    # Launch Game Engine.
    engine = game_engine.GameEngine(window, FPS, **assets)
    engine.start_game()

    # Main Game Loop.
    while engine.continue_game():
        engine.events()
        engine.update_state()
        engine.draw_frame()
        engine.next_frame()

    # Exit Game On Death.
    sleep(5)
    pygame.quit()
    exit()


if __name__ == "__main__":
    main()
