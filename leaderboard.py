import pygame
import json
import constants
from button import Button
from cursor import My_Cursor

def get_middle(surface):
    return constants.WIDTH / 2 - surface.get_width() / 2

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

# Load and save functions for leaderboard
def load_leaderboard(filename="assets/leaderboard.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_leaderboard(leaderboard, filename="assets/leaderboard.json"):
    with open(filename, "w") as f:
        json.dump(leaderboard, f)

# Combined function to get player name, save, and display leaderboard
def save_and_display_leaderboard(win, targets_pressed, misses, accuracy, sens):
    pygame.font.init()
    font = get_font(30)
    clock = pygame.time.Clock()
    input_text = ""
    active = True

    # Name input loop
    while active:
        win.fill("black")
        prompt_text = font.render("Enter your name:", True, "white")
        win.blit(prompt_text, (get_middle(prompt_text), constants.HEIGHT // 2 - 50))
        name_text = font.render(input_text, True, "white")
        win.blit(name_text, (get_middle(name_text), constants.HEIGHT // 2))

        pygame.display.update()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

    # Save the player's name and score to the leaderboard
  
    leaderboard = load_leaderboard()
    leaderboard.append({
        "name": input_text.strip(),
        "score": (targets_pressed * 20) - (misses * 5),
        "hits": targets_pressed,
        "misses": misses,
        "accuracy": accuracy
    })

    # Sort and keep top 10 scores
    leaderboard = sorted(leaderboard, key=lambda x: x["score"], reverse=True)[:10]
    save_leaderboard(leaderboard)

    # Display the leaderboard
    display_leaderboard(win, leaderboard, sens)

def display_leaderboard(win, leaderboard, sens):
    c = My_Cursor(sens)
    title_font = get_font(40)  # Larger font for the title
    entry_font = get_font(24)  # Smaller font for leaderboard entries

    # "Back" button
    back_button = Button(
        image=pygame.image.load("assets/Back.png"),
        pos=(constants.WIDTH // 2, constants.HEIGHT - 50),
        text_input="BACK",
        font=get_font(20),
        base_color="#d7fcd4",
        hovering_color="White"
    )

    active = True
    while active:
        constants.SCREEN.fill(constants.BG_COLOR)
        title_text = title_font.render("Leaderboard", True, "white")
        win.blit(title_text, (get_middle(title_text), 50))

        # Display each leaderboard entry
        y_position = 120  # Start position for entries
        for index, entry in enumerate(leaderboard):
            # Render name on one line
            name_text = entry_font.render(f"{index + 1}. {entry['name']}", True, "white")
            win.blit(name_text, (get_middle(name_text), y_position))

            # Render score details on the line below the name
            details_text = entry_font.render(
                f"Score: {entry['score']} | Hits: {entry['hits']} | Misses: {entry['misses']} | Accuracy: {entry['accuracy']}%", 
                True, 
                "white"
            )
            win.blit(details_text, (get_middle(details_text), y_position + 25))

            # Move down for the next entry
            y_position += 60

        # Draw the "Back" button
        back_button.changeColor(pygame.mouse.get_pos())
        back_button.update(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(pygame.mouse.get_pos()):
                    active = False  # Exit the leaderboard when "Back" is clicked
        c.draw()
        c.update()
        pygame.display.update()

