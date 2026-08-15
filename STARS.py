import pgzrun
import random


WIDTH = 800
HEIGHT = 600

currentLevel = 5
stars = []
colors = ["blue", "green", "yellow", "purple", "orange", "white", "black"]
gameOver = False
animations = []
FINAL_LEVEL = 10
endsoundplayed = "false"


def createStars():
    global currentLevel, FINAL_LEVEL, WIDTH, stars, colors, animations

    stars.append(Actor("red"))
    for _ in range(currentLevel - 1):
        star = Actor(random.choice(colors))
        stars.append(star)
    gapSize = WIDTH / (len(stars) + 1)
    distance = gapSize
    random.shuffle(stars)
    for star in stars:
        star.x = distance
        distance += gapSize
    duration = FINAL_LEVEL - currentLevel
    for star in stars:
        animation = animate(star, y=HEIGHT, duration=duration, on_finished=endGame)
        animations.append(animation)


def removeStars():
    global stars, animations
    stars = []
    for animation in animations:
        if animation.running:
            animation.stop()


def endGame():
    global gameOver
    gameOver = True


def on_mouse_down(pos):
    global currentLevel, stars
    for star in stars:
        if star.collidepoint(pos):
            if star.image == "red":
                currentLevel += 1
                sounds.level_win.play()
            else:
                endGame()


def draw():
    screen.clear()
    screen.blit("space", (0, 0))
    if not gameOver:
        for star in stars:
            star.draw()
    else:
        if currentLevel == FINAL_LEVEL:
            screen.draw.text(
                "You Win!",
                fontsize=62,
                fontname="font",
                center=(WIDTH / 2, HEIGHT / 2),
                color="deep blue",
                gcolor="dark gold",
            )
            screen.draw.text(
                "You Win!",
                fontsize=32,
                fontname="font",
                center=(WIDTH / 2, HEIGHT / 2 + 50),
                color="yellow",
                gcolor="orange",
            )
        else:
            screen.draw.text(
                "Game Over!",
                fontsize=62,
                fontname="font",
                center=(WIDTH / 2, HEIGHT / 2),
                color="deep pink",
                gcolor=" black",
            )
            screen.draw.text(
                "Try agin!",
                fontsize=32,
                fontname="font",
                center=(WIDTH / 2, HEIGHT / 2 + 50),
                color="gold",
                gcolor="silver",
            )


def update():
    global endsoundplayed
    if len(stars) != currentLevel and not gameOver:
        removeStars()
        createStars()
    if currentLevel == FINAL_LEVEL:
        if not endsoundplayed:
            sounds.game_win.play()
            endsoundplayed = True
        endGame()
    elif gameOver:
        if not endsoundplayed:
            sounds.game_over.play()
            endsoundplayed = True
        endGame()


music.play("background")
pgzrun.go()
