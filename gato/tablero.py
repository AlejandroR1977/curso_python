'''
tablero.py: dibuja el tablero del juego de el gato
'''
import random
def dibuja_tablero(simbolos:dict):
    '''
    Dibuja tablero del juego de el gato
    '''
    for i in range(1,10):
        if str(i) not in simbolos:
            simbolos[str(i)] = ''

    print(f'''
          {simbolos['1']} | {simbolos['2']} | {simbolos['3']}
      ----------------
          {simbolos['4']} | {simbolos['5']} | {simbolos['6']}
      ----------------
          {simbolos['7']} | {simbolos['8']} | {simbolos['9']}
        ''')

def ia(simbolos:dict):
    '''Juega la maquina'''
    ocupado = True
    while ocupado is True:
        x = random.choice(list(simbolos.keys()))
        if simbolos[x] not in ['X','O']:
            simbolos[x] = 'O'
            ocupado = False

def usuario(simbolos:dict):
    '''Juega el usuario'''
    lista_numeros = [str(i) for i in range(1,10)]
    ocupado = True
    while ocupado is True:
        x = input('ingresa el número de la casilla:')
        if x in lista_numeros:
            if simbolos[x] not in ['X','O']:
                simbolos[x] = 'X'
                ocupado = False
            else:
                print ('Casilla ocupada')
        else:
            print('numero incorrecto')
def juego(simbolos:dict):
    '''Juego del gato'''
    lista_combinaciones = {
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9'],
        ['1','4','7'],
        ['2','5','8'],
        ['3','6','9'],
        ['1','5','9'],
        ['3','5','7']        
        }
    en_juego = True
    ganador = ""
    movimientos = 0
    while en_juego:
        dibuja_tablero(simbolos)
        usuario(simbolos)
        dibuja_tablero(simbolos)
        movimientos += 1
        gana = checa_winner(simbolos, lista_combinaciones)
        if gana is True:
            en_juego = False
            ganador = "usuario/a"
        ia(simbolos)
        dibuja_tablero(simbolos)
        movimientos += 1
        gana = checa_winner(simbolos, lista_combinaciones)
        if gana is True:
            en_juego = False
            ganador = "computadora"
        if movimientos < 9:
            usuario(simbolos)
            dibuja_tablero(simbolos)
            movimientos += 1
            gana = checa_winner(simbolos, lista_combinaciones)
            if gana is True:
                en_juego = False
            if movimientos >= 9:
                en_juego = False
        else:
            en_juego = False



def checa_winner(simbolos:dict, combinaciones:list):
    '''Checa si hay ganador'''
    for c in combinaciones:
        if simbolos[c[0]] == simbolos[1] == simbolos[2]:
            return simbolos[c[0]]
        return None

if __name__ == '__main__':
    numeros = [str(x) for x in range (1,10)]
    dsimbolos = {x: x for x in numeros}
    juego(dsimbolos)
    '''
    dibuja_tablero(dsimbolos)
    ia(dsimbolos)
    dibuja_tablero(dsimbolos)
    usuario(dsimbolos)
    dibuja_tablero(dsimbolos)
    x = random.choice(numeros)
    numeros.remove(x)
    dsimbolos[x] = 'X'
    dibuja_tablero(dsimbolos)
    o = random.choice(numeros)
    numeros.remove(o)
    dsimbolos[o] = 'O'
    dibuja_tablero(dsimbolos)
    print(numeros)
    '''

