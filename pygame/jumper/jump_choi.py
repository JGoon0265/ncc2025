import pygame
import sys
import random

# Game constants
FPS = 60
MAX_WIDTH = 800
MAX_HEIGHT = 500
GRAVITY = 0.8
JUMP_STRENGTH = 15
GROUND_Y = MAX_HEIGHT - 60
INITIAL_ENEMY_SPEED = 5
SPEED_INCREMENT = 0.001
PLAYER_SPEED = 5
DOUBLE_JUMP_ALLOWED = True

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
RED = (255, 50, 50)
GREEN = (50, 200, 50)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
YELLOW = (255, 215, 0)

# Initialize pygame
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
pygame.display.set_caption("Jumping Game Enhanced")

# Font initialization
font = pygame.font.SysFont('Arial', 24)
large_font = pygame.font.SysFont('Arial', 48)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 60
        self.vel_y = 0
        self.is_jumping = False
        self.can_double_jump = DOUBLE_JUMP_ALLOWED

    def draw(self):
        player_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, BLUE, player_rect)
        pygame.draw.circle(screen, WHITE, (self.x + 25, self.y + 15), 8)
        pygame.draw.circle(screen, BLACK, (self.x + 25, self.y + 15), 4)
        return player_rect

    def jump(self):
        if not self.is_jumping:
            self.vel_y = -JUMP_STRENGTH
            self.is_jumping = True
        elif self.can_double_jump:
            self.vel_y = -JUMP_STRENGTH
            self.can_double_jump = False

    def update(self):
        self.vel_y += GRAVITY
        self.y += self.vel_y

        if self.y >= GROUND_Y - self.height:
            self.y = GROUND_Y - self.height
            self.vel_y = 0
            self.is_jumping = False
            self.can_double_jump = DOUBLE_JUMP_ALLOWED

class Coin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.collected = False
    
    def draw(self):
        if not self.collected:
            pygame.draw.circle(screen, YELLOW, (self.x, self.y), self.radius)
    
    def collect(self, player_rect):
        coin_rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
        if player_rect.colliderect(coin_rect):
            self.collected = True
            return True
        return False

class Enemy:
    def __init__(self, x, y, width=20, height=40):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        enemy_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, RED, enemy_rect)
        return enemy_rect

    def move(self, speed):
        self.x -= speed
        if self.x <= -self.width:
            self.width = random.randint(20, 50)
            self.height = random.randint(30, 60)
            self.y = GROUND_Y - self.height
            self.x = MAX_WIDTH

class Game:
    def __init__(self):
        self.player = Player(80, GROUND_Y - 60)
        self.enemies = [Enemy(MAX_WIDTH, GROUND_Y - 40)]
        self.coins = [Coin(random.randint(200, 700), GROUND_Y - 30)]
        self.score = 0
        self.high_score = 0
        self.speed = INITIAL_ENEMY_SPEED
        self.game_over = False
    
    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.x = max(0, self.player.x - PLAYER_SPEED)
        if keys[pygame.K_RIGHT]:
            self.player.x = min(MAX_WIDTH - self.player.width, self.player.x + PLAYER_SPEED)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()

    def update(self):
        self.player.update()
        for enemy in self.enemies:
            enemy.move(self.speed)
        for coin in self.coins:
            if coin.collect(pygame.Rect(self.player.x, self.player.y, self.player.width, self.player.height)):
                self.score += 5
                self.coins.remove(coin)
                self.coins.append(Coin(random.randint(200, 700), GROUND_Y - 30))
        
    def check_collisions(self):
        player_rect = pygame.Rect(self.player.x, self.player.y, self.player.width, self.player.height)
        for enemy in self.enemies:
            if player_rect.colliderect(pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)):
                self.game_over = True

    def draw(self):
        screen.fill(WHITE)
        pygame.draw.rect(screen, GREEN, (0, GROUND_Y, MAX_WIDTH, MAX_HEIGHT - GROUND_Y))
        self.player.draw()
        for enemy in self.enemies:
            enemy.draw()
        for coin in self.coins:
            coin.draw()
        score_text = font.render(f"Score: {self.score}", True, BLACK)
        screen.blit(score_text, (20, 20))
        pygame.display.update()

def main():
    game = Game()
    while True:
        game.handle_events()
        if not game.game_over:
            game.update()
            game.check_collisions()
        game.draw()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
