import pygame
from pygame.locals import *
import random
import math

# refactored modules.
from assets import background_assets
from player import Player
from obstacle import Obstacle
from window import game
from config import WINDOW_HEIGHT, WINDOW_WIDTH, FPS
from game_variables import score, speed
from background_manager import background_manager

# set the image for the sky
sky = pygame.image.load('images/bg/sky.png').convert_alpha()
num_bg_tiles = math.ceil(WINDOW_WIDTH / sky.get_width()) + 1

# for the parallax effect, determine how much each layer will scroll
parallax = []
for x in range(len(background_assets(pygame))):
    parallax.append(0)
    
# create the player
player = Player()

# create the obstacle
obstacles_group = pygame.sprite.Group()
obstacle = Obstacle()
obstacles_group.add(obstacle)

# load the heart images for representing health
heart_sprites = []
heart_sprite_index = 0
for i in range(8):
    heart_sprite = pygame.image.load(f'images/heart/heart{i}.png').convert_alpha()
    scale = 30 / heart_sprite.get_height()
    new_width = heart_sprite.get_width() * scale
    new_height = heart_sprite.get_height() * scale
    heart_sprite = pygame.transform.scale(heart_sprite, (new_width, new_height))
    heart_sprites.append(heart_sprite)


# game loop
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
quit = False
while not quit:
    
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            quit = True
            
        # press SPACE to jump
        if event.type == KEYDOWN and event.key == K_SPACE:
            player.jump()
        # press SPACE to jump
        if event.type == KEYDOWN and event.key == K_w:
            player.jump()
        # press key 'D' to walk forward
        if event.type == KEYDOWN and event.key == K_d:
            player.set_action('walk_forward')
        # press key 'A' to walk forward
        if event.type == KEYDOWN and event.key == K_a:
            player.set_action('walk_backward')
            
    # loads the background
    background_manager(
        game,     # pygame display
        parallax, # array of assets in the background
        background_assets(pygame),      # images o
        sky
    )
            
    # draw the player
    player.draw()
    
    # update the sprite and position of the player
    player.update()
    
    # draw the obstacle
    obstacle.draw()
    
    # update the position of the obstacle
    obstacle.update()
    
    #reset the obstacle
    if obstacle.x <= 0:
        obstacle.reset()
        speed += 1

    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time) // 1000  # Convert to seconds
    score = elapsed_time
    
    # check if player collides with the obstacle
    if pygame.sprite.spritecollide(player, obstacles_group, True, pygame.sprite.collide_mask):
        player.health -= 1
        player.invincibility_frame = 30
        
        # remove obstacle and replace with a new one
        obstacles_group.remove(obstacle)
        obstacle = Obstacle()
        obstacles_group.add(obstacle)
        
    # display a heart per remaining health
    for life in range(player.health):
        heart_sprite = heart_sprites[int(heart_sprite_index)]
        x_pos = 10 + life * (heart_sprite.get_width() + 10)
        y_pos = 10
        game.blit(heart_sprite, (x_pos, y_pos))
        
    # increment the index for the next heart sprite
    # use 0.1 to make the sprite change after 10 frames
    heart_sprite_index += 0.1
    
    # set index back to 0 after the last heart sprite is drawn
    if heart_sprite_index >= len(heart_sprites):
        heart_sprite_index = 0
        
    # display the score
    black = (0, 0, 0)
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render(f'Score: {score}', True, black)
    text_rect = text.get_rect()
    text_rect.center = (WINDOW_WIDTH - 50, 20)
    game.blit(text, text_rect)
            
    pygame.display.update()
    
    # gameover
    gameover = player.health == 0
    while gameover and not quit:
        
        # display game over message
        red = (255, 0, 0)
        pygame.draw.rect(game, red, (0, 50, WINDOW_WIDTH, 100))
        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render('Game over. Play again? (Enter Y or N)', True, black)
        text_rect = text.get_rect()
        text_rect.center = (WINDOW_WIDTH / 2, 100)
        game.blit(text, text_rect)
        
        for event in pygame.event.get():
            
            if event.type == QUIT:
                quit = True
                
            # get the player's input (Y or N)
            if event.type == KEYDOWN:
                if event.key == K_y:
                    # reset the game
                    gameover = False
                    speed = 3
                    score = 0
                    player = Player()
                    obstacle = Obstacle()
                    obstacles_group.empty()
                    obstacles_group.add(obstacle)
                elif event.key == K_n:
                    quit = True
                    
        pygame.display.update()
    
pygame.quit()