import pygame
import random

pygame.init()

# Цвета
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Параметры дисплея
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game with Improved Autoplay')

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 1000

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def is_collision_with_self(snake_List, x, y):
    for segment in snake_List:
        if segment[0] == x and segment[1] == y:
            return True
    return False

def get_next_move(x, y, foodx, foody, snake_List):
    directions = [
        (snake_block, 0),  # RIGHT
        (-snake_block, 0), # LEFT
        (0, -snake_block), # UP
        (0, snake_block)   # DOWN
    ]

    safe_moves = []
    for move in directions:
        new_x = x + move[0]
        new_y = y + move[1]

        # Проход змейки через стенки
        if new_x >= dis_width:
            new_x = 0
        elif new_x < 0:
            new_x = dis_width - snake_block
        if new_y >= dis_height:
            new_y = 0
        elif new_y < 0:
            new_y = dis_height - snake_block

        if not is_collision_with_self(snake_List, new_x, new_y):
            safe_moves.append((new_x, new_y, move))

    best_move = None
    min_distance = float('inf')
    for new_x, new_y, move in safe_moves:
        distance = abs(new_x - foodx) + abs(new_y - foody)
        if distance < min_distance:
            min_distance = distance
            best_move = move

    return best_move

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    autoplay = True  # Включаем режим автопилота

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN and not autoplay:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if autoplay:
            next_move = get_next_move(x1, y1, foodx, foody, snake_List)
            if next_move:
                x1_change, y1_change = next_move

        # Проход змейки через стенки
        if x1 >= dis_width:
            x1 = 0
        elif x1 < 0:
            x1 = dis_width - snake_block
        if y1 >= dis_height:
            y1 = 0
        elif y1 < 0:
            y1 = dis_height - snake_block

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
