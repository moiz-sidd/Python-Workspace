import pygame, sys, time, random

# Difficulty settings
# Easy      ->  10
# Medium    ->  25
# Hard      ->  40
# Harder    ->  60
# Impossible->  120
difficulty = 10

# Window size
frame_size_x = 720
frame_size_y = 480

# Checks for errors encountered
check_errors = pygame.init()
# pygame.init() example output -> (6, 0)
# second number in tuple gives number of errors
if check_errors[1] > 0:
    print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('[+] Game successfully initialised')

# Initialise game window
pygame.display.set_caption('Snake Eater')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# FPS (frames per second) controller
fps_controller = pygame.time.Clock()

# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

food_pos = [random.randrange(1, (frame_size_x // 10)) * 10, random.randrange(1, (frame_size_y // 10)) * 10]
food_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0
paused = False
game_over_flag = False

# Button variables
button_font = pygame.font.SysFont('times new roman', 20)
button_color = pygame.Color(50, 50, 50)
button_hover_color = pygame.Color(70, 70, 70)
button_text_color = white
button_width = 100
button_height = 50

# Define buttons
pause_button = pygame.Rect(frame_size_x - button_width - 20, 10, button_width, button_height)
restart_button = pygame.Rect((frame_size_x - button_width) // 2, (frame_size_y // 2) + 50, button_width, button_height)

# Game Over
def game_over():
    global game_over_flag
    game_over_flag = True
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU DIED', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x / 2, frame_size_y / 4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'times', 20)
    pygame.display.flip()

# Score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x / 10, 15)
    else:
        score_rect.midtop = (frame_size_x / 2, frame_size_y / 1.25)
    game_window.blit(score_surface, score_rect)

# Pause
def pause_game():
    global paused
    paused = True
    my_font = pygame.font.SysFont('times new roman', 90)
    pause_surface = my_font.render('PAUSED', True, blue)
    pause_rect = pause_surface.get_rect()
    pause_rect.midtop = (frame_size_x / 2, frame_size_y / 4)
    game_window.blit(pause_surface, pause_rect)
    pygame.display.flip()

# Unpause
def unpause_game():
    global paused
    paused = False

# Restart
def restart_game():
    global snake_pos, snake_body, food_pos, food_spawn, direction, change_to, score, paused, game_over_flag
    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    food_pos = [random.randrange(1, (frame_size_x // 10)) * 10, random.randrange(1, (frame_size_y // 10)) * 10]
    food_spawn = True
    direction = 'RIGHT'
    change_to = direction
    score = 0
    paused = False
    game_over_flag = False

# Draw buttons
def draw_button(button_rect, text):
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        color = button_hover_color
    else:
        color = button_color
    pygame.draw.rect(game_window, color, button_rect)
    text_surface = button_font.render(text, True, button_text_color)
    text_rect = text_surface.get_rect(center=button_rect.center)
    game_window.blit(text_surface, text_rect)

# Main logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            if event.key == pygame.K_p:
                if paused:
                    unpause_game()
                else:
                    pause_game()
            if event.key == pygame.K_r:
                restart_game()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if pause_button.collidepoint(mouse_pos) and not game_over_flag:
                if paused:
                    unpause_game()
                else:
                    pause_game()
            if restart_button.collidepoint(mouse_pos) and game_over_flag:
                restart_game()

    if paused:
        draw_button(pause_button, "Unpause")
        pygame.display.update()
        continue

    if game_over_flag:
        draw_button(restart_button, "Restart")
        pygame.display.update()
        continue

    # Making sure the snake cannot move in the opposite direction instantaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (frame_size_x // 10)) * 10, random.randrange(1, (frame_size_y // 10)) * 10]
    food_spawn = True

    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] > frame_size_x - 10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > frame_size_y - 10:
        game_over()
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    show_score(1, white, 'consolas', 20)
    
    # Draw pause button on the game screen only if the game is not over
    if not game_over_flag:
        draw_button(pause_button, "Pause" if not paused else "Unpause")
    
    pygame.display.update()
    fps_controller.tick(difficulty)
