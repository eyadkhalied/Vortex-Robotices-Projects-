import pgzrun
import random

WIDTH = 800
HEIGHT = 800
TITLE = "APPLE"
background_color = (40, 43, 59)
fruit = Actor("apple_small")
fruit.pos = WIDTH / 2, HEIGHT / 2
animal = Actor("bunny_small")
animal.pos = WIDTH + 100, random.randint(100, HEIGHT - 100)
score = 0
game_over = False


def draw():
    screen.clear()
    screen.fill(background_color)
    if not game_over:
        screen.draw.text(TITLE, center=(WIDTH / 2, 50), fontsize=50, color="white")
        screen.draw.text(
            f"Score: {score}", topleft=(10, 10), fontsize=40, color="white"
        )
        fruit.draw()
        animal.draw()
    else:
        screen.draw.text(
            "You lose!", center=(WIDTH / 2, HEIGHT / 2), fontsize=80, color="red"
        )


def on_mouse_down(pos):
    global score, game_over
    if game_over:
        return
    if fruit.collidepoint(pos):
        score += 1
        fruit.pos = random.randint(100, 700), random.randint(100, 700)
        print("Good shot!")
    elif animal.collidepoint(pos):
        print("You shot the animal! Game Over!")
        game_over = True
    else:
        score -= 1
        print("You missed!")


def update():
    if game_over:
        return
    fruit.x += 6
    if fruit.x > WIDTH:
        fruit.x = 0

    animal.x -= 4
    if animal.x < -50:
        animal.pos = WIDTH + random.randint(50, 100), random.randint(100, HEIGHT - 100)


pgzrun.go()
