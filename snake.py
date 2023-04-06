import random
import pygame as pygame
pygame.init()
clock = pygame.time.Clock()
width = 500
height = 500
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')
snake_block_size = 10
snake_speed = 20
font_style = pygame.font.SysFont(None, 30)


def snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, (0, 255, 0), [
                         x[0], x[1], snake_block_size, snake_block_size])


def food(x, y):
    pygame.draw.rect(game_display, (156, 255, 85), [
                     x, y, snake_block_size, snake_block_size])


def message(msg, color):
    text = font_style.render(msg, True, color)
    game_display.blit(text, [0, 0])


def game_loop():
    global snake_speed
    game_exit = False
    game_over = False
    score = 0
    snake_list = []
    snake_length = 1

    x = width/2
    y = height/2

    x_change = 0
    y_change = 0

    foodx = round(random.randrange(0, width - snake_block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block_size) / 10.0) * 10.0
    while not game_exit:

        while game_over == True:
            # Game over screen,
            game_over = False
            game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block_size
                    x_change = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_over = True

        x += x_change
        y += y_change

        game_display.fill((255, 255, 255))

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # for segment in snake_list[:-1]:
        #     if segment == snake_head:
        #         game_over = True
        food(foodx, foody)
        snake(snake_block_size, snake_list)

        pygame.display.update()
        if x == foodx and y == foody:
            foodx = round(random.randrange(
                0, width - snake_block_size) / 10.0) * 10.0
            foody = round(random.randrange(
                0, height - snake_block_size) / 10.0) * 10.0
            snake_length += 1
            score += 1
            if score % 10 == 0:
                snake_speed += 1
        message("Score: " + str(score), (0, 50, 255))
        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
