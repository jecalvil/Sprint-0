"""Main menu GUI for the Solitaire game."""

import os
import sys

import pygame

import components

# Requirements:
# Line, Check box, Text

pygame.init()

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


# -- Paths --
# Theme Paths
THEME1_PATH = os.path.join(SCRIPT_DIR, "images", "red_background.jpg")
THEME2_PATH = os.path.join(SCRIPT_DIR, "images", "wood_background.jpg")
THEME3_PATH = os.path.join(SCRIPT_DIR, "images", "green_background.jpg")
# Font Paths
FONT_PATH = os.path.join(SCRIPT_DIR, "PressStart2P-Regular.ttf")

# Create screen
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Game Menu")

# Load Themes
THEME1 = pygame.image.load(THEME1_PATH)
THEME2 = pygame.image.load(THEME2_PATH)
THEME3 = pygame.image.load(THEME3_PATH)

# Make background image scale
THEME1 = pygame.transform.scale(THEME1, (1280, 720))
THEME2 = pygame.transform.scale(THEME2, (1280, 720))
THEME3 = pygame.transform.scale(THEME3, (1280, 720))

# Fonts
font = pygame.font.Font(FONT_PATH, 40)
title_font = pygame.font.Font(FONT_PATH, 70)
checkbox_font = pygame.font.Font(FONT_PATH, 15)


def main_menu():
    """Runs the main menu loop until the player closes the game."""
    # Hints_Enabled? - Checkbox requirement
    hints_toggle = False
    # Initial Theme
    selected_theme = THEME1

    # Menu Buttons
    play_button = components.Button("PLAY", font, "White", "Yellow", (640, 300))
    rules_button = components.Button("HOW TO PLAY", font, "White", "Yellow", (640, 420))
    close_button = components.Button("CLOSE GAME", font, "White", "Yellow", (640, 540))

    # -- Radio Buttons --
    # x-coordinate
    radio1_x = 100
    radio2_x = radio1_x
    radio3_x = radio1_x
    # y coordinate
    radio1_y = 500
    radio2_y = radio1_y + 50
    radio3_y = radio2_y + 50

    # Create radio buttons
    radio_buttons = [
        components.RadioButton(
            radio1_x, radio1_y, 12, "Red Theme", THEME1, checkbox_font
        ),
        components.RadioButton(
            radio2_x, radio2_y, 12, "Wood Theme", THEME2, checkbox_font
        ),
        components.RadioButton(
            radio3_x, radio3_y, 12, "Green Theme", THEME3, checkbox_font
        ),
    ]

    # Main menu event and rendering loop
    while True:
        # Draw background image
        SCREEN.blit(selected_theme, (0, 0))

        # Current Mouse Position
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # -- Title Text --
        title_surface = title_font.render("GAME MENU", True, "White")
        title_rect = title_surface.get_rect(center=(640, 150))
        SCREEN.blit(title_surface, title_rect)

        # Divider Line (Line Requirement)
        pygame.draw.line(SCREEN, "Black", (340, 200), (940, 200), 4)

        # -- Draw Menu Buttons --
        play_button.draw(SCREEN, MENU_MOUSE_POS)
        rules_button.draw(SCREEN, MENU_MOUSE_POS)
        close_button.draw(SCREEN, MENU_MOUSE_POS)

        # -- Draw Radio Buttons --
        for radio_button in radio_buttons:
            radio_button.draw(SCREEN, selected_theme)

        # -- Create Checkbox --
        # Note: In the future, likely make a class if multiple are needed
        hints_rect = pygame.Rect(550, 600, 30, 30)
        pygame.draw.rect(SCREEN, "White", hints_rect, 2)
        # toggle checkbox
        checkbox_text = "HINTS DISABLED"
        if hints_toggle:
            pygame.draw.rect(SCREEN, "Yellow", pygame.Rect(555, 605, 20, 20))
            checkbox_text = "HINTS ENABLED"

        # checkbox label
        label_surface = checkbox_font.render(checkbox_text, True, "White")
        SCREEN.blit(label_surface, (590, 608))

        # -- Event Loop --
        for event in pygame.event.get():
            # Default X window button click
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Mouse Clicks
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Menu Buttons
                if play_button.check_click(MENU_MOUSE_POS):
                    print("Play button clicked")  # Add Functionality Later

                if rules_button.check_click(MENU_MOUSE_POS):
                    print("Rules button clicked")  # Add Functionality Later

                if close_button.check_click(MENU_MOUSE_POS):
                    print("Game closed")
                    pygame.quit()
                    sys.exit()

                # Menu Checkbox
                if hints_rect.collidepoint(event.pos):
                    hints_toggle = not hints_toggle

                # Radio Button Clicks
                if radio_buttons[0].check_click(event.pos):
                    selected_theme = radio_buttons[0].value
                elif radio_buttons[1].check_click(event.pos):
                    selected_theme = radio_buttons[1].value
                elif radio_buttons[2].check_click(event.pos):
                    selected_theme = radio_buttons[2].value

        # Refresh screen display
        pygame.display.update()


# Run menu
if __name__ == "__main__":
    main_menu()
