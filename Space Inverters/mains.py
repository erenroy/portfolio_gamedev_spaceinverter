import pygame
from pygame.locals import *
import sys
import random
import math
pygame.init()

width, height = 1800, 900
screen = pygame.display.set_mode((width, height))

# Making score table 
score_img = pygame.image.load("boooo_1.jpg")
font = pygame.font.Font(None, 40)
text = font.render("Score - 6 " , True , (255 , 255 , 255))
text_rect = text.get_rect(center=(width // 2, height // 2))

ship_img = pygame.image.load("boooo.jpg")

ship_1_img = pygame.image.load("arcade.png")
ship_2_img = pygame.image.load("arcade-game.png")
ship_3_img = pygame.image.load("spaceship_1.png")

# Load the background image and UFO image
background_image = pygame.image.load("background1.jpg")
ufo_image = pygame.image.load("spaceship2.png")
background_x = 0
ufo_y = height // 2.2
ufo_x = width // 8
clock = pygame.time.Clock()
score = 0
# Building the enemys and making them appear on the game 
enemy_image_1 = pygame.image.load("enemy.png")
enemy_image_2 = pygame.image.load("enemy21.png")
enemy_image_3 = pygame.image.load("enemy22.png")


# mylist = ["enemy
enemy_image = pygame.image.load("enemy21.png")
print(enemy_image)
#enemy1 = pygame.image.load("enemy.png")
enemy_x = width - enemy_image.get_width()  # Set the initial X-coordinate of the new enemy spaceship to align with the right edge of the screen
enemy_y = random.randint(0, height - 60 - enemy_image.get_height())  # Generate a random Y-coordinate for the new enemy spaceship
enemies = []  # List to store enemy objects
enemy_spawn_timer = 0  # Timer to control enemy spawning

bullet_image = pygame.image.load('missile1.png')
bullets = []
bullet_x = ufo_x + ufo_image.get_width()  # Start bullet from the spaceship's x position
bullet_y = ufo_y + ufo_image.get_height() // 2 - bullet_image.get_height() // 2  # Center bullet vertically
bullet_speed = 15
bullet_state = "ready"  # Indicates the state of the bullet, ready to be fired
running = True




def fire_bullet():
    global bullet_state, bullet_x, bullet_y
    bullet_state = "fire"  # Set the state of the bullet to fire
    bullet_x = ufo_x + ufo_image.get_width()  # Start bullet from the spaceship's x position
    bullet_y = ufo_y + ufo_image.get_height() // 2 - bullet_image.get_height() // 2  # Center bullet vertically

#enemy_x,enemy_y,bullet_x,bullet_y):
def isColusion(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2) + (math.pow(enemyY-bulletY,2)))
    if distance < 150:    # 147
        return True
    else:
        return False

while running:
    for event in pygame.event.get():       
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_t:
                running = False
            elif event.key == K_q:
                ufo_image = ship_1_img
            elif event.key == K_w:
                ufo_image = ship_2_img
            elif event.key == K_e:
                ufo_image = ship_3_img
            
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if bullet_state == 'ready':
                        fire_bullet()
        



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


    # Bullet movement

    background_x -= 1
    if background_x <= -background_image.get_width():
        background_x = 0

    # Draw two instances of the background image side by side
    screen.blit(background_image, (background_x, 0))
    screen.blit(background_image, (background_x + background_image.get_width(), 0))

    # creating multipe enemys
    enemy_spawn_timer += clock.get_rawtime()
    if enemy_spawn_timer >= 500:
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

    if bullet_state == "fire":
        bullet_x += bullet_speed  # Move the bullet forward
        screen.blit(bullet_image, (bullet_x, bullet_y))  # Draw the bullet

        if bullet_x > width:  # If the bullet goes off-screen, reset its state
            bullet_state = "ready"
    
    collusion = isColusion(enemy_x,enemy_y, bullet_x, bullet_y)
    if collusion:
        bullet_y = ufo_y + ufo_image.get_height() // 2 - bullet_image.get_height() // 2
        bullet_state = "ready"
        score += 1
        print(score)
        enemy_x = 10000
        enemy_y = 10000



    # Building the enemy and make them appear in the ground 
#    screen.blit(enemy1, (en_1 , en_2)) 
    
    screen.blit(score_img, (800 ,0))
    screen.blit(text, (815, 18))
    screen.blit(ship_img, (0,0))
    screen.blit(ship_1_img, (0,0))
    screen.blit(ship_2_img, (100,0))
    screen.blit(ship_3_img, (200,0))
    screen.blit(ufo_image, (ufo_x , ufo_y) )
#    screen.blit(ufo_image, (ufo_x, width // 2 - ufo_image.get_width() // 2))
    pygame.display.flip()
    clock.tick(60)