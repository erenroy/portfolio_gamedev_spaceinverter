import pygame
from pygame.locals import *
import sys
pygame.init()

width, height = 1800, 900
screen = pygame.display.set_mode((width, height))

# Load the background image and UFO image
background_image = pygame.image.load("background1.jpg")
ufo_image = pygame.image.load("spaceship2.png")

background_x = 0
ufo_y = height // 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        ufo_y -= 5
    elif keys[K_DOWN]:
        ufo_y += 5
        

    background_x -= 1
    if background_x <= -background_image.get_width():
        background_x = 0

    # Draw two instances of the background image side by side
    screen.blit(background_image, (background_x, 0))
    screen.blit(background_image, (background_x + background_image.get_width(), 0))

    screen.blit(ufo_image, (ufo_y, height // 2 - ufo_image.get_height() // 2))

    pygame.display.flip()
    clock.tick(120)















import pygame
from pygame.locals import *
import sys
import random

pygame.init()

width, height = 1800, 900
screen = pygame.display.set_mode((width, height))

# Load the background image and UFO image
background_image = pygame.image.load("background1.jpg")
ufo_image = pygame.image.load("spaceship2.png")

background_x = 0
ufo_y = height // 2.2
ufo_x = width // 8
clock = pygame.time.Clock()

# Building the enemys and making them appear on the game 
enemy_image = pygame.image.load("enemy.png")
enemy1 = pygame.image.load("enemy.png")
enemies = []  # List to store enemy objects
enemy_spawn_timer = 0  # Timer to control enemy spawning

bullet = pygame.image.load('missile.png')
bullet_x = 0
bullet_y = 480
bulletx_change = 0
bullety_change = 0
bullets = []
 
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_r:
                running = False


    keys = pygame.key.get_pressed()
    if keys[K_UP] and ufo_y > 14:
        ufo_y -= 5
    elif keys[K_DOWN] and ufo_y < 790:
        ufo_y += 5
    if keys[K_LEFT]  and ufo_x > 5:
        ufo_x -= 5
        print(ufo_x)
    elif keys[K_RIGHT] and ufo_x < 1670:
        ufo_x += 5


    background_x -= 1
    if background_x <= -background_image.get_width():
        background_x = 0

    # Draw two instances of the background image side by side
    screen.blit(background_image, (background_x, 0))
    screen.blit(background_image, (background_x + background_image.get_width(), 0))

    # creating multipe enemys
    enemy_spawn_timer += clock.get_rawtime()
    if enemy_spawn_timer >= 1000:
        enemy_x = width - enemy_image.get_width()  # Set the initial X-coordinate of the new enemy spaceship to align with the right edge of the screen
        enemy_y = random.randint(0, height - 60 - enemy_image.get_height())  # Generate a random Y-coordinate for the new enemy spaceship
        enemies.append((enemy_x, enemy_y))  # Add the new enemy position to the enemies list
        enemy_spawn_timer = 0  # Reset the timer

    for i, enemy in enumerate(enemies):
        enemy_x, enemy_y = enemy
        enemy_x -= 3  # Move the enemy spaceship forward by subtracting from its X-coordinate
        enemy_y += random.choice([-1, 0, 1])  # Randomly select -1, 0, or 1 to increment or decrement enemy_y
        enemies[i] = (enemy_x, enemy_y)  # Update the enemy position in the enemies list
        screen.blit(enemy_image,(enemy_x, enemy_y))
    



    # Building the enemy and make them appear in the ground 
#    screen.blit(enemy1, (en_1 , en_2)) 

    screen.blit(ufo_image, (ufo_x , ufo_y) )
#    screen.blit(ufo_image, (ufo_x, width // 2 - ufo_image.get_width() // 2))
    pygame.display.flip()
    clock.tick(60)