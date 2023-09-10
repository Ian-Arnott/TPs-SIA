# TP2 SIA - Algoritmos Genéticos

## Introducción

[Enunciado](docs/SIA-TP2-2023-2Q.pdf)

### Requisitos

- Python3
- pip3
- [pipenv](https://pypi.org/project/pipenv/)

### Instalación

En la carpeta _Tp2_, ejecutar.

```sh
pipenv install
```

para instalar las dependencias necesarias en el ambiente virtual.

## Ejecución

Para ejecutar el mismo se deberá correr el siguiente script desde la carpeta _Tp2_ del proyecto: 
```python
pipenv shell
python ./main.py 
```

Debido a la gran cantidad de parámetros posibles para el programa, se optó por incluir un archivo de configuración _config.json_ en lugar de enviar los parámetros por línea de comandos.

## Configuración
El archivo de configuración _config.json_ incluye 22 parámetros personalizables. A continuación se detalla cada uno de ellos:

### Parámetros de Población
- _**N**_: Determina la cantidad total de individuos que tendrá cada generación, incluida la inicial.
- _**K**_: Determina la cantidad de nuevos individuos (hijos) que se generarán en cada iteración. Los mismos, se generan tomando _K_ individuos de los _N_ padres de la generación anterior 

### Parámetros de Selección
- _**M**_: En el caso de haber elegido el método de selección por Torneo Determinístico, este parámetro indica entre cuántos de los _N_ individuos de la población se disputará cada "torneo". Es decir, se toman _M_ de los _N_ individuos y se elije al mejor de estos _M_, repitiendo el torneo la cantidad de veces necesaria para obtener _K_ individuos.
- _**threshold**_: Determina el valor del _Threshold_ a utilizar en el caso de haber elegido el método de selección por Torneo Probabilístico.



<!-- ,
    "threshold": 0.7,
    "character_type": "archer",
    "selection_method_1": "universal",
    "selection_method_2": "universal", 
    "selection_method_3": "universal", 
    "selection_method_4": "universal",  
    "crossing_method": "one_point",
    "mutation_method": "uniform_multigen",
    "new_generation_method": "new_over_actual",
    "gene": "height",
    "A": 0.5,
    "B": 0.5,
    "p_m": 0.1,
    "Tc": 0.1,
    "T0": 10,
    "k": 2,
    "max_generations": 150,
    "max_generations_without_change": 10,
    "delta": 0.01 -->