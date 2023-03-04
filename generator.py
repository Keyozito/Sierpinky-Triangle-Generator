import pygame
import random

pygame.init()
tela = pygame.display.set_mode((600,600))

white = (255,255,255)
blue = (0,170,255)

# Vars
run = True
C = True
P1 = (300, 30)
P2 = (30, 570)
P3 = (570, 570)
points = [P1, P2, P3]
L = (0,0)

def printThings(c, color=white):
  pygame.draw.rect(tela, color, c+(4,4) )
  pygame.display.update()

printThings(P1, blue)
printThings(P2, blue)
printThings(P3, blue)

while run:
  # First Click
  if C:
    for evento in pygame.event.get():
      if evento.type == pygame.MOUSEBUTTONDOWN:
        L = pygame.mouse.get_pos()
        C = False
        print("Start")
  
  # Fractal
  else:
    P = random.choice(points)
    
    # Set Middle Cords
    Np = ( int(((L[0]+P[0])/2)) , int(((L[1]+P[1])/2)) )
    printThings(Np)
    L = Np
