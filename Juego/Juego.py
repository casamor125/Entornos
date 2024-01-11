import pygame
import Elementos
import random

pygame.init()

tamaño = (800,600)
pantalla = pygame.display.set_mode(tamaño)

reloj = pygame.time.Clock()
FPS = 60
frecuenciaEnemigo = 60
running = True

# no empezar el juego hasta repasar el codigo de space 2 y preguntar por el nuevo
# empezar con el juego , luego si se va bien ya se harà el vampire survivors