# TP2 SIA - Algoritmos Genéticos

## Introducción

Implementación de un programa en Python con un motor de algoritmos genéticos para encontrar la mejor configuración de personajes para un juego de rol.

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
- **N** _[Número entero]_:
    - Determina la cantidad total de individuos que tendrá cada generación, incluida la inicial.
- **K** _[Número entero]_: 
    - Determina la cantidad de nuevos individuos (hijos) que se generarán en cada iteración. Los mismos, se generan tomando _K_ individuos de los _N_ padres de la generación anterior
-  **character_type** _[ warrior | archer | defender | infiltrator ]_: 
    - Determina la clase del personaje a utilizar para el algortimo. Se intentará obtener un personaje de este tipo con _performance_ máxima

### Parámetros de Selección
- **selection\_method\_1** _[ elite | roulette | universal | boltzmann | deterministic_tournament | probabilistic_tournament | ranking ]_: 
     - Determina el método de selección a utilizar para la primera parte de los _K_ individuos a generarl, según el parámetro _A_.
- **selection\_method\_2** _[ elite | roulette | universal | boltzmann | deterministic_tournament | probabilistic_tournament | ranking ]_: 
     - Determina el método de selección a utilizar para la segunda parte de los _K_ individuos a generarl, según el parámetro _A_.
- **selection\_method\_3** _[ elite | roulette | universal | boltzmann | deterministic_tournament | probabilistic_tournament | ranking ]_: 
     - Determina el método de selección a utilizar para la obtener la primera parte de los _N_ individuos a seleccionar del conjunto de padres e hijos previo al Reemplazo, según el parámetro _B_.
- **selection\_method\_4** _[ elite | roulette | universal | boltzmann | deterministic_tournament | probabilistic_tournament | ranking ]_: 
     - Determina el método de selección a utilizar para la obtener la segunda parte de los _N_ individuos a seleccionar del conjunto de padres e hijos previo al Reemplazo, según el parámetro _B_.
- **A** _[Decimal entre 0 y 1]_: 
    - Determina la proporción de los _K_ individuos a generar que se obtendrán mediante el método de selección _selection\_method\_1_ y el resto mediante el método _selection\_method\_2_.
- **B** _[Decimal entre 0 y 1]_:
    - Determina la proporción de los _N_ individuos a seleccionar del conjunto de padres e hijos previo al Reemplazo que se obtendrán mediante el método de selección _selection\_method\_3_ y el resto mediante el método _selection\_method\_4_.
- **M** _[Número entero]_: 
    - En el caso de haber elegido el método de selección por Torneo Determinístico, este parámetro indica entre cuántos de los _N_ individuos de la población se disputará cada "torneo". Es decir, se toman _M_ de los _N_ individuos y se elije al mejor de estos _M_, repitiendo el torneo la cantidad de veces necesaria para obtener _K_ individuos.
- **threshold** _[Decimal entre 0.5 y 1]_: 
    - Determina el valor del _Threshold_ a utilizar en el caso de haber elegido el método de selección por Torneo Probabilístico.
- **T0** _[Decimal entre 0 y 1]_: 
    - Determina el valor de la temperatura inicial a utilizar en el caso de haber elegido el método de selección Boltzmann.

### Parámetros de Cruza
- **crossing\_method** _[ one_point | double_point | uniform | anular ]_: 
    - Determina el método de cruza a utilizar para generar los _K_ individuos hijos.

### Parámetros de Mutación
- **mutation\_method** _[ gene_mutation | uniform_multigen | complete_mutation | limited_multigen ]_: 
    - Determina el método de mutación a aplicar a los _K_ individuos hijos.
- **p_m** _[Decimal entre 0 y 1]_:
    - Determina la probabilidad de que la mutación se aplique para a cada individuo.
- **gene** _[ height | items ]_: 
    - Determina el gen o grupo de genes a mutar, en el caso de haber elegido el método de mutación _gene\_mutation_.

### Parámetros de Reemplazo
- **new\_generation\_method** _[ use_all | new_over_actual ]_: 
    - Determina el método de reemplazo a utilizar para obtener los _N_ individuos de la siguiente generación.

### Parámetros de Criterios de Corte
- **max\_generations** _[Número entero]_: 
    - Determina la cantidad máxima de generaciones que se ejecutarán antes de detener el algoritmo.
- **max\_generations\_without\_change** _[Número entero]_:
    - Determina la cantidad máxima de generaciones que se ejecutarán sin que se produzca un cambio generacional antes de detener el algoritmo.
- **delta** _[Decimal entre 0 y 1]_: 
    - Determina el valor máximo de diferencia para considerar que dos valores son distintos.

### Parámetros el Método de Selección de Bolztmann
- **Tc** _[Decimal]_: 
    - Temperatura crítica.
- **T0** _[Número entero]_:
    - Temperatura inicial.
- **k** _[Número entero]_: 
    - Constante de decaimiento.