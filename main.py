import pygame
import sys
import random
#from pygame.locals import *


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = "Snake Game"
CELL_SIZE = 10 # Size of each cell in the grid (used for snake and apple)
BG = (255,200,150)
RED = (255,0,0)
BLACK = (0,0,0)
BODY_INNER = (50,175,25)
BODY_OUTER = (100,100,200)
APPLE_COLOR = (255,0,0)

FPS = 10
    
def draw_snake(screen, snake_pos):



    index = 0
    for segment in snake_pos:
        pygame.draw.rect(screen, BODY_OUTER, (segment[0],segment[1], CELL_SIZE,CELL_SIZE))
        if index == 0:
            pygame.draw.rect(screen, RED, (segment[0] + 1,segment[1] + 1, CELL_SIZE - 2, CELL_SIZE - 2))
        else:
            pygame.draw.rect(screen, BODY_INNER, (segment[0] + 1,segment[1] + 1, CELL_SIZE - 2, CELL_SIZE - 2))
        index += 1



def draw_apple(screen, apple_pos):
    pygame.draw.rect(screen, APPLE_COLOR, (apple_pos[0], apple_pos[1], CELL_SIZE, CELL_SIZE))

def draw_score(screen, score, font):
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text,[10,10])

def run_snake_game():

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    direction = 1
    score = 0
    snake_pos = [[int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)]]

    snake_pos.extend([[int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + CELL_SIZE * i] for i in range(1,4)])
    apple_pos = [random.randint(0, SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE, random.randint(0, SCREEN_HEIGHT // CELL_SIZE - 1)* CELL_SIZE]


    font = pygame.font.SysFont(None, 35)

    try:
        pygame.mixer.music.load('indigo-lo-fi-hip-hop_51-sec-320822.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    except pygame.error as e:
        print(f"Error loading or playing music in Snake game: {e}")

    running_game = True
    while running_game:
        screen.fill(BG)
        draw_apple(screen,apple_pos)
        draw_score(screen, score, font)
        draw_snake(screen, snake_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_game = False
            elif event.type == pygame.KEYDOWN:

                new_direction = direction
                if event.key == pygame.K_UP and direction != 3: 
                    new_direction = 1
                elif event.key == pygame.K_RIGHT and direction != 4: 
                    new_direction = 2
                elif event.key == pygame.K_DOWN and direction != 1: 
                    new_direction = 3
                elif event.key == pygame.K_LEFT and direction != 2: 
                    new_direction = 4
                direction = new_direction

        head_x, head_y = snake_pos[0]
        if direction == 1: head_y -= CELL_SIZE
        elif direction == 2: head_x += CELL_SIZE
        elif direction == 3: head_y += CELL_SIZE
        elif direction == 4: head_x -= CELL_SIZE

        snake_pos.insert(0, [head_x, head_y])


        if snake_pos[0] == apple_pos:
            while apple_pos in snake_pos:

                apple_pos = [random.randint(0, SCREEN_WIDTH // CELL_SIZE -1) * CELL_SIZE, random.randint(0,SCREEN_HEIGHT // CELL_SIZE - 1) * CELL_SIZE]
            score += 1
        else:
            snake_pos.pop()

        if head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT or snake_pos[0] in snake_pos[1:]:
            running_game = False

        pygame.display.flip()
        clock.tick(FPS)

    pygame.mixer.music.stop()

def main_menu():
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Main Menu")
    font = pygame.font.SysFont("Arial", 40)
    button_color = (100,100,200)
    text_color = (255,255,255)

    play_button_rect = pygame.Rect(0, screen_height // 3, 200, 50)
    play_button_rect.centerx = screen_width // 2 # Center the button horizontally
    play_text = font.render("PLAY", True, text_color) # Create the button text
    play_text_rect = play_text.get_rect(center=play_button_rect.center) # Center the text inside the button

# Define the "EXIT" button
    exit_button_rect = pygame.Rect(0, screen_height // 2, 200, 50)
    exit_button_rect.centerx = screen_width // 2 # Center the button horizontally
    exit_button_rect.y = screen_height // 2 + 20 # Adjust vertical position
    exit_text = font.render("EXIT", True, text_color) # Create the button text
    exit_text_rect = exit_text.get_rect(center=exit_button_rect.center) # Center the text inside the button


    running_menu = True # Variable to control the menu loop
    while running_menu:
        screen.fill((50, 50, 50)) # Fill the screen with a dark background

        pygame.draw.rect(screen, button_color, play_button_rect) # Draw the "PLAY" button
        screen.blit(play_text, play_text_rect) # Draw the "PLAY" button text

        pygame.draw.rect(screen, button_color, exit_button_rect) # Draw the "EXIT" button
        screen.blit(exit_text, exit_text_rect) # Draw the "EXIT" button text

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_menu = False # Exit the menu if the user closes the window
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Check for left mouse button click
                    mouse_pos = pygame.mouse.get_pos() # Get the position of the mouse click
                    if play_button_rect.collidepoint(mouse_pos): # Check if "PLAY" button was clicked
                        run_snake_game() # Start the Snake game
                    elif exit_button_rect.collidepoint(mouse_pos): # Check if "EXIT" button was clicked
                        running_menu = False # Exit the menu

        pygame.display.flip() # Update the display

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    pygame.init() # Initialize Pygame
    pygame.mixer.init() # Initialize Pygame mixer for audio
    main_menu()
        











        







