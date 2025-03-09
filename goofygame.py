import pygame
import math
import random
import time

# Initialize Pygame
pygame.init()

# Set up screen and clock
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)

# Set up the fonts
font = pygame.font.SysFont(None, 55)

# Liquid Motion - Simulating liquid sloshing in a container
def liquid_motion():
    pygame.draw.rect(screen, BLUE, (500, 400, 80, 100))  # Container
    pygame.draw.ellipse(screen, BLUE, (500, 480, 80, 40))  # Liquid inside
    pygame.draw.line(screen, BLUE, (500, 480), (580, 480), 5)  # Sloshing effect

# Human-like Character Walk Cycle with Smoother Movement
def character_walk(x, y, phase):
    # Body (torso)
    pygame.draw.rect(screen, RED, (x, y, 40, 80))
    
    # Head
    pygame.draw.circle(screen, GREEN, (x + 20, y - 10), 15)
    
    # Arms (swinging based on phase)
    if phase % 2 == 0:
        pygame.draw.line(screen, BLUE, (x - 10, y + 30), (x - 30, y + 50), 5)  # Left arm
        pygame.draw.line(screen, BLUE, (x + 40, y + 30), (x + 60, y + 50), 5)  # Right arm
    else:
        pygame.draw.line(screen, BLUE, (x - 10, y + 30), (x - 30, y + 10), 5)  # Left arm
        pygame.draw.line(screen, BLUE, (x + 40, y + 30), (x + 60, y + 10), 5)  # Right arm
    
    # Legs (walking animation)
    if phase % 2 == 0:
        pygame.draw.line(screen, BLUE, (x + 10, y + 80), (x + 20, y + 130), 5)  # Left leg
        pygame.draw.line(screen, BLUE, (x + 30, y + 80), (x + 30, y + 130), 5)  # Right leg
    else:
        pygame.draw.line(screen, BLUE, (x + 10, y + 80), (x + 10, y + 130), 5)  # Left leg
        pygame.draw.line(screen, BLUE, (x + 30, y + 80), (x + 40, y + 130), 5)  # Right leg
    
    # Update the position for the next frame
    x += 5
    if x > 800:  # Reset if it moves off-screen
        x = 0
    return x

# Character Transformation - Shape morphing effect
def character_transformation():
    time_elapsed = pygame.time.get_ticks() // 1000
    radius = 40 + 20 * math.sin(time_elapsed / 2)
    pygame.draw.circle(screen, GREEN, (200, 100), int(radius))  # Morph effect

# Environmental Animation - Moving sun
def environmental_animation():
    time_elapsed = pygame.time.get_ticks() // 100
    sun_x = 400 + 100 * math.cos(math.radians(time_elapsed))
    sun_y = 100 + 50 * math.sin(math.radians(time_elapsed))
    pygame.draw.circle(screen, YELLOW, (int(sun_x), int(sun_y)), 30)  # Sun

# Physics Animation - Bouncing ball with realistic physics
def bouncing_ball():
    gravity = 0.5
    ground_level = 500
    ball_y = 100
    speed = 0
    speed += gravity
    ball_y += speed
    if ball_y >= ground_level:
        ball_y = ground_level
        speed *= -0.8  # Simulate bounce
    pygame.draw.circle(screen, RED, (400, int(ball_y)), 20)

# Typography Animation - Moving text
def typography_animation():
    time_elapsed = pygame.time.get_ticks() // 100
    text = "Animation!"
    text_surface = font.render(text, True, CYAN)
    x_pos = 100 + 5 * time_elapsed  # Moving text
    screen.blit(text_surface, (x_pos % 800, 50))

# Abstract Geometric Patterns - Rotating circle
def geometric_patterns():
    time_elapsed = pygame.time.get_ticks() // 50
    angle = time_elapsed % 360
    pygame.draw.circle(screen, PURPLE, (400 + 100 * math.cos(math.radians(angle)),
                                       300 + 100 * math.sin(math.radians(angle))), 30)

# Animal Movements - Moving snake-like creature
def animal_movement():
    length = 10
    time_elapsed = pygame.time.get_ticks() // 100
    for i in range(length):
        pygame.draw.circle(screen, GREEN, (350 + i * 10, 250 + int(20 * math.sin(i + time_elapsed / 10))), 5)

# 2D Cutout Animation - Paper cutout moving
def cutout_animation():
    time_elapsed = pygame.time.get_ticks() // 100
    x_pos = 100 + 3 * time_elapsed
    pygame.draw.rect(screen, ORANGE, (x_pos % 800, 400, 50, 50))  # Simple cutout

# Stop-Motion Style Animation - Character moving like a stop-motion object
def stop_motion_style():
    time_elapsed = pygame.time.get_ticks() // 500
    x_pos = 200 + (time_elapsed % 5) * 20  # Moving with steps
    pygame.draw.rect(screen, BLUE, (x_pos, 350, 30, 30))

# Pixel Art Animation - Simple pixelated character
def pixel_art_animation():
    time_elapsed = pygame.time.get_ticks() // 500
    x_pos = 300 + (time_elapsed % 10) * 10  # Pixel movement
    for i in range(3):
        pygame.draw.rect(screen, RED, (x_pos + i * 10, 100, 10, 10))  # Pixelated squares

# Music Visualization - Simple pulsating circles (can sync with real music)
def music_visualization():
    time_elapsed = pygame.time.get_ticks() // 50
    radius = 20 + 10 * math.sin(time_elapsed / 10)
    pygame.draw.circle(screen, CYAN, (600, 300), int(radius))

# Morphing Objects - Morph a square into a circle
def morphing_objects():
    time_elapsed = pygame.time.get_ticks() // 1000
    size = 50 + 30 * math.sin(time_elapsed / 2)
    pygame.draw.circle(screen, RED, (200, 500), int(size))  # Morphing circle

# Surreal Motion - Floating umbrella
def surreal_motion():
    time_elapsed = pygame.time.get_ticks() // 100
    x_pos = 400 + 100 * math.sin(math.radians(time_elapsed))
    y_pos = 100 + 50 * math.cos(math.radians(time_elapsed))
    pygame.draw.rect(screen, BLUE, (x_pos, y_pos, 60, 10))  # Umbrella handle
    pygame.draw.ellipse(screen, BLUE, (x_pos - 30, y_pos - 30, 120, 40))  # Umbrella top

# Character Interaction - Two characters moving together
def character_interaction():
    time_elapsed = pygame.time.get_ticks() // 100
    x_pos1 = 50 + 5 * time_elapsed
    x_pos2 = 500 + 5 * time_elapsed
    pygame.draw.rect(screen, RED, (x_pos1, 500, 40, 80))  # First character body
    pygame.draw.circle(screen, GREEN, (x_pos1 + 20, 500 - 10), 15)  # First character head
    pygame.draw.rect(screen, GREEN, (x_pos2, 500, 40, 80))  # Second character body
    pygame.draw.circle(screen, BLUE, (x_pos2 + 20, 500 - 10), 15)  # Second character head

# Main game loop
running = True
x = 100  # Initial character position for walk cycle
phase = 0  # Walk cycle phase
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Call different animation functions
    liquid_motion()
    x = character_walk(x, 250, phase)
    phase += 1
    character_transformation()
    environmental_animation()
    bouncing_ball()
    typography_animation()
    geometric_patterns()
    animal_movement()
    cutout_animation()
    stop_motion_style()
    pixel_art_animation()
    music_visualization()
    morphing_objects()
    surreal_motion()
    character_interaction()

    pygame.display.flip()
    clock.tick(60)  # Limit frame rate to 60 FPS

pygame.quit()
