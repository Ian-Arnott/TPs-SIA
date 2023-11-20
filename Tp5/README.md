# TP5 SIA - Deep Learning

## Introducción

Implementación de diferentes programas en Python en donde podemos ver en funcionamiento 3 tipos de autoencoders: 
- Lineal Autoencoder
- Denoising Autoencoder
- Variational Autoencoder


### Requisitos

- Python3
- pip3
- [pipenv](https://pypi.org/project/pipenv/)

### Instalación

En la carpeta _Tp5_, ejecutar.

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

Cada ejercicio tiene su propio archivo de configuración.

### Parámetros
- **learning_rate** _[Decimal entre 0 y 1]_: 
    - Tasa de aprendizaje del perceptron.
- **training_percentage** _[Decimal entre 0 y 1]_: 
    - Porcentaje de los datos a utilizar para entrenar.
- **max_epochs** _[Número entero]_: 
    - Cantidad máxima de épocas por las que iterará el algoritmo.
- **bias** _[Número real]_: 
    - Umbral o bias del perceptron.
- **beta** _[Número real]_:
    - Beta del perceptron.
- **beta1** _[Número real]_:
    - Numero real entre [0,1] usado en el metodo de optimizacion ADAM.
- **beta2** _[Número real]_:
    - Numero real entre [0,1] usado en el metodo de optimizacion ADAM.
- **epsilon** _[Número real]_:
    - Valor que representa el error mínimo aceptable.
- **optimizer** _[ADAM | GRADIENT\_DESCENT]_:
    - Optimizador a utilizar.
- **activation** _[TANH | SIGMOID]_:
    - Función de activación a utilizar.