#Encontrar la solucion de un laberinto expresado en un matriz como la siguiente en donde S es el inicio y E el fin 
#Del laberinto, 0 el camino y 1 paredes que no permiten pasar por ahí, si ya se paso por el camino se marcara con 
# una X el valor minimo de la matriz es de 3 valores y un maximo indeterminado  
# [ 
#   ['S','0','1' ]
#   ['1','0','1' ]
#   ['1','0','E' ]
# ]

def matriz():
    print('Por favor introduce la matriz del laberinto como en el siguiente ejemplo:')
    print("['S', '0', '1'],")
    print("['1', '0', '1'],")
    print("['1', '0', 'E']")
    print('S: Representa el inicio del laberinto, E: El fin del laberinto, 1: Representa un muro, 0: Representa el camino por donde se puede pasar.')
    print("Introduce cada fila de la matriz (No es necesario agregar los corchetes ni las comas, pero si un espacio despues de cada dato), presiona Enter después de cada una, y escribe 'fin' cuando termines:")
    
    matriz = []
    while True:
        fila = input().upper().split()
        if fila[0].lower() == 'fin':
           break
        
        matriz.append(fila)
    
    return matriz

def laberinto(matriz_laberinto):
    """
        Funcion que obtinene como parametro la matriz ingresada por el usuario
    """

    def dfs(x, y):

        """
            Funcion que busca en profundidad la solucion al laberinto evaluando la matriz y devolviendo True si 
            ya se paso por alguno de los indices dentro de ella y poniendo X si ya se paso por el camino
        """
        #verificamos que no nos salgamos de los limites dentro de la matriz, asi como la posicion cuando sea 1 y si ya se visito el lugar de la matriz si alguna de estas condiciones se cumplen devuelve False 
        if x < 0 or x >= len(matriz_laberinto) or y < 0 or y >= len(matriz_laberinto[0]) or matriz_laberinto[x][y]== '1' or visitado[x][y]:

            return False
        
        visitado[x][y] = True
        if matriz_laberinto[x][y] == 'E':
            matriz_laberinto[x][y] = 'X'
            return True
        
        
        #Definimos las direcciones hacia donde se movera para poder verificar la solucion
        direcciones = [(0,1),(0,-1),(1,0),(-1,0)]

        for dx, dy in direcciones:
            if dfs(x + dx, y +dy):
                matriz_laberinto[x][y]= 'X'
                return True
            
                
        return False
    
    #Recorremos la matriz para buscar el inicio del laberinto 

    inicio_x = -1 
    inicio_y = -1

    for i in range(len(matriz_laberinto)):
        for j in range(len(matriz_laberinto[0])):
            if matriz_laberinto[i][j] == 'S':
                inicio_x, inicio_y = i, j
                break


    visitado = [[False] * len(matriz_laberinto[0]) for _ in range(len(matriz_laberinto))]
    if not dfs(inicio_x, inicio_y):
    
        return None
    return matriz_laberinto

# lab = [
    # ['S', '1', 'E'],
    # ['0', '1', '0'],
    # ['0', '0', '0']
# ]

lab= matriz()
laberints = laberinto(lab)
if lab:
    if laberints is not None:
        for fila in laberints:
            print(' ' ,fila)
    else:
        print('La matriz no tiene solución.')
else:
    print('No se ingreso ninguna matriz.')