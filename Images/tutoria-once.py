#Coliciones
from numpy import array
import pygame,sys
from pygame.locals import *

pygame.init() # inicializar pygame (OBLIGATORIO) para usar los recursos de pygame
ventanaSize=(400,400)
ventana=pygame.display.set_mode(ventanaSize) #seteo ventana
pygame.display.set_caption("Hola Mundo") #nombre de ventana
miImagen = pygame.image.load("Imagenes/auto-vista-superior.png") #Cargar imagen

#definir que porcentage de la horizontal tendra la imagen conservando relación de aspecto
imageSize=array(miImagen.get_rect().size)
windowSize=array(ventanaSize)
escala=0.1
relacionDeAspecto=imageSize/windowSize
scaleFactor=0.1/relacionDeAspecto[0]
imageNewSize=(scaleFactor*imageSize).astype(int)
print(relacionDeAspecto)
##################

miImagen = pygame.transform.scale(miImagen,imageNewSize )#cambiar tamaño de imagen


posX,posY=ventanaSize[0]-imageNewSize[0],ventanaSize[1]/2

 #Colocar la image en la variable "miImagen" su vertice superior derecho esta en (posX,posY)
velocidad=1
derecha = False

rectangulo=Rect(0,0,100,50)
rectangulo2=Rect(ventanaSize[0]/2-50,ventanaSize[1]/2-25,100,50)
#mostrar ventana
while True:
    ventana.fill((255,255,255))
    #ventana.blit(miImagen,(posX,posY))
    #Control de eventos
    pygame.draw.rect(ventana,(180,70,70),rectangulo2)
    pygame.draw.rect(ventana,(180,70,70),rectangulo)
    rectangulo.left,rectangulo.top=pygame.mouse.get_pos()
    
    if rectangulo.colliderect(rectangulo2):
        velocidad=0

    for evento in pygame.event.get():
        if evento.type==QUIT: #¿es el evento de apretar la cruz?
            pygame.quit() #Si==>cerrar los procesos de pygame
            sys.exit() #y cerrar ventana
    
    if derecha==False:
        if posX>0:
            posX-=velocidad
            rectangulo2.left=posX
        else:
            derecha=True
    else:
        if posX<ventanaSize[0]-rectangulo2.width:
            posX+=velocidad
            rectangulo2.left=posX

        else:
            derecha=False
    pygame.time.wait(4)
    #Actualizar contenido de ventana
    pygame.display.update()