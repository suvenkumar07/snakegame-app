import streamlit as st
import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Screen Dimensions
WIDTH = 400
HEIGHT = 300

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Snake settings
BLOCK_SIZE = 10
SNAKE_SPEED = 15


# Function to run the snake game
def run_snake_game():
  # Initialize screen
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption('Snake Game')

  clock = pygame.time.Clock()

  # Snake and food initial positions
  snake_pos = [100, 50]
  snake_body = [[100, 50], [90, 50], [80, 50]]
  food_pos = [
      random.randrange(1, (WIDTH // BLOCK_SIZE)) * BLOCK_SIZE,
      random.randrange(1, (HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE
  ]
  food_spawn = True

  # Initial direction and score
  direction = 'RIGHT'
  change_to = direction
  score = 0

  # Main game loop
  while True:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          change_to = 'UP'
        elif event.key == pygame.K_DOWN:
          change_to = 'DOWN'
        elif event.key == pygame.K_LEFT:
          change_to = 'LEFT'
        elif event.key == pygame.K_RIGHT:
          change_to = 'RIGHT'

    # Change direction if not opposite
    if change_to == 'UP' and not direction == 'DOWN':
      direction = 'UP'
    if change_to == 'DOWN' and not direction == 'UP':
      direction = 'DOWN'
    if change_to == 'LEFT' and not direction == 'RIGHT':
      direction = 'LEFT'
    if change_to == 'RIGHT' and not direction == 'LEFT':
      direction = 'RIGHT'

    # Move the snake
    if direction == 'UP':
      snake_pos[1] -= BLOCK_SIZE
    if direction == 'DOWN':
      snake_pos[1] += BLOCK_SIZE
    if direction == 'LEFT':
      snake_pos[0] -= BLOCK_SIZE
    if direction == 'RIGHT':
      snake_pos[0] += BLOCK_SIZE

    # Snake body growing mechanism
    # If food is eaten
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
      score += 1
      food_spawn = False
    else:
      snake_body.pop()

    if not food_spawn:
      food_pos = [
          random.randrange(1, (WIDTH // BLOCK_SIZE)) * BLOCK_SIZE,
          random.randrange(1, (HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE
      ]
    food_spawn = True

    # Fill screen
    screen.fill(BLUE)

    # Draw food
    pygame.draw.rect(
        screen, GREEN,
        pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))

    # Draw snake
    for block in snake_body:
      pygame.draw.rect(screen, BLACK,
                       pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

    # Check for collisions
    if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[
        1] < 0 or snake_pos[1] >= HEIGHT:
      break

    for block in snake_body[1:]:
      if snake_pos == block:
        break

    # Display score
    font = pygame.font.SysFont('times new roman', 20)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, [0, 0])

    pygame.display.update()
    clock.tick(SNAKE_SPEED)

  pygame.quit()


# Streamlit App
st.title("Snake Game in Streamlit")
st.write("Press the button below to play the Snake game!")

if st.button("Play Snake Game"):
  st.write(
      "Launching the game... Close the game window to return to Streamlit.")
  run_snake_game()
