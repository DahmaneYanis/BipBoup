import pygame as py

from barre import Barre, Direction
from keys_handler import move_barre, move_seconde_barre


class Game:
    score1 = 0
    score2 = 0

    def __init__(self, screen, clock, running):
        py.init()
        screen = py.display.set_mode((1280, 720))
        clock = py.time.Clock()
        running = True
        self.play()

    def play(self):

        barre = Barre(20, 0)
        seconde_barre = Barre(1240, 0)

        while running:
            # poll for events
            # py.QUIT event means the user clicked X to close your window
            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("purple")

            # RENDER YOUR GAME HERE

            # flip() the display to put your work on screen
            py.display.flip()

            self.clock.tick(60)  # limits FPS to 60

        py.quit()

    def testFin(self):
        if self.score1 == 10:
            self.victoire("Joueur1")
            running = False
        elif self.score2 == 10:
            self.victoire("Joueur2")
            running = False
    
    def victoire():
        return