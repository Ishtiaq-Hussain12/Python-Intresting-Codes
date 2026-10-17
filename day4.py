import pygame
import random
from datetime import datetime
pygame.init()

WIDTH, HEIGHT = 900,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Purple Digital Rain Clock")

font = pygame.font.SysFont("Consolas", 22, bold=True)
clock_font = pygame.font.SysFont("Consolas", 70, bold=True)

chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&"

columns = WIDTH // 20
drops = [random.randint(-20, 0) for _ in range(columns)]

clock = pygame.time.Clock()
running = True

while running:
    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.set_alpha(35)
    fade.fill((0, 0, 0))
    screen.blit(fade, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(columns):
        char = random.choice(chars)
        
        color = random.choice([
            (180, 0, 255),
            (200, 100, 255),
            (255, 0, 255),
            (220, 120, 255)
        ])

        text = font.render(char, True, color)
        
        x = i * 20
        y = drops[i] * 20

        glow = font.render(char, True, (60, 0, 100))
        screen.blit(glow, (x - 2, y))
        screen.blit(glow, (x + 2, y))
        screen.blit(glow, (x, y - 2))
        screen.blit(glow, (x, y + 2))

        screen.blit(text, (x, y))

        if y > HEIGHT and random.random() > 0.98:
            drops[i] = 0

        drops[i] += 1

    current_time = datetime.now().strftime("%H:%M:%S")

    for offset in range(18, 0, -3):
        glow = clock_font.render(current_time, True, (40, 0, 60))
        rect = glow.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(glow, (rect.x - offset, rect.y))
        screen.blit(glow, (rect.x + offset, rect.y))
        screen.blit(glow, (rect.x, rect.y - offset))
        screen.blit(glow, (rect.x, rect.y + offset))

    time_text = clock_font.render(
        current_time,
        True,
        (255, 180, 255)
    )

    rect = time_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(time_text, rect)

    pygame.display.flip()
    clock.tick(35)

pygame.quit()