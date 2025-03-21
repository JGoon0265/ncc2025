import pygame, sys
from pygame.locals import *
import random


FPS=30
MAX_WIDTH=400
MAX_HEIGHT=600

pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))

class Player():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def draw(self):
        return pygame.draw.rect(screen,(0,0,255),(self.x,self.y,40,40))
    
    def move(self):
        if pressed_keys[K_RIGHT]:
            if self.x < MAX_WIDTH-40:
                self.x+=5
        if pressed_keys[K_LEFT]:
            if self.x>0:
                self.x -=5

player = Player(MAX_WIDTH/2,MAX_HEIGHT-40)

def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                


        clock.tick(FPS)
        screen.fill((255,255,255))
        global pressed_keys
        pressed_keys = pygame.key.get_pressed()
        player_rect=player.draw()
        player.move()

        pygame.display.update()

if __name__=='__main__':
    main()