#создай игру "Лабиринт"!
from pygame import *



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(40,40))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -=  self.speed
        if keys[K_RIGHT]:
            self.rect.x +=  self.speed
        if keys[K_UP]: 
            self.rect.y -=  self.speed
        if keys[K_DOWN]:
            self.rect.y +=  self.speed


class Enemy(GameSprite):
    def update(self):
        if self.rect.x == 600:
            self.speed *= -1
        if self.rect.x == 320:
            self.speed *= -1
        self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_1 = color_2
        self.color_1 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

font.init()

font = font.Font(None, 70)
win = font.render("YOU WIN !", True, (120, 0, 0))
lose = font.render("YOU LOSE !", True, (120, 0, 0 ))

window = display.set_mode((700, 500))
display.set_caption("Догонялки")

background = transform.scale(image.load("background.jpg"), (700, 500))
player = Player('hero.png', 20, 450, 10)
enemy = Enemy('cyborg.png', 440, 295, 10)
treasure = GameSprite('treasure.png', 440, 425, 19)       

wall0 = Wall(23,23,123, 414, 100, 8, 163)
wall1 = Wall(23,23,123, 127, 100, 8, 777)
wall2 = Wall(23,23,123, 414, 360, 8, 777)
wall3 = Wall(23,23,123, 265, 0, 8, 410)
wall4 = Wall(222,255,23, 62, 100, 130, 8)
wall5 = Wall(222,255,23, 207, 195, 130, 8)
wall6 = Wall(222,255,23, 207, 410, 130, 8)
wall7 = Wall(222,255,23, 62, 290, 130, 8)
wall8 = Wall(222,255,23, 0, 195, 65, 8)
wall9 = Wall(222,255,23, 355, 92, 130, 8)
wall10 = Wall(0,255,255, 370, 260, 130, 8)
wall11 = Wall(0,255,255, 406, 360, 94, 8)
wall12 = Wall(222,255,23, 650, 310, 130, 8)




mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')
kick.play()


x1 = 100
y1 = 100
x2 = 200
y2 = 350
x3 = 350
y3 = 250

clock = time.Clock()
FPS = 25


game = True 
finish = False
while game:
    window.blit(background,(0, 0))
    player.reset()
    player.update()
    enemy.reset()
    enemy.update()
    treasure.reset()
    wall1.draw_wall()
    wall2.draw_wall()
    wall3.draw_wall()
    wall4.draw_wall()
    wall5.draw_wall()
    wall6.draw_wall()
    wall7.draw_wall()
    wall8.draw_wall()
    wall9.draw_wall()
    wall0.draw_wall()
    wall10.draw_wall()
    wall11.draw_wall()
    wall12.draw_wall()
    

    clock.tick(FPS)
    
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        if sprite.collide_rect(player, treasure):
            finish = True
            window.blit(win, (100, 100))
        display.update()
