# validar sodoku
El siguiente repositorio explica como validar si el sodoku tiene números repetidos en sus filas columnas y secciones 

Un sodoku tiene 81 casillas, estas casillas se agrupan en 9 casillas, formando asi un cuadrado de 9 divisiones.

![image](https://user-images.githubusercontent.com/45399791/230791848-18637098-8f32-447d-81e5-d80eacb3ad5e.png)

La idea principal que debemos seguir para solucionar un sodoku es que; no se deben repetir numeros en sus filas y en sus columnas, ademas las divisiones deben tener los numeros de 1 al 9 sin repetir.

A continuacion la explicacion del codigo que valida dicha idea.

Primero vamos hacer una función que toma una lista de longitud 9, y filtra los numeros mayores a cero, el cero no lo deja pasar, dejando una lista en donde es necesario saber si tiene numeros duplicados. 

    def has_duplicate(block) :
        block = list(filter(lambda x: x != 0, block))
        return len(block) != len(set(block))
