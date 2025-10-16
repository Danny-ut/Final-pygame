import pygame
from pygame.locals import *
from funciones.dibujar import *
from funciones.tablero import dibujar_tablero
from funciones.eventos import *
from data.variables import ESTADO_INICIAL

def main():
    pygame.init()
    pygame.mixer.music.load("sonidos/musica_fondo.wav")  
    pygame.mixer.music.set_volume(0.3)  
    pygame.mixer.music.play(-1)  
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Serpientes y Escaleras - Trivia")
    reloj = pygame.time.Clock()

    estado = ESTADO_INICIAL.copy()
    estado["puntajes"] = cargar_puntajes()
    estado["ultimo_tiempo"] = pygame.time.get_ticks()

    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if estado["estado"] == MENU:
                estado = manejar_eventos_menu(evento, estado)
            elif estado["estado"] == JUGANDO:
                estado = manejar_eventos_jugando(evento, estado)
            elif estado["estado"] == PUNTAJES and evento.type == MOUSEBUTTONDOWN:
                x, y = evento.pos
                if ANCHO//2 - 100 <= x <= ANCHO//2 + 100 and 550 <= y <= 590:
                    estado["estado"] = MENU
            elif estado["estado"] == FIN_JUEGO and evento.type == MOUSEBUTTONDOWN:
                x, y = evento.pos
                if ANCHO//2 - 100 <= x <= ANCHO//2 + 100 and 350 <= y <= 400:
                    estado["estado"] = MENU
                    estado.update(resetear_juego())

        if estado["estado"] == JUGANDO:
            estado = actualizar_tiempo(estado)

        pantalla.fill(BLANCO)
        if estado["estado"] == MENU:
            dibujar_menu(pantalla, estado)
        elif estado["estado"] == JUGANDO:
            dibujar_tablero(estado["posicion"], estado["jugador"], estado["puntaje"], estado["tiempo_restante"])
            if not estado["esperando_confirmacion"]:
                dibujar_pregunta(pantalla, estado["pregunta_actual"])
            else:
                dibujar_confirmacion(pantalla)
                dibujar_mensaje(pantalla, estado)
        elif estado["estado"] == PUNTAJES:
            dibujar_puntajes(pantalla, estado)
        elif estado["estado"] == FIN_JUEGO:
            dibujar_fin_juego(pantalla, estado)

        pygame.display.flip()
        reloj.tick(60)

main()
