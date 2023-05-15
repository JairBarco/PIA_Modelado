import random
import time

def main():
    # Definición de variables
    tiempos_reales = [2, 2, 2, 2, 5] # Tiempos reales de las operaciones
    tiempos_aleatorios = [10, 5, 7, 9, 8] # Tiempos aleatorios de las operaciones
    operacion_actual = 0 # Variable que indica la operación que se está realizando
    operaciones_correctas = False # Variable que indica si todas las operaciones fueron correctas
    DISENO_ESPALDA = "Diseño Espalda"
    LARGO_TALLE = "Largo Talle"
    CONTORNO_BUSTO = "Contorno Busto"
    DISENO_FINAL = "Diseño Final"
    operaciones = [DISENO_ESPALDA, LARGO_TALLE, CONTORNO_BUSTO, DISENO_FINAL]
    estaciones = ["Estación 1", "Estación 2", "Estación 3", "Estación 4", "Estación 5", "Estación 6"]
    estacion_actual = 0

    # Variables para almacenar el tiempo transcurrido en cada operación y el tiempo total
    tiempos_operacion = [0] * len(operaciones)
    tiempo_total = 0

    # Función para realizar una operación

    print(f"{estaciones[estacion_actual]}")

    def realizar_operacion(tiempo):
        inicio = time.perf_counter()  # Tiempo inicial
        print(f"Realizando operación {operaciones[operacion_actual]}...")
        time.sleep(tiempo)
        fin = time.perf_counter()  # Tiempo final
        tiempo_transcurrido = fin - inicio  # Tiempo transcurrido
        tiempos_operacion[operacion_actual] = tiempo_transcurrido  # Almacenar el tiempo transcurrido en la variable correspondiente
        print(f"Operación {operaciones[operacion_actual]} finalizada. Tiempo: {tiempo_transcurrido:.2f}s")

    # Función para validar si las operaciones fueron correctas
    def validar_operaciones():
        # Realizar validación de las operaciones realizadas
        # En este caso, simplemente se devuelve un valor aleatorio entre 0 y 1
        # para simular si las operaciones fueron correctas o no
        resultado_validacion = random.randint(0, 1)

        # Devolver True si las operaciones fueron correctas, False si no lo fueron
        if resultado_validacion == 1:
            print(f"Validación exitosa")
        else:
            print(f"Validación no exitosa")
        return resultado_validacion == 1

    # Función para avanzar a la siguiente estación
    def avanzar_a_siguiente_estacion():
        global estacion_actual
        estacion_actual += 1
        if estacion_actual == len(estaciones):
            estacion_actual = 0
        print(f"Avanzando a la siguiente estación: {estaciones[estacion_actual]}")

    # Bucle de simulación
    while not operaciones_correctas:
        # Realizar operación actual con su tiempo correspondiente
        tiempo_operacion = random.uniform(tiempos_aleatorios[operacion_actual], tiempos_reales[operacion_actual])
        realizar_operacion(tiempo_operacion)

        # Verificar si la operación actual es la última
        if operacion_actual == len(operaciones) - 1:
            # Validar operaciones
            operaciones_correctas = validar_operaciones()

            # Si las operaciones fueron correctas, avanzar a la siguiente estación
            if operaciones_correctas:
                avanzar_a_siguiente_estacion()
            # Si las operaciones fueron incorrectas, volver a la operación inicial
            else:
                operacion_actual = 0
        # Si no es la última operación, avanzar a la siguiente
        else:
            operacion_actual += 1

if __name__ == '__main__':
    main()