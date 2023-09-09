import pygame as py

from barre import Barre, Direction
from keys_handler import move_barre

class Game:
    score1 = 0
    score2 = 0

    def __init__(self):
        py.init()
        self.screen = py.display.set_mode((1280, 720))
        self.clock = py.time.Clock()
        self.running = True
        self.play()

    def play(self):

        barre = Barre(20, 0)
        seconde_barre = Barre(1240, 0)

        while self.running:
            # poll for events
            # py.QUIT event means the user clicked X to close your window
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.running = False

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("purple")
            
            barre.update(self.screen)
            seconde_barre.update(self.screen)
            
            move_barre(barre, py.K_z, py.K_s)
            move_barre(seconde_barre, py.K_UP, py.K_DOWN)

            # RENDER YOUR GAME HERE

            # flip() the display to put your work on screen
            py.display.flip()

            self.clock.tick(60)  # limits FPS to 60

        py.quit()

    def testFin(self):
        if self.score1 == 10:
            self.victoire("Joueur1")
            self.running = False
        elif self.score2 == 10:
            self.victoire("Joueur2")
            self.running = False
    
    def victoire(self, nomJoueur):
        self.screen.fill("White")
        # Félicite le avec un texte
        py.display.flip()
        return

    
    
if __name__ == "__main__":
    Game().play()
