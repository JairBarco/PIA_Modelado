import random
import time
import estacion2
import numpy as np
from scipy.stats import norm, kstest


def main():
    # Definición de variables
    estacion_actual = 0
    #datos_referencia = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    datos_referencia = [60, 12, 12, 12, 12, 12, 12, 12, 25, 20, 60, 12, 12, 20, 25]
    variables_aleatorias = []
    variable_aleatoria = 0
    operacion_actual = 0  # Variable que indica la operación que se está realizando
    operaciones_correctas = False  # Variable que indica si todas las operaciones fueron correctas
    DISENO_ESPALDA = "Diseño Espalda"
    LARGO_TALLE = "Largo Talle"
    CONTORNO_BUSTO = "Contorno Busto"
    CONTORNO_CINTURA = "Contorno Cintura"
    CONTORNO_CADERA = "Contorno Cadera"
    ALTURA_CADERA = "Altura Cadera"
    LARGO_MANGAS = "Largo Mangas"
    LARGO_TOTAL_CAMISA = "Largo Toral Camisa"
    COLECCIONES = "Colecciones"
    CREACION_COLOR = "Creacion Color"
    CREACION_TELA = "Creacion Tela"
    TIPOS_TELAS = "Tipos Telas"
    COLORES = "Colores"
    CONSULTA_DISENO = "Consulta Diseño"
    DISENO_FINAL = "Diseño Final"
    operaciones = [DISENO_ESPALDA, LARGO_TALLE, CONTORNO_BUSTO, CONTORNO_CINTURA, CONTORNO_CADERA, ALTURA_CADERA,
                   LARGO_MANGAS, LARGO_TOTAL_CAMISA, COLECCIONES, CREACION_COLOR, CREACION_TELA, TIPOS_TELAS, COLORES,
                   CONSULTA_DISENO, DISENO_FINAL]
    estaciones = ["Estación 1", "Estación 2", "Estación 3", "Estación 4", "Estación 5", "Estación 6"]
    inicio = time.perf_counter()

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
                        variable_aleatoria = abs(int(np.random.normal(media, desviacion_estandar)))
                    else:
                        variable_aleatoria = abs(np.round(np.random.normal(media, desviacion_estandar), 2))
                variables_aleatorias.append(variable_aleatoria)

            # Identificar la distribución de las variables aleatorias
            _, p_valor = kstest(datos_referencia, norm(media, desviacion_estandar).cdf)

            # Imprimir resultados generador de variables
            print("Variables Aleatorias Generadas:", variables_aleatorias)

            print(f"{estaciones[estacion_actual]}")

    def realizar_operacion(tiempo):
        inicio = time.perf_counter()  # Tiempo inicial
        time.sleep(tiempo)
        fin = time.perf_counter()  # Tiempo final
        tiempo_transcurrido = fin - inicio  # Tiempo transcurrido
        tiempos_operacion[operacion_actual] = tiempo_transcurrido  # Almacenar el tiempo transcurrido en la variable
        # correspondiente
        tiempos_estaciones[estacion_actual] += tiempo_transcurrido  # Acumular el tiempo en la estación actual
        #print(f"Operación {operaciones[operacion_actual]} finalizada en {tiempo_transcurrido:.2f}s")

    # Función para validar si las operaciones fueron correctas
    def validar_operaciones():
        global variables_aleatorias
        resultado_validacion = random.choices([True, False], weights=[1.00, 0.00])[0]

        # Imprimir el mensaje de validación correspondiente
        if resultado_validacion:
            print(f"Todas las operaciones han sido exitosas")
            resultado_validacion = True
        else:
            print(f"Operaciones no exitosas")
            variables_aleatorias = []
            resultado_validacion = False

        return resultado_validacion

    # Función para avanzar a la siguiente estación
    def avanzar_a_siguiente_estacion():
        global estacion_actual, operacion_actual  # Indicar que estacion_actual y operacion_actual se modificarán en el ámbito superior
        estacion_actual = 0
        estacion_actual += 1
        operacion_actual = 0
        if estacion_actual == len(estaciones):
            estacion_actual = 0
        print(f"Avanzando a la siguiente estación: {estaciones[estacion_actual]}")
        estacion2.main()

    generar_variables_aleatorias()

    # Bucle de simulación
    while True:
        operaciones_correctas = False  # Reiniciar la variable para cada iteración del bucle

        while not operaciones_correctas:
            # Realizar operación actual con su tiempo correspondiente
            tiempo_operacion = random.uniform(variables_aleatorias[operacion_actual], variables_aleatorias[operacion_actual])
            realizar_operacion(tiempo_operacion)

            # Si no es la última operación, avanzar a la siguiente
            if operacion_actual < len(operaciones) - 1:
                operacion_actual += 1
            else:
                # Si la operación actual es la última, pero no todas las operaciones son correctas, reiniciar el bucle interno
                if not validar_operaciones():
                    operacion_actual = 0  # Reiniciar la variable para cada iteración del bucle interno
                    variables_aleatorias = []
                    generar_variables_aleatorias()
                else:
                    operaciones_correctas = True

        operaciones_correctas = all(tiempos_operacion)
        if operaciones_correctas and operacion_actual == len(operaciones) - 1:
            tiempo_total = sum(tiempos_estaciones)
            print(f"Tiempo total de la estación {estaciones[estacion_actual]}: {(tiempo_total / 60):.2f} minutos")
            avanzar_a_siguiente_estacion()

        if operaciones_correctas and operacion_actual == len(operaciones) - 1:
            print("Todas las operaciones han sido completadas con éxito.")
            final = time.perf_counter() - inicio
            print(f"Tiempo total de ejecución: {(final / 60):.2f} minutos.")
        break


if __name__ == "__main__":
    main()
