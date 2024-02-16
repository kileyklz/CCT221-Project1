import pygame
import sys
import random
from score import Score
from levels import Level

pygame.init()

WIDTH, HEIGHT = 800, 600
PADDLE_SPEED = 7
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 15

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

clock = pygame.time.Clock()

class Paddle(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)

    def move(self, dy):
        self.y += dy
        if self.top < 0:
            self.top = 0
        if self.bottom > HEIGHT:
            self.bottom = HEIGHT

class Ball(pygame.Rect):
    def __init__(self, x, y, vx, vy):
        super().__init__(x, y, BALL_SIZE, BALL_SIZE)
        self.vx, self.vy = vx, vy

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def check_collision(self):
        if self.top <= 0 or self.bottom >= HEIGHT:
            self.vy = -self.vy

        if pygame.Rect.colliderect(self, player1) or pygame.Rect.colliderect(self, player2):
            self.vx = -self.vx

player1 = Paddle(20, HEIGHT // 2 - PADDLE_HEIGHT // 2)
player2 = Paddle(WIDTH - 20 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2)
ball = Ball(random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100), random.choice([-3, 3]), random.choice([-3, 3]))
score = Score()

level = Level(6)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1.move(-PADDLE_SPEED)
    if keys[pygame.K_s]:
        player1.move(PADDLE_SPEED)
    if keys[pygame.K_UP]:
        player2.move(-PADDLE_SPEED)
    if keys[pygame.K_DOWN]:
        player2.move(PADDLE_SPEED)

    ball.move()
    ball.check_collision()

    # Check for scoring
    if ball.left <= 0 or ball.right >= WIDTH:
        ball.vx = -ball.vx

    # Check if the ball goes out of bounds
    if ball.left <= 0:
        level.increase_level() 
        ball = Ball(random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100), level.get_ball_speed(), level.get_ball_speed())  
        score.updatePlayer2() 
    elif ball.right >= WIDTH:
        level.increase_level()  
        ball = Ball(random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100), -level.get_ball_speed(), level.get_ball_speed())  
        score.updatePlayer1()

    # Check for game over
    if level.current_level > 5:
        if score.score_player1 > score.score_player2:
            winner = "Player 1"
        elif score.score_player1 < score.score_player2:
            winner = "Player 2"
        else:
            winner = "It's a tie"
        
        print(f"Game Over! {winner} wins!")
        score.score_player1 = 0
        score.score_player2 = 0
        level.reset_level()
        ball.vx, ball.vy = level.get_ball_speed(), level.get_ball_speed()

    screen.fill(BLACK)

    font = pygame.font.Font(None, 36)
    level_text = font.render(level.get_level_text(), True, WHITE)
    screen.blit(level_text, (WIDTH // 2 - level_text.get_width() // 2, 10))


    pygame.draw.rect(screen, (255, 255, 255), player1)
    pygame.draw.rect(screen, (255, 255, 255), player2)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    score.draw(screen, WIDTH, HEIGHT)

    pygame.display.flip()
    clock.tick(60)
