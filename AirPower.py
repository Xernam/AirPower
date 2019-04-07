import pygame
import random
import time
pygame.init()

x = 0
y = 100
width = 20
height = 20
vel = 10
tempx = 0
tempy = 0
PTComplete = False

win = pygame.display.set_mode((700, 700))
pygame.font.init()
pygame.display.set_caption("The Armory")
def text_objects(text, font):
 textSurface = font.render(text, True, (255, 0, 0))
 return textSurface, textSurface.get_rect()
	
def message_display(text):
 largeText = pygame.font.Font('freesansbold.ttf',12)
 TextSurf, TextRect = text_objects(text, largeText)
 TextRect.center = (50,20)
 win.blit(TextSurf, TextRect)

 pygame.display.update()

    #time.sleep(2)

    #game_loop()


class Wall:
 def __init__(self, x1, x2, y1, y2):
  self.x1 = x1
  self.y1 = y1
  self.x2 = x2
  self.y2 = y2
 def contains(self,x,y):
  if(x>=self.x1 and x<=self.x2 and y>=self.y1 and y<=self.y2):
   return True
  return False

w1 = Wall(140, 160, 70, 490)
w2 = Wall(140, 690, 470, 490)
w3 = Wall(230, 690, 70, 90)
w4 = Wall(230, 250, 0, 170)
w5 = Wall(0, 70, 70, 90)
w6 = Wall(0, 70, 180, 200)
w7 = Wall(50, 70, 120, 190)
w8 = Wall(50, 70, 240, 440)
w9 = Wall(0, 70, 490, 700)
w10 = Wall(140, 160, 540, 640)
w11 = Wall(210, 230, 540, 570)
w12 = Wall(210, 260, 570, 590)
w13 = Wall(260, 280, 570, 640)
w14 = Wall(140, 210, 630, 650)
w15 = Wall(210, 700, 540, 560)
w16 = Wall(670, 700, 470, 550)
w17 = Wall(260, 330, 570, 590)
w18 = Wall(310, 330, 630, 700)
def blocked(x,y):
 if((w1.contains(x,y)) or (w2.contains(x,y)) or (w3.contains(x,y)) or (w4.contains(x,y)) or (w5.contains(x,y))
  or w6.contains(x,y) or w7.contains(x,y) or w8.contains(x,y) or w9.contains(x,y) or w10.contains(x,y)
  or w11.contains(x,y) or w12.contains(x,y) or w13.contains(x,y) or w14.contains(x,y) or w15.contains(x,y)
  or w16.contains(x,y) or w17.contains(x,y) or w18.contains(x,y)):
  return True
 return False


run = True
while run:
 pygame.time.delay(100)
 keys = pygame.key.get_pressed()
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   run = False
 if x==0 and y==100:
  PTComplete = False
 
 
 
 
 
 
 
 
 #500, 350
 if (x-500<=40 and 500-x<=40 and y-350<=40 and 350-y<=40 and not PTComplete):
  #Store location of player
  tempx = x
  tempy = y
  PTComplete = True
  #Run PT code
  pygame.display.set_caption("PT")
  exercises = 0
  x = 50
  y = 50
  width = 40
  height = 60
  vel = 10
  strength = 10
  timer = 0;
  timer2 = 0;
  talked = False
  repsNeeded = 5
  repsCompleted = 0;
  repx = random.randint(1, 660)
  repy = random.randint(1, 640)
  run = True
  while run and exercises<5:
   pygame.time.delay(100)
   
   for event in pygame.event.get():
    if event.type == pygame.QUIT:
     run = False
     
   keys = pygame.key.get_pressed()
   
   if keys[pygame.K_SPACE]:
    if ((x - repx) < 10 and (repx - x) < 10 and (y - repy) < 10 and (repy - y) < 10):
     pygame.draw.rect(win, (100, 0, 0), (x, y, width, height))
     pygame.display.update()
     pygame.time.delay(500)
     repsCompleted = repsCompleted + 1
     pygame.mixer.music.load('grunt.mp3')
     pygame.mixer.music.play(0)
     if repsCompleted == repsNeeded:
      exercises = exercises + 1
      if exercises == 5:
       x = tempx
       y = tempy
       width = 20
       height = 20
      repx = random.randint(1, 660)
      repy = random.randint(1, 640)
      repsCompleted = 0
   if keys[pygame.K_LEFT]:
    if (x-vel)>0:
     x -= vel
   if keys[pygame.K_RIGHT]:
    if (x+vel)<960:
     x += vel
   if keys[pygame.K_UP]:
    if (y-vel)>0:
     y -= vel
   if keys[pygame.K_DOWN]:
    if (y+vel)<940:
     y += vel 
   win.fill((0,0,0))
   if round(time.time()%3) == 0:
    largeText = pygame.font.Font('freesansbold.ttf',12)
    TextSurf, TextRect = text_objects("DOWN", largeText)
    TextRect.center = (repx - 40,repy -30)
    win.blit(TextSurf, TextRect)
    pygame.display.update()
   pygame.draw.rect(win, (224, 0, 0), (repx, repy, width, height))
   pygame.draw.rect(win, (100, 120, 50), (repx-60, repy, width, height))
   pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
   message_display("Number of reps: " + str(repsCompleted))
   pygame.display.update()
  if not run:
   pygame.quit()
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
 if keys[pygame.K_LEFT]:
  if (x-vel)>-10 and not blocked(x-vel, y):
   x -= vel
 if keys[pygame.K_RIGHT]:
  if (x+vel)<690 and not blocked(x+vel, y):
   x += vel
 if keys[pygame.K_UP]:
  if (y-vel)>-10 and not blocked(x, y-vel):
   y -= vel
 if keys[pygame.K_DOWN]:
  if (y+vel)<690 and not blocked(x, y+vel):
   y += vel 
 
 win.fill((0,0,0))
 #PT Area
 pygame.draw.rect(win, (255, 255, 0), (170, 80, 550, 400))
 
 #Black block
 pygame.draw.rect(win, (0, 0, 0), (170, 80, 70, 100))
 
 #Little Diemer
 pygame.draw.rect(win, (20, 200, 100), (500, 350, 20, 20))
 
 pygame.draw.rect(win, (255, 0, 0), (150, 80, 20, 400))
 pygame.draw.rect(win, (255, 0, 0), (150, 480, 700, 20))
 pygame.draw.rect(win, (255, 0, 0), (240, 80, 700, 20))
 
 pygame.draw.rect(win, (255, 0, 0), (240, 0, 20, 180))
 
 #w5 = Wall(0, 70, 70, 90)
 pygame.draw.rect(win, (255, 0, 0), (0, 80, 80, 20))
 
 #Dorm room
 pygame.draw.rect(win, (0, 255, 0), (0, 100, 80, 90))
 
 #w6 = Wall(0, 70, 180, 200)
 pygame.draw.rect(win, (255, 0, 0), (0, 190, 80, 20))
 #w7 = Wall(50, 70, 120, 190)
 pygame.draw.rect(win, (255, 0, 0), (60, 130, 20, 70))
 
 #Study Area
 pygame.draw.rect(win, (0, 0, 255), (0, 210, 80, 290))
 
 #w8 = Wall(50, 70, 240, 440)
 pygame.draw.rect(win, (255, 0, 0), (60, 250, 20, 200))
 
 #w9 = Wall(0, 70, 490, 700)
 pygame.draw.rect(win, (255, 0, 0), (0, 500, 80, 300))
 
 #w10 = Wall(140, 160, 540, 640)
 pygame.draw.rect(win, (255, 0, 0), (150, 550, 20, 100))
 
 #w11 = Wall(210, 230, 540, 570)
 pygame.draw.rect(win, (255, 0, 0), (220, 550, 20, 30))
 
 #w12 = Wall(210, 260, 570, 590)
 pygame.draw.rect(win, (255, 0, 0), (220, 580, 50, 20))
 
 #w13 = Wall(260, 280, 570, 640)
 pygame.draw.rect(win, (255, 0, 0), (270, 580, 20, 70))
 
 #w14 = Wall(140, 210, 630, 650)
 pygame.draw.rect(win, (255, 0, 0), (150, 640, 70, 20))
 
 #w15 = Wall(210, 700, 540, 560)
 pygame.draw.rect(win, (255, 0, 0), (220, 550, 600, 20))
 
 #w16 = Wall(670, 700, 470, 550)
 pygame.draw.rect(win, (255, 0, 0), (680, 480, 20, 80))
 
 #w17 = Wall(260, 330, 570, 590)
 pygame.draw.rect(win, (255, 0, 0), (270, 580, 70, 20))
 
 #w18 = Wall(310, 330, 630, 700)
 pygame.draw.rect(win, (255, 0, 0), (320, 640, 20, 70))
 
 pygame.draw.rect(win, (100, 100, 100), (x, y, width, height))
 #message_display("x pos: " + str(x))
 pygame.display.update()



pygame.quit()
