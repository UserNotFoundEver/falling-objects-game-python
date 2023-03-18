import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
OBJECT_SIZE = 25
SPEED = 5

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Objects")

# Create player and objects
player = pygame.Rect(WIDTH // 2 - PLAYER_WIDTH // 2, HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)
objects = []

def create_object():
    x = random.randint(0, WIDTH - OBJECT_SIZE)
    y = -OBJECT_SIZE
    return pygame.Rect(x, y, OBJECT_SIZE, OBJECT_SIZE)

def move_objects(objects):
    for obj in objects:
        obj.y += SPEED

def remove_offscreen_objects(objects):
    return [obj for obj in objects if obj.y < HEIGHT]

def check_collisions(player, objects):
    for obj in objects:
        if player.colliderect(obj):
            return True
    return False

# Game loop
clock = pygame.time.Clock()
object_timer = pygame.time.get_ticks()
while True:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= SPEED
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += SPEED

    current_time = pygame.time.get_ticks()
    if current_time - object_timer > 1000:
        objects.append(create_object())
        object_timer = current_time

    move_objects(objects)
    objects = remove_offscreen_objects(objects)
    
    if check_collisions(player, objects):
        pygame.quit()
        sys.exit()

    pygame.draw.rect(screen, WHITE, player)
    for obj in objects:
        pygame.draw.rect(screen, WHITE, obj)

    pygame.display.flip()
    clock.tick(60)
