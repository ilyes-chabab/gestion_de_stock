import pygame
import sys

pygame.init()
screen=pygame.display.set_mode((1250,600))
def message(size,message,message_rectangle,color):
    font=pygame.font.SysFont("arial",size)
    message = font.render(message,False,color)
    screen.blit(message,message_rectangle)

running = True

while running:
    screen.fill((255,255,255))
    
    pygame.draw.rect(screen , (0, 0, 0),(100,100,1000,300),3)
    pygame.draw.rect(screen , (0, 0, 0),(100,100,1000,100),3)
    pygame.draw.line(screen , (0, 0, 0),(100,270),(1100,270),3)
    pygame.draw.line(screen , (0, 0, 0),(290,200),(290,400),3)
    pygame.draw.line(screen , (0, 0, 0),(790,200),(790,400),3)
    pygame.draw.line(screen , (0, 0, 0),(940,200),(940,400),3)
    message(45,'Category',(530,120,0,0,),(0,0,0))
    message(45,'name                    description                        price        stock     ',(120,220,0,0,),(0,0,0))
    message(45,'Category',(530,120,0,0,),(0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    pygame.display.flip()  