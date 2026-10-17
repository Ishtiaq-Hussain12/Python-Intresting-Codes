import pygame
import random

pygame.init()

W, H = 1000, 1000
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Lightning Storm")
clock = pygame.time.Clock()

def lightning():
    x = random.randint(100, W - 100)
    points = [(x, 0)]
    
    while points[-1][1] < H:
        x += random.randint(-40, 40)
        y = points[-1][1] + random.randint(10, 30)
        points.append((x, y))
        
    return points

bolt = lightning()
flash = 0

running = True
while running:
    screen.fill((0, 0, 0))
    
    # Random lightning strike
    if random.randint(1, 50) == 1:
        bolt = lightning()
        flash = 255
        
    # Stronger blue flash effect
    if flash > 0:
        overlay = pygame.Surface((W, H))
        overlay.fill((100, 200, 255))
        overlay.set_alpha(flash)
        screen.blit(overlay, (0, 0))
        flash -= 12
        
    # Lightning glow layers
    pygame.draw.lines(screen, (0, 100, 255), False, bolt, 12)
    pygame.draw.lines(screen, (50, 180, 255), False, bolt, 8)
    pygame.draw.lines(screen, (150, 230, 255), False, bolt, 4)
    pygame.draw.lines(screen, (230, 250, 255), False, bolt, 2)
    
    pygame.display.flip()
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()