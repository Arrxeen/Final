from pygame import *
from random import *

win_width = 1280
win_height = 720
left_bount = win_width / 40
right_bound = win_width - 8 * left_bount
shift= 0
x_start = 20
y_start = 10

platforms = []
itims = sprite.Group()

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
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5 : 
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 1240: #650
            self.rect.x += self.speed
    def update_y(self): 
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5: 
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < -80: #450
            self.rect.y += self.speed
    

class Enemy(GameSprite): 
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, side='left'):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y, player_speed)        
        self.side = side
    
    def update(self):
        global side
        if self.side == 'right':
            self.rect.x -= self.speed
        if self.side == 'left':
            self.rect.x += self.speed
f=1
class Mana(GameSprite): 
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, side='left'):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y, player_speed)        
        self.side = side
    def update(self):
        global side,f      
        if self.side == 'left':
            self.rect.x -= self.speed
        if self.side == 'right':
            self.rect.x += self.speed
        

window = display.set_mode((win_width,win_height))
display.set_caption('sas')
background = transform.scale(image.load('bak.png'),(win_width,win_height))
books=[]
barrs_r=[]
barrs_l=[]
manas = sprite.Group()
mon=[]
stairs=[]
notings= []
font.init()
font1 =font.Font(None,40)
font2 = font.Font(None,80)
win = font1.render("WIN",True,(255,60,50))
lose = font1.render("lose",True,(255,0,0))




levl=["                                ",
"                                ",
"                                ",
"                                ",
"                                ",
"  b      l    e   k     r    d",
"-----s          s-----    s-----",
"     s          s         s     ",
"l e  sr         s  b      s  b  ",
"-----------s s------------------",
"           s s                  ",
"           s s                  ",
"   b       s s       b         p",
"--------------------------------",
"                                ",
"                                ",
"                                ",]

x=0
y=0

for r in levl:
    for c in r:
        if c == "l" :
            barr_l = GameSprite("not.png",x,y,40,40,0)
            barrs_l.append(barr_l)
            itims.add(barrs_l)
        if c == "r" :
            barr_r = GameSprite("not.png",x,y,40,40,0)
            barrs_r.append(barr_r)
            itims.add(barrs_r)

        if c ==" ":
            noting = GameSprite("not.png",x,y,40,40,0)
            notings.append(noting)
            itims.add(notings)
        if c == "-":
            platform = GameSprite('plat.png',x,y,40,40,0)
            platforms.append(platform)
            itims.add(platforms)
        if c == "p":
            player =Player('player.png',x,y,40,40,10)
            itims.add(player)
        if c == "s":
            stair = GameSprite('stair.png',x,y,40,40,0)
            stairs.append(stair)
            itims.add(stairs)
        if c == "d":
            dore = GameSprite('dore.png',x,y,40,40,0)
            itims.add(dore)
        if c == "e":
            monst = Enemy('snowman.png',x,y,40,40,10,"right")
            mon.append(monst)
            itims.add(monst)
        if c == "k":
            keyi = GameSprite('key.png',x,y,40,40,0)
            itims.add(keyi)
        if c == "b":
            book = GameSprite('book.png',x,y,40,40,0)
            books.append(book)
            itims.add(books)
        x+=40
    y+=40
    x=0

mana = Mana('kop.png',-150,0,20,20,3,'left')


over=""



boks=0
doorr=False
game = True
finish=False
clock = time.Clock()
FPS = 60
mixer.init()
while game:

    if finish != True:
        player.rect.y += 2
        window.blit(background,(0,0))
        itims.draw(window)
        for monst in mon:
            monst.update()
        mana.update()
        keys = key.get_pressed()
        if keys [K_SPACE]:
            mana.rect.x-player.rect.centerx
            mana.rect.y = player.rect.top
            if f==1:
                mana.side = "left"
            if f==0:
                mana.side = "right"
            manas.add(mana)
            itims.add(mana)


        coin_c = font2.render("coins:"+str(boks),True,(255,0,0))
        window.blit(coin_c,(40,0))


        for platform in platforms:
            if sprite.collide_rect(player,platform):
                player.update_1()
                player.rect.y -=2
            if sprite.collide_rect(player,noting):
                player.update_1()
                player.update_y()

        for stair in stairs:
            if sprite.collide_rect(player,stair):
                player.update_y()
                player.update_1()

        for book in books:
            if sprite.collide_rect(player,book):
                boks+=1
                books.remove(book)
                itims.remove(book)

        if sprite.collide_rect(player,keyi):
            doorr= True
            itims.remove(keyi)

        for barr_r in barrs_r: 
            for monst in mon:
                if sprite.collide_rect(monst, barr_r): # для ворогів
                    monst.side = 'right'
# торкання країв платформи справа
        for barr_l in barrs_l: 
            for monst in mon:
                if sprite.collide_rect(monst, barr_l):
                    monst.side = 'left'


        for monst in mon:

            if sprite.collide_rect(player,monst):
                player.rect.x = 1240
                player.rect.y = 480
            

                

        if sprite.collide_rect(player,dore) and doorr==True:
            over ='win'
            finish = True
            

    if over =='win':
        window.fill((0,0,0))
        window.blit(win,(400,300))
        
    elif over=='lose':
        window.blit(lose,(400,300))
        

    for e in event.get():
        
        if e.type == QUIT:
            game = False
    

    display.update()
    clock.tick(FPS)
