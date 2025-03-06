import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Simple Game")

FIGHTER_STEP = 0.5
BALL_STEP = 0.3
figther_image = pygame.image.load('images/fighter.png')
figther_width, figther_height = figther_image.get_size()
figther_x, fighter_y = screen_width / 2 - figther_width / 2, screen_height - figther_height
screen_fill_color = pygame.Color(32,52, 71)
fighter_is_moving_left, fighter_is_moving_right = False, False

ball_image = pygame.image.load('images/ball.png')
ball_width, ball_height = ball_image.get_size()
ball_x, ball_y = 0, 0
ball_was_fired = False


while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and figther_x >= FIGHTER_STEP:
                fighter_is_moving_left = True
            if event.key == pygame.K_RIGHT and figther_x <= screen_width - figther_width- FIGHTER_STEP:
                fighter_is_moving_right = True
            if event.key == pygame.K_SPACE:
                ball_was_fired = True
                ball_x = figther_x + figther_width / 2 - ball_width / 2
                ball_y = fighter_y - ball_height

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
               fighter_is_moving_left = False
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = False


    if fighter_is_moving_left and figther_x >= FIGHTER_STEP:
        figther_x -= FIGHTER_STEP
    if fighter_is_moving_right and figther_x <= screen_width - figther_width - FIGHTER_STEP:
        figther_x += FIGHTER_STEP

    if ball_was_fired and ball_y + ball_height < 0:
        ball_was_fired = False

    if ball_was_fired:
        ball_y -= BALL_STEP
    screen.fill(screen_fill_color)
    screen.blit(figther_image, (figther_x, fighter_y))

    if ball_was_fired:
        screen.blit(ball_image, (ball_x, ball_y))

    pygame.display.update()