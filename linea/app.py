#calculo de coordenadas de lineas
def calcular_y(x,m,b):
    '''
    Calcula el valor de y en una linea recta
    x: el valor de x
    m: pendiente
    b: intersección en y
    regresa el valor de y:
    '''
    return (m*x) + b

def main():
    m = 2
    b = 3
    X = [x for x in range(1,11)]
    Y = [funciones.calcular_y(x, m, b) fo x in X]
    print ("Enteros:")
    coordenadas:enteros = list(zip(X, Y))
    print(coordenadas_enteros)

if _name_ == '_main_':
    main()