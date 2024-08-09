import pygame
import random

# Initialize Pygame
pygame.init()

# Game settings
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
GROUND_HEIGHT = 100
PIPE_WIDTH = 60
PIPE_HEIGHT = 500
PIPE_GAP = 150
BIRD_WIDTH = 30
BIRD_HEIGHT = 30

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Bird class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0
        self.gravity = 0.5

    def flap(self):
        self.velocity = -8

    def move(self):
        self.velocity += self.gravity
        self.y += self.velocity

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, BIRD_WIDTH, BIRD_HEIGHT))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, BIRD_WIDTH, BIRD_HEIGHT)

# Pipe class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(50, SCREEN_HEIGHT - PIPE_GAP - GROUND_HEIGHT)
        self.passed = False

    def move(self):
        self.x -= 5

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, 0, PIPE_WIDTH, self.height))
        pygame.draw.rect(screen, GREEN, (self.x, self.height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT))

    def get_top_rect(self):
        return pygame.Rect(self.x, 0, PIPE_WIDTH, self.height)

    def get_bottom_rect(self):
        return pygame.Rect(self.x, self.height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT)

# Button class
class Button:
    def __init__(self, text, x, y, width, height, color, hover_color):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.SysFont(None, 35)
        text_surf = font.render(self.text, True, WHITE)
        screen.blit(text_surf, (self.rect.x + (self.rect.width - text_surf.get_width()) // 2, self.rect.y + (self.rect.height - text_surf.get_height()) // 2))

    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        return self.rect.collidepoint(mouse_pos) and mouse_pressed[0]

# Game loop
def game_loop():
    bird = Bird()
    pipes = [Pipe(SCREEN_WIDTH + i * (PIPE_WIDTH + 200)) for i in range(3)]
    clock = pygame.time.Clock()
    score = 0
    running = True
    game_over = False

    restart_button = Button("Restart", 150, 300, 100, 50, BLUE, RED)

    while running:
        screen.fill(BLACK)

        if not game_over:
            bird.move()
            bird.draw()

            for pipe in pipes:
                pipe.move()
                pipe.draw()

                if pipe.x + PIPE_WIDTH < 0:
                    pipes.remove(pipe)
                    pipes.append(Pipe(SCREEN_WIDTH + 200))

                if bird.get_rect().colliderect(pipe.get_top_rect()) or bird.get_rect().colliderect(pipe.get_bottom_rect()):
                    game_over = True

                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    score += 1

            # Check if bird hits the ground
            if bird.y + BIRD_HEIGHT > SCREEN_HEIGHT - GROUND_HEIGHT or bird.y < 0:
                game_over = True

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    bird.flap()

        if game_over:
            restart_button.draw(screen)
            if restart_button.is_clicked():
                game_loop()  # Restart the game

        # Display score
        font = pygame.font.SysFont(None, 35)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(30)

    pygame.quit()

# Run the game
game_loop()
