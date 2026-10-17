import pygame
import random
import math

WIDTH, HEIGHT = 800, 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Arial", 30)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Anime Fruit Slasher")
clock = pygame.time.Clock()

FRUIT_TYPES = {
    "Watermelon": ((46, 139, 87), 40),
    "Orange": ((255, 140, 0), 30),
    "Apple": ((220, 20, 60), 28),
    "Banana": ((255, 223, 0), 25),
    "Coconut": ((210, 105, 30), 35)
}

class Fruit:
    def __init__(self):
        self.name = random.choice(list(FRUIT_TYPES.keys()))
        self.color, self.radius = FRUIT_TYPES[self.name]
        self.x = random.randint(100, WIDTH - 100)
        self.y = HEIGHT + self.radius
        self.vx = random.uniform(-3, 3)
        self.vy = random.uniform(-16, -12)
        self.gravity = 0.3
        self.sliced = False

    def update(self):
        self.vy += self.gravity
        self.x += self.vx
        self.y += self.vy

    def draw(self, surface):
        if not self.sliced:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)
            pygame.draw.circle(surface, WHITE, (int(self.x - self.radius / 3), int(self.y - self.radius / 3)), 4)


class Particle:
    def __init__(self, x, y, color):
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 7)
        self.x = x
        self.y = y
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.gravity = 0.2
        self.life = 255
        self.color = color
        self.radius = 4

    def update(self):
        self.vy += self.gravity
        self.x += self.vx
        self.y += self.vy
        self.life -= 8

    def draw(self, surface):
        if self.life > 0:
            s = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(s, (*self.color, self.life), (self.radius, self.radius), self.radius)
            surface.blit(s, (int(self.x - self.radius), int(self.y - self.radius)))


def check_slice(f_x, f_y, f_r, p1, p2):
    if p1 == p2:
        dist = math.hypot(f_x - p1[0], f_y - p1[1])
        return dist <= f_r
        
    ax, ay = p1
    bx, by = p2
    lab = math.hypot(bx - ax, by - ay)
    dx = (bx - ax) / lab
    dy = (by - ay) / lab
    t = dx * (f_x - ax) + dy * (f_y - ay)
    t = max(0, min(lab, t))
    closest_x = ax + t * dx
    closest_y = ay + t * dy
    dist = math.hypot(f_x - closest_x, f_y - closest_y)
    return dist <= f_r


def main():
    running = True
    fruits = []
    particles = []
    mouse_trail = []
    score = 0
    lives = 3

    while running:
        screen.fill(BLACK)
        current_mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        if pygame.mouse.get_pressed()[0]:
            mouse_trail.append(current_mouse_pos)
            if len(mouse_trail) > 10:
                mouse_trail.pop(0)
        else:
            mouse_trail.clear()
            
        if random.random() < 0.02:
            fruits.append(Fruit())
            
        for fruit in fruits[:]:
            fruit.update()
            
            if len(mouse_trail) >= 2 and not fruit.sliced:
                if check_slice(fruit.x, fruit.y, fruit.radius, mouse_trail[-2], mouse_trail[-1]):
                    fruit.sliced = True
                    score += 10
                    for _ in range(20):
                        particles.append(Particle(fruit.x, fruit.y, fruit.color))
                        
            if fruit.y > HEIGHT + fruit.radius + 50:
                if not fruit.sliced:
                    lives -= 1
                fruits.remove(fruit)

        for particle in particles[:]:
            particle.update()
            if particle.life <= 0:
                particles.remove(particle)

        for particle in particles:
            particle.draw(screen)
            
        for fruit in fruits:
            fruit.draw(screen)
            
        if len(mouse_trail) >= 2:
            pygame.draw.lines(screen, WHITE, False, mouse_trail, 4)
            
        score_text = font.render(f"SCORE: {score}", True, WHITE)
        lives_text = font.render(f"LIVES: {'X ' * lives}", True, (220, 20, 60))
        screen.blit(score_text, (20, 20))
        screen.blit(lives_text, (WIDTH - 180, 20))
        
        if lives <= 0:
            game_over_text = font.render("GAME OVER", True, (220, 20, 60))
            screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2))
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False
            
        pygame.display.flip()
        clock.tick(FPS)
        
    pygame.quit()

if __name__ == "__main__":
    main()