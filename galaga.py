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
    
    if len(enemies) == 0:
        game_over()
    if len(enemies) >0 and (enemies[-1].x > WIDTH-50 or enemies[0].x<50):
        move_down = True
        direction = direction*-1
    for enemie in enemies:
        enemie.x +=5*direction
        if move_down == True :
            enemie.y +=100
        if enemie.y>HEIGHT :
            enemies.remove(enemie)
        
        for bullet in bullets:
            if enemie.colliderect(bullet):
                score += 100
                bullets.remove(bullet)
                enemies.remove(enemie)
                if len(enemies) ==0 :
                    game_over()
        
        if enemie.colliderect(ship):
            ship.dead =True
    if ship.dead == True : 
        ship.countdown -= 1
    
    if ship.countdown == 0:
        ship.dead = False
        ship.countdown = 60

def draw():
    screen.clear()
    screen.blit("fond_étoilé",(0,0))
    for bullet in bullets:
        bullet.draw()
    
    for enemie in enemies:
        enemie.draw()
    
    if ship.dead == False:
        ship.draw()
    
    display_score()
    if len (enemies) == 0:
        game_over()
pgzrun.go()
    
    
    
    
    
    
    

    
