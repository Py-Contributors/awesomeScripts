from cgitb import text
import pygame as pg
import math
import random

pg.init()

green = (0, 255, 0)
screen = pg.display.set_mode((1024, 768))
pg.display.set_caption("Space Shooter")
font = pg.font.Font('freesansbold.ttf', 32)

back = pg.image.load(r"background.jpg").convert_alpha()
bomb = pg.image.load(r"bomb.png").convert_alpha()
player = pg.image.load(r"spaceship.png").convert_alpha()
enemy = pg.image.load(r"ufo.png").convert_alpha()
bullet = pg.image.load(r"bullet.png").convert_alpha()
fire = pg.image.load(r"flame.png").convert_alpha()

run = True
gameOver = False
bx = 0
by = 0
px = 512
py = 700
ex = random.randint(5, 968)
ey = 68
pi = 0
speed = 1
speedEnemy = 20
ei = speed
bullet_state = "ready"
score = 0
lives = 1

text = font.render('Score : '+str(score)+' Lives : '+str(lives), True, green)
gameOverText = font.render(
    'Game Over. Your Final Score : '+str(score)+'. Press R to restart.', True, green)


def has_collided(x1, x2, y1, y2):
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    if d <= 50:
        return True
    else:
        return False


while run:
    if not gameOver:
        bomb = pg.transform.scale(bomb, (50, 50))
        bullet = pg.transform.scale(bullet, (20, 20))
        fire = pg.transform.scale(fire, (50, 50))
        player = pg.transform.smoothscale(player, (50, 50))
        enemy = pg.transform.scale(enemy, (50, 50))
        screen.blit(back, (0, 0))
        screen.blit(player, (px, py))
        screen.blit(enemy, (ex, ey))
        screen.blit(text, (5, 5))
    else:
        screen.blit(gameOverText, (100, 384))

    events = pg.event.get()
    for e in events:
        if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
            run = False
        if e.type == pg.MOUSEBUTTONDOWN and bullet_state == "ready" and not gameOver:
            bullet_state = "fire"
            bx = px
            by = py
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_d:
                pi = speed
            elif e.key == pg.K_a:
                pi = -speed
        if e.type == pg.KEYUP:
            pi = 0
        if e.type == pg.KEYDOWN and e.key == pg.K_r and gameOver:
            gameOver = False
            bx = 0
            by = 0
            px = 512
            py = 700
            ex = random.randint(5, 968)
            ey = 68
            pi = 0
            speed = 1
            speedEnemy = 20
            ei = speed
            bullet_state = "ready"
            score = 0
            lives = 1
            text = font.render('Score : '+str(score) +
                               ' Lives : '+str(lives), True, green)
            gameOverText = font.render('Press R to restart.', True, green)

    if bullet_state == "fire":
        screen.blit(bullet, (bx, by))
    if by < 0:
        bullet_state = "ready"
    if ex > 968:
        ex = 968
        ey += 20
        ei = -speedEnemy
    if ex < 5:
        ex = 5
        ey += 20
        ei = speedEnemy
    ex += ei
    if px > 968:
        px = 968
    if px < 5:
        px = 5
    px += pi
    by -= 2

    if has_collided(bx, ex, by, ey):
        screen.blit(fire, (ex, ey))
        bullet_state = "ready"
        ex = random.randint(5, 968)
        ey = 68
        score = (speedEnemy*50)
        speedEnemy += 0.5
        text = font.render('Score : '+str(score) +
                           ' Lives : '+str(lives), True, green)

    if has_collided(px, ex, py, ey):
        if lives > 0:
            screen.blit(fire, (ex, ey))
            bullet_state = "ready"
            ex = random.randint(5, 968)
            ey = 68
            lives -= 1
            text = font.render('Score : '+str(score) +
                               ' Lives : '+str(lives), True, green)
        else:
            gameOver = True

    pg.display.update()
