import pygame
import random
from funciones.datos import *
from data.variables import *

def verificar_respuesta(opcion, estado):
    '''
    Verifica si la respuesta seleccionada por el jugador es correcta o incorrecta
    y actualiza el estado del juego en consecuencia (puntaje, posición, mensaje, etc.).
    
    Si la respuesta es correcta:
    - Aumenta el puntaje.
    - Reproduce el sonido de acierto.
    - Avanza en el tablero (posiblemente más si cae en una escalera).
    
    Si la respuesta es incorrecta:
    - Resta puntos.
    - Reproduce el sonido de error.
    - Retrocede en el tablero (posiblemente más si cae en una serpiente).
    
    Parámetros:
    - opcion: índice (int) de la opción seleccionada por el jugador (-1 si no respondió a tiempo).
    - estado: diccionario con toda la información del juego (posición, puntaje, pregunta actual, etc.).
    
    Retorna:
    - estado actualizado con los nuevos valores de puntaje, posición, mensaje y estado del juego.
    '''
    correcta = opcion == estado["pregunta_actual"]["correcta"]
    movimiento = 1

    if correcta:
        estado["puntaje"] += PUNTOS_ACIERTO
        if sonido_correcto:
            sonido_correcto.play()
        estado["mensaje"] = "¡Respuesta correcta!"
        nueva_pos = min(estado["posicion"] + movimiento, CASILLEROS_TOTALES)
        if nueva_pos in casilleros_especiales:
            val = casilleros_especiales[nueva_pos]["valor"]
            nueva_pos = min(nueva_pos + val, CASILLEROS_TOTALES)
            estado["mensaje"] += f" ¡Escalera! avanzas {val}"
    else:
        estado["puntaje"] -= PUNTOS_ACIERTO
        if sonido_incorrecto:
            sonido_incorrecto.play()
        estado["mensaje"] = "Respuesta incorrecta"
        nueva_pos = max(estado["posicion"] - movimiento, 1)
        if nueva_pos in casilleros_especiales:
            val = casilleros_especiales[nueva_pos]["valor"]
            nueva_pos = max(nueva_pos - val, 1)
            estado["mensaje"] += f" ¡Serpiente! Retrocedes {val}"

    estado["posicion"] = nueva_pos
    estado["mostrar_mensaje"] = True
    estado["tiempo_mensaje"] = pygame.time.get_ticks()
    estado["esperando_confirmacion"] = True

    if "preguntas_restantes" in estado and estado["pregunta_actual"] in estado["preguntas_restantes"]:
        estado["preguntas_restantes"].remove(estado["pregunta_actual"])

    if not estado.get("preguntas_restantes"):
        estado["estado"] = FIN_JUEGO
        estado["mensaje"] = "Fin del juego, se acabaron las preguntas"
        estado = guardar_puntaje(estado)
        return estado

    if nueva_pos == 1 or nueva_pos >= CASILLEROS_TOTALES:
        estado["estado"] = FIN_JUEGO
        if "se acabaron las preguntas" not in estado["mensaje"].lower():
            estado["mensaje"] = "Fin del juego"
        estado = guardar_puntaje(estado)
    else:
        estado["pregunta_actual"] = random.choice(estado["preguntas_restantes"])

    return estado

