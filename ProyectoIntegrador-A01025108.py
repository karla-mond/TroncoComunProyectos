#Ana Paula Katsuda, A01025303
#Karla Mondragón, A01025108
#Syeni Perea, A01025129

#Importar librerías
import random
import copy

#Función para imprimir tablero
def tablero(lista):
    for a in lista: #filas
        for e in a: #columnas
            print(e, end = " ")
        print()
#Función para crear lista-tablero
def agregar(lista, lista1, lista2, num):
    #Primera fila: coordenadas de las columnas
    for i in range(num):
        #Convertir coordenadas a string
        lista1.append(str(i))
    #Agregar primera fila a lista
    lista.extend([lista1])
    #Agregar coordenada de fila
    for j in range(1):
        lista2.append(j)
        #Agregar "cartas"
        for k in range(num):
            lista2.append("_")
    #Agregar fila a lista
    for k in range(num):
        lista2 = lista2.copy()
        lista2[0] = k
        lista.extend([lista2])
    return lista

#Función para crear matriz
def crear_matriz(matriz, matriz1, num):
    a = num
    #Cantidad total de cartas en un tablero
    numero = int(num**2)
    #Agregar números a lista
    for i in range(1, numero+1):
        matriz.append(i)
    #Revolver números
    random.shuffle(matriz)
    #Crear matriz con números revueltos
    for j in range(0, numero, num):
        matriz1.append(matriz[j:a])
        a += num
    #vaciar matriz
    matriz.clear()
    #Agregar matriz con todos los números
    matriz.extend(matriz1)
    return matriz

#Función para destapar cartas en el tablero
def mostrar(fil1, col1, matriz, l1):
    l1[fil1+1][col1+1] = matriz[fil1][col1]
    
#Función que regresa el valor de la carta a _ si no es par válido   
def regresar(fil1, col1, matriz, l1):
    l1[fil1+1][col1+1] = '_'
    
#No aceptar valores menores a 0 o mayores a las coordenadas dadas
def rango(fil1, num):
    while (fil1<0 or fil1>num):
        fil1=int(input("Ingresa un número válido: "))
    return int(fil1)



#Tamaño de tableros en nivel inicial
num = int(input("Ingresa el tamaño de las filas y de las columnas de las matrices para comenzar (esta será la intensidad de tu nivel 1).\n RECOMENDACIÓN: inicia con valores pequeños pero no menores a 4): "))
#Marcar error si se ingresa un número menor o igual a 0
while (num<=0):
    num = int(input("Error, por favor ingrese un número válido: "))
#Instrucciones
print('Este es un juego de memoria en el que debes dar las coordenadas de la carta a destapar y el objetivo es encontar todos los pares')
inicio= input('Presiona A para empezar el juego: ')
print()
#Iniciar juego
while inicio == 'a' or inicio =='A':
    #Cantidad de pares
    p=0
    #Lista de pares
    par=[]
    #Cantidad de intentos
    cont=0
    #Inicializar listas
    lista = []
    lista1 = [" "]
    lista2 = []
    lista3 = []
    lista4 = [" "]
    lista5 = []
    matriz = []
    matriz1 = []
    matriz2 = []
    matriz3 = []
    #Primer tablero
    l1 = agregar(lista, lista1, lista2, num)
    #Segundo tablero
    l2 = agregar(lista3, lista4, lista5, num)
    #Imprimir primer tablero
    tablero(l1)
    print()
    #Imprimir segundo tablero
    tablero(l2)
    #Crear primera matriz
    m1 = crear_matriz(matriz, matriz1, num)
    print(m1)
    #Crear segunda matriz
    m2 = crear_matriz(matriz2, matriz3, num)
    print(m2)
    #Delimitar juego
    while (p < num**2):
        print()
        #Pedir coordenadas de la primera tabla y evaluar si están dentro del rango
        fil1 = int(input('Fila de primera carta a destapar: '))
        fil1 = rango(fil1, num)
        col1 = int(input('Columna de primera carta a destapar: '))
        col1 = rango(col1, num)
        #Destapar carta
        car1 = matriz[fil1][col1]
        mostrar(fil1, col1, m1, l1)
        tablero(l1)
        print()
        #Pedir coordenadas de la segunda tabla y evaluar si están dentro del rango
        fil2 = int(input('Fila de segunda carta a destapar: '))
        fil2 = rango(fil2, num)
        col2 = int(input('Columna de segunda carta a destapar: '))
        col2 = rango(col2, num)
        #Destapar carta
        car2 = matriz2[fil2][col2]
        car1 = matriz[fil1][col1]
        mostrar(fil2, col2, m2, l2)
        tablero(l2)
        print()
        #Comparar matrices (de tabla 1 y tabla 2)
        if (car1==car2):
            #Comprobar que la carta no haya sido destapada anteriormente
            if car1 not in par:
                print()
                print('¡Felicidades! Tienes un par')
                p+=1
                #Añadir carta a lista de pares
                par.append(car1)
                print("Los pares que tienes son: ", par)
                print()
                #Mostrar carta en el tablero
                mostrar(fil1, col1, m1, l1)
                #Imprimir tableros
                tablero(l1)
                print()
                mostrar(fil2, col2, m2, l2)
                tablero(l2)
                #print(m1)
                #print(m2)
            else:
                #Notificar al usuario que ya tenía el par
                print()
                print('Ya habías econtrado ese par, vuelve a intentar')
                print()
                tablero(l1)
                print()
                tablero(l2)
                print()
        else:
            #Notificar al usuario que no encontró un par
            print('¡Vuelve a intentar!')
            print()
            #Regresar guiones bajos a tablero
            if car1 not in par:
                regresar(fil1, col1, m1, l1)
                tablero(l1)
                print()
            else:
                tablero(l1)
            if car2 not in par:
                regresar(fil2, col2, m2, l2)
                tablero(l2)
                print()
            else:
                tablero(l2)
                print()
                     
        #Notificar número de intentos
        cont+=1
        print()
        print("Llevas",cont,"intentos")
    #Terminar juego cuando usuario encuentre todos los pares
    print("¡FELICIDADES, ganaste!")
    
    #Volver a jugar o salir del juego
    ini= input("Presiona 'A' para juagar el siguiente nivel o 'X' para salir del juego: ")
    #Continuar
    if ini =='a' or ini=='A':
        num = num + 1
        continue
    #Salir del juego
    elif ini =='x' or ini =='X':
        break