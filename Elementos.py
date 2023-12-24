import pygame
import math

class Enemigos:
    def __init__(self) -> None:
        self.lista = []
        self.momento_de_ultimo_enemigo_creado = 0

    def AddEnemigo(self):
        ticks = pygame.time.get_ticks()
        if ticks > self.momento_de_ultimo_enemigo_creado + 500:
            self.lista.append(Enemigo())
            self.momento_de_ultimo_enemigo_creado = ticks

    def MoverEnemigos(self):
        for enemigo in self.lista:
            enemigo.Mover()


    def DibujarEnemigos(self):
        for enemigo in self.lista:
            enemigo.Dibujar()

class Enemigo:

    def __init__(self):
        self.posIzEnemigo = 10
        self.posTopEnemigo = 10
        imagenTie = pygame.image.load("Tie.png")
        self.Tie = pygame.transform.scale(imagenTie,(60,60))

    

    def Mover (self):
        pantalla = pygame.display.get_surface()
        limite = pantalla.get_width() - self.Tie.get_width()
        self.posIzEnemigo +=5
        if(self.posIzEnemigo>limite):
            self.posIzEnemigo = 10
            self.posTopEnemigo += 70

    def Dibujar(self):
        pantalla = pygame.display.get_surface()
        pantalla.blit(self.Tie, (self.posIzEnemigo, self.posTopEnemigo))




class Nave:

    def __init__(self):
        self.posIz = 370
        self.posTop = 500
        imagenesHalcon = [pygame.image.load("milenario.png"),pygame.image.load("milenario.png") ]
        self.contador = 0
        self.Halcon = [pygame.transform.scale(imagenesHalcon[0],(60,90)) ,
                       pygame.transform.scale(imagenesHalcon[1],(60,90)) ]

    def Dibujar(self ):
       self.contador = (self.contador +1)%40
       pantalla = pygame.display.get_surface()
       seleccionada = self.contador//20
       pantalla.blit(self.Halcon[seleccionada], (self.posIz, self.posTop))
       

    def MoverIz(self):
        if (self.posIz > 10):
            self.posIz -=10

    def MoverDer(self): 
        self.contador = (self.contador +1)%40
        seleccionada = self.contador//20
        pantalla = pygame.display.get_surface()
        limite = pantalla.get_width() - self.Halcon[seleccionada].get_width() - 10
        if (self.posIz < limite):     
            self.posIz +=10
    
    def GetPosIz(self):
        return self.posIz
    
    def GetPosTop(self):
        return self.posTop

class Disparo:

    def __init__(self, nave):
       
        self.posIzdisparo = nave.GetPosIz()
        self.posTopdisparo = nave.GetPosTop()
        imagendisparo = pygame.image.load("disparo.png")
        self.disparo = pygame.transform.scale(imagendisparo,(60,90))

    def Dibujar(self ):
       pantalla = pygame.display.get_surface()
       pantalla.blit(self.disparo, (self.posIzdisparo, self.posTopdisparo))
       self.posTopdisparo -=10   

    def Mover(self):
        pantalla = pygame.display.get_surface()
        limite = pantalla.get_height 
        self.posTopdisparo -=10
        #while(self.posTopdisparo < limite ):
         #   self.posTopdisparo += 1    
    def GetPosTop (self):
        return self.getPosTop

class Disparos:
    def __init__(self) -> None:
        self.listadisparos = []
        self.momento_de_ultimo_disparo_creado = 0

    def AddDisparo(self):
        ticks = pygame.time.get_ticks()
        if ticks > self.momento_de_ultimo_disparo_creado + 333:
            self.listadisparos.append(Disparo())
            self.momento_de_ultimo_disparo_creado = ticks    

    def MoverDisparos(self):
        for disparo in self.listadisparos:
            disparo.Mover()


    def DibujarDisparos(self):
        for disparo in self.listadisparos:
            disparo.Dibujar()
    
class Fondo:
    def __init__(self):
        self.scroll = 0
        pantalla = pygame.display.get_surface()

        image = pygame.image.load("estrellas.jpg")
        self.fondo = pygame.transform.scale(image,(pantalla.get_width() , image.get_height()))
        self.piezas = math.ceil(pantalla.get_height()/ self.fondo.get_height()) + 1

    def Dibujar(self):
        pantalla = pygame.display.get_surface()
        for i in range(0,self.piezas):
            pantalla.blit(self.fondo, (0,-self.fondo.get_height() + i*self.fondo.get_height() + self.scroll))

        
        self.scroll += 1
        if self.scroll>self.fondo.get_height():
            self.scroll = 0