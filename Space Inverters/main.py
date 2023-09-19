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

bullet_image = pygame.image.load('missile1.png')
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
    if keys[K_SPACE]:
        bullet_x = ufo_x + ufo_image.get_width()  # Start bullet from the spaceship's x position
        bullet_y = ufo_y + ufo_image.get_height() // 2 - bullet_image.get_height() // 2  # Center bullet vertically
        bullet = (bullet_x, bullet_y)  # Create a bullet at the current position
        bullets.append(bullet)  # Add the bullet to the list of active bullets


    # Bullet movement

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

    for bullet in bullets:
        bullet_x, bullet_y = bullet  # Get the bullet's position
        bullet_x += 5  # Move the bullet horizontally
        bullet_rect = bullet_image.get_rect().move(bullet_x, bullet_y)  # Create a rect object for collision detection
        screen.blit(bullet_image, bullet_rect)  # Draw the bullet image using the rect object
   #     bullet = (bullet_x, bullet_y)  # Update the bullet's position in the bullets list
    bullets = [(bullet_x, bullet_y) for bullet_x, bullet_y in bullets if bullet_x < width]  # Update bullets list, remove bullets that go off-screen
    



    # Building the enemy and make them appear in the ground 
#    screen.blit(enemy1, (en_1 , en_2)) 

    screen.blit(ufo_image, (ufo_x , ufo_y) )
#    screen.blit(ufo_image, (ufo_x, width // 2 - ufo_image.get_width() // 2))
    pygame.display.flip()
    clock.tick(60)