# 2022-S2-Examen-3


## Instrucciones Generales
- El archivo **debe** llamarse **Examen3.py**
- **Debe** respetar el nombre de las funciones y el nombre de los parámetros que más adelante se describen
- Deben contruir las funciones con **Python**
- Debe utilizar la programación **recursiva**, en algunas preguntas se especificará el tipo de **recursión**
- Debe crear los comentarios de cada función tomando en cuenta **Nombre**, **Entrada**, **Salida** y **Restricciones**
- Utilizar el IDLE propio de Python, prohibido utilizar otro editor de código
- Cada pregunta vale 6 puntos:
	- Los comentarios 1 punto (1 cometario bueno, 0.5 comentario incompleto, 0 no hay comentarios)
	- Algoritmo 5 puntos (5 Excelente, 4 a 1 Termiando con errores de sintaxis o incompleto , 0 No lo hizo)
  - En el caso de las matrices, programar las funciones de validación, se le permite por iteración


## esVectorOrdenado(vector, forma)

Escriba un programa con sintaxis Python cuya función principal se llame **esVectorOrdenado(vector, forma)**, que reciba como entradas un **vector** y una **forma**, este último será un string que especificará si el vector está ordenado en forma **ascendente o descendente**. Esta función retornará **True** si el vector corresponde al tipo o **False** del caso contrario

Los valores para **forma** son:  'asc' o 'desc'

```python
>>> esVectorOrdenado([23, 656, 5533, 8120], 'asc')
True
>>> esVectorOrdenado([15, 4, 0], 'desc')
True
>>> esVectorOrdenado([11, 45], 'desc')
False
```


##	Número abundante  
Escriba un programa con sintaxis Python cuya función principal se llame **numeroAbundante(num)**, que reciba como entrada un número entero positivo denominado **num** y que retorne si cumple (True) o no los requisitos (False) de número abundante. 
Un número abundante es un número natural y que la suma de sus divisores es mayor que su duplo, es decir:
-	El valor de **num** será 12 y sus divisores son (1,2,3,4,6 y 12)
-	La suma de ellos son 1+2+3+4+6+12 = 28
-	Entonces el 12 es un número abundante porque la suma de sus divisores 28 y es mayor que el duplo de 12, es decir 24. (28 > 12 x 2)

```python
>>>numeroAbundate(12)
True
>>> numeroAbundate (8)
False
>>> numeroAbundate (-8)
“Error: La entrada, debe ser número positivo”
```

##	Lista Duplex (25 puntos) 

Escriba un programa con sintaxis Python cuya función principal se llame **lista_Duplex(lista)**, que reciba como entrada una **lista** con número enteros positivos denominada **lista** y que retorne **True** si los ítems de la lista están ordenados, de manera tal que, el valor del ítem siguiente es al menos el doble de su ítem anterior (con excepción del primer ítem), considerando el recorrido de izquierda a derecha; **False** en caso de no estar ordenados de esa manera.

```python
>>>lista_Duplex([7, 20, 41, 82])
True
>>> lista_Duplex ([15, 29, 60])
False
>>> lista_Duplex ([])
“Error en la entrada”
```

## Centro Matriz

Escriba un programa con sintaxis Python cuya función principal se llame **centroMatriz**, debe validar que la matriz tenga la misma cantidad de columnas en todas sus filas. La finción centroMatriz recibe como parámetro una matriz y debe tener como mínimo 3 columnas y 4 filas.

- Si la matriz tiene columnas pares, las columnas a tomar en cuenta será el valor de la mitad y mitad + 1, ejemplo: una matriz con 6 columnas (0-5), los índices a tomar en cuenta son 2 y 3 
- Si la matriz tiene columnas impares, las columnas a tomar en cuenta será el valor desde la mitad - 1 y mitad + 1, ejemplo: una matriz con 5 columnas (0-4), los índices a tomar en cuenta son 1 hasta 3 
- Si la matriz tiene filas pares, las filas a tomar en cuenta será el valor de la mitad y mitad + 1, ejemplo: una matriz con 6 filas (0-5), los índices a tomar en cuenta son 2 y 3 
- Si la matriz tiene filas impares, las columnas a tomar en cuenta será el valor desde la mitad - 1 y mitad + 1, ejemplo: una matriz con 5 filas (0-4), los índices a tomar en cuenta son 1 hasta 3 

```python
m1 = [ [0,1,2,3,4,5], [6,7,8,9,10,11], [12,13,14,15,16,17], [18,19,20,21,21,23], [24,25,26,27,28,29]]
m2 = [ [0,1,2,3,4], [6,7,8,9,10], [12,13,14,15,16], [18,19,20,21,21]]
m2 = [ [0,1,2,3,4], [6,7,8], [12,13,14,15,16], [18,19,20,21,21]]

>>>centroMatriz(m1)
[[8,9], [14,15], [20,21]]

>>>centroMatriz(m2)
[[7,8,9], [13,14,15]]

>>>centroMatriz(m3)
"Error: No es una Matriz"

```
