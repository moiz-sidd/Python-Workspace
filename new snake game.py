import pygame, sys, time, random

# Initialize Pygame
check_errors = pygame.init()
if check_errors[1] > 0:
    print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('[+] Game successfully initialised')

# Window size
frame_size_x = 720
frame_size_y = 480

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

# Button variables
button_font = pygame.font.SysFont('times new roman', 20)
button_color = pygame.Color(50, 50, 50)
button_hover_color = pygame.Color(70, 70, 70)
button_text_color = white
button_width = 200
button_height = 50

# Define buttons
easy_button = pygame.Rect((frame_size_x - button_width) // 2, frame_size_y // 2 - 100, button_width, button_height)
medium_button = pygame.Rect((frame_size_x - button_width) // 2, frame_size_y // 2 - 25, button_width, button_height)
hard_button = pygame.Rect((frame_size_x - button_width) // 2, frame_size_y // 2 + 50, button_width, button_height)
harder_button = pygame.Rect((frame_size_x - button_width) // 2, frame_size_y // 2 + 125, button_width, button_height)
impossible_button = pygame.Rect((frame_size_x - button_width) // 2, frame_size_y // 2 + 200, button_width, button_height)

pause_button = pygame.Rect(frame_size_x - button_width - 20, 10, button_width, button_height)
restart_button = pygame.Rect((frame_size_x - button_width) // 2, (frame_size_y // 2) + 50, button_width, button_height)

# Game variables
difficulty = None
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, (frame_size_x // 10)) * 10, random.randrange(1, (frame_size_y // 10)) * 10]
food_spawn = True
direction = 'RIGHT'
change_to = direction
score = 0
paused = False
game_over_flag = False
game_started = False

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

# Show score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x / 10, 15)
    else:
        score_rect.midtop = (frame_size_x / 2, frame_size_y / 1.25)
    game_window.blit(score_surface, score_rect)

# Game over
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

# Pause game
def pause_game():
    global paused
    paused = True
    my_font = pygame.font.SysFont('times new roman', 90)
    pause_surface = my_font.render('PAUSED', True, blue)
    pause_rect = pause_surface.get_rect()
    pause_rect.midtop = (frame_size_x / 2, frame_size_y / 4)
    game_window.blit(pause_surface, pause_rect)
    pygame.display.flip()

# Unpause game
def unpause_game():
    global paused
    paused = False

# Restart game
def restart_game():
    global snake_pos, snake_body, food_pos, food_spawn, direction, change_to, score, paused, game_over_flag, difficulty, game_started
    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    food_pos = [random.randrange(1, (frame_size_x // 10)) * 10, random.randrange(1, (frame_size_y // 10)) * 10]
    food_spawn = True
    direction = 'RIGHT'
    change_to = direction
    score = 0
    paused = False
    game_over_flag = False
    game_started = False
    difficulty = None

# Main menu
def main_menu():
    game_window.fill(black)
    draw_button(easy_button, "Easy")
    draw_button(medium_button, "Medium")
    draw_button(hard_button, "Hard")
    draw_button(harder_button, "Harder")
    draw_button(impossible_button, "Impossible")
    pygame.display.update()

# Main logic
while True:
    if not game_started:
        main_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if easy_button.collidepoint(mouse_pos):
                    difficulty = 10
                    game_started = True
                elif medium_button.collidepoint(mouse_pos):
                    difficulty = 25
                    game_started = True
                elif hard_button.collidepoint(mouse_pos):
                    difficulty = 40
                    game_started = True
                elif harder_button.collidepoint(mouse_pos):
                    difficulty = 60
                    game_started = True
                elif impossible_button.collidepoint(mouse_pos):
                    difficulty = 120
                    game_started = True
    else:
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
            food_spawn
