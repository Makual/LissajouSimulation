import pygame
import math
import sys
import os

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

path = resource_path('freesansbold.ttf')

W = 800

H = W + 100
fps = 300

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen  = pygame.display.set_mode((W+10, H+10))
screen.fill(WHITE)
pygame.display.set_caption("lissajou")
clock = pygame.time.Clock()

mainLayer = pygame.Surface((W, W))
mainLayer.fill(WHITE)


tailsLayer = pygame.Surface((W, W))
tailsLayer.fill(WHITE)
tailsLayer.set_alpha(100)

bgLayer = pygame.Surface((W, W))
bgLayer.fill(WHITE)
bgLayer.set_alpha(100)


ctrlLayer = pygame.Surface((W, 100))
ctrlLayer.fill(WHITE)
ctrlLayer.set_alpha(255)

addCircleLayerLeft = pygame.Surface((15, W))
addCircleLayerLeft.fill(WHITE)

addCircleLayerDown = pygame.Surface((W, 20))
addCircleLayerDown.fill(WHITE)

fontObj = pygame.font.Font(path, 10)


#(tick-2*math.pi/1600)
gap = 10

def drawSinusoidA(a1,p1,f1):
    tick = 0

    while tick <= math.pi*2:
        
        if tick%(math.pi*2/round(f1/10))*30 > 0.5:
            x1 = tick%(math.pi*2/round(f1/10))*30
            y1 = -math.sin(((tick%(math.pi*2/round(f1/10)))+p1/30)*round(f1/10))*a1+W/2
            pygame.draw.line(tailsLayer, BLACK, (x1,y1) , (((tick-2*math.pi/(W/2))%(math.pi*2/round(f1/10)))*30, -math.sin((((tick-2*math.pi/(W/2))%(math.pi*2/round(f1/10)))+p1/30)*round(f1/10))*a1+W/2))
            
        tick += 2*math.pi/W
        
def drawSinusoidB(a2,p2,f2):
    tick = 0
 
    while tick <= 2*math.pi:
        if ((tick%(math.pi*2/round(f2/10)))%(2*math.pi))*30 > 1:
            x2 = -math.sin(((tick%(math.pi*2/round(f2/10)))+p2/30)*round(f2/10))*a2+W/2
            y2 = W-((tick%(math.pi*2/round(f2/10)))%(2*math.pi))*30
            pygame.draw.line(tailsLayer, BLACK, (x2,y2),(-math.sin((((tick-2*math.pi/W)%(math.pi*2/round(f2/10)))+p2/30)*round(f2/10))*a2+W/2,W-(((tick-2*math.pi/W)%(math.pi*2/round(f2/10)))%(2*math.pi))*30))
        tick += 2*math.pi/W



#Отрисовка всех хвостов
def drawTails(a1,a2,p1,p2,f1,f2):
    tailsLayer.fill(WHITE)
    drawSinusoidA(a1,p1,f1)
    drawSinusoidB(a2,p2,f2)




#Обработка слайдеров
def updateControllers(a1,a2,p1,p2,f1,f2,fps):
    if (pygame.mouse.get_pressed()[0] != 0) and (pygame.mouse.get_pos()[0] < 100) and (pygame.mouse.get_pos()[1] > W+20) and ((pygame.mouse.get_pos()[1] < W+50)):
        a1 = pygame.mouse.get_pos()[0] - 5
        if (a1 < 10):
            a1 = 10
        if (a1 > 100):
            a1 = 100

    if (pygame.mouse.get_pressed()[0] != 0) and (pygame.mouse.get_pos()[0] > W-100) and (pygame.mouse.get_pos()[1] > W+20) and ((pygame.mouse.get_pos()[1] < W+50)):
        a2 = pygame.mouse.get_pos()[0] - 5  - W + 100
        if (a2 < 10):
            a2 = 10
        if (a2 > 90):
            a2 = 90

    if (pygame.mouse.get_pressed()[0] != 0) and (pygame.mouse.get_pos()[0] > W-100) and (pygame.mouse.get_pos()[1] > W+50) and ((pygame.mouse.get_pos()[1] < W+80)):
        p2 = pygame.mouse.get_pos()[0] - 5 - W + 100
        if (p2 < 10):
            p2 = 10
        if (p2 > 90):
            p2 = 90

    if (pygame.mouse.get_pressed()[0] != 0) and (pygame.mouse.get_pos()[0] < 100) and (pygame.mouse.get_pos()[1] > W+80) and ((pygame.mouse.get_pos()[1] < W+110)):
        f1 = pygame.mouse.get_pos()[0] - 5
        if (f1 < 10):
            f1 = 10
        if (f1 > 100):
            f1 = 100

    if (pygame.mouse.get_pressed()[0] != 0) and (pygame.mouse.get_pos()[0] > W-100) and (pygame.mouse.get_pos()[1] > W+80) and ((pygame.mouse.get_pos()[1] < W+110)):
        f2 = pygame.mouse.get_pos()[0] - 5 - W + 100
        if (f2 < 10):
            f2 = 10
        if (f2 > 90):
            f2 = 90
    
    if (pygame.mouse.get_pressed()[0] != 0) and (pygame.mouse.get_pos()[0] > W/2-150) and (pygame.mouse.get_pos()[0] < W/2+150) and (pygame.mouse.get_pos()[1] > W+10) and ((pygame.mouse.get_pos()[1] < W+100)):
        fps = pygame.mouse.get_pos()[0] - 5 - 250
        
        if (fps < 15):
            fps = 15
        if (fps > 300):
            fps = 300

    if (pygame.mouse.get_pressed()[0] != 0):    
         drawTails(a1,a2,p1,p2,f1,f2)    
    return a1,a2,p1,p2,f1,f2,fps




a1 = 50 #Амплитуда
a2 = 50
p1 = 0 #Смещение по фазе
p2 = 10
f1 = 10 #Частота
f2 = 10

updateControllers(a1,a2,p1,p2,f1,f2,fps)
drawSinusoidA(a1,p1,f1)
drawSinusoidB(a2,p2,f2)

tick = 0



#Отрисовка поля
pygame.draw.line(bgLayer, BLACK, (W/2,0),(W/2,W),1)
pygame.draw.line(bgLayer, BLACK, (0,W/2),(W,W/2),1)
pygame.draw.line(bgLayer, BLACK, (0,W),(W,W),1)



#Предотрисовка Ручек
pygame.draw.rect(ctrlLayer, BLACK, (0, 20, 100,2))
pygame.draw.rect(ctrlLayer, BLACK, (W-100, 20, 100, 2))
pygame.draw.rect(ctrlLayer, BLACK, (W-100, 50, 100,2))
pygame.draw.rect(ctrlLayer, BLACK, (0, 80, 100,2))
pygame.draw.rect(ctrlLayer, BLACK, (W-100, 80, 100,2))
pygame.draw.rect(ctrlLayer, BLACK, (W/2-150, 50, 300,2))

pygame.draw.ellipse(ctrlLayer, BLACK, (a1, 14, 15, 15))
pygame.draw.ellipse(ctrlLayer, BLACK, (a2+W-100, 14, 15, 15))
pygame.draw.ellipse(ctrlLayer, BLACK, (p2+W-100, 44, 15, 15))
pygame.draw.ellipse(ctrlLayer, BLACK, (f1, 74, 15, 15))
pygame.draw.ellipse(ctrlLayer, BLACK, (f2+W-100, 74, 15, 15))
pygame.draw.ellipse(ctrlLayer, BLACK, (fps+W/4+50, 44, 15, 15))

textF1 = fontObj.render(str(round(f1/10)), True, BLACK)
textF2 = fontObj.render(str(round(f2/10)), True, BLACK)

#Основной цикл
running = True
while running:
    mainLayer.fill(WHITE)
    addCircleLayerLeft.fill(WHITE)
    addCircleLayerDown.fill(WHITE)
    clock.tick(fps)

    #Выход
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Слайдеры
    if pygame.mouse.get_pos()[1] > W:
        a1,a2,p1,p2,f1,f2,fps = updateControllers(a1,a2,p1,p2,f1,f2,fps)

        ctrlLayer.fill(WHITE)

        #Отрисовка линий
        pygame.draw.rect(ctrlLayer, BLACK, (0, 20, 100,2))
        pygame.draw.rect(ctrlLayer, BLACK, (W-100, 20, 100, 2))
        pygame.draw.rect(ctrlLayer, BLACK, (W-100, 50, 100,2))
        pygame.draw.rect(ctrlLayer, BLACK, (0, 80, 100,2))
        pygame.draw.rect(ctrlLayer, BLACK, (W-100, 80, 100,2))

        pygame.draw.rect(ctrlLayer, BLACK, (W/2-150, 50, 300,2))

        
        #Отрисовка ручек
        pygame.draw.ellipse(ctrlLayer, BLACK, (a1, 14, 15, 15))
        pygame.draw.ellipse(ctrlLayer, BLACK, (a2+W-100, 14, 15, 15))
        pygame.draw.ellipse(ctrlLayer, BLACK, (p2+W-100, 44, 15, 15))
        pygame.draw.ellipse(ctrlLayer, BLACK, (f1, 74, 15, 15))
        pygame.draw.ellipse(ctrlLayer, BLACK, (f2+W-100, 74, 15, 15))

        pygame.draw.ellipse(ctrlLayer, BLACK, (fps+W/4+50, 44, 15, 15))

        
        #Отрисовка чисел
        textF1 = fontObj.render(str(round(f1/10)), True, BLACK)
        textF2 = fontObj.render(str(round(f2/10)), True, BLACK)

 

    x1 = (tick%(math.pi*2/round(f1/10)))*30-5
    y1 = -math.sin(((tick%(math.pi*2/round(f1/10)))+p1/30)*round(f1/10))*a1+W/2-5

    x2 = -math.sin(((tick%(math.pi*2/round(f2/10)))+p2/30)*round(f2/10))*a2+W/2-5
    y2 = W-5-((tick%(math.pi*2/round(f2/10)))%(2*math.pi))*30
    
    #Первая синусоида
    pygame.draw.ellipse(mainLayer, RED, (x1,y1,10,10))
    #Вторая синусоида
    pygame.draw.ellipse(mainLayer, BLUE, (x2,y2,10,10))


    #Отрисовка дополнительных пометок
    pygame.draw.ellipse(addCircleLayerLeft, RED, (0,y1,10,10))
    pygame.draw.ellipse(addCircleLayerDown, BLUE, (x2,0,10,10))
    
    #Результат
    pygame.draw.ellipse(mainLayer, GREEN, (x2,y1,10,10))
    pygame.draw.line(tailsLayer, BLACK, (x2+5,y1+5),(-math.sin((((tick-2*math.pi/(W*2))%(math.pi*2/round(f2/10)))+p2/30)*round(f2/10))*a2+W/2,-math.sin((((tick-2*math.pi/(W*2))%(math.pi*2/round(f1/10)))+p1/30)*round(f1/10))*a1+W/2))



    #Соединительные линии        
    pygame.draw.line(mainLayer, RED, (x1+5,y1+5), (-math.sin((tick+p2/30)*round(f2/10))*a2+W/2,-math.sin((tick+p1/30)*round(f1/10))*a1+W/2))
    pygame.draw.line(mainLayer, BLUE, (x2+5,y2+5), (-math.sin((tick+p2/30)*round(f2/10))*a2+W/2,-math.sin((tick+p1/30)*round(f1/10))*a1+W/2))
    
    #Счет тиков для отрисовки
    tick += 2*math.pi/(W*2)



    #Наложение слоев
    
    screen.blit(addCircleLayerLeft, (0, 0))
    screen.blit(mainLayer, (20, 0))
    screen.blit(bgLayer, (20, 0))
    screen.blit(tailsLayer, (20, 0))
    screen.blit(ctrlLayer, (0, W+20))
    
    screen.blit(textF1,(120,W+95))
    screen.blit(textF2,(W-120,W+95))
    screen.blit(addCircleLayerDown, (20, W+10))
    pygame.display.flip()

sys.exit()
#pygame.quit()
