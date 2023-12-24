from typing import Any
import pygame



class Nave(pygame.sprite.Sprite):
    
    def __init__(self , posicion):

        super().__init__()
        self.indice_Imagenes = 0
        imagenes = [pygame.image.load("milenario.png"),pygame.image.load("Tie.png")]
        self.Halcon = [pygame.transform.scale(imagenes[0],(60,90)) ,
                       pygame.transform.scale(imagenes[1],(60,90)) ]
        self.image = self.Halcon[self.indice_Imagenes]
        # self.image = pygame.transform.scale(self.image,(60,90))
        self.contador = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion 
        self.ultimo_disparo = 0


    def update(self, *args: Any, **kwargs: Any):
        teclas = args[0]
        pantalla = pygame.display.get_surface()
        if teclas[pygame.K_LEFT]:
            if (self.rect.x > 10):
                self.rect.x -= 10

        if teclas[pygame.K_RIGHT]:
            pantalla = pygame.display.get_surface()
            limite = pantalla.get_width() - self.image.get_width() - 10
            if (self.rect.x < limite):     
                self.rect.x += 10

        momento_Actual = pygame.time.get_ticks()
        self.contador = (self.contador+1)%40
        self.indice_Imagenes = self.contador //20
        self.image = self.Halcon[self.indice_Imagenes]
        pass

    def disparar(self):
        momento_actual = pygame.time.get_ticks()
        self.ultimo_disparo 



class Enemigo(pygame.sprite.Sprite):

    def __init__(self, posicion) -> None:
    
        super().__init__()
        imagen = pygame.image.load("Tie.png")
        # self.image = pygame.transform.rotate(imagen,180)
        self.image = pygame.transform.scale(imagen,(60,90))
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion 
    
    def update(self, *args: Any, **kwargs: Any) :
        self.rect.y +=1
        pantalla = pygame.display.get_surface()
        if (self.rect.y>pantalla.get_height()):
            self.kill()





class Fondo(pygame.sprite.Sprite):

    def __init__(self, posicion) -> None:
    
        super().__init__()
        imagen = pygame.image.load("estrellas.jpg")
        pantalla = pygame.display.get_surface()
        self.image = pygame.transform.scale(imagen,(pantalla.get_width() , pantalla.get_height()))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0) 
    

        
    
    def update(self, *args: Any, **kwargs: Any) :
         self.rect.y =1


class Disparo(pygame.sprite.Sprite):

    def __init__(self, posicion) -> None:
    
        super().__init__()
        self.image = pygame.Surface((5,10))
        imagen = pygame.image.load("disparo.png")
        self.image = pygame.transform.scale(imagen,(5,10))
        self.rect = self.image.get_rect()
        self.rect.center = posicion 
    
    def update(self, *args: Any, **kwargs: Any) :
        self.rect.y -=5

    def disparar(self):
        bala = Disparo((self.rect.x +self.image.get_width()))