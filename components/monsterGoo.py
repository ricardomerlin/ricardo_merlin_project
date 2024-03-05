import pygame

class MonsterGoo(pygame.sprite.Sprite):
    goos = pygame.sprite.Group()

    def __init__(self, x, y, screen_height):
        super().__init__()
        self.image = pygame.image.load('../sprites/monster_goo.png')
        self.image = pygame.transform.scale(self.image, (20, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5
        self.screen_height = screen_height

    def update(self, dt):
        self.rect.y += self.speed
        if self.rect.top > self.screen_height:
            self.kill()

    @classmethod
    def update_all(cls, dt):
        cls.goos.update(dt)

    @classmethod
    def draw_all(cls, screen):
        cls.goos.draw(screen)