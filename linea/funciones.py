def calcular_y(x, m, b):
    '''
    Calcula el valor de y en una linea recta
    x: el valor de x
    m: pendiente
    b: intersección en y
    regresa el valor de y:
    '''
    return (m*x) + b

def test_lineal():
    '''
    Prueba de funcionamiento de calcular_y()
    '''
    assert calcular_y (0, 2, 3) = 3
    return y

if _name: == '_main_':
    if test_lineal() == 3:
        print('Todo bien')
    else:
        print('Algo salio mal')