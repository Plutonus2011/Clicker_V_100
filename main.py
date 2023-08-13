import pygame
import time
from time import sleep
from random import randint
pygame.init()
back = (200, 255, 255) #колір фону (background)
mw = pygame.display.set_mode((500, 500)) #вікно програми (main window)
mw.fill(back)
clock = pygame.time.Clock()
'''клас прямокутник'''
class Area():
  def __init__(self, x=0, y=0, width=10, height=10, color=None):
      self.rect = pygame.Rect(x, y, width, height) #прямокутник
      self.fill_color = color
  def color(self, new_color):
      self.fill_color = new_color
  def fill(self):
      pygame.draw.rect(mw, self.fill_color, self.rect)
  def outline(self, frame_color, thickness): #обведення існуючого прямокутника
      pygame.draw.rect(mw, frame_color, self.rect, thickness)   
  def collidepoint(self, x, y):
      return self.rect.collidepoint(x, y)      
'''клас напис'''
class Label(Area):
  def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
      self.image = pygame.font.SysFont('pixel', fsize).render(text, True, text_color)
  def draw(self, shift_x=0, shift_y=0):
      self.fill()
      mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self, shift_x=0, shift_y=0):
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

    

RED = (255, 0, 0)
GREEN = (255, 255, 255)
YELLOW = (255, 255, 255)
DARK_BLUE = (0, 0, 100)
BLUE = (0, 0, 100)
LIGHT_GREEN = (255, 255, 250)
LIGHT_RED = (255, 0, 0)
cards = []
num_cards = 2
x = 110


start_time = time.time()
cur_time = start_time


''' інтерфейс гри'''


time_text = Label(0,0,50,50,back)
time_text.set_text('Time in game:',40, DARK_BLUE)
time_text.draw(20, 20)


timer = Label(50,55,50,40,back)
timer.set_text('0', 40, DARK_BLUE)
timer.draw(0,0)


score_text = Label(380,0,50,50,back)
score_text.set_text('Clicks:',45, DARK_BLUE)
score_text.draw(20,20)


score = Label(430,55,50,40,back)
score.set_text('0', 40, DARK_BLUE)
score.draw(0,0)

last = Label(430,55,50,40,back)
last.set_text('')

# Замість циклу for, створюємо тільки одну карточку
new_card = Picture('ball.jpg', 200, 170, 70, 100)
new_card.outline(BLUE, 10)
cards.append(new_card)

wait = 0
points = 0
a = 1
b = 10

from random import randint

while True:
 # Відмальовування картки
 if wait == 0:
  wait = 20
  click = 1  # Карточка завжди буде обраною
  cards[0].draw(10, 40)
 else:
  wait -= 1
  
 for event in pygame.event.get():
  if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
   x, y = event.pos
   # Шукаємо, чи попав клік на картку
   if cards[0].collidepoint(x, y):
    if click == 1:
     cards[0].color(GREEN)
     points += a
    else:
     if points >= b:
      cards[0].color(RED)
      points -= b
      b *= 5
      a += 1
    cards[0].fill()
    score.set_text(str(points), 40, DARK_BLUE)
    score.draw(0, 0)

 # Останній код та перемога/поразка залишаються без змін
 '''Перемога та поразка'''
 new_time = time.time()


 if int(new_time) - int(cur_time) == 1: 
  timer.set_text(str(int(new_time - start_time)),40, DARK_BLUE)
  timer.draw(0,0)
  cur_time = new_time

 if points <= -100:
  win = Label(0, 0, 500, 500, LIGHT_GREEN)
  win.set_text("You lose!!!", 60, DARK_BLUE)
  win.draw(140, 180)
  resul_time = Label(90, 230, 250, 250, LIGHT_GREEN)
  resul_time.set_text("time: " + str (int(new_time - start_time)) + " sec",40, DARK_BLUE)
  
  resul_time.draw(0, 0)
  break


 pygame.display.update()
 clock.tick(40)
