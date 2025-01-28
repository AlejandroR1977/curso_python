#calculo de coordenadas de lineas
def calcular_y(x:float,m:float,b:float)->float:
    '''
    Calcula el valor de y en una linea recta
    x: el valor de x
    m: pendiente
    b: intersección en y  
    regresa el valor de y:
    '''
    return (m*x) + b

def main():
    #m = 2
    #b = 3
    #X = [x for x in range(1,11)]
    #Y = [funciones.calcular_y(x, m, b) fo x in X]
    #print ("Enteros:")
    #coordenadas:enteros = list(zip(X, Y))
    print(coordenadas_enteros)
    XF = [x for x in range(1,11,0.5)]
    XY = [funciones.calcular_y(x, m, b) for x in XF]
    coordenadas_flotantes = list(zip(XF,XY))
    print("Flotantes")
    print(coordenadas_flotantes)


if _name_ == '_main_':
    parser = argparse.ArgumentPerser()
    parser.add_argument('-m', type=float,
    helps='Pendiente de la linea', default=2.0)
    parser.add_argument('-b', type=float,
    helps='Ordenada al origen', default=3.0)
    args = parser.parse_args()
    main(args.m, args.b)