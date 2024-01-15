import pygame
from pygame.locals import QUIT

def show_menu():
    pygame.init()
    background = pygame.image.load('background.png')

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Space Invader")

    white = (255, 255, 255)
    black = (0, 0, 0)

    font = pygame.font.Font('seguisb.ttf', 32)

    start_button = pygame.Rect(300, 200, 200, 50)
    leaderboard_button = pygame.Rect(300, 300, 200, 50)
    quit_button = pygame.Rect(300, 400, 200, 50)

    running = True
    while running:
        screen.fill(black)
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return "start"
                elif leaderboard_button.collidepoint(event.pos):
                    return "leaderboard"
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    quit()

        pygame.draw.rect(screen, white, start_button)
        pygame.draw.rect(screen, white, leaderboard_button)
        pygame.draw.rect(screen, white, quit_button)

        start_text = font.render("Start", True, black)
        leaderboard_text = font.render("Leaderboard", True, black)
        quit_text = font.render("Quit", True, black)

        screen.blit(start_text, (355, 215))
        screen.blit(leaderboard_text, (325, 315))
        screen.blit(quit_text, (355, 415))

        pygame.display.update()

if __name__ == "__main__":
    show_menu()
