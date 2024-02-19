from principal import *
from configuracion import *
from pygame.locals import *
import random
import math
import pygame

#-------------------------------------------------------------------------------

def lectura(archivo, salida):
    """
        Lee el archivo, y lo guarda en una lista sin enter(\n)
    """
    lista=archivo.readlines()
    for pal in lista:
        salida.append(pal[:-1])

#-------------------------------------------------------------------------------

def nuevaPalabra(silabas):
    """
        Elige una palabra aleatoria
    """
    return random.choice(silabas)

#-------------------------------------------------------------------------------

def silabasTOpalabra(silaba):
    """
        Guarda la palabra sin guiones
    """
    nueva=""
    for caracter in silaba:
        if caracter!="-":
            nueva=nueva+caracter
    return nueva

#-------------------------------------------------------------------------------

def palabraTOsilaba(palabra):
    """
        Funcion opcional que separa en silabas
    """
    nueva=separador(palabra)
    return nueva

#-------------------------------------------------------------------------------

def dameUltimaSilaba(enSilabas):
    """
        Recibe palabra separada en silabas y devuelve la ultima
    """
    ultima=""
    for i in range (len(enSilabas)-1,-1,-1):
        if enSilabas[i] !="-":
            ultima=enSilabas[i] + ultima
        else:
            return ultima
    return ultima

#-------------------------------------------------------------------------------

def damePrimeraSilaba(enSilabas):
    """
        Recibe palabra separada en silabas y devuelve la primera
    """
    primera=""
    for i in range (len(enSilabas)):
        if enSilabas[i] !="-":
            primera=primera+ enSilabas[i]
        else:
            return primera
    return primera

#-------------------------------------------------------------------------------

def esValida(palabraUsuario, palabraUsuarioEnSilabas,palabraEnSilabas, listaPalabrasDiccionario):
    """
        Debe recibir 4 parametros y chequear que la palabra que escribe el usuario sea correcta.
        Devuelve True o False.
    """
    if palabraUsuario in listaPalabrasDiccionario:
        primerasilaba=damePrimeraSilaba(palabraUsuarioEnSilabas)
        ultimasilaba=dameUltimaSilaba(palabraEnSilabas)
        if palabraUsuarioEnSilabas!=palabraEnSilabas:
            if ultimasilaba==primerasilaba:
                return True
        else:
            return False

#-------------------------------------------------------------------------------

def Puntos(palabraUsuario):
    """
        Recibe la palabra del usuario y devuelve un entero calculado de la siguiente manera:
        -Cada vocal suma 2 puntos.
        -Si la palabra del usuario contiene consonantes "raras", es decir, poco frecuentes,
        se le suman 10 puntos.
        -Al resto de consonantes, valen 4 puntos
    """
    consRaras=["q","h","k","w","x","y","z"]
    vocal=["a","e","i","o","u"]
    consNormales=["b","c","d","f","g","j","l","m","n","p","r","s","t","v"]
    puntos=0
    for letra in palabraUsuario:
        if letra in consRaras:
            puntos+=4
        elif letra in vocal:
            puntos+=1
        elif letra in consNormales:
            puntos+=1
        else:
            puntos+=0
    return puntos

#-------------------------------------------------------------------------------

def procesar(palabraUsuario, palabraUsuarioEnSilabas,palabraActual, palabraEnSilabas, listaPalabrasDiccionario):
    """
        verificar que la palabra sea correcta y retornar el puntaje.
    """
    p=Puntos(palabraUsuario)
    if esValida(palabraUsuario, palabraUsuarioEnSilabas,palabraEnSilabas, listaPalabrasDiccionario):
        return p
    return 0

#-------------------------------------------------------------------------------

##debe recibir una silaba y el lemario de silabas y buscar una palabra que empiece con esta silaba.
def buscarPalabraQueEmpieceCon(silaba,lemarioEnSilabas):
    """
        Busca una palabra que empieze con la silaba ingresada y la retorna, o no
    """
    global palabrasRepetidas
    lista=[]
    palabrasRepes=[]
    n=1
    for i in range (len(lemarioEnSilabas)):
        if silaba==damePrimeraSilaba(lemarioEnSilabas[i]):
            lista.append(lemarioEnSilabas[i])
        while n<=len(lista):
            palabra=lista[random.randrange(len(lista))]
            if palabra not in palabrasRepes:
                palabrasRepes.append(palabra)
                n+=1
            if palabra not in palabrasRepetidas and len(palabra)<=13:
                palabrasRepetidas.append(palabra)
                return palabra
    return random.choice(lemarioEnSilabas)

#-------------------------------------------------------------------------------

def objetotxt(txt,color,tamanno):
    """
       Objetos de texto
    """
    #Agrega el tamanno de la letra y la tipografia
    if tamanno == "pequenno":
        textoSuperficie = FuentePequenna.render(txt,True,color)
    elif tamanno == "grande":
        textoSuperficie = FuenteGrande.render(txt,True,color)
    #Retorna las caracteristicas de la letra y la superficie del rectangulo del texto
    return textoSuperficie, textoSuperficie.get_rect()

#-------------------------------------------------------------------------------

def mensaje(msg,color,desplazamientoY=0,tamanno="pequenno"):
    """
       Para imprimir en pantalla texto
    """
    #Variables con los valores de la funcion objetotxt
    textoSuperficie, textoRect= objetotxt(msg,color,tamanno)
    #Centra el Texto en pantalla
    textoRect.center = (ANCHO/2),(ALTO/2)+desplazamientoY
    #Imprime en pantalla el Texto
    pantalla.blit(textoSuperficie,textoRect)

#-------------------------------------------------------------------------------

def TextoBoton(msg,color,BotonX,BotonY,Ancho,Alto,tamanno="pequenno"):
    """
       Texto dentro de un boton
    """
    #Variables con los valores de la funcion objetotxt
    textoSuperficie, textoRect= objetotxt(msg,color,tamanno)
    #centra el texto en el boton
    textoRect.center = (BotonX+(Ancho/2),BotonY+(Alto/2))
    #Imprime en pantalla el Texto y su ubicacion en el boton
    pantalla.blit(textoSuperficie,textoRect)

#-------------------------------------------------------------------------------












