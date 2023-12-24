import pygame
import Elementos2
import random

pygame.init()

tamaño = (800,600)
pantalla = pygame.display.set_mode(tamaño)

reloj = pygame.time.Clock()
FPS = 60
frecuenciaEnemigo = 60
running = True

posicion = (370,500)
nave = Elementos2.Nave(posicion)
enemigo = Elementos2.Enemigo(posicion)
grupo_sprites = pygame.sprite.Group(nave)
disparo = Elementos2.Disparo(posicion)
# fondo = Elementos2.Fondo((0,0))
# grupo_sprites.add(Elementos2.Nave((300,100)))
# grupo_sprites.add(Elementos2.Nave((400,100)))
# grupo_sprites.add(Elementos2.Nave((500,100)))
# grupo_sprites.add(Elementos2.Fondo((0,0)))

#enemigo = Elementos2.Enemigo((50,50))
#grupo_sprites.add(enemigo)

ultimo_Enemigo_Creado = 0


while(running):

    reloj.tick(FPS)#limitamos el juego a 60 fps

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False

    momento = pygame.time.get_ticks()

    if (momento>ultimo_Enemigo_Creado+frecuenciaEnemigo):
        grupo_sprites.add(Elementos2.Enemigo((random.randint(0, pantalla.get_width()), 0)))
        ultimo_Enemigo_Creado = momento

    teclas = pygame.key.get_pressed()

    # if (pygame.K_SPACE):
    #     bala = Disparo(self.rect.center)
    #     grupo_sprites.add(bala)

    
    pantalla.fill((255,255,255))

    grupo_sprites.update(teclas)
    grupo_sprites.draw(pantalla)

    pygame.display.flip()
        

pygame.quit()
