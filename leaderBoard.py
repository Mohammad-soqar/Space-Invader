import pygame

pygame.init()
background = pygame.image.load('background.png')

font = pygame.font.Font('seguisb.ttf', 32)
over_font = pygame.font.Font('seguisb.ttf', 64)

def load_leaderboard():
    try:
        with open('leaderboard.txt', 'r') as file:
            leaderboard = [int(line.strip()) for line in file]
    except FileNotFoundError:
        leaderboard = []
    return leaderboard

def show_leaderboard(screen):
    leaderboard = load_leaderboard()
    leaderboard_text = over_font.render("Leaderboard", True, (255,0, 100))
    screen.blit(leaderboard_text, (200, 100))

    y_position = 200
    for i, score in enumerate(leaderboard, start=1):
        text = font.render(f"{i}. {score}", True, (255, 0, 100))
        screen.blit(text, (300, y_position))
        y_position += 50


    back_button = pygame.Rect(300, 500, 200, 50)
    pygame.draw.rect(screen, (255, 255, 255), back_button)
    back_text = font.render("Back", True, (0, 0, 0))
    screen.blit(back_text, (355, 515))

    pygame.display.update()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting_for_input = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                if back_button.collidepoint(event.pos):
                    waiting_for_input = False


if __name__ == "__main__":
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Space Invader")

    show_leaderboard(screen)
