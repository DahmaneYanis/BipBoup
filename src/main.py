import pygame as py

from barre import Barre, Direction
from keys_handler import move_barre, move_seconde_barre

# pygame setup
py.init()
screen = py.display.set_mode((1280, 720))
clock = py.time.Clock()
running = True


barre = Barre(20, 0)
seconde_barre = Barre(1240, 0)

while running:
    # poll for events
    # py.QUIT event means the user clicked X to close your window
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    
    barre.update(screen)
    seconde_barre.update(screen)
    
    move_barre(barre)
    move_seconde_barre(seconde_barre)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    py.display.flip()

    clock.tick(60)  # limits FPS to 60

py.quit()