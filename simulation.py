from traffic import *
from land import *
from tools import *

widht=800
height=600
traffic=Traffic(widht,height)
land=Land(widht,height)
pygame.init() # inicializar pygame (OBLIGATORIO) para usar los recursos de pygame
windowsSize=(land.size)
window=pygame.display.set_mode(windowsSize) #seteo ventana
pygame.display.set_caption("Traffic Simulator") #nombre de ventana

cars=False
click=False
lanes=1
clickNumber=-1
currentStreet=False
predict=True
predictBorderCoincidence=False
run=False
updateIntersecrions=False
pygame.Rect(0,0,10,10)
while True:
    window.fill((30,180,40))#recibe tupla con RGB
    #Control de eventos
    for event in pygame.event.get():
        if event.type==QUIT: #¿es el evento de apretar la cruz?
            pygame.quit() #Si==>cerrar los procesos de pygame
            sys.exit() #y cerrar ventana
        if event.type==KEYDOWN:
            if cars==False:
                if event.key==pygame.K_q and clickNumber==-1:
                    print('car will be placed')
                    cars=True
                if event.key==pygame.K_w:
                    if clickNumber==1:
                        lanes+=1
            if event.key==pygame.K_e:
                    predict=False
            if event.key==pygame.K_a:
                    predictBorderCoincidence=True
            if event.key==pygame.K_r:
                    run=not run
        if event.type==KEYUP:
            if event.key==pygame.K_e:
                predict=True
            if event.key==pygame.K_a:
                    predictBorderCoincidence=False
        if cars==False:
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    updateIntersecrions=True
                    click=True
                    pos1=pygame.mouse.get_pos()
                    if predict==True:
                        pos1=magnet_street(pos1,clickNumber,land.streetList)
                        if predictBorderCoincidence==True:
                            pos1=traffic.magnet_horizontal_and_vertical(pos1,clickNumber,land.streetList)
                        pos1=magnet_street_intersection(pos1,land.intersections)
                    clickNumber=clickNumber*-1
                    if clickNumber==-1:
                        lanes=1
                  

    if run==True:
        traffic.run(land.streetList,land.intersections)

    if predict == True:
        pos2=magnet_street(pygame.mouse.get_pos(),clickNumber,land.streetList)
        if predictBorderCoincidence==True:
                        pos2=traffic.magnet_horizontal_and_vertical(pos2,clickNumber,land.streetList)
        pos2=magnet_street_intersection(pos2,land.intersections)
        
    else:
        pos2=pygame.mouse.get_pos()
    if clickNumber==1 :
        
        land.street_append(pos1,pos2,click,lanes)
        click=False
    
    if clickNumber==-1 and updateIntersecrions==True:
        land.intersect_point()
        land.update_intersections()
        updateIntersecrions=False

    if cars==True:
        traffic.vehicleAppend(3,land.streetList)
        cars=False
        

    

    for street in land.streetList:
        street.draw(window)
    for car in traffic.vehicleList:
        car.draw(window)
    if predict==True:
        aux=magnet_street(pygame.mouse.get_pos(),clickNumber,land.streetList)
        if predictBorderCoincidence==True:
                        aux=traffic.magnet_horizontal_and_vertical(aux,clickNumber,land.streetList)
        aux=magnet_street_intersection(aux,land.intersections)
        aux1=int(aux[0])
        aux2=int(aux[1])
        pygame.draw.circle(window,(20,20,20),(aux1,aux2),5)
    else:
        pygame.draw.circle(window,(20,20,20),pygame.mouse.get_pos(),5)
    #Actualizar contenido de ventana
    pygame.display.update()