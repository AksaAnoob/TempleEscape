import pygame
import sys
import settings

# Initialize Pygame
pygame.init()

# ==========================
# Screen Settings
# ==========================
WIDTH = settings.WIDTH
HEIGHT = settings.HEIGHT

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(settings.TITLE)

clock = pygame.time.Clock()
FPS = settings.FPS

# ==========================
# Player Settings
# ==========================
player_size = 40

player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT // 2 - player_size // 2

player_speed = 5
# ==========================
# Wall Settings
# ==========================
WALL_THICKNESS = 40

WALL_COLOR = (60, 52, 40)

# ==========================
# Game Loop
# ==========================
running = True

while running:

    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ==========================
    # Player Movement
    # ==========================
    keys = pygame.key.get_pressed()

    new_x = player_x
    new_y = player_y

    if keys[pygame.K_a]:
        new_x -= player_speed

    if keys[pygame.K_d]:
        new_x += player_speed

    if keys[pygame.K_w]:
        new_y -= player_speed

    if keys[pygame.K_s]:
        new_y += player_speed

        # Collision with temple walls

    if new_x >= WALL_THICKNESS and new_x <= WIDTH - WALL_THICKNESS - player_size:
        player_x = new_x

    if new_y >= WALL_THICKNESS and new_y <= HEIGHT - WALL_THICKNESS - player_size:
        player_y = new_y
    

    # ==========================
    # Draw Background
    # ==========================
    top_color = settings.TOP_COLOR
    bottom_color = settings.BOTTOM_COLOR

    for y in range(HEIGHT):
        ratio = y / (HEIGHT - 1)

        color = (
            int(top_color[0] * (1 - ratio) + bottom_color[0] * ratio),
            int(top_color[1] * (1 - ratio) + bottom_color[1] * ratio),
            int(top_color[2] * (1 - ratio) + bottom_color[2] * ratio)
        )

        pygame.draw.line(screen, color, (0, y), (WIDTH, y))
    # ==========================
    # Draw Temple Walls
    # ==========================

    # Top Wall
    pygame.draw.rect(
        screen,
        WALL_COLOR,
        (0, 0, WIDTH, WALL_THICKNESS)
    )

    # Bottom Wall
    pygame.draw.rect(
        screen,
        WALL_COLOR,
        (0, HEIGHT - WALL_THICKNESS, WIDTH, WALL_THICKNESS)
    )

    # Left Wall
    pygame.draw.rect(
        screen,
        WALL_COLOR,
        (0, 0, WALL_THICKNESS, HEIGHT)
    )

    # Right Wall
    pygame.draw.rect(
        screen,
        WALL_COLOR,
        (WIDTH - WALL_THICKNESS, 0, WALL_THICKNESS, HEIGHT)
    )
    # ==========================
    # Draw Player
    # ==========================
    pygame.draw.rect(
        screen,
        settings.PLAYER_COLOR,
        (player_x, player_y, player_size, player_size),
        border_radius=8
    )

    # Update Display
    pygame.display.flip()

    # Limit FPS
    clock.tick(FPS)

pygame.quit()
sys.exit()