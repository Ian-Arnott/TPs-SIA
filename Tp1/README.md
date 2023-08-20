# TP1 SIA - Métodos de Búsqueda

## Introducción

Implementación de un programa en Python para encontrar soluciones con diferentes métodos de búsqueda del juego [Sokoban](http://www.game-sokoban.com/index.php?mode=level&lid=200).

[Enunciado](docs/SIA-TP1-2023-2Q.pdf)

### Requisitos

- Python3
- pip3
- [pipenv](https://pypi.org/project/pipenv/)

### Instalación

En la carpeta del tp1 ejecutar.

```sh
pipenv install
```

para instalar las dependencias necesarias en el ambiente virtual.

## Ejecución

Para ejecutar el mismo se deberá correr el siguiente script desde la carpeta raíz del proyecto: 
```python
pipenv shell
python ./main.py -l level4.txt -m astar -h manhattan
```

Significado de cada uno de los parámetros: 
| Parámetro |  Descripción | Valores soportados |
|----       | ------------------ | ------------------ |
| -l             | Indica el nivel a resolver. | level[1-5].txt|
| -m             | Indica el método de búsqueda que utilizará para resolver el tablero.  | bfs, dfs, astar, greedy|
| -H             | Indica la heurística que se utilizará (en caso de haber elegido un método de búsqueda informado).  | manhattan, combined|

Sin embargo, el programa también viene con una configuración por default donde el usuario puede correr simplemente:
```python
python ./main.py
```
De esta manera, se ejecutará el programa con el método de búsqueda A* y la heurística de Manhattan para el nivel 2 ([level2.txt](boards/level2.txt)).