###file for pong

import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720)) 
clock = pygame.time.Clock()
running = True
x = 640
y = 360
vel_x = 5
vel_y = 5
color = (255, 255, 255)
logo_original = pygame.image.load("dvdlogo.png")
logo_original = pygame.transform.scale(logo_original, (80, 40))
logo_width = logo_original.get_width()
logo_height = logo_original.get_height()
paddle1_y = 310
paddle2_y = 310
score = 0
highscore = 0
font = pygame.font.SysFont(None, 48)
game_over_img = pygame.image.load("gameover.png")
game_over_img = pygame.transform.scale(game_over_img, (640, 360))
title_font = pygame.font.SysFont(None, 120)
button_font = pygame.font.SysFont(None, 60)

menu_x = 640
menu_y = 360
menu_vel_x = 4
menu_vel_y = 4
menu_color = (150, 150, 255)

in_menu = True
while in_menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.collidepoint(event.pos):
                in_menu = False

    screen.fill("black")
    title_text = title_font.render("DVD PONG", True, "white")
    screen.blit(title_text, (440, 200))
    play_button = pygame.Rect(540, 350, 180, 60)
    pygame.draw.rect(screen, "white", play_button)
    play_text = button_font.render("PLAY", True, "black")
    screen.blit(play_text, (580, 365))
    menu_logo = logo_original.copy()
    menu_logo.fill(menu_color, special_flags=pygame.BLEND_RGB_MULT)
    screen.blit(menu_logo, (menu_x, menu_y))
    menu_x += menu_vel_x
    menu_y += menu_vel_y
    if menu_x <= 0 or menu_x >= 1280 - logo_width:
        menu_vel_x = -menu_vel_x
        menu_color = (random.randint(150,255), random.randint(150,255), random.randint(150,255))
    if menu_y <= 0 or menu_y >= 720 - logo_height:
        menu_vel_y = -menu_vel_y
        menu_color = (random.randint(150,255), random.randint(150,255), random.randint(150,255))
    pygame.display.flip()
    clock.tick(60)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    logo = logo_original.copy()
    logo.fill(color, special_flags=pygame.BLEND_RGB_MULT)
    screen.blit(logo, (x, y))
    x += vel_x
    y += vel_y
    if x >= 1280 - logo_width:
        vel_x = -vel_x
        color = (random.randint(150,255), random.randint(150,255), random.randint(150,255))
    if x <= 0:
        if score > highscore:
            highscore = score
        running = False
    if y <= 0 or y >= 720 - logo_height:
        vel_y = -vel_y
        color = (random.randint(150,255), random.randint(150,255), random.randint(150,255))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= 5
    if keys[pygame.K_s] and paddle1_y < 620:
        paddle1_y += 5
    
    if paddle2_y + 50 < y:
        paddle2_y += 5
    elif paddle2_y + 50 > y:
        paddle2_y -= 5

    paddle1 = pygame.Rect(50, paddle1_y, 10, 100)
    paddle2 = pygame.Rect(1220, paddle2_y, 10, 100)
    pygame.draw.rect(screen, "white", paddle1)
    pygame.draw.rect(screen, "white", paddle2)
    if paddle1.colliderect(pygame.Rect(x, y, logo_width, logo_height)):
        vel_x = -vel_x
        color = (random.randint(150,255), random.randint(150,255), random.randint(150,255))
    if paddle2.colliderect(pygame.Rect(x, y, logo_width, logo_height)):
        vel_x = -(vel_x + (1 if vel_x > 0 else -1))
        score += 1
        color = (random.randint(150,255), random.randint(150,255), random.randint(150,255))
    pygame.display.flip()
    clock.tick(60)
screen.blit(game_over_img, (320, 50))
score_text = font.render(f"Score: {score}", True, "white")
high_text = font.render(f"High Score: {highscore}", True, "yellow")
screen.blit(score_text, (500, 450))
screen.blit(high_text, (500, 520))
pygame.display.flip()
pygame.time.wait(5000)

pygame.quit()