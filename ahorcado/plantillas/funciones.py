import string
import unicodedata
from random import choice

def carga_archivo_texto(archivo: str) -> list:
    '''
    Carga un archivo de texto y devuelve una lista con las oraciones del archivo
    '''
    with open(archivo, 'r', encoding='utf-8') as file:
        oraciones = file.readlines()
    return oraciones

def carga_plantillas(nombre_plantilla: str) -> dict:
    '''
    Carga las plantillas del juego apartir de un archivo de texto
    '''
    plantillas = {}
    for i in range(6):
        plantillas[i] = carga_archivo_texto(f'C:/Users/52662/Desktop/Desarrollo4_WalterAlejandro/curso_python/ahorcado/plantillas/{nombre_plantilla}-{i}.txt')
    return plantillas

def despliega_plantilla(diccionario: dict, nivel: int):
    '''
    Despliega una plantilla del juego
    '''
    if nivel >= 0 and nivel <= 5:
        plantilla = diccionario[nivel]
        for renglon in plantilla:
            print(renglon)

def obten_palabras(lista: list) -> list:
    '''
    Obtiene las palabras de los datos.
    '''
    texto = ' '.join(lista[120:])  # Concatenar las líneas del archivo en una cadena
    palabras = texto.split()  # Dividir el texto en palabras
    # Convertimos a minúsculas
    minusculas = [palabra.lower() for palabra in palabras]
    set_palabras = set(minusculas)  # Eliminamos duplicados

    # Removemos signos de puntuación y caracteres especiales
    set_palabras = {palabra.strip(string.punctuation) for palabra in set_palabras}

    # Removemos números, paréntesis, corchetes y otros caracteres no alfabéticos
    set_palabras = {palabra for palabra in set_palabras if palabra.isalpha()}

    # Removemos acentos
    set_palabras = {unicodedata.normalize('NFKD', palabra).encode('ascii', 'ignore').decode('ascii') for palabra in set_palabras}

    return list(set_palabras)  # Aseguramos de retornar la lista de palabras procesadas


def adivinina_letra(abc: str, palabra: str, letras_adivinadas: set, letras_fallidas: set, turnos: int):
    '''
    Adivina una letra de una palabra.
    '''
    palabra_oculta = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_oculta += letra
        else:
            palabra_oculta += "_"
    
    print(f'La palabra es: {palabra_oculta}')
    
    # Mostrar el abecedario con letras ya utilizadas reemplazadas por '*' o '-'
    abecedario_visible = ""
    for letra in abc:
        if letra in letras_adivinadas:
            abecedario_visible += "*"
        elif letra in letras_fallidas:
            abecedario_visible += "-"
        else:
            abecedario_visible += letra
    
    print(f'Abecedario: {abecedario_visible}')
    
    letra = input('Ingresa una letra: ').lower()
    
    if len(letra) != 1 or letra not in abc:
        print('Ingresa una letra válida')
    elif letra in letras_adivinadas or letra in letras_fallidas:
        print('Ya ingresaste esa letra')
    else:
        if letra in palabra:
            letras_adivinadas.add(letra)
            print('Bien hecho')
        else:
            letras_fallidas.add(letra)
            turnos -= 1
            if turnos > 0:  # Solo mostrar los intentos restantes si no quedan 0 intentos
                print(f'Letra incorrecta, te quedan {turnos} intentos')

    return turnos, letras_adivinadas, letras_fallidas  # Retornamos los turnos, el conjunto de letras adivinadas y fallidas







