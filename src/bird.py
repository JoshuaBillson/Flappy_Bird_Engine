"""
This module defines the Bird class.

Classes:
    Bird
"""

import pygame
from src.game_object import GameObject

MAX_JUMP = -10
MAX_FALL = 15


class Bird(GameObject):
    """
    This class represents a bird object which is controlled by the player.

    Inherits From:
        GameObject.

    Args:
        window (pygame.Surface): The window on which to draw the bird.

    Attributes:
        jump_force: The upward acceleration imparted by jumping.
    """
    def __init__(self, image, window):
        GameObject.__init__(self, image, [0, 0], window)
        self.pos = [75, (self.window.get_height() // 2) - (self.image.get_height() // 2)]
        self.jump_force = 20
        self.velocity = [0, -10]

    def jump(self):
        """
        Adjusts the bird's vertical velocity according to the jump force.

        Takes no arguments and returns nothing.
        """
        self.velocity[1] -= self.jump_force
        if self.velocity[1] <= MAX_JUMP:
            self.velocity[1] = MAX_JUMP

    def fall(self, gravity):
        """
        Adjusts the bird's vertical velocity according to the force of gravity.

        Args:
            gravity (int): The acceleration of gravity.

        Returns:
            None.
        """
        if self.velocity[1] <= MAX_FALL:
            self.velocity[1] += gravity

    def hit_edge(self, ground_height):
        """
        Determines if the bird has hit the edge of the playing area.

        Args:
            ground_height (int): The height of the ground in pixels.

        Returns:
            bool: True if the bird is outside of the play area and False otherwise.
        """
        return self.pos[1] <= 0 or self.pos[1] >= (ground_height - self.image.get_height())
