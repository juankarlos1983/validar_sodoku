# validar sodoku
El siguiente repositorio explica como validar si el sodoku tiene números repetidos en sus filas columnas y secciones 

Un sodoku tiene 81 casillas, estas casillas se agrupan en 9 casillas, formando asi un cuadrado de 9 divisiones.

![image](https://user-images.githubusercontent.com/45399791/230791848-18637098-8f32-447d-81e5-d80eacb3ad5e.png)

La idea principal que debemos seguir para solucionar un sodoku es que; no se deben repetir numeros en sus filas y en sus columnas, ademas las divisiones deben tener los numeros de 1 al 9 sin repetir.

A continuacion la explicacion del codigo que valida dicha idea.

Primero declaramos una variable, este es el tablero completo o Sodoku

sodoku = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

![image](https://user-images.githubusercontent.com/45399791/230801751-4a7cb154-2f5e-48dd-a0d4-44b7a8f528e0.png)
"partial_assignment"

Ahora vamos hacer una función que toma una lista de longitud 9 (block), y filtra los numeros mayores a cero, el cero no lo deja pasar, dejando una lista en donde es necesario saber si tiene numeros duplicados (funcion set()). 

    def has_duplicate(block) :
        block = list(filter(lambda x: x != 0, block))
        return len(block) != len(set(block))

Esta funcion es la que nos permitira saber si existen duplicados, tanto en filas como en columnas, ademas si existen duplicados en cada una de las divisiones.

## Validar filas y columnas

Se muestra una funcion que toma primero una fila del Sodoku y valida si esta tiene numeros repetidos lo misma se hace con las columnas, se la funcion de arriba devuelve verdadero, entonces existen duplicados.


n = len(partial_assignment)
    if any( has_duplicate([partial_assignment[i][j] for j in range(n)]) --> Para validar las filas
            or has_duplicate([partial_assignment[j][i] for j in range(n)]) --> Para validar las columnas
            for i in range(n)):
        return False
Si en alguna fila o columna se devuelve True, entra a la condicion y retorna falso, indicando que el tablero no es valido.

## Validar cada una de las 9 divisiones del tablero

Tenemos el codigo 

    region_size = int(math.sqrt(n))
    return all(not has_duplicate([partial_assignment[a][b] 
                for a in range(region_size * I, region_size * (I + 1))
                for b in range(region_size * J, region_size * (J + 1))])          
                
                for I in range(region_size) for J in range(region_size))
![image](https://user-images.githubusercontent.com/45399791/230812549-9cca6a24-1da1-4c22-8c05-a4eb906a06db.png)
La imagen muestra la funcion de a y b, a recorre todas las filas y b las columnas.
por ultimo tenemos a I y J estas recorren el cuadro de tres en tres, para evaluar cada division.


## El problema de mirar y decir
Este problema solo usa numeros, comenzamos con un primer numero, puede ser el 1
la idea es mirar el numero y lego decir cuantos ve.

Por ejemplo comenzamos viendo el 1, entonces se dice, veo UN UNO: 11 --> esta seria la segunda cadena
La tercer cadena seria veo DOS UNOS: 21, luego seria veo UN DOS y UN UNO: 1211, y asi secesivamente. 

la idea es resolver esta secuencia con codigo python.
Debemos ver primero que al seguir esta secuencia lo que se hace es agrupar los numeros y decir el nombre del numero; por ejemplo 11 DOS UNOs.

Para esto usaremos la funcion GROUPBY del modulo ITERTOOLS, quedaria de la siguiente forma.

import itertools
s = '1'
for _ in range(8):
    s = "". join(str(len(list(group))) + key for key, group in itertools.groupby(s))

las variables key y group hacen lo siguiente, la variable key muestra el string.
La variable group muestra el strin s en forma de lista ['1']
La secuencia seria la siguiente: primero la variable s = '1' se muestra por medio de las demas variables asi; k = 1 group = ['1'] de manera que al sumar las variables "str(len(list(group))) + key", 11, al volver entraria asi k = 1 group = ['1','1'] y al volver a sumar 21.
