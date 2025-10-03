import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 800, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Динозавр у шляпі — пригинайся!")

# Кольори
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (200, 0, 0)

GRAVITY = 1

class Dino:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT - 90
        self.vel_y = 0
        self.is_jumping = False
        self.is_crouching = False
        self.normal_height = 60
        self.crouch_height = 30
        self.width = 40

    def draw(self):
        height = self.crouch_height if self.is_crouching else self.normal_height
        y_offset = (self.normal_height - height) if self.is_crouching else 0
        body_y = self.y + y_offset

        # Тіло
        pygame.draw.rect(WIN, GREEN, (self.x, body_y, self.width, height))

        # Хвіст
        pygame.draw.polygon(WIN, GREEN, [
            (self.x - 20, body_y + 20),
            (self.x, body_y + 30),
            (self.x, body_y + 40)
        ])

        if not self.is_crouching:
            # Голова
            head_x = self.x + 30
            head_y = body_y - 20
            pygame.draw.rect(WIN, GREEN, (head_x, head_y, 20, 20))

            # Шляпа
            pygame.draw.rect(WIN, BLACK, (head_x - 2, head_y - 5, 24, 5))
            pygame.draw.rect(WIN, BLACK, (head_x + 2, head_y - 20, 16, 15))

            # Окуляри
            pygame.draw.rect(WIN, BLACK, (head_x + 2, head_y + 5, 6, 6))   # ліва лінза
            pygame.draw.rect(WIN, BLACK, (head_x + 12, head_y + 5, 6, 6))  # права лінза
            pygame.draw.rect(WIN, BLACK, (head_x + 8, head_y + 7, 4, 2))   # місток

            # Шарфик
            pygame.draw.rect(WIN, RED, (self.x + 10, body_y + 5, 20, 5))    # поперек
            pygame.draw.rect(WIN, RED, (self.x + 20, body_y + 10, 5, 15))   # вниз

    def update(self):
        if self.is_jumping:
            self.vel_y += GRAVITY
            self.y += self.vel_y
            if self.y >= HEIGHT - 90:
                self.y = HEIGHT - 90
                self.vel_y = 0
                self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.vel_y = -18
            self.is_jumping = True

    def crouch(self, status):
        self.is_crouching = status

    def get_rect(self):
        height = self.crouch_height if self.is_crouching else self.normal_height
        y_offset = (self.normal_height - height) if self.is_crouching else 0
        return pygame.Rect(self.x, self.y + y_offset, self.width, height)

class Obstacle:
    def __init__(self):
        self.type = random.choice(['high', 'low'])  # високий або низький блок
        self.width = 30
        self.speed = 6
        if self.type == 'high':
            self.height = random.randint(40, 70)
            self.y = HEIGHT - self.height - 30
        else:
            self.height = 30
            self.y = HEIGHT - self.height - 30

        self.x = WIDTH

    def draw(self):
        pygame.draw.rect(WIN, GRAY, (self.x, self.y, self.width, self.height))

    def update(self):
        self.x -= self.speed

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Bird:
    def __init__(self):
        self.width = 30
        self.height = 20
        self.x = WIDTH
        self.y = random.choice([130, 160, 190])  # середня висота
        self.speed = 8

    def draw(self):
        pygame.draw.polygon(WIN, BLACK, [
            (self.x, self.y + 10),
            (self.x + 10, self.y),
            (self.x + 20, self.y + 10),
            (self.x + 30, self.y)
        ])

    def update(self):
        self.x -= self.speed

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

def reset_game():
    return Dino(), [], [], 0

def main():
    clock = pygame.time.Clock()
    dino, obstacles, birds, score = reset_game()
    font = pygame.font.SysFont(None, 36)

    SPAWN_OBSTACLE = pygame.USEREVENT + 1
    SPAWN_BIRD = pygame.USEREVENT + 2
    pygame.time.set_timer(SPAWN_OBSTACLE, 1500)
    pygame.time.set_timer(SPAWN_BIRD, 4000)

    running = True
    while running:
        clock.tick(60)
        WIN.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SPAWN_OBSTACLE:
                obstacles.append(Obstacle())
            if event.type == SPAWN_BIRD:
                birds.append(Bird())

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            dino.jump()
        dino.crouch(keys[pygame.K_DOWN])

        dino.update()

        for obstacle in obstacles[:]:
            obstacle.update()
            if obstacle.x + obstacle.width < 0:
                obstacles.remove(obstacle)
                score += 1

            if dino.get_rect().colliderect(obstacle.get_rect()):
                pygame.time.delay(1000)
                dino, obstacles, birds, score = reset_game()

        for bird in birds[:]:
            bird.update()
            if bird.x + bird.width < 0:
                birds.remove(bird)
                score += 1

            if dino.get_rect().colliderect(bird.get_rect()):
                pygame.time.delay(1000)
                dino, obstacles, birds, score = reset_game()

        dino.draw()
        for obstacle in obstacles:
            obstacle.draw()
        for bird in birds:
            bird.draw()

        pygame.draw.line(WIN, BLACK, (0, HEIGHT - 30), (WIDTH, HEIGHT - 30), 2)
        text = font.render(f"Очки: {score}", True, BLACK)
        WIN.blit(text, (10, 10))

        pygame.display.update()

if __name__ == "__main__":
    main()
