'''
este archi es el punto de entrada de la aplicación
'''
import tablero

def main():
    '''
    Funion principal
    '''
    X = {"G":0,"E":0,"P":0}
    O = {"G":0,"E":0,"P":0}
    score = {"X":X,"O":O}
    numeros = [str(i) for i in range (1,10)]
    corriendo = True
    while corriendo:
        dsimbolos = {x: x for x in numeros}
        g = tablero.juego(dsimbolos)
        tablero.actualiza_score(score, g)
        tablero.despliega_tablero(score)
        seguir = input('¿Quieres seguir jugando? (s/n): ')
        while corriendo is not False or True:
            if seguir.lower() == 'n':
                corriendo = False
            elif seguir.lower() == 's':
                corriendo = True


if __name__ == '__main__':
    main()