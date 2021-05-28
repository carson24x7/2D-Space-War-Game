 # Imports
import pygame
import random


# Window settings
WIDTH = 1900
HEIGHT = 1000
TITLE = "Space Invaders"
FPS = 60

# Game Stages
START = 0
PLAYING = 1
END = 2
WIN = 3

# Create window
pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (48, 25, 52)
LIGHTGREY = (169,169,169)
DARKDARKERWHITE = (137, 139, 140)

# Load fonts
title_font = pygame.font.Font('assets/fonts/recharge bd.ttf', 80) 
default_font = pygame.font.Font('assets/fonts/recharge bd.ttf', 40)
game_font = pygame.font.Font('assets/fonts/recharge bd.ttf', 25) 


# Load images
ship_img = pygame.image.load('assets/images/playerShip.png'). convert_alpha()
ship2_img = pygame.image.load('assets/images/playerShip2_blue.png'). convert_alpha()
laser_img = pygame.image.load('assets/images/laserBlue.png'). convert_alpha()
bomb_img = pygame.image.load('assets/images/laserRed.png'). convert_alpha()
dbllaser_img = pygame.image.load('assets/images/laserBlue16.png'). convert_alpha()
powershotlaser_img = pygame.image.load('assets/images/laserBlue08.png'). convert_alpha()

# Asteroids
asteroidbig4_img = pygame.image.load('assets/images/meteorBrown_big4.png'). convert_alpha()
asteroidbig3_img = pygame.image.load('assets/images/meteorBrown_big3.png'). convert_alpha()
asteroidbig2_img = pygame.image.load('assets/images/meteorBrown_big2.png'). convert_alpha()
asteroidbig1_img = pygame.image.load('assets/images/meteorBrown_big1.png'). convert_alpha()
asteroidmed1_img = pygame.image.load('assets/images/meteorBrown_med1.png'). convert_alpha()
asteroidmed3_img = pygame.image.load('assets/images/meteorBrown_med3.png'). convert_alpha()
asteroidsmall1_img = pygame.image.load('assets/images/meteorBrown_small1.png'). convert_alpha()
asteroidsmall2_img = pygame.image.load('assets/images/meteorBrown_small2.png'). convert_alpha()
asteroidtiny2_img = pygame.image.load('assets/images/meteorBrown_tiny2.png'). convert_alpha()


# Enemies
enemy16_img = pygame.image.load('assets/images/enemyBlack1.png').convert_alpha()
enemy8_img = pygame.image.load('assets/images/enemyBlack2.png').convert_alpha()
enemy6_img = pygame.image.load('assets/images/enemyBlack3.png').convert_alpha()
enemy2_img = pygame.image.load('assets/images/enemyBlack.png'). convert_alpha()
enemy5_img = pygame.image.load('assets/images/enemyBlack5.png').convert_alpha()

enemy10_img = pygame.image.load('assets/images/enemyGreen1.png').convert_alpha()
enemy4_img = pygame.image.load('assets/images/enemyGreen2.png').convert_alpha()
enemy9_img = pygame.image.load('assets/images/enemyGreen3.png').convert_alpha()
enemy17_img = pygame.image.load('assets/images/enemyGreen4.png').convert_alpha()

enemy_img = pygame.image.load('assets/images/enemyRed.png'). convert_alpha()
enemy12_img = pygame.image.load('assets/images/enemyRed2.png').convert_alpha()
enemy7_img = pygame.image.load('assets/images/enemyRed4.png').convert_alpha()

enemy11_img = pygame.image.load('assets/images/enemyBlue1.png').convert_alpha()
enemy3_img = pygame.image.load('assets/images/enemyBlue2.png').convert_alpha()
enemy13_img = pygame.image.load('assets/images/enemyBlue3.png').convert_alpha()
enemy14_img = pygame.image.load('assets/images/enemyBlue4.png').convert_alpha()
enemy15_img = pygame.image.load('assets/images/enemyBlue5.png').convert_alpha()


# Power Ups
shieldpowerup_img = pygame.image.load('assets/images/powerupYellow_shield.png').convert_alpha()
pillpowerup_img = pygame.image.load('assets/images/pill_yellow.png').convert_alpha()
invincibilitypowerup_img = pygame.image.load('assets/images/powerupYellow_star.png').convert_alpha()
superfastpowerup_img = pygame.image.load('assets/images/powerupYellow_bolt.png').convert_alpha()
powershotpowerup_img = pygame.image.load('assets/images/things_gold.png').convert_alpha()

# Load sounds
laser_snd = pygame.mixer.Sound('assets/sounds/laser.ogg')
explosion_snd = pygame.mixer.Sound('assets/sounds/explosion.ogg')
powerup_snd = pygame.mixer.Sound('assets/sounds/powerup.ogg')
shipexplosion_snd = pygame.mixer.Sound('assets/sounds/shipexplosion.ogg')
asterpoidexplosion_snd = pygame.mixer.Sound('assets/sounds/asteroidexplosion.ogg')

# Music 
theme_music = 'assets/music/thememusic.ogg'
intro_music = 'assets/music/intromusic.ogg'
end_music = 'assets/music/end.ogg'
win_music = 'assets/music/win.ogg'

# Game classes
class Ship(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = x,y

        self.speed = 5
        self.shield = 3
        self.shoot_double = False
        self.power_shot = False
        self.invincibility_time = 0
        self.superfast_time = 0
        
    def move_left(self):
        self.rect.x -= self.speed

        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        self.rect.x += self.speed

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def move_down(self):
        self.rect.y += self.speed

        if self.rect.bottom > 995:
            self.rect.bottom = 995

    def move_up(self):
        self.rect.y -= self.speed

        if self.rect.top < 700:
            self.rect.top = 700
            
    def shoot(self):
        if self.power_shot > 0:
            x = self.rect.centerx
            y = self.rect.top
            lasers.add( Laser(x, y, powershotlaser_img,2) )
               
        elif self.shoot_double:
            x = self.rect.left + 3
            y = self.rect.centery
            lasers.add( Laser(x, y, dbllaser_img, 1) )
                
            x = self.rect.right - 3
            y = self.rect.centery 
            lasers.add( Laser(x, y, dbllaser_img, 1) )
                
        else:
            x = self.rect.centerx
            y = self.rect.top
            lasers.add( Laser(x, y, laser_img, 1) )
            
        laser_snd.play()
            
    def check_bombs(self):
        hits = pygame.sprite.spritecollide(self, bombs, True, pygame.sprite.collide_mask)
        
        if self.invincibility_time == 0:
            for hit in hits:
                self.shield -=1
                self.shoot_double = False
                shipexplosion_snd.play()
                    
                if self.shield <= 0:    
                    self.kill()
                    explosion_snd.play()
        else:
            self.invincibility_time -= 1
                
    def check_powerups(self):
        hits = pygame.sprite.spritecollide(self, powerups, True, pygame.sprite.collide_mask)

        for hit in hits:
            hit.apply(self)
            powerup_snd.play()
            
    def check_asteroids(self):
        hits = pygame.sprite.spritecollide(self, asteroids, True, pygame.sprite.collide_mask)

        for hit in hits:
            hit.apply(self)
            if self.shield <= 0:
                self.kill()
            asterpoidexplosion_snd.play()
            
    def update(self):
        if ship.superfast_time == 0:
            self.speed = 5
        else:
            self.superfast_time -= 1
            
        if self.power_shot > 0:
            self.power_shot -=1
        
        if self.invincibility_time == 0 and ship.superfast_time == 0 and self.power_shot == 0:
            self.image = ship_img
            self.mask = pygame.mask.from_surface(self.image)
            

        self.check_bombs()
        self.check_powerups()
        self.check_asteroids()

class Laser(pygame.sprite.Sprite):

    def __init__(self, x, y, image, damage):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = x,y

        self.speed = 7
        self.damage = damage
        
    def update(self):
        self.rect.y -= self.speed
        
        if self.rect.bottom < 0:
            self.kill()


class Bomb(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = x,y

        self.speed = 4

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > HEIGHT:
            self.kill()
            
class ShieldPowerup(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = x,y

        self.speed = 5

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > HEIGHT:
            self.kill()
            
    def apply(self,ship):
        if ship.shield >= 1:
            ship.shield += 1
        

        player.score += 50

        
class DoubleshotPowerup(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = x,y

        self.speed = 5

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > HEIGHT:
            self.kill()
            
    def apply(self,ship):
        ship.shoot_double = True
        player.score += 50

class PowershotPowerup(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = x,y

        self.speed = 5

    def update(self):
        self.rect.y += self.speed
    
        if self.rect.top > HEIGHT:
            self.kill()
            
    def apply(self,ship):
        ship.power_shot = 10 * FPS
        ship.image = ship2_img
        ship.mask = pygame.mask.from_surface(ship.image)
        player.score += 50

class InvincibilityPowerup(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = x,y

        self.speed = 5

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > HEIGHT:
            self.kill()
            
    def apply(self,ship):
        ship.invincibility_time = 10 * FPS
        ship.image = ship2_img
        ship.mask = pygame.mask.from_surface(ship.image)
        player.score += 50

class SuperfastPowerup(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = x,y

        self.speed = 5

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > HEIGHT:
            self.kill()
            
    def apply(self,ship):
        ship.speed = 15
        ship.superfast_time = 10 * FPS
        ship.image = ship2_img
        ship.mask = pygame.mask.from_surface(ship.image)
        player.score += 50
            
class Asteroid(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = x,y

        self.speed = 7

    def update(self):
        self.rect.y += 7

        if self.rect.top > HEIGHT:
            self.kill()
            
    def apply(self,ship):
        ship.shield -= 2

        player.score -= 100

class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y, image, shield, value):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = x,y

        self.shield = shield
        self.value = value

    def drop_bomb(self):
        x = self.rect.centerx
        y = self.rect.bottom
        bombs.add( Bomb(x, y, bomb_img) )
        laser_snd.play()

    def update(self):
        hits = pygame.sprite.spritecollide(self, lasers, True, pygame.sprite.collide_mask)

        for laser in hits:
            self.shield -= laser.damage

        if self.shield <= 0:
            self.kill()
            explosion_snd.play()
            player.score += self.value
            
class Fleet (pygame.sprite.Group):

    def __init__(self, *sprites):
        super().__init__(*sprites)

        self.speed = 2
        self.bomb_rate = 2

    def move(self):
        reverse = False
        
        for sprite in self.sprites():
            sprite.rect.x += self.speed

            if sprite.rect.right > WIDTH or sprite.rect.left < 0:
                reverse = True

        if reverse :
            self.speed *= -1

    def select_bomber(self):
        sprites = self.sprites()
        
        if len(sprites) > 0:
            r = random.randrange(0, 120)

            if r < self.bomb_rate + 0.25 * player.level:
                bomber = random.choice(sprites)
                bomber.drop_bomb()
            
    
    def update (self, *args):
        super().update(*args)
        
        self.move()
        
        if len(player) > 0:
            self.select_bomber()


# Stars
def draw_stars(loc, color):
    x = loc[0]
    y = loc[1]
    pygame.draw.ellipse(screen, WHITE, [x, y, 3, 3])

def backgrounddraw_stars(loc, color):
    x = loc[0]
    y = loc[1]
    pygame.draw.ellipse(screen, WHITE, [x, y, 1.9, 1.9])

def backbackgrounddraw_stars(loc, color):
    x = loc[0]
    y = loc[1]
    pygame.draw.ellipse(screen, DARKDARKERWHITE, [x, y, 1, 1])

num_stars = 40
backnum_stars = 40
backbacknum_stars = 40

stars_locs = []
while len(stars_locs) < num_stars:
    x = random.randrange(0, WIDTH)
    y = random.randrange(0, HEIGHT)
    loc = [x, y]
    stars_locs.append(loc)

backgroundstars_locs = []
while len(backgroundstars_locs) < backnum_stars:
    x = random.randrange(0, WIDTH)
    y = random.randrange(0, HEIGHT)
    loc = [x, y]
    backgroundstars_locs.append(loc)

backbackgroundstars_locs = []
while len(backbackgroundstars_locs) < backbacknum_stars:
    x = random.randrange(0, WIDTH)
    y = random.randrange(0, HEIGHT)
    loc = [x, y]
    backbackgroundstars_locs.append(loc)

# Setup

def new_game():
    global ship, player
    
    start_x = WIDTH / 2
    start_y = HEIGHT - 150
    ship = Ship(start_x, start_y, ship_img)
    
    player = pygame.sprite.GroupSingle(ship)
    player.score = 0
    player.level = 1

    pygame.mixer.music.load(intro_music)
    pygame.mixer.music.play(-1)
    

def start_level():
    global enemies, lasers, bombs, powerups, asteroids
    powerups = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    if player.level == 1:
        
        x = random.randint(0, WIDTH)
        y = random.randrange(-2000, -1000)
        p1 = Asteroid (x, y, asteroidsmall1_img)
        asteroids.add(p1)

        x = random.randint(0, WIDTH)
        y = random.randrange(-2000, -1000)
        p2 = Asteroid (x, y, asteroidsmall2_img)
        asteroids.add(p2)

        x = random.randint(0, WIDTH)
        y = random.randrange(-2000, -1000)
        p3 = Asteroid (x, y, asteroidtiny2_img)
        asteroids.add(p3)

        e3 = Enemy (450, 250, enemy_img, 1, 100)
        e4 = Enemy (600, 250, enemy_img, 1, 100)
        e5 = Enemy (750, 250, enemy_img, 1, 100)
        e6 = Enemy (900, 250, enemy_img, 1, 100)
        e7 = Enemy (1050, 250, enemy_img, 1,100)
        e8 = Enemy (1200, 250, enemy_img, 1, 100)
        e9 = Enemy (1350, 250, enemy_img, 1, 100)
        enemies = Fleet(e3, e4, e5, e6, e7, e8, e9)
        
    elif player.level == 2:

        x = random.randint(0, WIDTH)
        y = random.randrange(-2500, -1000)
        p1 = Asteroid (x, y, asteroidsmall2_img)
        asteroids.add(p1)

        x = random.randint(0, WIDTH)
        y = random.randrange(-2500, -1000)
        p2 = Asteroid (x, y, asteroidmed1_img)
        asteroids.add(p2)

        x = random.randint(0, WIDTH)
        y = random.randrange(-2500, -1000)
        p3 = Asteroid (x, y, asteroidsmall2_img)
        asteroids.add(p3)

        x = random.randint(0, WIDTH)
        y = random.randrange(-2500, -1000)
        p4 = Asteroid (x, y, asteroidsmall2_img)
        asteroids.add(p4)
        
        x = random.randint(0, WIDTH)
        y = random.randrange(-2500, -1000)
        p5 = SuperfastPowerup (x,y, superfastpowerup_img)
        powerups.add(p5)
        
        e2 = Enemy(800, 100, enemy3_img, 2, 150)
        e3 = Enemy (450, 250, enemy3_img, 2, 150)
        e4 = Enemy (600, 250, enemy_img, 1, 100)
        e5 = Enemy (750, 250, enemy_img, 1, 100)
        e6 = Enemy (900, 250, enemy_img, 1, 100)
        e7 = Enemy (1050, 250, enemy_img, 1,100)
        e8 = Enemy (1200, 250, enemy_img, 1, 100)
        e9 = Enemy (1350, 250, enemy3_img, 2, 150)
        e10 = Enemy (950, 100, enemy3_img, 2, 150)
        enemies = Fleet(e2, e3, e4, e5, e6, e7, e8, e9, e10)
        
    elif player.level == 3:

        x = random.randint(0, WIDTH)
        y = random.randrange(-3000, -1000)
        p1 = Asteroid (x, y, asteroidsmall1_img)
        asteroids.add(p1)

        x = random.randint(0, WIDTH)
        y = random.randrange(-3000, -1000)
        p2 = Asteroid (x, y, asteroidmed3_img)
        asteroids.add(p2)

        x = random.randint(0, WIDTH)
        y = random.randrange(-3000, -1000)
        p3 = Asteroid (x, y, asteroidsmall2_img)
        asteroids.add(p3)

        x = random.randint(0, WIDTH)
        y = random.randrange(-3000, -1000)
        p4 = Asteroid (x, y, asteroidmed1_img)
        asteroids.add(p4)
        
        x = random.randint(0, WIDTH)
        y = random.randrange(-3000, -1000)
        p5 = ShieldPowerup (x,y, shieldpowerup_img)
        powerups.add(p5)
        
        e1 = Enemy(500, 100, enemy3_img, 2, 150)
        e2 = Enemy(650, 100, enemy3_img, 2, 150)
        e3 = Enemy(800, 100, enemy2_img, 3, 200)
        e4 = Enemy (450, 250, enemy_img, 1, 100)
        e5 = Enemy (600, 250, enemy_img, 1, 100)
        e6 = Enemy (750, 250, enemy_img, 1, 100)
        e7 = Enemy (900, 250, enemy_img, 1, 100)
        e8 = Enemy (1050, 250, enemy_img, 1,100)
        e9 = Enemy (1200, 250, enemy_img, 1, 100)
        e10 = Enemy (1350, 250, enemy_img, 1, 100)
        e11 = Enemy (950, 100, enemy2_img, 3, 200)
        e12 = Enemy (1100, 100, enemy3_img, 2, 150)
        e13 = Enemy (1250, 100, enemy3_img, 2, 150)
        enemies = Fleet(e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13)
        
    elif player.level == 4:

        x = random.randint(0, WIDTH)
        y = random.randrange(-3000, -1000)
        p1 = Asteroid (x, y, asteroidsmall1_img)
        asteroids.add(p1)

        x = random.randint(0, WIDTH)
        y = random.randrange(-3000, -1000)
        p2 = Asteroid (x, y, asteroidmed3_img)
        asteroids.add(p2)

        x = random.randint(0, WIDTH)
        y = random.randrange(-3000, -1000)
        p3 = Asteroid (x, y, asteroidbig1_img)
        asteroids.add(p3)

        x = random.randint(0, WIDTH)
        y = random.randrange(-3000, -1000)
        p4 = Asteroid (x, y, asteroidmed1_img)
        asteroids.add(p4)
        
        x = random.randint(0, WIDTH)
        y = random.randrange(-3000, -1000)
        p5 = DoubleshotPowerup (x,y, pillpowerup_img)
        powerups.add(p5)

        x = random.randint(0, WIDTH)
        y = random.randrange(-3000, -1000)
        p6 = InvincibilityPowerup (x,y, invincibilitypowerup_img)
        powerups.add(p6)
        
        e1 = Enemy(500, 100, enemy3_img, 2, 150)
        e2 = Enemy(650, 100, enemy3_img, 2, 150)
        e3 = Enemy(800, 100, enemy3_img, 2, 150)
        e4 = Enemy (450, 250, enemy2_img, 3, 200)
        e5 = Enemy (600, 250, enemy2_img, 3, 200)
        e6 = Enemy (750, 250, enemy2_img, 3, 200)
        e7 = Enemy (900, 250, enemy2_img, 3, 200)
        e8 = Enemy (1050, 250, enemy2_img, 3,200)
        e9 = Enemy (1200, 250, enemy2_img, 3, 200)
        e10 = Enemy (1350, 250, enemy2_img, 3, 200)
        e11 = Enemy (950, 100, enemy3_img, 2, 150)
        e12 = Enemy (1100, 100, enemy3_img, 2, 150)
        e13 = Enemy (1250, 100, enemy3_img, 2, 150)
        enemies = Fleet(e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13)

    elif player.level == 5:

        x = random.randint(0, WIDTH)
        y = random.randrange(-3000, -1000)
        p1 = Asteroid (x, y, asteroidbig4_img)
        asteroids.add(p1)

        x = random.randint(0, WIDTH)
        y = random.randrange(-3000, -1000)
        p2 = Asteroid (x, y, asteroidbig1_img)
        asteroids.add(p2)

        x = random.randint(0, WIDTH)
        y = random.randrange(-3000, -1000)
        p3 = Asteroid (x, y, asteroidbig2_img)
        asteroids.add(p3)

        x = random.randint(0, WIDTH)
        y = random.randrange(-3000, -1000)
        p4 = Asteroid (x, y, asteroidbig3_img)
        asteroids.add(p4)
        
        x = random.randint(0, WIDTH)
        y = random.randrange(-3000, -1000)
        p5 = ShieldPowerup (x,y, shieldpowerup_img)
        powerups.add(p5)

        x = random.randint(0, WIDTH)
        y = random.randrange(-2500, -1000)
        p6 = PowershotPowerup (x,y, powershotpowerup_img)
        powerups.add(p6)
        
        e1 = Enemy(900, 100, enemy6_img, 5, 300)
        e2 = Enemy (750, 250, enemy6_img, 5, 300)
        e3 = Enemy (900, 250, enemy5_img, 10, 600)
        e4 = Enemy (1050, 250, enemy6_img, 5, 300)
        e5 = Enemy (900, 400, enemy6_img, 5, 300)

        enemies = Fleet(e1, e2, e3, e4, e5)

    elif player.level == 6:

        x = random.randint(0, WIDTH)
        y = random.randrange(-3500, -1000)
        p1 = Asteroid (x, y, asteroidbig2_img)
        asteroids.add(p1)

        x = random.randint(0, WIDTH)
        y = random.randrange(-3500, -1000)
        p2 = Asteroid (x, y, asteroidbig3_img)
        asteroids.add(p2)

        x = random.randint(0, WIDTH)
        y = random.randrange(-3500, -1000)
        p3 = Asteroid (x, y, asteroidmed3_img)
        asteroids.add(p3)

        x = random.randint(0, WIDTH)
        y = random.randrange(-3500, -1000)
        p4 = Asteroid (x, y, asteroidmed3_img)
        asteroids.add(p4)

        x = random.randint(0, WIDTH)
        y = random.randrange(-3500, -1000)
        p5 = Asteroid (x, y, asteroidbig4_img)
        asteroids.add(p5)
        
        x = random.randint(0, WIDTH)
        y = random.randrange(-3000, -1000)
        p6 = SuperfastPowerup (x,y, superfastpowerup_img)
        powerups.add(p6)
        
        e1 = Enemy(900, 100, enemy6_img, 5, 300)
        e2 = Enemy (750, 250, enemy6_img, 5, 300)
        e3 = Enemy (900, 250, enemy5_img, 10, 600)
        e4 = Enemy (1050, 250, enemy6_img, 5, 250)
        e5 = Enemy (900, 400, enemy6_img, 5, 250)
        e6 = Enemy (600, 250, enemy7_img, 3, 200)
        e7 = Enemy (1200, 250, enemy7_img, 3, 200)
        e8 = Enemy (750, 400, enemy7_img, 3, 200)
        e9 = Enemy (1050, 400, enemy7_img, 3, 200)
        e10 = Enemy (750, 100, enemy7_img, 3, 200)
        e11 = Enemy (1050, 100, enemy7_img, 3, 200)
        e12 = Enemy (600, 100, enemy11_img, 1, 100)
        e13 = Enemy (1200, 100, enemy11_img, 1, 100)
        e14 = Enemy (450, 250, enemy11_img, 1, 100)
        e15 = Enemy (1350, 250, enemy11_img, 1, 100)
        e16 = Enemy (600, 400, enemy11_img, 1, 100)
        e17 = Enemy (1200, 400, enemy11_img, 1, 100)

        enemies = Fleet(e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17)

        
    elif player.level == 7:

        x = random.randint(0, WIDTH)
        y = random.randrange(-4000, -1000)
        p1 = Asteroid (x, y, asteroidmed1_img)
        asteroids.add(p1)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4000, -1000)
        p2 = Asteroid (x, y, asteroidbig1_img)
        asteroids.add(p2)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4000, -1000)
        p3 = Asteroid (x, y, asteroidmed3_img)
        asteroids.add(p3)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4000, -1000)
        p4 = Asteroid (x, y, asteroidmed1_img)
        asteroids.add(p4)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4000, -1000)
        p5 = Asteroid (x, y, asteroidbig3_img)
        asteroids.add(p5)

        x = random.randint(0, WIDTH)
        y = random.randrange(-3000, -1000)
        p6 = ShieldPowerup (x,y, shieldpowerup_img)
        powerups.add(p6)
        
        x = random.randint(0, WIDTH)
        y = random.randrange(-3000, -1000)
        p7 = DoubleshotPowerup (x,y, pillpowerup_img)
        powerups.add(p7)

        x = random.randint(0, WIDTH)
        y = random.randrange(-3000, -1000)
        p8 = InvincibilityPowerup (x,y, invincibilitypowerup_img)
        powerups.add(p8)

        x = random.randint(0, WIDTH)
        y = random.randrange(-3000, -1000)
        p9 = SuperfastPowerup (x,y, superfastpowerup_img)
        powerups.add(p9)
        
        e1 = Enemy(500, 100, enemy3_img, 2, 150)
        e2 = Enemy(650, 100, enemy3_img, 2, 150)
        e3 = Enemy(800, 100, enemy3_img, 2, 150)
        e4 = Enemy (450, 250, enemy2_img, 3, 200)
        e5 = Enemy (600, 250, enemy2_img, 3, 200)
        e6 = Enemy (750, 250, enemy2_img, 3, 200)
        e7 = Enemy (900, 250, enemy2_img, 3, 200)
        e8 = Enemy (1050, 250, enemy2_img, 3,200)
        e9 = Enemy (1200, 250, enemy2_img, 3, 200)
        e10 = Enemy (1350, 250, enemy2_img, 3, 200)
        e11 = Enemy (950, 100, enemy3_img, 2, 150)
        e12 = Enemy (1100, 100, enemy3_img, 2, 150)
        e13 = Enemy (1250, 100, enemy3_img, 2, 150)
        e14 = Enemy (500, 400, enemy4_img, 2, 150)
        e15 = Enemy (650, 400, enemy4_img, 2, 150)
        e16 = Enemy (800, 400, enemy4_img, 2, 150)
        e17 = Enemy (950, 400, enemy4_img, 2, 150)
        e18 = Enemy (1100, 400, enemy4_img, 2,150)
        e19 = Enemy (1250, 400, enemy4_img, 2, 150)
        enemies = Fleet(e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19)

    elif player.level == 8:

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p1 = Asteroid (x, y, asteroidtiny2_img)
        asteroids.add(p1)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p2 = Asteroid (x, y, asteroidsmall2_img)
        asteroids.add(p2)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p3 = Asteroid (x, y, asteroidtiny2_img)
        asteroids.add(p3)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p4 = Asteroid (x, y, asteroidsmall1_img)
        asteroids.add(p4)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p5 = Asteroid (x, y, asteroidsmall1_img)
        asteroids.add(p5)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p6 = Asteroid (x, y, asteroidtiny2_img)
        asteroids.add(p6)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p7 = Asteroid (x, y, asteroidsmall2_img)
        asteroids.add(p7)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p8 = Asteroid (x, y, asteroidsmall2_img)
        asteroids.add(p8)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p9 = Asteroid (x, y, asteroidtiny2_img)
        asteroids.add(p9)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p10 = Asteroid (x, y, asteroidtiny2_img)
        asteroids.add(p10)
        
        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p11 = SuperfastPowerup (x,y, superfastpowerup_img)
        powerups.add(p11)
        
        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p12 = InvincibilityPowerup (x,y, invincibilitypowerup_img)
        powerups.add(p12)
        
        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p13 = ShieldPowerup (x,y, shieldpowerup_img)
        powerups.add(p13)

        x = random.randint(0, WIDTH)
        y = random.randrange(-2500, -1000)
        p14 = PowershotPowerup (x,y, powershotpowerup_img)
        powerups.add(p14)

        e1 = Enemy(500, 100, enemy8_img, 2, 150)
        e2 = Enemy(650, 100, enemy8_img, 2, 150)
        e3 = Enemy(800, 100, enemy8_img, 2, 150)
        e4 = Enemy (450, 250, enemy8_img, 2, 150)
        e5 = Enemy (600, 250, enemy8_img, 2, 150)
        e6 = Enemy (750, 250, enemy8_img, 2, 150)
        e7 = Enemy (900, 250, enemy8_img, 2, 150)
        e8 = Enemy (1050, 250, enemy8_img, 2,150)
        e9 = Enemy (1200, 250, enemy8_img, 2, 150)
        e10 = Enemy (1350, 250, enemy8_img, 2, 150)
        e11 = Enemy (950, 100, enemy8_img, 2, 150)
        e12 = Enemy (1100, 100, enemy8_img, 2, 150)
        e13 = Enemy (1250, 100, enemy8_img, 2, 150)
        e14 = Enemy (500, 400, enemy8_img, 2, 150)
        e15 = Enemy (650, 400, enemy8_img, 2, 150)
        e16 = Enemy (800, 400, enemy8_img, 2, 150)
        e17 = Enemy (950, 400, enemy8_img, 2, 150)
        e18 = Enemy (1100, 400, enemy8_img, 2,150)
        e19 = Enemy (1250, 400, enemy8_img, 2, 150)
        e20 = Enemy (450, 550, enemy8_img, 2, 150)
        e21 = Enemy (600, 550, enemy8_img, 2, 150)
        e22 = Enemy (750, 550, enemy8_img, 2, 150)
        e23 = Enemy (900, 550, enemy8_img, 2, 150)
        e24 = Enemy (1050, 550, enemy8_img, 2, 150)
        e25 = Enemy (1200, 550, enemy8_img, 2, 150)
        e26 = Enemy (1350, 550, enemy8_img, 2, 150)
        e27 = Enemy (350, 100, enemy8_img, 2, 150)
        e28 = Enemy (1400, 100, enemy8_img, 2, 150)
        e29 = Enemy (300, 250, enemy8_img, 2, 150)
        e30 = Enemy (1500, 250, enemy8_img, 2, 150)
        e31 = Enemy (150, 250, enemy8_img, 2, 150)
        e32 = Enemy (1650, 250, enemy8_img, 2, 150)
        e33 = Enemy (350, 400, enemy8_img, 2, 150)
        e34 = Enemy (1400, 400, enemy8_img, 2, 150)
        e35 = Enemy (200, 400, enemy8_img, 2, 150)
        e36 = Enemy (1550, 400, enemy8_img, 2, 150)
        e37 = Enemy (300, 550, enemy8_img, 2, 150)
        e38 = Enemy (1500, 550, enemy8_img, 2, 150)

        
        enemies = Fleet(e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25, e26, e27, e28, e29, e30, e31, e32, e33, e34, e35, e36, e37, e38)

    elif player.level == 9:

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p1 = Asteroid (x, y, asteroidmed1_img)
        asteroids.add(p1)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p2 = Asteroid (x, y, asteroidmed3_img)
        asteroids.add(p2)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p3 = Asteroid (x, y, asteroidmed1_img)
        asteroids.add(p3)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p4 = Asteroid (x, y, asteroidsmall1_img)
        asteroids.add(p4)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p5 = Asteroid (x, y, asteroidsmall1_img)
        asteroids.add(p5)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p6 = Asteroid (x, y, asteroidmed3_img)
        asteroids.add(p6)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p7 = Asteroid (x, y, asteroidsmall2_img)
        asteroids.add(p7)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p8 = Asteroid (x, y, asteroidsmall2_img)
        asteroids.add(p8)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p9 = Asteroid (x, y, asteroidmed3_img)
        asteroids.add(p9)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p10 = Asteroid (x, y, asteroidmed1_img)
        asteroids.add(p10)
        
        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p11 = SuperfastPowerup (x,y, superfastpowerup_img)
        powerups.add(p11)
        
        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p12 = InvincibilityPowerup (x,y, invincibilitypowerup_img)
        powerups.add(p12)
        
        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p13 = ShieldPowerup (x,y, shieldpowerup_img)
        powerups.add(p13)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p14 = DoubleshotPowerup (x,y, pillpowerup_img)
        powerups.add(p14)

        e1 = Enemy (200, 100, enemy10_img, 1, 100)
        e2 = Enemy (350, 100, enemy10_img, 1, 100)
        e3 = Enemy (500, 100, enemy12_img, 2, 150)
        e4 = Enemy (650, 100, enemy12_img, 2, 150)
        e5 = Enemy (800, 100, enemy2_img, 3, 200)
        e6 = Enemy (950, 100, enemy2_img, 3, 200)
        e7 = Enemy (1100, 100, enemy12_img, 2, 150)
        e8 = Enemy (1250, 100, enemy12_img, 2, 150)
        e9 = Enemy (1400, 100, enemy10_img, 1, 100)
        e10 = Enemy (1550, 100, enemy10_img, 1, 100)

        e11 = Enemy (150, 250, enemy10_img, 1, 100)
        e12 = Enemy (300, 250, enemy10_img, 1, 100)
        e13 = Enemy (450, 250, enemy12_img, 2, 150)
        e14 = Enemy (600, 250, enemy12_img, 2, 150)
        e15 = Enemy (750, 250, enemy2_img, 3, 200)
        e16 = Enemy (900, 250, enemy2_img, 3, 200)
        e17 = Enemy (1050, 250, enemy2_img, 3, 200)
        e18 = Enemy (1200, 250, enemy12_img, 2, 150)
        e19 = Enemy (1350, 250, enemy12_img, 2, 150)
        e20 = Enemy (1500, 250, enemy10_img, 1, 100)
        e21 = Enemy (1650, 250, enemy10_img, 1, 100)

        e22 = Enemy (200, 400, enemy10_img, 1, 100)
        e23 = Enemy (350, 400, enemy10_img, 1, 100)
        e24 = Enemy (500, 400, enemy12_img, 2, 150)
        e25 = Enemy (650, 400, enemy12_img, 2, 150)
        e26 = Enemy (800, 400, enemy2_img, 3, 200)
        e27 = Enemy (950, 400, enemy2_img, 3, 200)
        e28 = Enemy (1100, 400, enemy12_img, 2, 150)
        e29 = Enemy (1250, 400, enemy12_img, 2, 150)
        e30 = Enemy (1400, 400, enemy10_img, 1, 100)
        e31 = Enemy (1550, 400, enemy10_img, 1, 100)

        e32 = Enemy (150, 550, enemy10_img, 1, 100)
        e33 = Enemy (300, 550, enemy10_img, 1, 100)
        e34 = Enemy (450, 550, enemy12_img, 2, 150)
        e35 = Enemy (600, 550, enemy12_img, 2, 150)
        e36 = Enemy (750, 550, enemy2_img, 3, 200)
        e37 = Enemy (900, 550, enemy2_img, 3, 200)
        e38 = Enemy (1050, 550, enemy2_img, 3, 200)
        e39 = Enemy (1200, 550, enemy12_img, 2, 150)
        e40 = Enemy (1350, 550, enemy12_img, 2, 150)
        e41 = Enemy (1500, 550, enemy10_img, 1, 100)
        e42 = Enemy (1650, 550, enemy10_img, 1, 100)
        
        enemies = Fleet(e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25, e26, e27, e28, e29, e30, e31, e32, e33, e34, e35, e36, e37, e38, e39, e40, e41, e42)

    elif player.level >= 10:

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p1 = Asteroid (x, y, asteroidmed1_img)
        asteroids.add(p1)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p2 = Asteroid (x, y, asteroidmed3_img)
        asteroids.add(p2)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p3 = Asteroid (x, y, asteroidmed1_img)
        asteroids.add(p3)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p4 = Asteroid (x, y, asteroidbig1_img)
        asteroids.add(p4)

        x = random.randint(0, WIDTH)
        y = random.randrange(-3000, -1000)
        p5 = Asteroid (x, y, asteroidbig4_img)
        asteroids.add(p5)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p6 = Asteroid (x, y, asteroidmed3_img)
        asteroids.add(p6)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p7 = Asteroid (x, y, asteroidbig2_img)
        asteroids.add(p7)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p8 = Asteroid (x, y, asteroidbig1_img)
        asteroids.add(p8)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p9 = Asteroid (x, y, asteroidmed3_img)
        asteroids.add(p9)

        x = random.randint(0, WIDTH)
        y = random.randrange(-4500, -1000)
        p10 = Asteroid (x, y, asteroidmed1_img)
        asteroids.add(p10)
        
        x = random.randint(0, WIDTH)
        y = random.randrange(-3000, -1000)
        p11 = SuperfastPowerup (x,y, superfastpowerup_img)
        powerups.add(p11)
        
        x = random.randint(0, WIDTH)
        y = random.randrange(-3000, -1000)
        p12 = InvincibilityPowerup (x,y, invincibilitypowerup_img)
        powerups.add(p12)
        
        x = random.randint(0, WIDTH)
        y = random.randrange(-3000, -1000)
        p13 = ShieldPowerup (x,y, shieldpowerup_img)
        powerups.add(p13)

        x = random.randint(0, WIDTH)
        y = random.randrange(-3000, -1000)
        p14 = DoubleshotPowerup (x,y, pillpowerup_img)
        powerups.add(p14)
        
        x = random.randint(0, WIDTH)
        y = random.randrange(-2500, -1000)
        p15 = PowershotPowerup (x,y, powershotpowerup_img)
        powerups.add(p15)

        e1 = Enemy (200, 100, enemy17_img, 3, 200)
        e2 = Enemy (350, 100, enemy17_img, 3, 200)
        e3 = Enemy (500, 100, enemy13_img, 5, 300)
        e4 = Enemy (650, 100, enemy13_img, 5, 300)
        e5 = Enemy (800, 100, enemy5_img, 10, 600)
        e6 = Enemy (950, 100, enemy5_img, 10, 600)
        e7 = Enemy (1100, 100, enemy13_img, 5, 300)
        e8 = Enemy (1250, 100, enemy13_img, 5, 300)
        e9 = Enemy (1400, 100, enemy17_img, 3, 200)
        e10 = Enemy (1550, 100, enemy17_img, 3, 200)

        e11 = Enemy (150, 250, enemy17_img, 3, 200)
        e12 = Enemy (300, 250, enemy17_img, 3, 200)
        e13 = Enemy (450, 250, enemy6_img, 5, 300)
        e14 = Enemy (600, 250, enemy6_img, 5, 300)
        e15 = Enemy (750, 250, enemy15_img, 10, 600)
        e16 = Enemy (900, 250, enemy15_img, 10, 600)
        e17 = Enemy (1050, 250, enemy15_img, 10, 600)
        e18 = Enemy (1200, 250, enemy6_img, 5, 300)
        e19 = Enemy (1350, 250, enemy6_img, 5, 300)
        e20 = Enemy (1500, 250, enemy17_img, 3, 200)
        e21 = Enemy (1650, 250, enemy17_img, 3, 200)

        e22 = Enemy (200, 400, enemy17_img, 3, 200)
        e23 = Enemy (350, 400, enemy17_img, 3, 200)
        e24 = Enemy (500, 400, enemy13_img, 5, 300)
        e25 = Enemy (650, 400, enemy13_img, 5, 300)
        e26 = Enemy (800, 400, enemy5_img, 10, 600)
        e27 = Enemy (950, 400, enemy5_img, 10, 600)
        e28 = Enemy (1100, 400, enemy13_img, 5, 300)
        e29 = Enemy (1250, 400, enemy13_img, 5, 300)
        e30 = Enemy (1400, 400, enemy17_img, 3, 200)
        e31 = Enemy (1550, 400, enemy17_img, 3, 200)

        e32 = Enemy (150, 550, enemy17_img, 3, 200)
        e33 = Enemy (300, 550, enemy17_img, 3, 200)
        e34 = Enemy (450, 550, enemy6_img, 5, 300)
        e35 = Enemy (600, 550, enemy6_img, 5, 300)
        e36 = Enemy (750, 550, enemy15_img, 10, 600)
        e37 = Enemy (900, 550, enemy15_img, 10, 600)
        e38 = Enemy (1050, 550, enemy15_img, 10, 600)
        e39 = Enemy (1200, 550, enemy6_img, 5, 300)
        e40 = Enemy (1350, 550, enemy6_img, 5, 300)
        e41 = Enemy (1500, 550, enemy17_img, 3, 200)
        e42 = Enemy (1650, 550, enemy17_img, 3, 200)
        
        enemies = Fleet(e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25, e26, e27, e28, e29, e30, e31, e32, e33, e34, e35, e36, e37, e38, e39, e40, e41, e42)

    lasers = pygame.sprite.Group()
    bombs = pygame.sprite.Group()

def display_stats():
    score_text = game_font.render("Score : " + str(player.score), True, WHITE)
    rect = score_text.get_rect()
    rect.top = 20
    rect.left = 20
    screen.blit(score_text, rect)

    level_text = game_font.render("Level : " + str(player.level), True, WHITE)
    rect = score_text.get_rect()
    rect.top = 20
    rect.right = WIDTH - 20
    screen.blit(level_text, rect)

    shield_text = game_font.render("Shield : " + str(ship.shield), True, WHITE)
    rect = score_text.get_rect()
    rect.bottom = HEIGHT - 20
    rect.left = 20
    screen.blit(shield_text, rect)

def start_screen():
    screen.fill(PURPLE)
    
    title_text = title_font.render(TITLE, True, WHITE)
    rect = title_text.get_rect()
    rect.centerx = WIDTH // 2
    rect.bottom = HEIGHT // 2 - 15
    screen.blit(title_text, rect)

    key_text = default_font.render("Use W A S D To Move, And Space To Shoot!", True, WHITE)
    rect = key_text.get_rect()
    rect.centerx = WIDTH // 2
    rect.bottom = HEIGHT // 2 + 45
    screen.blit(key_text, rect)

    sub_text = default_font.render("Press Space To Start", True, WHITE)
    rect = sub_text.get_rect()
    rect.centerx = WIDTH // 2
    rect.top = HEIGHT // 2 + 60
    screen.blit(sub_text, rect)

    rect = ship_img.get_rect()
    rect.centerx = WIDTH // 2
    rect.top = HEIGHT // 2 + 150
    screen.blit(ship_img, rect)


def end_screen():
    end_text = default_font.render("Game Over", True, WHITE)
    rect = end_text.get_rect()
    rect.centerx = WIDTH // 2
    rect.bottom = HEIGHT // 2
    screen.blit(end_text, rect)

    end_text = default_font.render("Press R To Restart", True, WHITE)
    rect = end_text.get_rect()
    rect.centerx = WIDTH // 2
    rect.top = HEIGHT // 2 + 15
    screen.blit(end_text, rect)
    
def win_screen():
    end_text = default_font.render("Congratulations, You Won!", True, WHITE)
    rect = end_text.get_rect()
    rect.centerx = WIDTH // 2
    rect.bottom = HEIGHT // 2
    screen.blit(end_text, rect)

    end_text = default_font.render("Press R To Play Again", True, WHITE)
    rect = end_text.get_rect()
    rect.centerx = WIDTH // 2
    rect.top = HEIGHT // 2 + 15
    screen.blit(end_text, rect)



# Game loop
new_game()
start_level()
stage = START

running = True

while running:
    # Input handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
                    pygame.mixer.music.load(theme_music)
                    pygame.mixer.music.play(-1)
            elif stage == PLAYING:
                if event.key == pygame.K_SPACE:
                    ship.shoot()
            elif stage == END or stage == WIN:
                if event.key == pygame.K_r:
                    new_game()
                    start_level()
                    stage = START
                    
    if stage == PLAYING:
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]:
            ship.move_left()
        elif pressed[pygame.K_d]:
            ship.move_right()
        elif pressed[pygame.K_s]:
            ship.move_down()
        elif pressed[pygame.K_w]:
            ship.move_up()

    
    # Game logic
    if stage != START:
        lasers.update()
        bombs.update()
        enemies.update()
        player.update()
        powerups.update()
        asteroids.update()
    if stage == PLAYING:
        if len(enemies) == 0:
            if player.level == 10:
                stage = WIN
                pygame.mixer.music.load(win_music)
                pygame.mixer.music.play(0)
            else:
                player.level += 1
                start_level()
        elif len(player) == 0:
            stage = END
            pygame.mixer.music.load(end_music)
            pygame.mixer.music.play(0)

    for loc in stars_locs:
        loc[0] += .35

        if loc[0] > WIDTH:
            loc[0] = random.randrange(-1 * WIDTH, -100)

    for loc in backgroundstars_locs:
        loc[0] += .15

        if loc[0] > WIDTH:
            loc[0] = random.randrange(-1 * WIDTH, -100)

    for loc in backbackgroundstars_locs:
        loc[0] += 0.005

        if loc[0] > WIDTH:
            loc[0] = random.randrange(-1 * WIDTH, -100)
            
    
    # Drawing code
    screen.fill(PURPLE)
    lasers.draw(screen)
    bombs.draw(screen)
    player.draw(screen)
    enemies.draw(screen)
    powerups.draw(screen)
    asteroids.draw(screen)
    display_stats()

    for loc in stars_locs:
        draw_stars(loc, WHITE)

    for loc in backgroundstars_locs:
        backgrounddraw_stars(loc, WHITE)

    for loc in backbackgroundstars_locs:
        backbackgrounddraw_stars(loc, DARKDARKERWHITE)

    if stage == START:
        start_screen()
    elif stage == END:
        end_screen()
    elif stage == WIN:
        win_screen()
    # Update screen
    pygame.display.update()


    # Limit refresh rate of game loop 
    clock.tick(FPS)


# Close window and quit
pygame.quit()

