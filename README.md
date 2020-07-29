# Flappy Bird Game Engine
The purpose of this project is to provide a simple game engine for running Flappy Bird. The engine is powered by Pygame and can be used simply by importing the GameEngine class into a project and utilizing the provided methods. 

## Gameplay
The space bar is used to jump and the score is tracked as the number of elapsed seconds since the game began. Hitting the pipes, ground, or ceiling results in instant death.

## Constants
**game_engine.WINDOW_SIZE**
A tuple declaring the width and height of the game window.

## Classes
**game_engine.GameEngine**
This class maintains the state of the game and provides several methods for updating its state. It is the only class needed to start, run, and maintain the game.

## Functions
**game_engine.GameEngine(window, fps)**
Creates a GameEngine object for running a game of Flappy Bird.
*window (pygame.Surface):* A window inside which the game is drawn.
*fps (int):* The number of game frames to be rendered per second, recommended value is 30.

**game_engine.GameEngine.start_game()**
Starts a new game with a brief 3 second countdown allowing for the player to ready themselves.

**game_engine.GameEngine.events()**
Handles player diven events, to be called once each frame.

**game_engine.GameEngine.update_state()**
Updates the state of the game, to be called once each frame.

**game_engine.GameEngine.draw_frame()**
Draws the current frame to the screen, called once each frame.

**game_engine.GameEngine.next_frame()**
Waits an appropriate length of time to ensure the desired FPS is maintained, called once at the end of each frame.
