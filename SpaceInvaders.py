import pygame
from Elementos import Enemigos, Nave , Fondo , Disparos

pygame.init()

pantalla = pygame.display.set_mode((800,600))

salir = False

clock = pygame.time.Clock()
FPS = 60

#imagenTie = pygame.image.load("astronave.png")
#Tie = pygame.transform.scale(imagenTie,(60,60))
mi_nave = Nave()
caza = Enemigos()      
disparo = Disparos()
fondo = Fondo()



while not salir:
    clock.tick(FPS)
    #gestionar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              salir = True

    teclas =pygame.key.get_pressed()   
    
    if teclas[pygame.K_LEFT]:  
        
            mi_nave.MoverIz()
    if teclas[pygame.K_RIGHT]:
        
            mi_nave.MoverDer()    

    

    #caza.Mover()
    #caza.Dibujar() un enemigo y que se mueva
    # si es un enemigo = Enemigos() no necesita el self

    #gestionar cambios

    #pantalla.fill((0, 15, 80))
    fondo.Dibujar()
    #redibujar el juego
    mi_nave.Dibujar()
    
    #Enemigos.dibujar()
    #enemigos.append(Enemigos)

    caza.AddEnemigo()
    caza.MoverEnemigos()
    caza.DibujarEnemigos()
    #cazas.append(Enemigos())
    #for enemigo in cazas:
     #     caza.Dibujar()
      #    caza.Mover()


    if teclas[pygame.K_SPACE]:
          disparo.AddDisparo(mi_nave)

    disparo.DibujarDisparos()
    disparo.MoverDisparos()
     
    

    #if teclas[pygame.K_SPACE]:
     #     disparos.append(Disparos(mi_nave)) 
    #for disparo in disparos:
    #      disparo.Dibujar()
          #if (disparos<0):
           #      disparos.remove(disparo)   
    #for disparo in disparos:
    #      disparo.Dibujar()
          #if (disparos<0):
           #      disparos.remove(disparo)
    
        
          

    #Tie.posIzEnemigo += 0.5
    #if (Enemigos()):
    #    Tie.bajarNivel
    pygame.display.flip()

pygame.quit()



    
# Crear una instancia de la clase
#mi_objeto = Enemigos("valor1", "valor2")

# Acceder a los atributos y métodos de la instancia
#print(mi_objeto.atributo1)
#3print(mi_objeto.atributo2)
#mi_objeto.metodo1()
#mi_objeto.metodo2()

    