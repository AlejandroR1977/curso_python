import matplotlib.pyplot as plt

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
    assert calcular_y (0.0, 2.0, 3.0)
    return (m*b) + y

def grafica_linea(X:list,Y:list, m:float, b:float):
    plt.plot(X, Y)
    plt.title(f'linea con pendiente {m} y ordenada al origen {b}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

if __name__ == '__main__':
    if test_lineal() == 3.0:
        print('Todo bien')
    else:
        print('Algo salio mal')