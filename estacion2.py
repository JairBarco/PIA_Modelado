import random
import time

import estacion1


def main():
    # Definición de variables
    estacion_actual = 1
    tiempos_reales = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]  # Tiempos reales de las operaciones
    tiempos_aleatorios = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]  # Tiempos aleatorios de las operaciones
    #tiempos_reales = [46, 53, 22, 22, 21, 40, 46, 46, 22, 53, 22, 53, 46, 40, 40]
    #tiempos_aleatorios = [39, 29, 47, 37, 38, 46, 37, 33, 25, 30, 33, 40, 40, 48, 36]
    operacion_actual = 0  # Variable que indica la operación que se está realizando
    operaciones_correctas = False  # Variable que indica si todas las operaciones fueron correctas
    ENVIO_REGISTRO = "Envio de orden y registro para telas y corte"
    ENVIO_MP = "Envio de MP a corte"
    TENDER = "Tender tela"
    PLANTILLA_CORTE = "Poner plantilla para corte"
    CORTAR_PLANTILLA = "Cortar plantilla"
    BLOQUES_CORTADOS = "Piezas y bloques cortados"
    ALINEACION_BLOQUE = "Alineación de bloque"
    FOLIAR = "Foliar piezas"
    PREPARAR_ENVIO = "Preparar para enviar"
    GUARDAR_MODELO = "Se guarda el modelo en bolsa"
    ALINEAR_EMPELLONADAS = "Llevar tela empellonada a alinear"
    ENVIO_ORDEN = "Envio de orden"
    INSPECCION_CORTE = "Inspección de corte"
    ASEGURAR_PLANTILLA = "Asegurar plantilla"
    operaciones = [ENVIO_REGISTRO, ENVIO_MP, TENDER, PLANTILLA_CORTE, CORTAR_PLANTILLA, BLOQUES_CORTADOS,
                   ALINEACION_BLOQUE, FOLIAR, PREPARAR_ENVIO, GUARDAR_MODELO, ALINEAR_EMPELLONADAS,
                   ENVIO_ORDEN, INSPECCION_CORTE, ASEGURAR_PLANTILLA]
    estaciones = ["Estación 1", "Estación 2", "Estación 3", "Estación 4", "Estación 5", "Estación 6"]

    # Variables para almacenar el tiempo transcurrido en cada operación y el tiempo total
    tiempos_operacion = [0] * len(operaciones)
    tiempos_estaciones = [0] * len(estaciones)
    tiempo_total = 0

    print(f"{estaciones[estacion_actual]}")

    if operacion_actual == 14:
        operacion_actual = 0

    # Función para realizar una operación
    def realizar_operacion(tiempo):
        inicio = time.perf_counter()  # Tiempo inicial
        print(f"Realizando operación {operaciones[operacion_actual]}...")
        time.sleep(tiempo)
        fin = time.perf_counter()  # Tiempo final
        tiempo_transcurrido = fin - inicio  # Tiempo transcurrido
        tiempos_operacion[operacion_actual] = tiempo_transcurrido  # Almacenar el tiempo transcurrido en la variable
        # correspondiente
        tiempos_estaciones[estacion_actual] += tiempo_transcurrido  # Acumular el tiempo en la estación actual
        print(f"Operación {operaciones[operacion_actual]} finalizada. Tiempo: {tiempo_transcurrido:.2f}s")

    # Función para validar si las operaciones fueron correctas
    def validar_operaciones():
        resultado_validacion = random.choices([True, False], weights=[1.00, 0.00])[0]

        # Imprimir el mensaje de validación correspondiente
        if resultado_validacion:
            print(f"Validación de {operaciones[operacion_actual]} exitosa")
        else:
            print(f"Validación de {operaciones[operacion_actual]} no exitosa")
            reiniciar_flujo_simulacion()

        return resultado_validacion

    def reiniciar_flujo_simulacion():
        global operacion_actual, tiempo_total, estacion_actual, operaciones_correctas
        operacion_actual = 0
        tiempo_total = 0
        operaciones_correctas = False
        estacion_actual = 1
        print("Reiniciando el flujo de la simulación...")
        estacion1.main()

    # Función para avanzar a la siguiente estación
    def avanzar_a_siguiente_estacion():
        global estacion_actual  # Indicar que estacion_actual y operacion_actual se modificarán en el ámbito superior
        estacion_actual = 1
        estacion_actual += 1
        if estacion_actual == len(estaciones):
            estacion_actual = 1
        print(f"Avanzando a la siguiente estación: {estaciones[estacion_actual]}")

    # Bucle de simulación
    while True:
        while not operaciones_correctas:
            # Realizar operación actual con su tiempo correspondiente
            tiempo_operacion = random.uniform(tiempos_aleatorios[operacion_actual], tiempos_reales[operacion_actual])
            realizar_operacion(tiempo_operacion)

            # Si no es la última operación, avanzar a la siguiente
            if operacion_actual < len(operaciones) - 1:
                operacion_actual += 1
            else:
                # Si la operación actual es la última, pero no todas las operaciones son correctas, regresar a la primera operación
                if not validar_operaciones():
                    operacion_actual = 0

            # Verificar si todas las operaciones han sido completadas
            if all(tiempos_operacion):  # Verificar si todos los tiempos de operación tienen un valor distinto de cero
                operaciones_correctas = True
                tiempo_total = sum(tiempos_estaciones[:2])
                print(f"Tiempo total de la estación 2: {tiempo_total:.2f}s")
                avanzar_a_siguiente_estacion()

        # Si la operación actual es la última y todas las operaciones fueron completadas, romper el bucle y finalizar la simulación
        if operacion_actual == len(operaciones) - 1 and operaciones_correctas:

            break


if __name__ == '__main__':
    main()
