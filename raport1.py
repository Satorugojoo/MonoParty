import time 
import random
import pygame as py
import sys
#import time
from pygame.locals import *

mainClock = py.time.Clock()

py.init()
py.display.set_caption('Party Time')
screen = py.display.set_mode((1920, 1080), 0, 32)
font_A = py.font.SysFont('None', 70)
font_S = py.font.SysFont('None', 50)
font_B = py.font.SysFont('None', 100)
click = False

A = [[1530,870],[1330,870],[1130,870],[930,870],[730,870],[530,870],[330,870],[130,870],[330,870],[530,720],[730,720],[930,720],[1130,720],[1330,720],[1530,720]]

#def Gracz1_ruch():
    #Pole = (random.randint(0, 5))
    #print(Pole)
    #i = Pole;
    #x_chopek = A[i][0];
    #y_chopek = A[i][1];

class Gracz(object):
    def __init__(self, x, y, width, height):
        self.wlewo = [py.image.load('elementy/GL1.png'), py.image.load('elementy/GL2.png'),
                      py.image.load('elementy/GL3.png'), py.image.load('elementy/GL4.png'),
                      py.image.load('elementy/GL5.png'), py.image.load('elementy/GL6.png'),
                      py.image.load('elementy/GL7.png'), py.image.load('elementy/GL8.png'),
                      py.image.load('elementy/GL9.png')]

        self.wprawo = [py.image.load("elementy/GR1.png"), py.image.load('elementy/GR2.png'),
                       py.image.load('elementy/GR3.png'), py.image.load('elementy/GR4.png'),
                       py.image.load('elementy/GR5.png'), py.image.load('elementy/GR6.png'),
                       py.image.load('elementy/GR7.png'), py.image.load('elementy/GR8.png'),
                       py.image.load('elementy/GR9.png')]

        self.stoi = py.image.load('elementy/gracz.png')
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.move = 9
        self.jump = 0
        self.jumped = False
        self.left = False
        self.right = False
        self.walk = 0
        self.in_air = False

    def draw(self):
        if self.walk + 1 >= 27:
            self.walk = 0
        if self.left:
            screen.blit(self.wlewo[self.walk//3], (self.x, self.y))
            self.walk += 1
        elif self.right:
            screen.blit(self.wprawo[self.walk//3], (self.x, self.y))
            self.walk += 1
        else:
            screen.blit(self.stoi, (self.x, self.y))

    def ruch(self):
        dy = 0

        keys = py.key.get_pressed()
        if (keys[py.K_a] or keys[py.K_LEFT]) and self.x > self.move:
            self.x -= self.move
            self.left = True
            self.right = False
        elif (keys[py.K_d] or keys[py.K_RIGHT]) and self.x < screen.get_width() - self.width:
            self.x += self.move
            self.left = False
            self.right = True
        else:
            self.right = False
            self.left = False
            self.walk = 0

class Gracz2(object):
    def __init__(self, x, y, width, height):
        self.wlewo = [py.image.load('elementy/GL1.png'), py.image.load('elementy/GL2.png'),
                      py.image.load('elementy/GL3.png'), py.image.load('elementy/GL4.png'),
                      py.image.load('elementy/GL5.png'), py.image.load('elementy/GL6.png'),
                      py.image.load('elementy/GL7.png'), py.image.load('elementy/GL8.png'),
                      py.image.load('elementy/GL9.png')]

        self.wprawo = [py.image.load("elementy/GR1.png"), py.image.load('elementy/GR2.png'),
                       py.image.load('elementy/GR3.png'), py.image.load('elementy/GR4.png'),
                       py.image.load('elementy/GR5.png'), py.image.load('elementy/GR6.png'),
                       py.image.load('elementy/GR7.png'), py.image.load('elementy/GR8.png'),
                       py.image.load('elementy/GR9.png')]

        self.stoi = py.image.load('elementy/gracz2.png')
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.move = 9
        self.jump = 0
        self.jumped = False
        self.left = False
        self.right = False
        self.walk = 0
        self.in_air = False

    def draw(self):
        if self.walk + 1 >= 27:
            self.walk = 0
        if self.left:
            screen.blit(self.wlewo[self.walk//3], (self.x, self.y))
            self.walk += 1
        elif self.right:
            screen.blit(self.wprawo[self.walk//3], (self.x, self.y))
            self.walk += 1
        else:
            screen.blit(self.stoi, (self.x, self.y))

    def ruch(self):
        dy = 0

        keys = py.key.get_pressed()
        if (keys[py.K_a] or keys[py.K_LEFT]) and self.x > self.move:
            self.x -= self.move
            self.left = True
            self.right = False
        elif (keys[py.K_d] or keys[py.K_RIGHT]) and self.x < screen.get_width() - self.width:
            self.x += self.move
            self.left = False
            self.right = True
        else:
            self.right = False
            self.left = False
            self.walk = 0
        
            
def draw_text(text, font, color, surface, x, y):

    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    global click
    while True:

        tlo = py.image.load('tło_menu.jpg')
        screen.fill((0, 0, 0))
        screen.blit(tlo, (0, 0))

        mx, my = py.mouse.get_pos()

        button_1 = py.Rect(775, 100, 200, 55)
        button_2 = py.Rect(775, 300, 200, 55)
        button_3 = py.Rect(775, 500, 200, 55)
        button_6 = py.Rect(1700, 1000, 200, 60)

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        if button_3.collidepoint((mx, my)):
            if click:
                py.quit()
                sys.exit(0)
        if button_6.collidepoint((mx, my)):
            if click:
                tworcy()

        py.draw.rect(screen, (123, 17, 179), button_1)
        py.draw.rect(screen, (123, 17, 179), button_2)
        py.draw.rect(screen, (123, 17, 179), button_3)
        py.draw.rect(screen, (123, 17, 179), button_6)

        draw_text('Twórcy', font_A, (120, 30, 30), screen, 1700, 1000)
        
        screen.blit(py.image.load('start.jpg'), (775, 100))
        screen.blit(py.image.load('wejście.jpg'), (775, 300))
        screen.blit(py.image.load('end.jpg'), (775, 500))

        click = False
        for event in py.event.get():
            if event.type == QUIT:
                py.quit()
                sys.exit(0)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    py.quit()
                    sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        py.display.update()
        mainClock.tick(60)
        
def przycisk_main(x, y):
    global click
    mx, my = py.mouse.get_pos()
    button_5 = py.Rect(x, y, 250, 60)
    py.draw.rect(screen, (70, 35, 242), button_5)
    draw_text('Menu Główne', font_S, (120, 30, 30), screen, x + 10, y + 5)

    if button_5.collidepoint((mx, my)):
        if click:
            main_menu()
    for event in py.event.get():
        if event.type == QUIT:
            py.quit()
            sys.exit(0)
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                main_menu()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
                
def game():
    global click
    click = False

    # dane pozycji i rozmiaru gracza
    y_chopek = 875
    x_chopek = 1700
    chopek_width = 25
    chopek_height = 64
    
    y_chopek2 = 875
    x_chopek2 = 1780
    chopek_width = 25
    chopek_height = 64

    chopek = Gracz(x_chopek, y_chopek, chopek_width, chopek_height)
    chopek2 = Gracz2(x_chopek2, y_chopek2, chopek_width, chopek_height)
    
    tlo = py.image.load('plansza.jpg')
    running = True
    screen.blit(tlo, (0, 0))
    
    while running:

        #tlo = py.image.load('plansza.jpg')

        #screen.fill((0, 0, 0))
        #screen.blit(tlo, (0, 0))
        przycisk_main(800, 5)
        chopek.draw()
        chopek2.draw()

        py.display.update()
        mainClock.tick(60)

        # ruch gracza

        #chopek.ruch()
        #chopek2.ruch()
        
        #Pole = (random.randint(0, 5))
        #print(Pole)
        #i = Pole;
        #x_chopek = A[i][0];
        #y_chopek = A[i][1];

        py.display.flip()
        mainClock.tick(60)
        
        for m in range(1):
            kostka = (random.randint(0, 5))
            #print(Pole)
            i = kostka;
            x_chopek = A[i][0];
            y_chopek = A[i][1];
            print(x_chopek, y_chopek)
            chopek.draw()
            py.display.update() 
            py.display.flip()
            time.sleep(5)   
            
def options():
    running = True

    global click
    click = False

    while running:

        screen.fill((0, 0, 0))
        draw_text('Gra składa się z dwóch trybów', font_A, (255, 255, 255), screen, 20, 20)

        draw_text(' Party Mode  - w tym trybie 4 graczy wyląduje na planszy, na której będą się znajdować pola kilku',font_S,(255, 255, 255), screen, 20, 100)
        draw_text('różnych kolorach oraz gwiazdka. Celem każdego z graczy będzie zebranie największej ilości gwiazdek',font_S,(255, 255, 255), screen, 20, 130)
        draw_text('spośród uczestników. Aby zebrać gwiazdkę potrzebujemy monety, które będziemy zdobywać po drodze.',font_S,(255, 255, 255), screen, 20, 160)
        draw_text(' Po drodze będą się  również znajdować wspomagacze, a także pułapki. Gra będzie trwała prawdopodobnie',font_S,(255, 255, 255), screen, 20, 190)
        draw_text('kilkanaście lub kilkadziesiąt tur (gracze sami będą mogli ustawiać długość rozgrywki).',font_S,(255, 255, 255), screen, 20, 220)
        
        draw_text(' KO Stage – w tym trybie 8 graczy będzie rywalizowało w formacie pucharowym o tytuł', font_S,(255, 255, 255), screen, 20, 270)
        draw_text('Mistrza Gwiazd. W odróżnieniu od Party Mode tutaj rywalizacja będzie miała miejsce na', font_S,(255, 255, 255), screen, 20, 300)
        draw_text('planszy, której droga prowadzi do gwiazdy (bez pętli jak w poprzednim trybie) i kto pierwszy', font_S,(255, 255, 255), screen, 20, 330)
        draw_text('ten wygrywa. Oczywiście pojedynki są w formie 1 vs 1 (przegrany odpada, zwycięzca przechodzi dalej).', font_S,(255, 255, 255), screen, 20, 360)

        # przycisk Main Menu

        przycisk_main(800, 5)

        py.display.update()
        mainClock.tick(60)


def tworcy():
    running = True

    global click
    click = False

    while running:
        tlo = py.image.load('tło_menu.jpg')
        screen.fill((0, 0, 0))
        screen.blit(tlo, (0, 0))
        draw_text(' Miłosz Kapłanek ', font_B, (15, 69, 29), screen, 600, 400)

        # przycisk Main Menu

        przycisk_main(800, 5)

        py.display.update()
        mainClock.tick(60)


main_menu()