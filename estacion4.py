import random
import time
import estacion1
import numpy as np
from scipy.stats import norm, kstest

import estacion5


def main():
    # Definición de variables
    estacion_actual = 3
    datos_referencia = [0.50, 0.32, 0.63, 0.45, 0.45, 0.45, 0.32, 0.32, 0.45, 0.32, 0.20, 0.45, 0.20, 0.20, 0.32]
    variables_aleatorias = []
    variable_aleatoria = 0
    operacion_actual = 0  # Variable que indica la operación que se está realizando
    operaciones_correctas = False  # Variable que indica si todas las operaciones fueron correctas
    MONTAJE_FALSO_BOLSA = "Montaje de falso de bolsa"
    FALSO_BOLSA = "Falso de bolsa"
    SOBRECOSTURA_BOLSA = "Sobrecostura de bolsa"
    COSTURA_BOLSA_1_4 = "Costura de bolsa a 1/4'"
    SOBRECOSTURA_FALSO_BOLSA = "Sobrecostura de falso de bolsa"
    UNION_FALSOS_BOLSA = "Unión de falsos de bolsa"
    LIMPIEZA_BOLSA = "Limpieza de bolsa"
    UNION_COSTADO = "Unión de costado"
    UNION_ENTREPIERNA = "Unión de entrepierna"
    UNION_TIRO_CIRCULAR = "Unión de tiro circular"
    LIMPIEZA_RUEDO = "Limpieza de ruedo"
    COSTURA_RUEDO = "Costura de ruedo"
    AFIANZAR_ELASTICO = "Afianzar elástico"
    PRETINADO = "Pretinado"
    PEGADO_PRETINA = "Pegado de pretina"
    operaciones = [MONTAJE_FALSO_BOLSA, FALSO_BOLSA, SOBRECOSTURA_BOLSA, COSTURA_BOLSA_1_4, SOBRECOSTURA_FALSO_BOLSA,
                   UNION_FALSOS_BOLSA, LIMPIEZA_BOLSA, UNION_COSTADO, UNION_ENTREPIERNA, UNION_TIRO_CIRCULAR,
                   LIMPIEZA_RUEDO, COSTURA_RUEDO, AFIANZAR_ELASTICO, PRETINADO, PEGADO_PRETINA]

    estaciones = ["Estación 1", "Estación 2", "Estación 3", "Estación 4", "Estación 5", "Estación 6"]

    # Variables para almacenar el tiempo transcurrido en cada operación y el tiempo total
    tiempos_operacion = [0] * len(operaciones)
    tiempos_estaciones = [0] * len(estaciones)
    tiempo_total = 0

    def generar_variables_aleatorias():
        # Generar variables aleatorias solo si la lista está vacía
        if not variables_aleatorias:
            # Generación de variables aleatorias
            media = np.mean(datos_referencia)
            desviacion_estandar = np.std(datos_referencia)

            # Verificar si los datos son enteros o con decimales
            if all(isinstance(dato, int) for dato in datos_referencia):
                generar_enteros = True
            else:
                generar_enteros = False

            # Generar variables aleatorias
            for _ in range(len(datos_referencia)):
                variable_aleatoria = 0  # Inicializar la variable aleatoria con cero
                while variable_aleatoria == 0:  # Repetir hasta obtener un valor diferente de cero
                    if generar_enteros:
                        variable_aleatoria = abs(int(np.random.normal(media, desviacion_estandar))/1000)
                    else:
                        variable_aleatoria = abs(np.round(np.random.normal(media, desviacion_estandar), 2)/1000)
                variables_aleatorias.append(variable_aleatoria)

            # Identificar la distribución de las variables aleatorias
            _, p_valor = kstest(datos_referencia, norm(media, desviacion_estandar).cdf)

    if operacion_actual == 14:
        operacion_actual = 0

    # Función para realizar una operación
    def realizar_operacion(tiempo):
        inicio = time.perf_counter()  # Tiempo inicial
        time.sleep(tiempo)
        fin = time.perf_counter()  # Tiempo final
        tiempo_transcurrido = fin - inicio  # Tiempo transcurrido
        tiempos_operacion[operacion_actual] = tiempo_transcurrido  # Almacenar el tiempo transcurrido en la variable
        # correspondiente
        tiempos_estaciones[estacion_actual] += tiempo_transcurrido  # Acumular el tiempo en la estación actual

    # Función para validar si las operaciones fueron correctas
    def validar_operaciones():
        resultado_validacion = random.choices([True, False], weights=[1.00, 0.00])[0]

        # Imprimir el mensaje de validación correspondiente
        if resultado_validacion:
            resultado_validacion = True
        else:
            reiniciar_flujo_simulacion()

        return resultado_validacion

    def reiniciar_flujo_simulacion():
        global operacion_actual, tiempo_total, estacion_actual, operaciones_correctas, variables_aleatorias, variable_aleatoria
        operacion_actual = 0
        tiempo_total = 0
        operaciones_correctas = False
        variables_aleatorias = []
        variable_aleatoria = 0
        estacion_actual = 0
        print("Reiniciando el flujo de la simulación...")
        estacion1.main()

    # Función para avanzar a la siguiente estación
    def avanzar_a_siguiente_estacion():
        global estacion_actual  # Indicar que estacion_actual y operacion_actual se modificarán en el ámbito superior
        estacion_actual = 3
        estacion_actual += 1
        if estacion_actual == len(estaciones):
            estacion_actual = 3
        estacion5.main()

    if not operaciones_correctas:
        generar_variables_aleatorias()

    # Bucle de simulación
    while True:
        while not operaciones_correctas:
            # Realizar operación actual con su tiempo correspondiente
            tiempo_operacion = random.uniform(variables_aleatorias[operacion_actual], variables_aleatorias[operacion_actual])
            realizar_operacion(tiempo_operacion)

            # Si no es la última operación, avanzar a la siguiente
            if operacion_actual < len(operaciones) - 1:
                operacion_actual += 1
            else:
                # Si la operación actual es la última, pero no todas las operaciones son correctas,
                # regresar a la primera operación
                if not validar_operaciones():
                    operacion_actual = 0

            # Verificar si todas las operaciones han sido completadas
            if all(tiempos_operacion):  # Verificar si todos los tiempos de operación tienen un valor distinto de cero
                operaciones_correctas = True
                tiempo_total = sum(tiempos_estaciones[:4])
                tiempo_total *= 1000
                print(f"Tiempo total de la estación 4: {(tiempo_total/60):.2f} minutos")
                avanzar_a_siguiente_estacion()

        # Si la operación actual es la última y todas las operaciones fueron completadas,
        # romper el bucle y finalizar la simulación
        if operacion_actual == len(operaciones) - 1 and operaciones_correctas:

            break


if __name__ == '__main__':
    main()
