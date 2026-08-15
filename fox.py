import pgzrun
from random import randint

WIDTH = 500
HEIGHT = 500
TITLE = "COIN AND FOX"
player = Actor("fox")
player.pos = 100, 100
coin = Actor("coin")
coin.pos = 400, 400
score = 0
game_over = False


def draw():
    global score, score
    if not game_over:
        screen.clear()
        screen.blit("background", (0, 0))
        coin.draw()
        player.draw()
        screen.draw.text("score:" + str(score), (10, 10))

    else:
        screen.clear()
        screen.fill("maroon")
        screen.draw.text("game_over", (200, 200))
        screen.draw.text("score:" + str(score), (200, 250))


def update():
    global score
    if keyboard.Right:
        if player.x < WIDTH:
            player.x += 2
        else:
            player.x = 0
    if keyboard.Left:
        if player.x > 0:
            player.x -= 2
        else:
            player.x = WIDTH
    if keyboard.Up:
        if player.y > 0:
            player.y -= 2
        else:
            player.y = HEIGHT
    if keyboard.Down:
        if player.y < HEIGHT:
            player.y += 2
        else:
            player.y = HEIGHT
    if player.colliderect(coin):
        coin.pos = randint(0, 500), randint(0, 500)
        score += 1


def timeUp():
    global game_over
    game_over = True
    print("time's Up")


clock.schedule(timeUp, 50)


pgzrun.go()
