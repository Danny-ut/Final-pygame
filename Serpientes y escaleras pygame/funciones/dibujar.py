import pygame
from data.variables import *
from funciones.datos import wrap_text

def dibujar_menu(pantalla, estado):
    '''
    Dibuja el menú principal del juego, incluyendo el campo para ingresar el nombre
    del jugador y los botones de "Jugar", "Ver Puntajes" y "Salir".
    
    Parámetros:
    - pantalla: superficie de pygame donde se dibuja el menú.
    - estado: diccionario con los datos actuales del juego (nombre del jugador, etc.).
    '''
    if fondo_img:
        pantalla.blit(fondo_img, (0, 0))
    else:
        pantalla.fill(AZUL_CLARO)

    titulo = fuente_grande.render("Serpientes y Escaleras", True, NEGRO)
    pantalla.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 100))

    pygame.draw.rect(pantalla, BLANCO, (ANCHO // 2 - 150, 200, 300, 40))
    nombre_texto = fuente_med.render(f"Nombre: {estado['jugador']}", True, NEGRO)
    pantalla.blit(nombre_texto, (ANCHO // 2 - 140, 210))

    botones = [("Jugar", VERDE, 300), ("Ver Puntajes", AMARILLO, 370), ("Salir", ROJO, 440)]
    for texto, color, y in botones:
        pygame.draw.rect(pantalla, color, (ANCHO // 2 - 100, y, 200, 50))
        t = fuente_med.render(texto, True, NEGRO)
        pantalla.blit(t, (ANCHO // 2 - t.get_width() // 2, y + 15))

def dibujar_fondo(pantalla):
    '''
    Dibuja el fondo principal del juego, usando la imagen de fondo si está cargada.
    
    Parámetros:
    - pantalla: superficie de pygame donde se dibuja el fondo.
    '''
    pantalla.blit(fondo_img, (0, 0)) if fondo_img else pantalla.fill(BLANCO)

def dibujar_pregunta(pantalla, pregunta):
    '''
    Dibuja en pantalla el recuadro con la pregunta y sus opciones de respuesta.
    
    Parámetros:
    - pantalla: superficie de pygame donde se dibuja la pregunta.
    - pregunta: diccionario con las claves "pregunta" (texto) y "opciones" (lista de respuestas).
    '''
    pygame.draw.rect(pantalla, AZUL_CLARO, (50, 340, 800, 125))
    pygame.draw.rect(pantalla, NEGRO, (50, 340, 800, 125), 2)

    for i, line in enumerate(wrap_text(pregunta["pregunta"], fuente_med, 780)):
        texto = fuente_med.render(line, True, NEGRO)
        pantalla.blit(texto, (60, 350 + i * 30))

    for i, opcion in enumerate(pregunta["opciones"]):
        x = 100 + i * 250
        pygame.draw.rect(pantalla, AMARILLO, (x, 410, 200, 40))
        pygame.draw.rect(pantalla, NEGRO, (x, 410, 200, 40), 2)
        texto = fuente_peq.render(opcion, True, NEGRO)
        pantalla.blit(texto, (x + 100 - texto.get_width() // 2, 427 - texto.get_height() // 2))

def dibujar_confirmacion(pantalla):
    '''
    Dibuja una ventana de confirmación para preguntar al jugador si desea continuar jugando.
    
    Parámetros:
    - pantalla: superficie de pygame donde se dibuja la ventana de confirmación.
    '''
    rect = pygame.Rect(ANCHO // 2 - 200, ALTO // 2 - 75, 400, 150)
    pygame.draw.rect(pantalla, AMARILLO, rect)
    pygame.draw.rect(pantalla, NEGRO, rect, 3)
    texto = fuente_med.render("¿Querés seguir jugando?", True, NEGRO)
    pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2 - 50))

    botones = [("Sí", VERDE, -120), ("No", ROJO, 30)]
    for t, c, dx in botones:
        pygame.draw.rect(pantalla, c, (ANCHO // 2 + dx, ALTO // 2, 120, 40))
        txt = fuente_med.render(t, True, NEGRO)
        pantalla.blit(txt, (ANCHO // 2 + dx + 60 - txt.get_width() // 2, ALTO // 2 + 20 - txt.get_height() // 2))

def dibujar_mensaje(pantalla, estado):
    '''
    Dibuja un mensaje temporal en el centro de la pantalla (por ejemplo, "Respuesta correcta").
    
    Parámetros:
    - pantalla: superficie de pygame donde se muestra el mensaje.
    - estado: diccionario con el estado del juego (mensaje actual, tiempo, etc.).
    '''
    if estado["mostrar_mensaje"] and pygame.time.get_ticks() - estado["tiempo_mensaje"] < 2000:
        rect = pygame.Rect(ANCHO // 2 - 400, ALTO // 2 - 25, 800, 50)
        pygame.draw.rect(pantalla, BLANCO, rect)
        pygame.draw.rect(pantalla, NEGRO, rect, 2)
        texto = fuente_med.render(estado["mensaje"], True, NEGRO)
        pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2 - texto.get_height() // 2))

def dibujar_puntajes(pantalla, estado):
    '''
    Dibuja la pantalla de los mejores puntajes del juego.
    
    Parámetros:
    - pantalla: superficie de pygame donde se dibuja el listado de puntajes.
    - estado: diccionario que contiene la lista de puntajes.
    '''
    if fondo_img:
        pantalla.blit(fondo_img, (0, 0))
    else:
        pantalla.fill(BLANCO)

    titulo = fuente_grande.render("Mejores Puntajes", True, NEGRO)
    pantalla.blit(titulo, (ANCHO//2 - titulo.get_width()//2, 50))
    
    if not estado["puntajes"]:
        texto = fuente_med.render("No hay puntajes aún", True, NEGRO)
        pantalla.blit(texto, (ANCHO//2 - texto.get_width()//2, 150))
    else:
        for i, p in enumerate(estado["puntajes"][:10]):
            texto = fuente_med.render(f"{i+1}. {p['nombre']}: {p['puntaje']}", True, NEGRO)
            pantalla.blit(texto, (ANCHO//2 - texto.get_width()//2, 120 + i * 40))
    
    pygame.draw.rect(pantalla, VERDE, (ANCHO//2 - 100, 550, 200, 40))
    volver_texto = fuente_med.render("Volver al Menú", True, NEGRO)
    pantalla.blit(volver_texto, (ANCHO//2 - volver_texto.get_width()//2, 560))

def dibujar_fin_juego(pantalla, estado):
    '''
    Dibuja la pantalla final del juego, mostrando el mensaje de fin, puntaje del jugador
    y su posición en el ranking.
    
    Parámetros:
    - pantalla: superficie de pygame donde se dibuja la pantalla final.
    - estado: diccionario con los datos del jugador, puntaje y ranking.
    '''
    if fondo_img:
        pantalla.blit(fondo_img, (0, 0))
    else:
        pantalla.fill(BLANCO)

    mensaje_final = estado.get("mensaje", "Fin del juego")

    titulo = fuente_grande.render(mensaje_final, True, NEGRO)
    pantalla.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 100))
    
    resultado = fuente_med.render(f"{estado['jugador']}, tu puntaje final es: {estado['puntaje']}", True, NEGRO)
    pantalla.blit(resultado, (ANCHO // 2 - resultado.get_width() // 2, 200))
    
    rank = 1 + sum(p["puntaje"] > estado["puntaje"] for p in estado["puntajes"])
    pos_texto = fuente_med.render(f"Tu posición en el ranking: {rank}", True, NEGRO)
    pantalla.blit(pos_texto, (ANCHO // 2 - pos_texto.get_width() // 2, 250))
    
    pygame.draw.rect(pantalla, VERDE, (ANCHO // 2 - 100, 350, 200, 50))
    texto = fuente_med.render("Volver al Menú", True, NEGRO)
    pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, 365))
