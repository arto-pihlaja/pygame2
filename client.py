import pygame
from player import Player
from network import Network
# from server import readPos, makePos

width = 500
height = 500
win = pygame.display.set_mode((width, height))

def redrawWindow(win, player, player2):
    win.fill((255,255,255))
    player.draw(win)
    try:
        player2.draw(win)
    except AttributeError:
        pass
    pygame.display.update()

def main():
    run = True
    n = Network()
    myPlayer = n.getPlayer()        
    if not myPlayer:
        run = False        
    else:
        pygame.display.set_caption("Client " + str(myPlayer.id))
    clock = pygame.time.Clock()
    while run:
        clock.tick(20)
        otherPlayer = n.send(myPlayer)
        try:
            otherPlayer.update()
        except AttributeError:
            print("Wait for other player!")
        myPlayer.move()
        redrawWindow(win, myPlayer, otherPlayer)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

if __name__ == "__main__":
    main()