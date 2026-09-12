import pygame
import sys

pygame.init()

# Create screen and load background
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Game Menu")
BG = pygame.image.load("wood_background.jpg")
# Make background image scale
BG = pygame.transform.scale(BG, (1280, 720))

# Set font
font = pygame.font.Font(None, 60)

def main_menu():

    while True:
        # Draw background image
        SCREEN.blit(BG, (0,0))

        # Current Mouse Position
        MENU_MOUSE_POS = pygame.mouse.get_pos()


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
                if play_rect.collidepoint(MENU_MOUSE_POS):
                    print("Play button clicked") # Add Functionality Later

                if rules_rect.collidepoint(MENU_MOUSE_POS):
                    print("Rules button clicked") # Add Functionality Later

                if close_rect.collidepoint(MENU_MOUSE_POS):
                    print("Game closed") # Add Functionality Later
                    pygame.quit()
                    sys.exit()
        

        # Refresh screen display
        pygame.display.update()

# Run menu
main_menu()
    

