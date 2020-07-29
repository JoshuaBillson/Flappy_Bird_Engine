from flappy_bird import game_engine
from sys import exit
from time import sleep
import pygame
pygame.init()

FPS = 30


def main():
    window = pygame.display.set_mode(game_engine.WINDOW_SIZE)
    pygame.display.set_caption("Flappy Bird")
    engine = game_engine.GameEngine(window, FPS)
    engine.start_game()

    while engine.continue_game:
        engine.events()
        engine.update_state()
        engine.draw_frame()
        engine.next_frame()

    sleep(5)
    pygame.quit()
    exit()


if __name__ == "__main__":
    main()
