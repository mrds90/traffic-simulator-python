from traffic import *

traffic=Traffic(800,600)
pygame.init() # inicializar pygame (OBLIGATORIO) para usar los recursos de pygame
windowsSize=(traffic.size)
window=pygame.display.set_mode(windowsSize) #seteo ventana
pygame.display.set_caption("Traffic Simulator") #nombre de ventana

cars=False
click=False
lanes=1
clickNumber=-1
currentStreet=False
predict=True
pygame.Rect(0,0,10,10)
while True:
    window.fill((30,180,40))#recibe tupla con RGB
    #Control de eventos
    for evento in pygame.event.get():
        if evento.type==QUIT: #¿es el evento de apretar la cruz?
            pygame.quit() #Si==>cerrar los procesos de pygame
            sys.exit() #y cerrar ventana
        if evento.type==KEYDOWN:
            if cars==False:
                if evento.key==pygame.K_q and clickNumber==-1:
                    print('car will be placed')
                    cars=True
                if evento.key==pygame.K_w:
                    if clickNumber==1:
                        lanes+=1
            if evento.key==pygame.K_e:
                    predict=False
        if evento.type==KEYUP:
            if evento.key==pygame.K_e:
                predict=True
        if cars==False:
            if evento.type==pygame.MOUSEBUTTONDOWN:
                click=True
                pos1=pygame.mouse.get_pos()
                if predict==True:
                    pos1=traffic.magnetStreet(pos1,clickNumber)
                    pos1=traffic.magnetStreetLimits(pos1,clickNumber)
                    pos1=traffic.magnetStreetIntercetion(pos1)
                clickNumber=clickNumber*-1
                if clickNumber==-1:
                    lanes=1
                  

    

    if predict == True:
        pos2=traffic.magnetStreet(pygame.mouse.get_pos(),clickNumber)
        pos2=traffic.magnetStreetLimits(pos2,clickNumber)
        pos2=traffic.magnetStreetIntercetion(pos2)
    else:
        pos2=pygame.mouse.get_pos()
    if clickNumber==1 :
        
        traffic.streetAppend(pos1,pos2,click,lanes)
        click=False
    
    traffic.intersections()

    if cars==True:
        traffic.vehicleAppend(3)
        cars=False
        

    

    for street in traffic.streetList:
        street.draw(window)
    for car in traffic.vehicleList:
        car.draw(window)
    if predict==True:
        aux=traffic.magnetStreet(pygame.mouse.get_pos(),clickNumber)
        aux=traffic.magnetStreetLimits(aux,clickNumber)
        aux=traffic.magnetStreetIntercetion(aux)
        aux1=int(aux[0])
        aux2=int(aux[1])
        pygame.draw.circle(window,(20,20,20),(aux1,aux2),5)
    else:
        pygame.draw.circle(window,(20,20,20),pygame.mouse.get_pos(),5)
    #Actualizar contenido de ventana
    pygame.display.update()