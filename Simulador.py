import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parámetros de la simulación
num_nodos = 20000
duracion_simulacion = 1000

# Inicializar la matriz de transferencia de archivos
transferencia_archivos = np.zeros((num_nodos, duracion_simulacion))

# Función para actualizar la gráfica en cada cuadro de la animación
def update(frame):
    plt.clf()  # Limpiar el gráfico anterior
    for nodo_id in range(num_nodos):
        for tiempo in range(frame + 1):
            transferencia_archivos[nodo_id, tiempo] = np.random.choice([0, 10], p=[0.8, 0.2])
    plt.imshow(transferencia_archivos, cmap='binary', aspect='auto', interpolation='none')
    plt.xlabel('Tiempo')
    plt.ylabel('Nodo')
    plt.title('Simulador')
    plt.colorbar(label='Estado de Transmisión (0: No, 1: Sí)')

# Crear la animación
ani = FuncAnimation(plt.gcf(), update, frames=duracion_simulacion, interval=200)

# Mostrar la animación
plt.show()