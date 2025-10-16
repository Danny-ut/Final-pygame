import pygame
from data.variables import *
from funciones.dibujar import *

def obtener_color_casillero(num):
    '''
    Devuelve el color y el valor asociado a un casillero específico del tablero.
    
    Parámetros:
    - num: número del casillero (int).
    
    Retorna:
    - Una tupla (color, valor) donde:
      - color es el color del casillero según su tipo (normal, especial, inicio o fin).
      - valor es el número de avance o retroceso si es un casillero especial.
    '''
    if num == 1:
        return ROJO, 0
    elif num == CASILLEROS_TOTALES:
        return AZUL, 0
    elif num in casilleros_especiales:
        e = casilleros_especiales[num]
        return e["color"], e["valor"]
    return VERDE_CLARO, 0

def obtener_posicion_casillero(num):
    '''
    Calcula las coordenadas (x, y) en pantalla correspondientes al casillero indicado.
    
    Parámetros:
    - num: número del casillero (int).
    
    Retorna:
    - Una tupla (x, y) con las coordenadas donde debe dibujarse el casillero.
    '''
    fila = (num - 1) // COLUMNAS
    col = (num - 1) % COLUMNAS
    x = INICIO_X + col * ANCHO_CASILLA
    y = INICIO_Y + fila * ALTO_CASILLA
    return x, y

def dibujar_casillero(pantalla, fuente, num):
    '''
    Dibuja en pantalla un casillero individual con su número y color correspondiente.
    
    Parámetros:
    - pantalla: superficie de pygame donde se dibuja el casillero.
    - fuente: fuente de texto utilizada para renderizar el número del casillero.
    - num: número del casillero (int).
    '''
    x, y = obtener_posicion_casillero(num)
    color, _ = obtener_color_casillero(num)

    pygame.draw.rect(pantalla, color, (x, y, ANCHO_CASILLERO, ANCHO_CASILLERO))
    pygame.draw.rect(pantalla, NEGRO, (x, y, ANCHO_CASILLERO, ANCHO_CASILLERO), 1)

    texto = fuente.render(str(num), True, NEGRO)
    pantalla.blit(
        texto,
        (x + ANCHO_CASILLERO // 2 - texto.get_width() // 2,
         y + ANCHO_CASILLERO // 2 - texto.get_height() // 2)
    )

def dibujar_tablero(posicion, jugador, puntaje, tiempo_restante):
    '''
    Dibuja todo el tablero de juego junto con la información del jugador
    (nombre, puntaje y tiempo restante).
    
    Parámetros:
    - posicion: número de casillero actual del jugador (int).
    - jugador: nombre del jugador (str).
    - puntaje: puntaje actual del jugador (int).
    - tiempo_restante: tiempo restante para responder (int).
    '''
    pantalla = pygame.display.get_surface()
    fuente = pygame.font.SysFont("Arial", 14, bold=True)

    dibujar_fondo(pantalla)
    pantalla.blit(fondo_tablero, (MARGEN_TABLERO, MARGEN_TABLERO))
    pygame.draw.rect(
        pantalla,
        NEGRO,
        (MARGEN_TABLERO, MARGEN_TABLERO, ANCHO - 2 * MARGEN_TABLERO, ALTO - 2 * MARGEN_TABLERO),
        2
    )

    for num in range(1, CASILLEROS_TOTALES + 1):
        dibujar_casillero(pantalla, fuente, num)

    dibujar_jugador(pantalla, posicion)
    dibujar_info(pantalla, jugador, puntaje, tiempo_restante)

def dibujar_jugador(pantalla, posicion):
    '''
    Dibuja al jugador como un círculo rojo sobre el casillero correspondiente.
    
    Parámetros:
    - pantalla: superficie de pygame donde se dibuja al jugador.
    - posicion: número del casillero en el que se encuentra el jugador (int).
    '''
    if not (1 <= posicion <= CASILLEROS_TOTALES):
        return
    x, y = obtener_posicion_casillero(posicion)
    pygame.draw.circle(pantalla, ROJO, (x + ANCHO_CASILLERO // 2, y + ANCHO_CASILLERO // 2), 15)
    pygame.draw.circle(pantalla, NEGRO, (x + ANCHO_CASILLERO // 2, y + ANCHO_CASILLERO // 2), 15, 1)

def dibujar_info(pantalla, jugador, puntaje, tiempo_restante):
    '''
    Muestra la información del jugador en la parte inferior de la pantalla,
    incluyendo su nombre, puntaje actual y tiempo restante.
    
    Parámetros:
    - pantalla: superficie de pygame donde se muestra la información.
    - jugador: nombre del jugador (str).
    - puntaje: puntaje actual (int).
    - tiempo_restante: segundos restantes para responder (int).
    '''
    fuente = pygame.font.SysFont("Arial", TAMANO_FUENTE_MED, bold=True)
    x, y = 65, 465
    pantalla.blit(fuente.render(f"Jugador: {jugador}", True, NEGRO), (x, y))
    pantalla.blit(fuente.render(f"Puntaje: {puntaje}", True, NEGRO), (x, y + 30))
    pantalla.blit(fuente.render(f"Tiempo: {tiempo_restante}", True, NEGRO), (x, y + 60))
