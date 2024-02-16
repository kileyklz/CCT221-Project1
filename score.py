import pygame

WHITE = (255, 255, 255)

class Score:
    def __init__(self):
        self.score_player1 = 0
        self.score_player2 = 0

    def updatePlayer1(self):
        self.score_player1 += 1

    def updatePlayer2(self):
        self.score_player2 += 1

    def draw(self, screen, width, height):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Player 1: {self.score_player1}  Player 2: {self.score_player2}", True, WHITE)
        screen.blit(score_text, (width // 2 - score_text.get_width() // 2, height // 2 - score_text.get_height() // 2))
