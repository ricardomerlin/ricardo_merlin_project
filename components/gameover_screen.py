import pygame

class GameOverScreen:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.title_font = pygame.font.SysFont(None, 100)
        self.start_font = pygame.font.SysFont(None, 50)

        self.title_text = self.title_font.render("Game Over", True, (255, 255, 255))
        self.start_text = self.start_font.render("Press SPACE to continue", True, (255, 255, 255))

        self.title_rect = self.title_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 50))
        self.start_rect = self.start_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 50))

        self.color_timer = 0
        self.color_speed = 5

    def update(self, screen):
        color_value = (255, 255 - self.color_timer, 255 - self.color_timer)
        self.title_text = self.title_font.render("Game Over", True, color_value)
        self.start_text = self.start_font.render("Press SPACE to continue", True, color_value)

        screen.fill((0, 0, 0))
        screen.blit(self.title_text, self.title_rect)
        screen.blit(self.start_text, self.start_rect)

        self.color_timer = (self.color_timer + self.color_speed) % 256

    def start_game(self):
        pass
