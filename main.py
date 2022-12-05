import pygame
import random
import math
from pygame import mixer

mixer.init()
pygame.init()

mixer.music.load('background_music.mp3')
mixer.music.play(-1)

screen = pygame.display.set_mode((1240, 700))
pygame.display.set_caption('Space Shooter Game')
ufo_icon = pygame.image.load('ufo (1).png')
pygame.display.set_icon(ufo_icon)

background = pygame.image.load('space1.jpg')

spaceship_img = pygame.image.load('spaceship.png')

alien1 = []
alien1X = []
alien1Y = []
alien_speed1X = []
alien_speed1Y = []
alien2 = []
alien2X = []
alien2Y = []
alien_speed2X = []
alien_speed2Y = []
alien3 = []
alien3X = []
alien3Y = []
alien_speed3X = []
alien_speed3Y = []
alien4 = []
alien4X = []
alien4Y = []
alien_speed4X = []
alien_speed4Y = []

no_of_aliens = 4

for i in range(no_of_aliens):
    alien1.append(pygame.image.load('cool.png'))
    alien1X.append(random.randint(0, 1176))
    alien1Y.append(random.randint(30, 175))
    alien2.append(pygame.image.load('ufo (2).png'))
    alien2X.append(random.randint(0, 1176))
    alien2Y.append(random.randint(30, 175))
    alien3.append(pygame.image.load('alien.png'))
    alien3X.append(random.randint(0, 1176))
    alien3Y.append(random.randint(30, 175))
    alien4.append(pygame.image.load('alien (1).png'))
    alien4X.append(random.randint(0, 1176))
    alien4Y.append(random.randint(30, 175))

    alien_speed1X.append(-0.45)
    alien_speed1Y.append(40)
    alien_speed2X.append(-0.5)
    alien_speed2Y.append(40)
    alien_speed3X.append(-0.55)
    alien_speed3Y.append(40)
    alien_speed4X.append(-0.7)
    alien_speed4Y.append(40)

score_img = pygame.image.load('high-score.png')
gameover_img = pygame.image.load('sad.png')
score = 0

bullet = pygame.image.load('bullet (1).png')
check = False
bulletX = 556
bulletY = 571

spaceshipX = 590
spaceshipY = 560
changeX = 0
running = True

font = pygame.font.SysFont('Serif', 35, 'bold')


def score_text():
    screen.blit(score_img, (10, 10))
    img = font.render(f'Score: {score}', True, 'white')
    screen.blit(img, (48, 10))


font_gameOver = pygame.font.SysFont('Arial', 64, 'bold')


def game_over():
    img_gameover = font_gameOver.render('GAME OVER', True, 'white')
    screen.blit(img_gameover, (350, 292))
    screen.blit(gameover_img, (728, 292))


while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX = -1.5
            if event.key == pygame.K_RIGHT:
                changeX = 1.5
            if event.key == pygame.K_SPACE:
                if check is False:
                    bullets = mixer.Sound('laser.mp3')
                    bullets.play()
                    check = True
                    bulletX = spaceshipX + 16

        if event.type == pygame.KEYUP:
            changeX = 0

    spaceshipX += changeX
    if spaceshipX <= 0:
        spaceshipX = 0
    elif spaceshipX >= 1176:
        spaceshipX = 1176
    for i in range(no_of_aliens):
        if alien4Y[i] > 530:
            for j in range(no_of_aliens):
                alien4Y[i] = 10000
                alien3Y[i] = 10000
                alien2Y[i] = 10000
                alien1Y[i] = 10000
            game_over()
            break
        if alien3Y[i] > 530:
            for j in range(no_of_aliens):
                alien4Y[i] = 10000
                alien3Y[i] = 10000
                alien2Y[i] = 10000
                alien1Y[i] = 10000
            game_over()
            break
        if alien2Y[i] > 530:
            for j in range(no_of_aliens):
                alien4Y[i] = 10000
                alien3Y[i] = 10000
                alien2Y[i] = 10000
                alien1Y[i] = 10000
            game_over()
            break
        if alien1Y[i] > 530:
            for j in range(no_of_aliens):
                alien4Y[i] = 10000
                alien3Y[i] = 10000
                alien2Y[i] = 10000
                alien1Y[i] = 10000
            game_over()
            break
        alien1X[i] += alien_speed1X[i]
        if alien1X[i] <= 0:
            alien_speed1X[i] = 0.45
            alien1Y[i] += alien_speed1Y[i]
        if alien1X[i] >= 1176:
            alien_speed1X[i] = -0.45
            alien1Y[i] += alien_speed1Y[i]

        alien2X[i] += alien_speed2X[i]
        if alien2X[i] <= 0:
            alien_speed2X[i] = 0.5
            alien2Y[i] += alien_speed2Y[i]
        if alien2X[i] >= 1176:
            alien_speed2X[i] = -0.5
            alien2Y[i] += alien_speed2Y[i]

        alien3X[i] += alien_speed3X[i]
        if alien3X[i] <= 0:
            alien_speed3X[i] = 0.55
            alien3Y[i] += alien_speed3Y[i]
        if alien3X[i] >= 1176:
            alien_speed3X[i] = -0.55
            alien3Y[i] += alien_speed3Y[i]

        alien4X[i] += alien_speed4X[i]
        if alien4X[i] <= 0:
            alien_speed4X[i] = 0.7
            alien4Y[i] += alien_speed4Y[i]
        if alien4X[i] >= 1176:
            alien_speed4X[i] = -0.7
            alien4Y[i] += alien_speed4Y[i]

        distance1 = math.sqrt(math.pow(bulletX - alien1X[i], 2) + math.pow(bulletY - alien1Y[i], 2))
        distance2 = math.sqrt(math.pow(bulletX - alien2X[i], 2) + math.pow(bulletY - alien2Y[i], 2))
        distance3 = math.sqrt(math.pow(bulletX - alien3X[i], 2) + math.pow(bulletY - alien3Y[i], 2))
        distance4 = math.sqrt(math.pow(bulletX - alien4X[i], 2) + math.pow(bulletY - alien4Y[i], 2))
        if distance1 < 27:
            ex1 = mixer.Sound('explosion-01.mp3')
            ex1.play()
            bulletY = 571
            check = False
            alien1X[i] = random.randint(0, 1176)
            alien1Y[i] = random.randint(30, 175)
            score += 1
        if distance2 < 27:
            ex2 = mixer.Sound('explosion-01.mp3')
            ex2.play()
            bulletY = 571
            check = False
            alien2X[i] = random.randint(0, 1176)
            alien2Y[i] = random.randint(30, 175)
            score += 1

        if distance3 < 27:
            ex3 = mixer.Sound('explosion-01.mp3')
            ex3.play()
            bulletY = 571
            check = False
            alien3X[i] = random.randint(0, 1176)
            alien3Y[i] = random.randint(30, 175)
            score += 1

        if distance4 < 27:
            ex4 = mixer.Sound('explosion-01.mp3')
            ex4.play()
            bulletY = 571
            check = False
            alien4X[i] = random.randint(0, 1176)
            alien4Y[i] = random.randint(30, 175)
            score += 1
        screen.blit(alien1[i], (alien1X[i], alien1Y[i]))
        screen.blit(alien2[i], (alien2X[i], alien2Y[i]))
        screen.blit(alien3[i], (alien3X[i], alien3Y[i]))
        screen.blit(alien4[i], (alien4X[i], alien4Y[i]))

    if bulletY <= 0:
        bulletY = 582
        check = False
    if check:
        screen.blit(bullet, (bulletX, bulletY))
        bulletY -= 1.5

    screen.blit(spaceship_img, (spaceshipX, spaceshipY))

    score_text()
    pygame.display.update()
