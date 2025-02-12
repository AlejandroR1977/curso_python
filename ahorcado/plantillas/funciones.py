import string
import unicodedata
from random import choice

def carga_archivo_texto(archivo:str)->list:
    '''
    Carga un archivo de texto y devuelve una lista con las oraciones del archivo
    '''
    with open(archivo, 'r', encoding='utf-8') as file:
        oraciones = file.readlines()
    return oraciones

def carga_plantillas(nombre_plantilla:str)->dict:
    '''
    Carga las plantillas del juego apartir de un archivo de texto
    '''
    plantillas = {}
    for i in range(6):
        plantillas[i] = carga_archivo_texto(f'C:/Users/52662/Desktop/Desarrollo4_WalterAlejandro/curso_python/ahorcado/plantillas/{nombre_plantilla}-{i}.txt')
    return plantillas

def despliega_plantilla(diccionario:dict, nivel:int):
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


def adivinina_letra(abc: str, palabra: str, letras_adivinadas: set, turnos: int):
    '''
    Adivina una letra de una palabra.
    '''
    palabra_oculta = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_oculta += letra
        else:
            palabra_oculta += "_"
    
    print(f'Tienes {turnos} turnos')
    print(f'La palabra es: {palabra_oculta}')
    print(f'El abecedario es: {abc}')
    
    letra = input('Ingresa una letra: ').lower()
    
    if len(letra) != 1 or letra not in abc:
        print('Ingresa una letra válida')
    elif letra in letras_adivinadas:
        print('Ya ingresaste esa letra')
    else:
        if letra in palabra:
            letras_adivinadas.add(letra)
            print('Bien hecho')
        else:
            turnos -= 1
            print(f'Letra incorrecta, te quedan {turnos} turnos')

    return turnos  # Retornar los turnos actualizados


if __name__ == '__main__':
    plantilla = carga_plantillas('plantilla')
    despliega_plantilla(plantilla,5)
    lista_oraciones = carga_archivo_texto('C:/Users/52662/Desktop/Desarrollo4_WalterAlejandro/curso_python/ahorcado/datos/pg15532.txt')
    lista_palabras = obten_palabras(lista_oraciones)
    print(len(lista_palabras))
    p = choice(lista_palabras)
    print(p)
    abcdario = {letra: letra for letra in string.ascii_lowercase}
    letras_adivinadas = set()
    turnos = 5
    print(f"Tienes {turnos} turnos")
    print(f'El abecedario es: {abcdario}')
    adivinina_letra(abcdario, p, letras_adivinadas, turnos)
    print(f"Tienes {turnos} turnos")
    adivinina_letra(abcdario, p, letras_adivinadas, turnos)
