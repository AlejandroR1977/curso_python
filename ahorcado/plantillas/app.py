from funciones import carga_plantillas, carga_archivo_texto, obten_palabras, adivinina_letra, despliega_plantilla
import string
from random import choice

class App:
    def __init__(self):
        self.plantilla = carga_plantillas('plantilla')
        self.lista_oraciones = carga_archivo_texto('C:/Users/52662/Desktop/Desarrollo4_WalterAlejandro/curso_python/ahorcado/datos/pg15532.txt')
        self.lista_palabras = obten_palabras(self.lista_oraciones)
        self.abcdario = string.ascii_lowercase  # Solo las letras del abecedario
        self.letras_adivinadas = set()
        self.letras_fallidas = set()
        self.turnos = 5
        self.plantilla_mostrar = 5  # Empezamos con la plantilla 5
        self.p = choice(self.lista_palabras)  # Elegir una palabra aleatoria

    def run(self):
        # Solo imprimimos los intentos una vez, antes de la primera llamada a la función
        print(f"Tienes {self.turnos} intentos")
        
        # Desplegar la plantilla 5 al principio
        despliega_plantilla(self.plantilla, self.plantilla_mostrar)

        while self.turnos > 0:
            # Llamada a la función, sin necesidad de imprimir los intentos aquí nuevamente
            self.turnos, self.letras_adivinadas, self.letras_fallidas = adivinina_letra(self.abcdario, self.p, self.letras_adivinadas, self.letras_fallidas, self.turnos)
            
            # Si la palabra es adivinada, salimos del ciclo
            if all(letra in self.letras_adivinadas for letra in self.p):
                print(f"¡Ganaste! La palabra es '{self.p}'.")
                break
            
            # Si el jugador falló, mostramos la siguiente plantilla
            if self.turnos < 5:
                self.plantilla_mostrar -= 1  # Reducimos el nivel de plantilla para el siguiente turno
                despliega_plantilla(self.plantilla, self.plantilla_mostrar)

        # Si se pierde, mostramos la plantilla 0 al final
        if self.turnos == 0:
            despliega_plantilla(self.plantilla, 0)
            print(f"¡Perdiste! La palabra era '{self.p}'.")

if __name__ == "__main__":
    app = App()
    app.run()
