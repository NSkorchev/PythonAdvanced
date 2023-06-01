import pygame
import random
import time

# Initialize the game
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Digger")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Game settings
block_size = 20
player_speed = 5
enemy_speed = 3

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([block_size, block_size])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = window_width // 2
        self.rect.y = window_height // 2

    def update(self, *args):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= player_speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += player_speed
        if keys[pygame.K_UP]:
            self.rect.y -= player_speed
        if keys[pygame.K_DOWN]:
            self.rect.y += player_speed

        # Keep the player within the window boundaries
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > window_width - block_size:
            self.rect.x = window_width - block_size
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > window_height - block_size:
            self.rect.y = window_height - block_size

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([block_size, block_size])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Enemy(pygame.sprite.Sprite):
    def __init__(self, target):
        super().__init__()
        self.image = pygame.Surface([block_size, block_size])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.target = target
        self.rect.x = random.randrange(window_width - block_size)
        self.rect.y = random.randrange(window_height - block_size)

    def update(self):
        if self.rect.x < self.target.rect.x:
            self.rect.x += enemy_speed
        elif self.rect.x > self.target.rect.x:
            self.rect.x -= enemy_speed

        if self.rect.y < self.target.rect.y:
            self.rect.y += enemy_speed
        elif self.rect.y > self.target.rect.y:
            self.rect.y -= enemy_speed

all_sprites = pygame.sprite.Group()
player = Player()
blocks = pygame.sprite.Group()

# Create blocks
for row in range(window_height // block_size):
    for col in range(window_width // block_size):
        # Exclude the area around the player's initial position
        if col < 5 and row < 5:
            continue
        if col > window_width // block_size - 6 and row > window_height // block_size - 6:
            continue
        block = Block(col * block_size, row * block_size)
        all_sprites.add(block)
        blocks.add(block)

all_sprites.add(player)

enemies = pygame.sprite.Group()
for _ in range(3):
    enemy = Enemy(player)
    all_sprites.add(enemy)
    enemies.add(enemy)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    # Check for collision between player and enemies
    if pygame.sprite.spritecollide(player, enemies, False):
        running = False

    window.fill(BLACK)
    all_sprites.draw(window)
    pygame.display.flip()
    clock.tick(60)

    # Add a small delay to the game loop
    time.sleep(0.1)

pygame.quit()