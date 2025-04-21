import pygame
import random
import time

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 30)

# Chim
bird = pygame.Rect(100, 300, 30, 30)
gravity = 0
jump = -10

# Ống
pipes = []
PIPE_WIDTH = 60
PIPE_GAP = 150
pipe_speed = 3

# Điểm
score = 0

# Hàm tạo ống mới
def new_pipe():
    height = random.randint(100, 400)
    top = pygame.Rect(WIDTH, 0, PIPE_WIDTH, height)
    bottom = pygame.Rect(WIDTH, height + PIPE_GAP, PIPE_WIDTH, HEIGHT)
    return top, bottom

pipes.extend(new_pipe())

# Game loop
running = True
while running:
    screen.fill((135, 206, 235))  # Màu trời

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            gravity = jump

    # Chim rơi
    gravity += 1
    bird.y += gravity

    # Vẽ chim
    pygame.draw.ellipse(screen, (255, 255, 0), bird)

    # Di chuyển và vẽ ống
    for pipe in pipes:
        pipe.x -= pipe_speed
        pygame.draw.rect(screen, (0, 255, 0), pipe)

    # Xoá ống cũ, thêm ống mới
    if pipes[0].x + PIPE_WIDTH < 0:
        pipes = pipes[2:]
        pipes.extend(new_pipe())
        score += 1

    # Va chạm
    for pipe in pipes:
        if bird.colliderect(pipe):
            screen.blit(font.render("Game Over!", True, (255, 0, 0)), (100, 250))
            time.sleep(3)
            running = False

    if bird.y > HEIGHT or bird.y < 0:
        screen.blit(font.render("Game Over!", True, (255, 0, 0)), (100, 250))
        time.sleep(3)
        running = False

    # Vẽ điểm
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
