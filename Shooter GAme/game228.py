from pygame import *
from random import randint



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_y, size_x, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_y,size_x))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Rocket(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet("bullet.png",self.rect.x+15, self.rect.y,20,40,50)
        bullets.add(bullet)


class Enemy(GameSprite):
    def update(self):
        self.rect.y +=randint(1,5)
        if self.rect.y >500:
            self.rect.x = randint(80,600)
            self.rect.y = 0


class Bullet(GameSprite):
    def update(self):
        self.rect.y -=6
        if self.rect.y <0:
            self.kill()



window = display.set_mode((700,500))
display.set_caption("Шутер")
background = transform.scale(image.load("galaxy.jpg"),(700,500))


game=True
clock = time.Clock()
FPS = 30
finish = False

monsters = sprite.Group()
for i in range(3):
    enemy=Enemy("ufo.png",randint(80,600),randint(-50,0),80,50,randint(1,5))
    monsters.add(enemy)

bullets = sprite.Group()



rocket=Rocket("rocket.png",350,350,80,120,10)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish!=True:
        window.blit(background,(0,0))
        rocket.reset()
        rocket.update()
        monsters.draw(window)
        monsters.update()


    clock.tick(FPS)
    display.update()