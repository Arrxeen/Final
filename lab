from pygame import *
from random import *

win_width = 1280
win_height = 720
#left_bount = win_width / 40
#right_bound = win_width - 8 * left_bount
#shift= 0
#x_start = 20
#y_start = 10








class GameSprite (sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x , size_y, player_speed): 
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y)) 
        self.speed = player_speed
        self.rect = self.image.get_rect() 
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5 : 
            self.rect.x -= self.speed
        if keys [K_RIGHT] and self.rect.x < -80: #650
            self.rect.x += self.speed
        if keys [K_UP] and self.rect.y > 5: 
            self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y < -80: #450
            self.rect.y += self.speed
    

class Enemy (GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x , size_y, player_speed,side="left"): 
        self.side = side

    def update(self):
        global side
        if self.rect.x <= 400: 
            self.direction = "right"
        if self.rect.x >= 650: 
            self.direction = "left"

        if self.direction == "left": 
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


window = display.set_mode((win_width,win_height))
display.set_caption('sas')
#background = transform.scale(image.load('<<<>>>'),(win_width,win_height))
















game = True
finish=False
clock = time.Clock()
FPS = 60
mixer.init()
while game:


    for e in event.get():
        
        if e.type == QUIT:
            game = False


    display.update()
    clock.tick(FPS)
