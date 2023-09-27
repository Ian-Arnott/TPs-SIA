# TP3 SIA - Redes neuronales

## Introducción

Implementación de diferentes programas en Python en donde podemos ver en funcionamiento perceptrones simples (lineales y no lineales) y multicapa. En el caso de los perceptrones simples, se intenta aprender los problemas lógicos AND y XOR, y en el caso de los perceptrones multicapa, se intenta aprender los problemas lógicos XOR y paridad, y clasificar dígitos.


### Requisitos

- Python3
- pip3
- [pipenv](https://pypi.org/project/pipenv/)

### Instalación

En la carpeta _Tp3_, ejecutar.

```sh
pipenv install
```

para instalar las dependencias necesarias en el ambiente virtual.

## Ejecución

Cada ejercicio consta de una carpeta propia, dentro de la misma se encuentra su respectivo `main.py`.
Para ejecutar el mismo se deberá correr el siguiente script desde la carpeta del ejercicio  del proyecto: 
```python
pipenv shell
python ./main.py 
```

Debido a la gran cantidad de parámetros posibles para el programa, se optó por incluir un archivo de configuración _config.json_ en lugar de enviar los parámetros por línea de comandos.

## Configuración

Cada ejercicio tiene su propio archivo de configuración en su respectiva carpeta.

### Parámetros del Ejercicio 1
- **operation** _[AND | XOR]_:
    - Operacion a realizar.
- **learning_rate** _[Decimal entre 0 y 1]_: 
    - Tasa de aprendizaje del perceptron.
- **max_epochs** _[Número entero]_: 
    - Cantidad máxima de épocas por las que iterará el algoritmo.
- **bias** _[Número real]_: 
    - Umbral o bias del perceptron.

### Parámetros del Ejercicio 2
- **perceptron_type** _[LINEAR | HIPERBOLIC | LOGISTIC]_:
    - Tipo de perceptron a utilizar.
- **learning_rate** _[Decimal entre 0 y 1]_: 
    - Tasa de aprendizaje del perceptron.
- **training_percentage** _[Decimal entre 0 y 1]_: 
    - Porcentaje de los datos a utilizar para entrenar.
- **max_epochs** _[Número entero]_: 
    - Cantidad máxima de épocas por las que iterará el algoritmo.
- **bias** _[Número real]_: 
    - Umbral o bias del perceptron.
- **beta** _[Número real]_:
    - Valor de beta para el perceptron no lineal.
- **epsilon** _[Número real]_:
    - Valor que representa el error mínimo aceptable.

### Parámetros del Ejercicio 3
- **ej** _[1 | 2 | 3]_:
    - Ejercicio a ejecutar.
        - 1: XOR
        - 2: Paridad
        - 3: Dígitos
- **learning_rate** _[Decimal entre 0 y 1]_: 
    - Tasa de aprendizaje del perceptron.
- **training_percentage** _[Decimal entre 0 y 1]_: 
    - Porcentaje de los datos a utilizar para entrenar.
- **max_epochs** _[Número entero]_: 
    - Cantidad máxima de épocas por las que iterará el algoritmo.
- **bias** _[Número real]_: 
    - Umbral o bias del perceptron.
- **beta** _[Número real]_:
    - Valor de beta para el perceptron no lineal.
- **epsilon** _[Número real]_:
    - Valor que representa el error mínimo aceptable.
- **optimizer** _[ADAM | GRADIENT\_DESCENT]_:
    - Optimizador a utilizar.

 
