import json
import random
from data.preguntas import preguntas

def cargar_puntajes():
    '''
    Carga los puntajes guardados desde el archivo JSON ("puntajes.json").
    Si el archivo no existe o contiene errores, devuelve una lista vacía.
    
    Parámetros:
    - Ninguno.
    
    Retorna:
    - Lista de puntajes cargados desde el archivo, o una lista vacía si no se pudo leer.
    '''
    try:
        with open("puntajes.json", "r") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_puntaje(estado):
    '''
    Guarda el puntaje actual del jugador en el archivo "puntajes.json"
    y actualiza el listado general de puntajes ordenado de mayor a menor.
    
    Parámetros:
    - estado: diccionario con la información del juego (jugador, puntaje, lista de puntajes, etc.).
    
    Retorna:
    - estado actualizado, con la lista de puntajes actualizada.
    '''
    estado["puntajes"].append({"nombre": estado["jugador"], "puntaje": estado["puntaje"]})
    estado["puntajes"].sort(key=lambda x: x["puntaje"], reverse=True)
    with open("puntajes.json", "w") as archivo:
        json.dump(estado["puntajes"], archivo, indent=4)
    return estado

def obtener_pregunta_aleatoria():
    '''
    Devuelve una pregunta aleatoria del banco de preguntas.
    
    Parámetros:
    - Ninguno.
    
    Retorna:
    - Diccionario que representa una pregunta con sus opciones y respuesta correcta.
    '''
    return random.choice(preguntas)

def obtener_todas_las_preguntas():
    '''
    Devuelve una copia completa del banco de preguntas del juego.
    
    Parámetros:
    - Ninguno.
    
    Retorna:
    - Lista de todas las preguntas disponibles.
    '''
    return preguntas.copy()

def wrap_text(text, font, max_width):
    '''
    Divide un texto largo en varias líneas, asegurando que cada línea no
    exceda el ancho máximo permitido en píxeles. Útil para mostrar textos
    largos en pantalla (como las preguntas del juego).
    
    Parámetros:
    - text: texto a dividir (str).
    - font: objeto pygame.font usado para calcular el ancho del texto.
    - max_width: ancho máximo permitido por línea (int).
    
    Retorna:
    - Lista de cadenas, donde cada elemento es una línea ajustada al ancho.
    '''
    words = text.split(' ')
    lines, current_line = [], []
    for word in words:
        test_line = ' '.join(current_line + [word])
        if font.size(test_line)[0] <= max_width:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
    if current_line:
        lines.append(' '.join(current_line))
    return lines

