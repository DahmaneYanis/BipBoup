import pygame as py

# pygame setup
py.init()
screen = py.display.set_mode((1280, 720))
clock = py.time.Clock()
running = True

while running:
    # poll for events
    # py.QUIT event means the user clicked X to close your window
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    py.display.flip()

    clock.tick(60)  # limits FPS to 60

py.quit()