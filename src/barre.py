import pygame as py 

from enum import Enum, auto 


class Direction(Enum):
    TOP = auto()
    BOTTOM = auto()


class Barre:
    def __init__(self, x : int, y : int) -> None:
        self.x = x 
        self.y = y 
        
        
    def update(self, window : py.Surface) -> None:
        self.draw(window)
        self.check_collisions(window)
        
    def draw(self, window : py.Surface) -> None:
        py.draw.rect(window, (0, 0, 0), (self.x, self.y, 20, 200))
        
        
    def move(self, direction : Direction) -> None:
        if direction == Direction.TOP:
            self.y -= 10
        elif direction == Direction.BOTTOM:
            self.y += 10
            
            
    def check_collisions(self, window : py.Surface) -> None:
        if self.y < 0:
            self.y = 0
        elif self.y > window.get_height() - 200:
            self.y = window.get_height() - 200
    