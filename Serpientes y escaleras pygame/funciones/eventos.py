import pygame
import sys
from funciones.logica import *

def manejar_eventos_menu(evento, estado):
    '''
    Gestiona los eventos que ocurren en el menú principal:
    ingreso del nombre del jugador mediante el teclado y clics en los botones
    "Jugar", "Ver Puntajes" o "Salir".
    
    Parámetros:
    - evento: evento de teclado o mouse capturado por pygame.
    - estado: diccionario con el estado actual del juego (nombre del jugador, estado, etc.).
    
    Retorna:
    - estado actualizado según la acción realizada por el jugador.
    '''
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_BACKSPACE:
            estado["jugador"] = estado["jugador"][:-1]
        elif evento.unicode.isprintable():
            estado["jugador"] += evento.unicode

    elif evento.type == pygame.MOUSEBUTTONDOWN:
        x, y = evento.pos
        if ANCHO // 2 - 100 <= x <= ANCHO // 2 + 100:
            if 300 <= y <= 350 and estado["jugador"].strip():
                estado["estado"] = JUGANDO
                
                estado["preguntas_restantes"] = obtener_todas_las_preguntas().copy()
                
                estado["pregunta_actual"] = random.choice(estado["preguntas_restantes"])
                estado["ultimo_tiempo"] = pygame.time.get_ticks()
            elif 370 <= y <= 420:
                estado["estado"] = PUNTAJES
            elif 440 <= y <= 490:
                pygame.quit()
                sys.exit()
    return estado

def manejar_eventos_jugando(evento, estado):
    '''
    Gestiona los eventos que ocurren durante la partida:
    clics sobre las opciones de respuesta, decisiones de continuar o finalizar
    y detección de la tecla ESC para salir del juego.
    
    Parámetros:
    - evento: evento de teclado o mouse capturado por pygame.
    - estado: diccionario con la información actual del juego (pregunta, posición, puntaje, etc.).
    
    Retorna:
    - estado actualizado después de procesar el evento.
    '''
    if estado["esperando_confirmacion"]:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            
            if ANCHO // 2 - 150 <= x <= ANCHO // 2 - 30 and ALTO // 2 <= y <= ALTO // 2 + 40:
                estado["esperando_confirmacion"] = False
                if estado["posicion"] == 1 or estado["posicion"] >= CASILLEROS_TOTALES:
                    estado["estado"] = FIN_JUEGO
                    estado = guardar_puntaje(estado)
                else:
                    
                    if estado["preguntas_restantes"]:
                        estado["pregunta_actual"] = random.choice(estado["preguntas_restantes"])
                        estado["tiempo_restante"] = TIEMPO_PREGUNTA
                        estado["ultimo_tiempo"] = pygame.time.get_ticks()
                    else:
                        estado["estado"] = FIN_JUEGO
                        estado["mensaje"] = "Fin del juego, se acabaron las preguntas"
                        estado = guardar_puntaje(estado)

            elif ANCHO // 2 + 30 <= x <= ANCHO // 2 + 150 and ALTO // 2 <= y <= ALTO // 2 + 40:
                estado["esperando_confirmacion"] = False
                estado["estado"] = FIN_JUEGO
                estado = guardar_puntaje(estado)
    elif evento.type == pygame.MOUSEBUTTONDOWN:
        x, y = evento.pos
        for i in range(3):
            if 100 + i * 250 <= x <= 300 + i * 250 and 410 <= y <= 450:
                estado = verificar_respuesta(i, estado)
    elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
        estado["estado"] = FIN_JUEGO
        estado = guardar_puntaje(estado)
    return estado

def actualizar_tiempo(estado):
    '''
    Actualiza el temporizador del juego mientras el jugador responde preguntas.
    Si el tiempo se agota, se considera una respuesta incorrecta.
    
    Parámetros:
    - estado: diccionario con la información temporal y de progreso del juego.
    
    Retorna:
    - estado actualizado con el tiempo restante o resultado de la verificación.
    '''
    if not estado["esperando_confirmacion"]:
        ahora = pygame.time.get_ticks()
        if ahora - estado["ultimo_tiempo"] >= 1000:
            estado["tiempo_restante"] -= 1
            estado["ultimo_tiempo"] = ahora
            if estado["tiempo_restante"] <= 0:
                estado["tiempo_restante"] = 0
                estado = verificar_respuesta(-1, estado)
    return estado

def resetear_juego():
    '''
    Reinicia las variables principales del juego: puntaje, posición y tiempo restante.
    
    Retorna:
    - Un diccionario con los valores iniciales del juego.
    '''
    return {"puntaje": 0, "posicion": POSICION_INICIAL, "tiempo_restante": TIEMPO_PREGUNTA}
