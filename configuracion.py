import pygame
from collections import namedtuple
from pygame.locals import *

pygame.init()

TAMANNO_LETRA = 20
TAMANNO_LETRA_GRANDE = 80
FPS_inicial = 3
TIEMPO_MAX = 60
Punto = namedtuple('Punto','x y')

#-------------------------------------------------------------------------------
#                               Pantalla
#-------------------------------------------------------------------------------

ANCHO = 800
ALTO = 600
pantalla=pygame.display.set_mode((ANCHO,ALTO))

#-------------------------------------------------------------------------------
#                               Colores
#-------------------------------------------------------------------------------

COLOR_LETRAS = (145,73,254)
COLOR_FONDO = (0,0,0)
COLOR_TEXTO = (255,255,255)
COLOR_RACHA = (254, 146, 40)
COLOR_TIEMPO_FINAL = (200,20,10)
negro=0,0,0
azul=0,0,255
gris= 232,224,224
vClaro=169, 204, 227

#-------------------------------------------------------------------------------
#                              Fuente del Texto
#-------------------------------------------------------------------------------

FuentePequenna=pygame.font.SysFont("comicsansms",15)
FuenteGrande=pygame.font.SysFont("comicsansms",80)

#-------------------------------------------------------------------------------
#                               Datos de Boton
#-------------------------------------------------------------------------------

Boton1=[300,290]
TamBoton=[200,45]
ColorBoton1=[vClaro,gris]
#---------------
Boton2=[300,340]
ColorBoton2=[vClaro,gris]
#---------------
Boton3=[300,390]
ColorBoton3=[vClaro,gris]
#---------------
Boton4=[300,440]
ColorBoton4=[vClaro,gris]
#---------------
Boton5=[80,210]
TamBoton2=[140,45]
ColorBoton4=[vClaro,gris]

#-------------------------------------------------------------------------------
#                             Variables Globales
#-------------------------------------------------------------------------------

premio=0
puntos = 0
fin=True
entrada=True
introJuego=True
juego=False
ingresar=False
musica_15=True
musica_principal=False
musica_60=True
facil=False
Dificultad=False
palabrasRepetidas=[]
sonidoMenuPrincipal=pygame.mixer.Sound("SonidoMenu1.wav")

#-------------------------------------------------------------------------------






