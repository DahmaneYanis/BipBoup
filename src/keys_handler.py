import pygame as py

from barre import Barre, Direction

def move_barre(barre : Barre) -> None:
    keys = py.key.get_pressed()
    
    if keys[py.K_z]:
        barre.move(Direction.TOP)
    elif keys[py.K_s]:
        barre.move(Direction.BOTTOM)
            
def move_seconde_barre(barre : Barre) -> None:
    keys = py.key.get_pressed()
    
    if keys[py.K_UP]:
        barre.move(Direction.TOP)
    elif keys[py.K_DOWN]:
        barre.move(Direction.BOTTOM)