"""
This module defines a pipe object which the player will have to avoid in order to survive.

Classes:
    Pipe

Functions:
    Pipe(image, pos, scroll_speed, window)
"""

import pygame
from src.game_object import GameObject


class Pipe(GameObject):
    """
    This class represents a pipe object which the player will have to avoid in order to survive.

    Inherits From:
        GameObject.

    Args:
        orientation (str): Determines pipe orientation, either "top" or "bottom".
        pos (list): A pair of cartesian coordinates indicating the pipe's position.
        scroll_speed (int): The speed at which the pipe scrolls across the screen.
        window (pygame.Surface): The window on which to draw the bird.
    """
    def __init__(self, image, orientation, pos, scroll_speed, window):
        assert orientation in ("top", "bottom"), "Error: Invalid Orientation!"
        GameObject.__init__(self, image, pos, window)
        self.velocity = [-scroll_speed, 0]
        if orientation == "top":
            self.image = pygame.transform.flip(self.image, False, True)

    def off_screen(self):
        """
        Indicates whether the pipe is off the edge of the screen.

        Args:
            None.

        Returns:
            bool: True if off screen, False otherwise.
        """
        return self.pos[0] <= (-self.image.get_width())
