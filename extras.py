import pygame
from pygame.locals import *
from configuracion import *
from funcionesVACIAS import *
from funcionesSeparador import *

def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_KP_MINUS:
        return("-")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")

def escribirEnPantalla(screen, palabra, posicion, tamano, color):
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), tamano)
    ren = defaultFont.render(palabra, 1, color)
    screen.blit(ren, posicion)

def escribirEnPantalla2(screen, palabra, posicion):
    defaultFont= pygame.font.Font(None, 20)
    ren = defaultFont.render(palabra, 1,(0,0,0))
    screen.blit(ren, posicion)

def listaPalabraActual(palabraActual):
    lista=[]
    for letra in palabraActual:
        lista.append(letra)
    return lista

def lista_cadena(lista):
    cadena=""
    for elem in lista:
        cadena=cadena+elem
    return cadena

def obtener_ultsilaba(palabraActual):
    palabra=separador(palabraActual)
    ultimasilaba=dameUltimaSilaba(palabra)
    return ultimasilaba

def borrar_ultsilaba(palabraActual):
    lista=listaPalabraActual(palabraActual)
    ultimasilaba=obtener_ultsilaba(palabraActual)
    for i in range (len(lista)-1,len(lista)-len(ultimasilaba)-1,-1):
            lista.pop(i)
    palabra_act=lista_cadena(lista)
    return palabra_act

def dibujar(screen, palabraUsuario, palabraActual, puntos, segundos,facil):

    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    #Linea Horizontal
    pygame.draw.line(screen, (255,255,255), (0, ALTO-60) , (ANCHO, ALTO-60), 5)

    #muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_TEXTO), (190, 570))

    #muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO), (680, 10))

    #muestra los segundos y puede cambiar de color con el tiempo
    if(segundos<15):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    screen.blit(ren, (10, 10))

    flacas=["t","f","j","r"]
    gordas=["m","w"]

    #muestra la palabra
    if facil:
        palabra=borrar_ultsilaba(palabraActual)
        palabra_silabas=separador(palabraActual)
        ultsilaba=obtener_ultsilaba(palabra_silabas)
        pos=0
        for letra in palabra:
            screen.blit(defaultFontGrande.render(letra, 1, COLOR_LETRAS), (ANCHO//2-len(palabraActual)*TAMANNO_LETRA_GRANDE//4+pos,ALTO-200))
            if letra=="i" or letra=="l":
                pos=pos+TAMANNO_LETRA_GRANDE//3
            elif letra in flacas:
                pos=pos+TAMANNO_LETRA_GRANDE//2.4
            elif letra in gordas:
                pos=pos+TAMANNO_LETRA_GRANDE//1
            else:
                pos=pos+TAMANNO_LETRA_GRANDE//1.7
        for letra in ultsilaba:
            screen.blit(defaultFontGrande.render(letra, 1, azul), (ANCHO//2-len(palabraActual)*TAMANNO_LETRA_GRANDE//4+pos,ALTO-200))
            if letra=="i" or letra=="l":
                pos=pos+TAMANNO_LETRA_GRANDE//3
            elif letra in flacas:
                pos=pos+TAMANNO_LETRA_GRANDE//2.2
            elif letra in gordas:
                pos=pos+TAMANNO_LETRA_GRANDE//1
            else:
                pos=pos+TAMANNO_LETRA_GRANDE//1.7
    else:
        screen.blit(defaultFontGrande.render(palabraActual, 1, COLOR_LETRAS), (ANCHO//2-len(palabraActual)*TAMANNO_LETRA_GRANDE//4,ALTO-200))
    #muestra su longitud
##    screen.blit(defaultFontGrande.render(str(len(palabraActual)), 1, (200,20,10)), (ANCHO-400,ALTO-500))

#Funcion extra annadida, muestra en pantalla racha de aciertos
def dibujar_2(screen,cont_aciertos):
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    #Muestra la racha de puntos
    if cont_aciertos>0 and cont_aciertos<5:
        screen.blit(defaultFont.render("X"+str(cont_aciertos),1,COLOR_TEXTO),(680,50))
    else:
        if cont_aciertos>=5:
            screen.blit(defaultFont.render("X"+str(cont_aciertos),1,COLOR_RACHA),(680,50))





