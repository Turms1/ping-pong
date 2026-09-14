from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (80, 80))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.inflate_ip(-10, -10)
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
    def updater(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y<395:
            self.rect.y += self.speed
    def updatel(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y>5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y<395:
            self.rect.y += self.speed

background = transform.scale(image.load('background.jpg'), (700, 500))

window = display.set_mode((700, 500))
window.blit(background, (0, 0))

racket1 = Player('racket.png', 0, 250, 8)
racket2 = Player('racket.png', 620, 250, 8)
ball = GameSprite('ball.png', 350, 250, 7)
clock = time.Clock()

fps = 60

game = True

while game:
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    racket1.updatel()
    racket2.updater()
    racket1.reset()
    racket2.reset()
    ball.reset()
    display.update()
    clock.tick(60)