#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *
from configuracion import *
from extras import *
from funcionesSeparador import *

from funcionesVACIAS import *

#Nombre del Juego
pygame.display.set_caption("El juego del Mago Goma")

#Icono del Juego
icon=pygame.image.load("Icono.png")
pygame.display.set_icon(icon)

def botones(texto,superficie,estado,Posicionamiento,tam, identidad=None):

    sonidoBotones=pygame.mixer.Sound("botonS.wav")
    #Posicion del Mouse
    Mouse= pygame.mouse.get_pos()
    #Indica cual boton del Mouse se Clickeo
    Click=pygame.mouse.get_pressed()

    global fin
    global introJuego
    global juego
    global entrada
    global puntos
    global ingresar
    global premio
    global facil
    global Dificultad
    global palabrasRepetidas

    #Si el mouse Pasa por el boton
    if Posicionamiento[0] + tam[0] > Mouse[0] > tam[0] and  Posicionamiento[0]+tam[0]<Mouse[0]+tam[0] and Posicionamiento[1]+ tam[1] > Mouse[1] > tam[1] and Posicionamiento[1] +tam[1]<Mouse[1]+tam[1]:
        #Si se Clickeo el boton izquierdo del Mouse
        if Click[0]==1:
            sonidoBotones.play()

            ##Botones del MenuIntro()

            #Boton para Iniciar el Juego
            if identidad=="MenuIntroComenzar":
                palabrasRepetidas=[]
                Dificultad=True
                MenuDificultad()
            #Boton para Menu de Puntajes
            elif identidad=="MenuIntroPuntos":
                ingresar=True
                MenuPuntos(" ",-1)
            #Boton para Menu de Creditos
            elif identidad=="MenuIntroCreditos":
                entrada=True
                MenuCreditos()
            #Boton pasa Salir del Juego
            elif identidad=="MenuIntroSalida":
                introJuego=False
                juego=False
                main()

            ##Botones del MenuGameOver()

            #Boton para Reiniciar el Juego
            elif identidad=="MenuGameOverReinicio":
                palabrasRepetidas=[]
                puntos=0
                premio+=10
                juego=True
                ingresar=True
                main()
            #Boton para Volver al Menu Principal
            elif identidad=="MenuGameOverMenu":
                introJuego=True
                main()
            #Boton pasa Salir del Juego
            elif identidad=="MenuGameOverSalida":
                introJuego=False
                juego=False
                fin=False
                main()

            ##Boton del MenuCreditos() y MenuPuntos()

            #Boton para Volver al Menu Principal
            elif identidad=="Atras":
                ingresar=False
                entrada=False
                introJuego=True
                juego=False
                main()

            ##Botones del MenuDificultad()

            elif identidad=="DificultadFacil":
                facil=True
                introJuego=False
                juego=True
                ingresar=True
                main()
            elif identidad=="DificultadDificil":
                facil=False
                introJuego=False
                juego=True
                ingresar=True
                main()

        boton=pygame.draw.rect(superficie,estado[1],(Posicionamiento [0],Posicionamiento[1],tam[0],tam[1]))

    #Si el mouse No Pasa por el boton
    else:

        boton=pygame.draw.rect(superficie,estado[0],(Posicionamiento [0],Posicionamiento[1],tam[0],tam[1]))

    TextoBoton(texto,negro,Posicionamiento[0],Posicionamiento[1],tam[0],tam[1])

    return boton

def MenuCreditos():
    """
        Muestra el Menu de los Creditos
    """
    global entrada
    global introJuego
    global juego

    while entrada:
        imagen=pygame.image.load("Creditos.png")
        pantalla.blit(imagen,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                juego=False
                entrada=False
                introJuego=False
                main()

        botones("Atras",pantalla,ColorBoton4,Boton4,TamBoton,identidad="Atras")
        pygame.display.update()#Impide el desvanecimiento
        #gameClock.tick()

def MenuGameOver():
    """
        Muestra el Menu GameOver
    """
    global fin
    global puntos
    global juego

    pantalla=pygame.display.set_mode((ANCHO,ALTO))
    while fin:
        imagen=pygame.image.load("MenuFin.png")
        pantalla.blit(imagen,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                juego=False
                fin=False
                main()

        mensaje("Game Over",negro,-90,tamanno="grande")
        mensaje("Puntaje:"+ str(int(puntos)),negro,-30,tamanno="pequenno")
        botones("Reiniciar",pantalla,ColorBoton1,Boton1,TamBoton,identidad="MenuGameOverReinicio")
        botones("Menu Principal",pantalla,ColorBoton2,Boton2,TamBoton,identidad="MenuGameOverMenu")
        botones("Salir",pantalla,ColorBoton2,Boton3,TamBoton,identidad="MenuGameOverSalida")

        #Impide el desvanecimiento del contenido de la pantalla
        pygame.display.update()

def MenuDificultad():
    """
        Muestra el Menu De Dificultad
    """
    global juego
    global introJuego
    global Dificultad
    global ingresar

    pantalla=pygame.display.set_mode((ANCHO,ALTO))
    while Dificultad:
        imagen=pygame.image.load("Menu.png")
        pantalla.blit(imagen,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                introJuego=False
                juego=False
                ingresar=False
                main()

            botones("Facil",pantalla,ColorBoton2,Boton1,TamBoton,identidad="DificultadFacil")
            botones("Dificil",pantalla,ColorBoton2,Boton2,TamBoton,identidad="DificultadDificil")
            pygame.display.update()

def MenuIntro():
    """
        Muestra el Menu Principal
    """
    global sonidoMenuPrincipal
    global juego
    global introJuego

    sonidoMenuPrincipal.play(-1)
    pantalla=pygame.display.set_mode((ANCHO,ALTO))

    while introJuego:
        imagen=pygame.image.load("Menu.png")
        pantalla.blit(imagen,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                juego=False
                introJuego=False
                main()

            botones("Jugar",pantalla,ColorBoton2,Boton1,TamBoton,identidad="MenuIntroComenzar")
            botones("Puntaje",pantalla,ColorBoton2,Boton2,TamBoton,identidad="MenuIntroPuntos")
            botones("Creditos",pantalla,ColorBoton2,Boton3,TamBoton,identidad="MenuIntroCreditos")
            botones("Salir",pantalla,ColorBoton2,Boton4,TamBoton,identidad="MenuIntroSalida")
            pygame.display.update()

def MenuPuntos(nombreUsuario,puntajeUsuario):
    """
    Recibe el nombre del usuario y el puntaje obtenido.
    Analiza los puntajes e imprime los records guardados
    """

    ###########################################################################
    #                      MANEJO DE ARCHIVOS                                 #
    ###########################################################################

    #Abrir los archivos
    archivo=open("Nombres.txt","r")
    archivo2=open("Puntajes.txt","r")
    listaDePuntajes=open("ListaPuntajes.txt","r")

    #Lectura de archivos
    #Se  pasan los nombres de los usuarios a una lista
    #Lista auxiliar
    nombres_aux=[]
    lineas=archivo.readlines()
    for linea in lineas:
        nombres_aux.append(linea)
    global nombres
    nombres=[]
    for i in range(5):
        if not i==4:
            nombres.append(nombres_aux[i][:-1])
    else:
        nombres.append(nombres_aux[i])

    #............................................................#
    #Se pasan los puntajes a una lista
    global puntajes
    puntajes=[]
    lineas2=archivo2.readlines()
    for linea in lineas2:
        puntajes.append(int(linea))

    #Ordenamos la lista de puntajes de mayor a menor
    puntajes.sort(reverse=True)

    #Verificamos el menor puntaje obtenido hasta ahora
    #Indicamos el menor puntaje obtenido
    menorPuntaje=min(puntajes)
    #Indice del menor puntaje
    indiceMenor=puntajes.index(menorPuntaje)

    #................................................................#

    global juego
    global introJuego
    global ingresar

    pantalla2=pygame.display.set_mode([600,393])
    fondoImagen=pygame.image.load("WizardRecord1.png")

    #COMPARAMOS EL PUNTAJE DEL USUARIO CON EL MENOR OBTENIDO HASTA AHORA#
    if puntajeUsuario>menorPuntaje:

        #Abrimos la lista de puntajes/nombres/puntajes para sobreescribirla
        listaDePuntajes=open("ListaPuntajes.txt","w")

        #Agregamos el puntaje del usuario a la lista de puntajes
        puntajes.append(puntajeUsuario)

        #Reordenamos la lista de puntajes de mayor a menor
        puntajes.sort(reverse=True)

        #Se busca el indice en el que aparece el puntaje del usuario
        ip=puntajes.index(puntajeUsuario)
        #Se ingresa el nombre del usuario con el mismo indice que su puntaje
        nombres.insert(ip,nombreUsuario)

        #Se eliminan los ultimos elementos de ambas listas
        puntajes.remove(menorPuntaje)
        nombres.pop()

        #------------------------------------------------------------------------#
        #ORDENAMOS ARMAMOS LA LISTA PARA REESCRIBIR EL ARCHIVO: LISTA DE PUNTAJES/NOMBRES/PUNTAJES#
        #------------------------------------------------------------------------#
        archivo=open("Nombres.txt","w")
        archivo2=open("Puntajes.txt","w")

                #Reinscribimos los archivos de nombres y puntajes
        for elemento in nombres:
            line=archivo.write(elemento+"\n")

        for elemento in puntajes:
            line2=archivo2.write(str(elemento)+"\n")

        listaPuntaje=[]

        #Establecemos un contador
        k=1

        #Armamos la lista de puntajes
        for i in range(len(puntajes)):
            linea=str(k)+". "+nombres[i]+" "+str(puntajes[i])+" "+"Puntos"
            listaPuntaje.append(linea)
            k+=1

        #Se escribe cada elemento de la lista como una linnea en el archivo
        for elemento in listaPuntaje:
            a=listaDePuntajes.write(elemento+"\n")

        fuenteRecords=pygame.font.SysFont("Comic Sans MS",14)
        titulo=fuenteRecords.render("*PUNTUACIONES*",0,(0,0,0))

        while ingresar:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    juego=False
                    introJuego=False
                    ingresar=False
                    main()

            pantalla2.blit(fondoImagen,(0,0))
            pantalla2.blit(titulo,(85,80))

            botones("Atras",pantalla,ColorBoton2,Boton5,TamBoton2,identidad="Atras")

            j=0
            for elemento in listaPuntaje:
                line=fuenteRecords.render(elemento,0,(0,0,0))
                pantalla2.blit(line,(85,100+j))
                j+=20

            pygame.display.update()

    #Si el usuario tiene un menor puntaje al ultimo guardado
    else:
        nombres[4]=(nombres[4])[:-1]

        listaPuntaje=[]
        #Establecemos un contador:
        k=1

        #Armamos la lista de puntajes
        for i in range(len(puntajes)):
            linea=str(k)+". "+nombres[i]+" "+str(puntajes[i])+" "+"Puntos"
            listaPuntaje.append(linea)
            k+=1

        fuenteRecords=pygame.font.SysFont("Comic Sans MS",14)
        titulo=fuenteRecords.render("*PUNTUACIONES*",0,(0,0,0))

        while ingresar:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    juego=False
                    introJuego=False
                    ingresar=False
                    main()

            pantalla2.blit(fondoImagen,(0,0))
            pantalla2.blit(titulo,(85,80))

            botones("Atras",pantalla,ColorBoton2,Boton5,TamBoton2,identidad="Atras")

            j=0
            for elemento in listaPuntaje:
                line=fuenteRecords.render(elemento,0,(0,0,0))
                pantalla2.blit(line,(85,100+j))
                j+=20

            pygame.display.update()

    archivo.close()
    archivo2.close()
    listaDePuntajes.close()

def IngresarNombre():

    #se prepara la pantalla para el usuario
    pantallaUsuario=pygame.display.set_mode([400,292])
    fondoImagen=pygame.image.load("IngresoNombre.png").convert_alpha()

    #Creamos fuente
    fuenteIngreso=pygame.font.Font(None,19)
    texto=fuenteIngreso.render("Ingrese su nombre: ",0,(0,0,0))

    global ingresar
    global juego
    global introJuego
    global premio

    nombreUsuario=""

    while ingresar:
        for event in pygame.event.get():
            #Si apreta "x" se sale:
            if event.type==pygame.QUIT:
                juego=False
                introJuego=False
                ingresar=False
                main()

            if event.type==KEYDOWN:
                letra=dameLetraApretada(event.key)
                if len(nombreUsuario)<=5:
                    nombreUsuario+=letra
                if event.key ==K_BACKSPACE:
                    nombreUsuario=nombreUsuario[0:len(nombreUsuario)-1]
                if event.key==K_RETURN:
                    ingresar=False
                    premio+=pygame.time.get_ticks()/1000-premio
                    return(nombreUsuario)

        pantallaUsuario.blit(fondoImagen,(0,0))
        pantallaUsuario.blit(texto,(45,35))
        escribirEnPantalla2(pantallaUsuario,nombreUsuario,(180,35))
        pygame.display.update()

def main():
    global juego
    global premio
    global ingresar
    global facil

    intro=MenuIntro()
    NombreUsuario=IngresarNombre()

    gameClock = pygame.time.Clock() ##Objeto que ayuda a controlar el tiempo
    pantalla=pygame.display.set_mode((ANCHO,ALTO))

    while juego:

        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()

        #pygame.mixer.init()
        global sonidoMenuPrincipal
        sonidoMenuPrincipal.stop()
        sonidoganar=pygame.mixer.Sound("correcto.ogg")
        sonidoperder=pygame.mixer.Sound("error.ogg")
        pygame.mixer.music.load("musica_principal.mp3")
        pygame.mixer.music.play(-1)

        #tiempo total del juego
        #gameClock = pygame.time.Clock() ##Objeto que ayuda a controlar el tiempo

        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial
        global puntos
        palabraUsuario = ""
        lemarioEnSilabas=[]
        listaPalabrasDiccionario=[]

        archivo= open("lemario.txt","r")
        archivo2= open ("lemarioSilabas.txt","r")

        #lectura del diccionario
        lectura(archivo, listaPalabrasDiccionario)

        #lectura del archivo en silabas
        lectura(archivo2, lemarioEnSilabas)

        #elige una al azar
        palabraEnSilabas=nuevaPalabra(lemarioEnSilabas)
        palabraActual=silabasTOpalabra(palabraEnSilabas)

        cont_aciertos=0
        dibujar(pantalla, palabraUsuario, palabraActual, puntos,segundos,facil)
        dibujar_2(pantalla,cont_aciertos)

        #Contador de aciertos, si se acumulan 5 aciertos consecutivos, se reproducira un efecto especial
        racha=pygame.mixer.Sound("racha_5.ogg")

        #n=0
        while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            if True:
            	fps = 60

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    quit()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    if len(palabraUsuario)<=20:
                        palabraUsuario += letra
                    if e.key == K_BACKSPACE:
                        palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]
                    if e.key == K_RETURN:
                        #pasa la palabra a silabas
                        palabraUsuarioEnSilabas=palabraTOsilaba(palabraUsuario)
                        #chequea si es correcta y suma o resta puntos, y ademas suma cantidad de aciertos
                        if procesar(palabraUsuario, palabraUsuarioEnSilabas,palabraActual, palabraEnSilabas, listaPalabrasDiccionario)>0:
                            premio+=5
                            puntos += procesar(palabraUsuario, palabraUsuarioEnSilabas,palabraActual, palabraEnSilabas, listaPalabrasDiccionario)
                            cont_aciertos=cont_aciertos+1
                        else:
                            premio+=0
                            puntos += procesar(palabraUsuario, palabraUsuarioEnSilabas,palabraActual, palabraEnSilabas, listaPalabrasDiccionario)
                            cont_aciertos=0
                        #reproduce sonido de acierto, perdida, o racha de aciertos
                        if cont_aciertos!=0:
                            if cont_aciertos>=5:
                                racha.play()
                            else:
                                sonidoganar.play()
                        else:
                            sonidoperder.play()

                        #busca la ultima silaba y busca una palabra que empiece asi
                        silaba=dameUltimaSilaba(palabraUsuarioEnSilabas)
                        palabraEnSilabas=buscarPalabraQueEmpieceCon(silaba,lemarioEnSilabas)

                        palabraActual=silabasTOpalabra(palabraEnSilabas)
                        palabraUsuario = ""

            #Imprime el menu Game Over
            if segundos<1:
                pygame.mixer.music.stop()
                ingresar=False
                MenuPuntos(NombreUsuario,puntos)
                MenuGameOver()

            global musica_15
            global musica_principal
            global musica_60

            #Musica cuando segundos <= 15
            if segundos<=15 and musica_15==True:
                musica_15=False
                pygame.mixer.music.load("musica_15.mp3")
                pygame.mixer.music.play(-1)
                musica_principal=True
                musica_60=True

            #Musica cuando segundos > 15
            if segundos>15 and musica_principal==True:
                musica_principal=False
                pygame.mixer.music.load("musica_16.mp3")
                pygame.mixer.music.play(-1)
                musica_15=True

            #Musica cuando puntos >60
            if segundos>15 and puntos>60 and musica_60==True:
                musica_principal=False
                musica_60=False
                pygame.mixer.music.load("musica_60.mp3")
                pygame.mixer.music.play(-1)
                musica_15=True

            #Cuenta regresiva constante del juego
            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000 +premio

            #Limpiar pantalla anterior
            imagen=pygame.image.load("Mago.png")
            pantalla.blit(imagen,(0,0))

            #Dibujar de nuevo todo
            dibujar(pantalla, palabraUsuario, palabraActual,puntos,segundos,facil)
            dibujar_2(pantalla,cont_aciertos)

            pygame.display.flip()

        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    juego=False

        archivo.close()
        archivo2.close()

    pygame.quit()
    quit()

#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()


