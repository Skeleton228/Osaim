from pygame import *
import random
import time as t
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Osu")
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, height, width, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (height, width))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 
background = GameSprite('back1.jpg', 0, 0, win_width, win_height, 0)
sprite = GameSprite('sprite.png', 200, 200, 50, 50, 4)
clock = time.Clock()
FPS = 60
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        background.reset()
        sprite.update()
        sprite.reset()
        display.update()
        clock.tick(FPS)