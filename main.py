import pygame
import random
import sys

width = 1000
height = 700

pygame.display.init()
display = pygame.display.set_mode((width,height))

pygame.display.set_caption("Snake Game")

icon = pygame.image.load('./img/logo.png')
pygame.display.set_icon(icon)

pygame.mixer.init()

eat_sound = pygame.mixer.Sound('./audio/eat.wav')
snake_sound = pygame.mixer.Sound('./audio/snake.wav')

clock = pygame.time.Clock()

square_size = 20

def apple_spawn():
    apple = [random.randrange(1,(width // square_size)) * square_size, random.randrange(1,(height // square_size)) * square_size]
    return apple


def main():
    snake_pos = [100,60]
    snake_body = [[100,60],[90,60],[80,60]]
    direction = 'RIGHT'
    apple_pos = apple_spawn()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Game Initialized :)")
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                snake_sound.play()
                if event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP': 
                    direction = 'DOWN'

        if direction == 'UP':
            snake_pos[1] -= square_size
        elif direction == 'DOWN':
            snake_pos[1] += square_size
        elif direction == 'LEFT':
            snake_pos[0] -= square_size
        elif direction == 'RIGHT':
            snake_pos[0] += square_size

        if snake_pos[0] < 0:
            snake_pos[0] = width - square_size
        elif snake_pos[0] > width - square_size:
            snake_pos[0] = 0
        elif snake_pos[1] < 0:
            snake_pos[1] = height - square_size
        elif snake_pos[1] > height - square_size:
            snake_pos[1] = 0

        snake_body.insert(0, list(snake_pos))
        if snake_pos == apple_pos:
            eat_sound.play()
            apple_pos = apple_spawn()
        else:
            snake_body.pop()

        display.fill((0,0,0))

        for snake_part in snake_body:
            pygame.draw.rect(display, (0, 255, 0, 1), pygame.Rect(snake_part[0], snake_part[1],square_size,square_size))

        pygame.draw.rect(display, (255,0,0,1), pygame.Rect(apple_pos[0], apple_pos[1], square_size, square_size))

        if snake_pos in snake_body[1:]:
            snake_pos = [100,60]
            snake_body = [[100,60],[90,60],[80,60]]
            direction = 'RIGHT'

        pygame.display.update()
        clock.tick(15)

main()
