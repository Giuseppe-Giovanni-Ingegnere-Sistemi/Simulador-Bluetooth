>[!IMPORTANT]
>ESTE NO ES UN SIMULADOR REAL Y FUNCIONAL, SOLO MUESTRA EN UN DIAGRAMA DE MATRICES COMO ES EL TRASPASO DE DATOS

# Simulador de Transferencia de Archivos

Este proyecto es una simulación visual de la transferencia de archivos entre nodos en una red, desarrollado como parte de un proyecto escolar. Utiliza Python y las bibliotecas matplotlib y numpy para visualizar cómo los archivos se transfieren entre nodos a lo largo del tiempo mediante una animación.

## Requisitos

Para ejecutar este proyecto, necesitas tener instaladas las siguientes bibliotecas de Python:

- numpy
- matplotlib

Puedes instalar las dependencias necesarias usando pip:

````bash
pip install numpy matplotlib
````
## Descripción del Código

- num_nodos: Define el número total de nodos en la red.
- duracion_simulacion: Especifica la duración total de la simulación en unidades de tiempo.

La matriz transferencia_archivos almacena los datos de transferencia para cada nodo a lo largo del tiempo.

La función update(frame) se encarga de actualizar la gráfica en cada cuadro de la animación. La gráfica muestra la transferencia de archivos como una imagen donde los valores se actualizan en función del tiempo.

## Ejecución del Código

Para ejecutar la simulación y ver la animación, simplemente ejecuta el script:

````bash
python nombre_del_script.py
````
Donde nombre_del_script.py es el nombre del archivo que contiene el código.

## Visualización
La animación muestra la transferencia de archivos entre nodos en la red a lo largo del tiempo. Los valores en la matriz se representan en una imagen binaria donde los nodos están en el eje vertical y el tiempo en el eje horizontal. El color blanco indica transferencia de archivos y el color negro indica ausencia de transferencia.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarnos a través de:

- Email: ing.josejuangallegos@gmail.com
- GitHub: Giuseppe-Giovanni-Ingegnere-Sistemi
