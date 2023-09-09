import pygame as py

from barre import Barre, Direction


def move_barre(barre : Barre, top_key : int, bottom_key : int) -> None:
    keys = py.key.get_pressed()
    
    if keys[top_key]:
        barre.move(Direction.TOP)
    elif keys[bottom_key]:
        barre.move(Direction.BOTTOM)
            
