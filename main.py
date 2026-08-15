import pgzrun

WIDTH = 800
HEIGHT = 600
TITLE = "Heros & Dragons"

lives = 2
eggs_collected = 0
game_over = False
game_complete = False
reset_required = False

easy_lair = {
    "dragon": Actor("dragon-asleep", pos=(600, 100)),
    "eggs": Actor("one-egg", pos=(400, 100)),
    "egg_count": 1,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": 3,
    "sleep_counter": 0,
    "wake_counter": 0,
}

medium_lair = {
    "dragon": Actor("dragon-asleep", pos=(600, 300)),
    "eggs": Actor("two-eggs", pos=(400, 300)),
    "egg_count": 2,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": 2,
    "sleep_counter": 0,
    "wake_counter": 0,
}

hard_lair = {
    "dragon": Actor("dragon-asleep", pos=(600, 500)),
    "eggs": Actor("three-eggs", pos=(400, 500)),
    "egg_count": 3,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": 1,
    "sleep_counter": 0,
    "wake_counter": 0,
}

lairs = [easy_lair, medium_lair, hard_lair]
hero = Actor("hero", pos=(200, 300))


def draw():
    global lairs, game_complete
    screen.clear()
    screen.blit("dungeon", (0, 0))
    if game_over:
        screen.draw.text(
            "GAME OVER", fontsize=150, fontname="font", center=(WIDTH / 2, HEIGHT / 2)
        )
    elif game_complete:
        screen.draw.text(
            "YOU WON", fontsize=150, fontname="font", center=(WIDTH / 2, HEIGHT / 2)
        )
    else:
        hero.draw()
        draw_lairs()
        draw_counters()


def draw_lairs():
    global lairs
    for lair in lairs:
        lair["dragon"].draw()
        if lair["egg_hidden"] is False:
            lair["eggs"].draw()


def draw_counters():
    global eggs_collected, lives
    screen.blit("egg-count", (5, HEIGHT - 35))
    screen.draw.text(
        str(eggs_collected), fontsize=40, fontname="font", pos=(40, HEIGHT - 40)
    )
    screen.blit("life-count", (90, HEIGHT - 35))
    screen.draw.text(str(lives), fontsize=40, fontname="font", pos=(125, HEIGHT - 40))


def update():
    if keyboard.right:
        hero.x += 3
        if hero.x > WIDTH:
            hero.x = WIDTH
    elif keyboard.left:
        hero.x -= 3
        if hero.x < 0:
            hero.x = 0
    elif keyboard.down:
        hero.y += 3
        if hero.y > HEIGHT:
            hero.y = HEIGHT
    elif keyboard.up:
        hero.y -= 3
        if hero.y < 0:
            hero.y = 0
    check_for_collisions()


def check_for_collisions():
    global lairs, eggs_collected, lives, reset_required, game_complete
    for lair in lairs:
        if lair["egg_hidden"] is False:
            check_for_egg_collision(lair)
        if lair["dragon"].image == "dragon-awake" and reset_required is False:
            check_for_dragon_collision(lair)


def check_for_dragon_collision(lair):
    global reset_required
    if hero.colliderect(lair["dragon"]):
        reset_required = True
        animate(hero, pos=(200, 300), on_finished=subtract_life)
        sounds.hero_hit.play()


def check_for_egg_collision(lair):
    global eggs_collected, game_complete
    if hero.colliderect(lair["eggs"]):
        lair["egg_hidden"] = True
        eggs_collected += lair["egg_count"]
        sounds.egg_collected.play()
        if eggs_collected >= 20:
            game_complete = True
            music.stop()
            sounds.game_win.play()
            clock.unschedule(update_lairs)


def subtract_life():
    global lives, reset_required, game_over
    lives -= 1
    if lives == 0:
        game_over = True
        music.stop()
        sounds.game_over.play()
        clock.unschedule(update_lairs)
    reset_required = False


def update_lairs():
    global lairs, hero, lives
    for lair in lairs:
        if lair["dragon"].image == "dragon-asleep":
            update_sleeping_dragon(lair)
        elif lair["dragon"].image == "dragon-awake":
            update_waking_dragon(lair)
        update_egg(lair)


def update_sleeping_dragon(lair):
    if lair["sleep_counter"] >= lair["sleep_length"]:
        lair["dragon"].image = "dragon-awake"
        lair["sleep_counter"] = 0
        sounds.dragon_fire.play()
    else:
        lair["sleep_counter"] += 1


def update_waking_dragon(lair):
    if lair["wake_counter"] >= 2:
        lair["dragon"].image = "dragon-asleep"
        lair["wake_counter"] = 0
    else:
        lair["wake_counter"] += 1


def update_egg(lair):
    if lair["egg_hidden"] is True:
        if lair["egg_hide_counter"] >= 5:
            lair["egg_hidden"] = False
            lair["egg_hide_counter"] = 0
            sounds.egg_respawned.play()
        else:
            lair["egg_hide_counter"] += 1


clock.schedule_interval(update_lairs, 1)
music.play("background")
pgzrun.go()
