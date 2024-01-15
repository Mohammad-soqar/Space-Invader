import pygame
from menu import show_menu
from game import play_game
from leaderBoard import show_leaderboard

def main():
    pygame.init()
    background = pygame.image.load('background.png')

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Space Invader")

    while True:
        screen.blit(background, (0, 0))
        menu_result = show_menu()

        if menu_result == "start":
            play_game()
        elif menu_result == "leaderboard":
            show_leaderboard(screen)

if __name__ == "__main__":
    main()
