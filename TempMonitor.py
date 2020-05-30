from gpiozero import CPUTemperature
import pygame
import time

pygame.init()
screen=pygame.display.set_mode((50,110))

v1=pygame.image.load('temp1.png')
v2=pygame.image.load('temp2.png')
v3=pygame.image.load('temp3.png')
v4=pygame.image.load('temp4.png')
v5=pygame.image.load('temp5.png')
v6=pygame.image.load('temp6.png')
vc=pygame.image.load('tempC.png')
vd=pygame.image.load('tempD.png')


run=True
while run:
    cput = CPUTemperature()
    cpt=str(cput)
    cpus=cpt[44:46]
    cpu=int(cpus)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    if(cpu<0.00):
        screen.blit(vc,(0,0))
    elif(cpu>=0.00 and cpu<=30.00):
        screen.blit(v6,(0,0))
    elif(cpu>=30.00 and cpu<=40.00):
        screen.blit(v5,(0,0))
    elif(cpu>=40.00 and cpu<=50.00):
        screen.blit(v4,(0,0))
    elif(cpu>=50.00 and cpu<=60.00):
        screen.blit(v3,(0,0))
    elif(cpu>=60.00 and cpu<=70.00):
        screen.blit(v2,(0,0))
    elif(cpu>=70.00 and cpu<=80.00):
        screen.blit(v1,(0,0))
    elif(cpu>80.00):
        screen.blit(vd,(0,0))
    pygame.display.update()
    time.sleep(4)
    
pygame.quit()
            
