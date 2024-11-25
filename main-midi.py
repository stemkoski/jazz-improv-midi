import pygame
from pygame import mixer

pygame.init()
pygame.mixer.set_num_channels(50)

# load custom icon
icon = pygame.image.load("assets/logo.png") 
pygame.display.set_icon(icon)

fps = 60
timer = pygame.time.Clock()
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Jazz Improv Demo")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (150, 150, 150)

# Button settings
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 100
button_x = (WIDTH - BUTTON_WIDTH) // 2
button_y = (HEIGHT - BUTTON_HEIGHT) // 2
button_rect = pygame.Rect(button_x, button_y, BUTTON_WIDTH, BUTTON_HEIGHT)

# Font
font = pygame.font.Font("assets/ADLaMDisplay.ttf", 32)
button_text = font.render("Start Music", True, BLACK)

file_names =  ['A0', 'B0', 
               'C1', 'D1', 'Db1', 'E1', 'Eb1', 'F1', 'G1', 'Gb1', 'A1', 'Ab1', 'B1', 'Bb1', 
               'C2', 'D2', 'Db2', 'E2', 'Eb2', 'F2', 'G2', 'Gb2', 'A2', 'Ab2', 'B2', 'Bb2', 
               'C3', 'D3', 'Db3', 'E3', 'Eb3', 'F3', 'G3', 'Gb3', 'A3', 'Ab3', 'B3', 'Bb3',
               'C4', 'D4', 'Db4', 'E4', 'Eb4', 'F4', 'G4', 'Gb4', 'A4', 'Ab4', 'B4', 'Bb4',
               'C5', 'D5', 'Db5', 'E5', 'Eb5', 'F5', 'G5', 'Gb5', 'A5', 'Ab5', 'B5', 'Bb5',
               'C6', 'D6', 'Db6', 'E6', 'Eb6', 'F6', 'G6', 'Gb6', 'A6', 'Ab6', 'B6', 'Bb6',
               'C7', 'D7', 'Db7', 'E7', 'Eb7', 'F7', 'G7', 'Gb7', 'A7', 'Ab7', 'B7', 'Bb7',
               'C8']

key_to_note = {"1":"G4", "2":"A4", "3":"C5", "4":"D5", "5":"E5"}

note_sound = { }
for file_name in file_names:
    note_sound[file_name] = mixer.Sound("assets/notes/" + file_name + ".wav")

run = True

# Function to run when button is clicked
def on_button_click():
    pygame.mixer.music.load("accompaniment.midi")
    pygame.mixer.music.play()

while run:
    
    timer.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            # print(key_name)
            if key_name == "0":
                on_button_click()
            if key_name in key_to_note:
                note_name = key_to_note[key_name]
                # print(key_name + "-down")
                note_sound[note_name].play(0) # without second argument, plays length of entire recording

        if event.type == pygame.KEYUP:
            key_name = pygame.key.name(event.key)
            if key_name in key_to_note:
                note_name = key_to_note[key_name]
                # print(key_name + "-down")
                note_sound[note_name].fadeout(250)

        # Check for mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                on_button_click()

    # Clear screen
    screen.fill(WHITE)

    # Draw button with black border
    pygame.draw.rect(screen, BLACK, button_rect.inflate(4, 4))  # Draw border
    pygame.draw.rect(screen, GRAY, button_rect)  # Draw button
    screen.blit(button_text, (button_x + (BUTTON_WIDTH - button_text.get_width()) // 2,
                             button_y + (BUTTON_HEIGHT - button_text.get_height()) // 2))
    
    pygame.display.flip()

pygame.quit()
