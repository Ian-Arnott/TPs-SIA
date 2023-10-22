# TP4 SIA - Aprendizaje No Supervisado

## Introducción

Implementación de diferentes programas en Python en donde podemos ver en funcionamiento: 
- El modelo de Kohonen utilizado comunmente para agrupar datos de alta dimensión.
- El modelo de Hopfield utlizado para recuperar patrones de memoria.
- La regla de Oja utilizada para reducir la dimensionalidad de los datos, extrayendo componentes principales o caracteristicas relevantes de los mismos


### Requisitos

- Python3
- pip3
- [pipenv](https://pypi.org/project/pipenv/)

### Instalación

En la carpeta _Tp4_, ejecutar.

```sh
pipenv install
```

para instalar las dependencias necesarias en el ambiente virtual.

## Ejecución

Cada modelo consta de una carpeta propia, dentro de la misma se encuentra su respectivo `main.py`.
Para ejecutar el mismo se deberá correr el siguiente script desde la carpeta del ejercicio  del proyecto: 
```python
pipenv shell
python ./main.py 
```

Debido a la gran cantidad de parámetros posibles para el programa, se optó por incluir un archivo de configuración _config.json_ en lugar de enviar los parámetros por línea de comandos.

## Configuración

Cada modelo tiene su propio archivo de configuración en su respectiva carpeta.

### Parámetros del Modelo de Kohonen
- **k** _[Número entero]_:
    - Cantidad de neuronas en la capa de salida.
- **learning_rate** _[Decimal entre 0 y 1]_: 
    - Tasa de aprendizaje del perceptron.
- **radius** _[Decimal entre 0 y 1]_: 
    - Radio de la vecindario.
- **max_epochs** _[Número entero]_: 
    - Cantidad máxima de épocas por las que iterará el algoritmo.
- **likeness_type** _[EUCLIDEAN | EXPONENTIAL]_: 
    - Tipo de similitud a utilizar.

### Parámetros de la Regla de Oja
- **learning_rate** _[Decimal entre 0 y 1]_: 
    - Tasa de aprendizaje del perceptron.
- **max_epochs** _[Número entero]_: 
    - Cantidad máxima de épocas por las que iterará el algoritmo.

 
