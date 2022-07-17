#! python3

import pygame, sys

pygame.init()

# Define screen dimensions and frames per second.
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('Diamond')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

# Load/import sprites and background images.
background_surf = pygame.image.load('images/background.png').convert()
buildings_surf = pygame.image.load('images/buildings.png').convert()
death_surf = pygame.image.load('images/death.png').convert_alpha()
death_rect = death_surf.get_rect(midbottom = (900, 450))
player_surf = pygame.image.load('images/player.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (350, 475))
player_walk1_surf = pygame.image.load('images/player_walk1.png').convert_alpha()
player_walk1_rect = player_walk1_surf.get_rect(midbottom = (350, 475))
cat_surf = pygame.image.load('images/cat.png').convert_alpha()
cat_rect = cat_surf.get_rect(midbottom = (200, 500))
airplane_surf = pygame.image.load('images/airplane.png').convert_alpha()
airplane_x_pos = 100
player_x_pos = 0

# Gravity
player_gravity = 0
cat_gravity = 0


# Load/import music and sound effects.
music = pygame.mixer.music.load('audio/lorn_diamond.mp3')
pygame.mixer.music.play(-1)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # Check for key events.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 475:
                player_gravity = -20
                cat_gravity = -20
            
            if event.key == pygame.K_RIGHT:
                player_x_pos = 1

            if event.key == pygame.K_LEFT:
                player_x_pos -= 1
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player_x_pos = 0
            if event.key == pygame.K_LEFT:
                player_x_pos = 0


    # Display surfaces to the screen.
    # x axis is left to right, y axis is up and down.
    screen.blit(background_surf,(0,0))
    screen.blit(buildings_surf,(700, 102))
    
    death_rect.x -= 4
    if death_rect.right == 200:
        death_rect.left = 900
    screen.blit(death_surf, death_rect)
    
    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 475:
        player_rect.bottom = 475
    screen.blit(player_surf, player_rect)

    player_rect.x += player_x_pos
    screen.blit(player_surf, player_rect)
    
    cat_rect.x += player_x_pos
    screen.blit(cat_surf, cat_rect)

    
    cat_gravity += 0.85
    cat_rect.y += cat_gravity
    if cat_rect.bottom >= 500:
        cat_rect.bottom = 500
    screen.blit(cat_surf, cat_rect)
    
    screen.blit(airplane_surf, (airplane_x_pos, 75))
    airplane_x_pos += 3
    if airplane_x_pos > 1000:
        airplane_x_pos = 100
    
    
    
    pygame.display.update()
    clock.tick(60)
    
