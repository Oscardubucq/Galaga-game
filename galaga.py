import pgzrun
HEIGHT = 600
WIDTH = 1200
ship = Actor("vaisseau")
bug = Actor("ennemi")
ship.pos = (WIDTH/2,HEIGHT-50)
speed = 5
bullets = []
enemies = []

for x in range(8):
    for y in range(4):
        enemies.append(Actor("ennemi"))
        enemies[-1].x = 100+50*x
        enemies[-1].y = 100+50*y

score = 0
direction = 1
ship.dead = False
ship.countdown = 90

def display_score():
    screen.draw.text(str(score),(20,20))
def game_over():
    screen.draw.text("GAME OVER",(600,300))
def on_key_down(key):
    if ship.dead == False:
        if key == keys.SPACE:
            bullets.append(Actor("galaga"))
            bullets[-1].x = ship.x
            bullets[-1].y = ship.y-50

def update():
    global score
    global direction
    move_down = False

    if ship.dead == False:
        if keyboard.left:
            ship.x -= speed
            if ship.x <= 0:
                ship.x = 0
        elif keyboard.right:
            ship.x += speed
            if ship.x >= WIDTH:
                ship.x = WIDTH

    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet)
        else:
            bullet.y-=10


