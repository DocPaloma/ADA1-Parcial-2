# Swap Nodes [Algo]

## Descripción

Este programa resuelve el problema **Swap Nodes [Algo]** de HackerRank.

La solución representa el árbol binario mediante el arreglo `indexes` proporcionado por el problema, sin necesidad de crear una estructura de nodos adicional. Para cada consulta (`k`), el programa:

1. Intercambia los hijos izquierdo y derecho de todos los nodos cuya profundidad sea múltiplo de `k`.
2. Realiza un recorrido **inorder** del árbol.
3. Almacena el recorrido obtenido.

Finalmente, retorna un arreglo bidimensional con el resultado de cada consulta.

---

## Requisitos

- Python 3.x

No requiere instalar librerías externas.

---

## Ejecución

Desde una terminal, ubíquese en la carpeta donde se encuentra el archivo y ejecute:

```bash
python Solution.py
```

El programa espera los datos de entrada por la entrada estándar (`stdin`), siguiendo exactamente el formato solicitado por HackerRank.

Ejemplo:

```
3
2 3
-1 -1
-1 -1
2
1
1
```

La salida será impresa automáticamente siguiendo el formato requerido por la plataforma.

---

## Algoritmos utilizados

- Recorrido recursivo **Inorder**.
- Recorrido recursivo para realizar el intercambio de hijos.
- Manipulación directa de la representación del árbol mediante el arreglo `indexes`.

---

# Huffman Decoding

## Descripción

Este programa implementa la decodificación de un mensaje utilizando un árbol de Huffman.

El programa:

1. Calcula la frecuencia de cada carácter del texto ingresado.
2. Construye el árbol de Huffman utilizando una cola de prioridad.
3. Genera los códigos binarios correspondientes a cada carácter.
4. Codifica el mensaje.
5. Decodifica el mensaje recorriendo nuevamente el árbol de Huffman.

El resultado mostrado corresponde al mensaje original decodificado.

---

## Requisitos

- Python 3.x

No requiere instalar librerías externas.

---

## Ejecución

Desde una terminal, ubíquese en la carpeta donde se encuentra el archivo y ejecute:

```bash
python Solution.py
```

Ingrese una cadena de texto cuando el programa lo solicite.

Ejemplo:

```
ABRACADABRA
```

El programa construirá automáticamente el árbol de Huffman, realizará la codificación y finalmente imprimirá el mensaje decodificado.

---

## Algoritmos utilizados

- Árbol de Huffman.
- Cola de prioridad (`PriorityQueue`).
- Recorrido en profundidad (DFS) para generar los códigos binarios.
- Recorrido del árbol para realizar la decodificación.

---

## Autor

Alejandro Medina