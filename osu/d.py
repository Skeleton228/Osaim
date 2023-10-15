from pygame import *
from random import *
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
        #self.kill()
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 
    def kl(self):
        self.kill()
        sprit.kill()
        #sprit = GameSprite('sprite.png', randint(0,600), randint(0,500), 50, 50, 4)
        print(2)
spr = sprite.Group()
for i in range(5):
    sprit = GameSprite('sprite.png', randint(0, 550), randint(0,450), 50, 50, 4)#monster = Enemy('pngwing.com.png', randint(80, win_width - 80), -40, 80, 50, randint(1,5))
    spr.add(sprit)

background = GameSprite('back1.jpg', 0, 0, win_width, win_height, 0)
#sprit = GameSprite('sprite.png', randint(0, 550), randint(0,450), 50, 50, 4)
clock = time.Clock()
FPS = 60
font.init()
font1 = font.Font(None, 36)
mixer.init()
mixer.music.load('fon.mp3')
mixer.music.play(-1)
game = True
finish = False
n_time=t.time()
scor=0
while game:
    
    for e in event.get():
        if e.type == QUIT:
            
            game = False
        elif e.type == MOUSEBUTTONDOWN:
            #if e.button == 1:
                mousex, mousey = mouse.get_pos()
                mmx=[]
                mmy=[]
                for x in range(-50,0):
                    mmx.append(mousex+x)
                for y in range(-50,0):
                    mmy.append(mousey+y)
                for s in spr:
                    if  s.rect.x in mmx and s.rect.y in mmy:
                        s.kill()
                        sprit = GameSprite('sprite.png', randint(0, 550), randint(0,450), 50, 50, 4)
                        spr.add(sprit)
                        scor+=1
                        break
    if t.time()-n_time>=60:
        finish=1
    #if t.time()-n_time==int(t.time()-n_time):print(int(t.time()-n_time))
    tttime=int(t.time()-n_time)

  
        

    if finish != True:
        background.reset()
        spr.update()
        spr.draw(window)
        #sprit.reset()
        text_score = font1.render('очки: ' + str(scor), True, (255,255,255))
        window.blit(text_score, (10, 20))
        text_time = font1.render('время: ' + str(60 - tttime), True, (255,255,255))
        window.blit(text_time, (10, 40))
    else:
        background = GameSprite('finish.jpg', 0, 0, win_width, win_height, 0)
        background.reset() 
        text_score = font1.render('Ваши очки: ' + str(scor), True, (255,255,255))
        window.blit(text_score, (210,310))
        text_time = font1.render('Ваше время: ' + str(60), True, (255,255,255))
        window.blit(text_time, (210,330))
    display.update()
    clock.tick(FPS)
        