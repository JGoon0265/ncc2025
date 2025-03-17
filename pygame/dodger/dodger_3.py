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

class Poop():
    def __init__(self):
        self.x=random.randrange(0,MAX_WIDTH-40)
        self.y=50
        self.speed=random.randrange(10,20)
        self.enemy=pygame.image.load(r'C:\2025ncc\2025ncc\pygame\dodger\응.png')
        self.enemy=pygame.transform.scale(self.enemy,(40,40))

    def draw(self):
        return screen.blit(self.enemy,(self.x,self.y,20,20))
    
    def move(self):
        self.y=self.y+self.speed
        if self.y>=MAX_HEIGHT:
            self.y=50
            self.x=random.randrange(0,MAX_WIDTH-40)
            self.speed=random.randrange(7,15)

player = Player(MAX_WIDTH/2,MAX_HEIGHT-40)
poop=Poop()

def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                


        clock.tick(FPS)
        screen.fill((255,255,255))
        global pressed_keys   #광역변수 선언
        pressed_keys = pygame.key.get_pressed()
        player_rect=player.draw()
        player.move()

        poop_rect=poop.draw()
        poop.move()

        if player_rect.colliderect(poop_rect):
            print("lol you died.")
            pygame.quit()
            sys.exit()

        pygame.display.update()

if __name__=='__main__':
    main()