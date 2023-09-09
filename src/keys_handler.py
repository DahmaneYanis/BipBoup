import pygame as py

from barre import Barre, Direction


def move_barre(barre : Barre, top_key : int, bottom_key : int) -> None:
    keys = py.key.get_pressed()
    
    if keys[top_key]:
        barre.move(Direction.TOP)
    elif keys[bottom_key]:
        barre.move(Direction.BOTTOM)
            
def move_seconde_barre(barre : Barre) -> None:
    keys = py.key.get_pressed()
    
    if keys[py.K_UP]:
        barre.move(Direction.TOP)
    elif keys[py.K_DOWN]:
        barre.move(Direction.BOTTOM)
