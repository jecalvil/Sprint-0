import pygame
import sys
import os

# Requirements:
# Line, Check box, Text

pygame.init()

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BG_PATH = os.path.join(SCRIPT_DIR, "wood_background.jpg")

# Create screen and load background
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Game Menu")
BG = pygame.image.load(BG_PATH)
# Make background image scale
BG = pygame.transform.scale(BG, (1280, 720))

# Fonts
font = pygame.font.Font(None, 60)
title_font = pygame.font.Font(None, 90)
checkbox_font = pygame.font.Font(None, 23)

def main_menu():
    # Hints_Enabled? - Checkbox requirement
    hints_toggle = False

    while True:
        # Draw background image
        SCREEN.blit(BG, (0,0))

        # Current Mouse Position
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # -- Title Text --
        title_surface = title_font.render("GAME MENU", True, "White")
        title_rect = title_surface.get_rect(center=(640, 150))
        SCREEN.blit(title_surface, title_rect)

        # Divider Line (Line Requirement)
        pygame.draw.line(SCREEN, "Black", (440, 180), (840, 180), 4)

        # -- Create Buttons --
        # Button 1 - PLAY
        play_surface = font.render("PLAY", True, "White")
        play_rect = play_surface.get_rect(center=(640, 300))

        # Button 2 - HOW TO PLAY
        rules_surface = font.render("HOW TO PLAY", True, "White")
        rules_rect = rules_surface.get_rect(center=(640, 420))

        # Button 3 - CLOSE GAME
        close_surface = font.render("CLOSE GAME", True, "White")
        close_rect = close_surface.get_rect(center=(640, 540))

        # -- Create Checkbox --
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

        # -- Hover Effect -- 
        if play_rect.collidepoint(MENU_MOUSE_POS):
            play_surface = font.render("PLAY", True, "Yellow")

        if rules_rect.collidepoint(MENU_MOUSE_POS):
            rules_surface = font.render("HOW TO PLAY", True, "Yellow")

        if close_rect.collidepoint(MENU_MOUSE_POS):
            close_surface = font.render("CLOSE GAME", True, "Yellow")

        # -- Place Buttons on Screen --
        SCREEN.blit(play_surface, play_rect)
        SCREEN.blit(rules_surface, rules_rect)
        SCREEN.blit(close_surface, close_rect)

        # -- Event Loop --
        for event in pygame.event.get():
            # Default X window button click
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Mouse Clicks
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Menu Buttons
                if play_rect.collidepoint(MENU_MOUSE_POS):
                    print("Play button clicked") # Add Functionality Later

                if rules_rect.collidepoint(MENU_MOUSE_POS):
                    print("Rules button clicked") # Add Functionality Later

                if close_rect.collidepoint(MENU_MOUSE_POS):
                    print("Game closed") # Add Functionality Later
                    pygame.quit()
                    sys.exit()
                # Menu Checkbox
                if hints_rect.collidepoint(event.pos):
                    hints_toggle = not hints_toggle

        

        # Refresh screen display
        pygame.display.update()

# Run menu
main_menu()
    

