import pygame as py
from enum import Enum, auto 

class Direction(Enum):
    TOP = auto()
    LEFT = auto()
    BOTTOM = auto()
    RIGHT = auto()

class Element():
    def __init__(self, x : int, y : int) -> None:
        self.x = x 
        self.y = y 
        
    def update(self, window : py.Surface) -> None:
        self.draw(window)
        self.check_collisions(window)

