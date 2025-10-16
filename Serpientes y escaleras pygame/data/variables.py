import pygame
from data.config import *

pygame.init()

fuente_peq = pygame.font.SysFont("Arial", TAMANO_FUENTE_PEQ)
fuente_med = pygame.font.SysFont("Arial", TAMANO_FUENTE_MED, bold=True)
fuente_grande = pygame.font.SysFont("Arial", TAMANO_FUENTE_GRANDE, bold=True)

sonido_correcto = pygame.mixer.Sound("sonidos/correcto.wav")
sonido_incorrecto = pygame.mixer.Sound("sonidos/incorrecto.wav")

fondo_img = pygame.image.load("imagenes/fondo.png")
fondo_img = pygame.transform.scale(fondo_img, (ANCHO, ALTO))

fondo_tablero = pygame.image.load("imagenes/fondo_tablero.png")
fondo_tablero = pygame.transform.scale(fondo_tablero, (ANCHO - 2*MARGEN_TABLERO, ALTO - 2*MARGEN_TABLERO))


casilleros_especiales = {
    3: {"valor": 1, "color": DORADO},
    8: {"valor": 1, "color": DORADO},
    10:{"valor": 2, "color": NARANJA},
    13: {"valor": 2, "color": NARANJA},
    16: {"valor": 1, "color": DORADO},
    18: {"valor": 1, "color": DORADO},
    21: {"valor": 2, "color": NARANJA},
    25: {"valor": 2, "color": NARANJA},
    28: {"valor": 1, "color": DORADO}
}

# ------------------ ESTADO INICIAL DEL JUEGO ------------------

ESTADO_INICIAL = {
    "estado": MENU,
    "jugador": "",
    "pregunta_actual": None,
    "posicion": POSICION_INICIAL,
    "puntaje": 0,
    "tiempo_restante": TIEMPO_PREGUNTA,
    "ultimo_tiempo": 0,  
    "mostrar_mensaje": False,
    "mensaje": "",
    "tiempo_mensaje": 0,
    "esperando_confirmacion": False,
    "puntajes": [],
    "preguntas_restantes": []
}
