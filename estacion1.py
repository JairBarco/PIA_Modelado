import random
import time

def main():
    # Definición de variables
    estacion_actual = 0
    tiempos_reales = [6, 1, 1, 1, 1, 1, 1, 1, 2, 2, 6, 1, 1, 2, 2]  # Tiempos reales de las operaciones
    tiempos_aleatorios = [5, 5, 1, 5, 1, 2, 5, 2, 3, 3, 2, 1, 1, 5, 5]  # Tiempos aleatorios de las operaciones
    #tiempos_reales = [60, 12, 12, 12, 12, 12, 12, 12, 25, 20, 60, 12, 12, 20, 25]  # Tiempos reales de las operaciones
    #tiempos_aleatorios = [52, 56, 12, 59, 15, 22, 52, 20, 31, 33, 23, 12, 14, 15, 53]  # Tiempos aleatorios de las operaciones
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
    operaciones = [DISENO_ESPALDA, LARGO_TALLE, CONTORNO_BUSTO, CONTORNO_CINTURA, CONTORNO_CADERA, ALTURA_CADERA, LARGO_MANGAS, LARGO_TOTAL_CAMISA, COLECCIONES, CREACION_COLOR, CREACION_TELA, TIPOS_TELAS, COLORES, CONSULTA_DISENO, DISENO_FINAL]
    estaciones = ["Estación 1", "Estación 2", "Estación 3", "Estación 4", "Estación 5", "Estación 6"]
    prendas = [ {"diseno_espalda": "A", "largo_talle": 55, "contorno_busto": 115}]

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
        if operaciones[operacion_actual] == DISENO_ESPALDA:
            # Actualizar el diseño de espalda en todas las prendas
            for prenda in prendas:
                prenda["diseno_espalda"] = "A"
        elif operaciones[operacion_actual] == LARGO_TALLE:
            # Actualizar el largo de talle en todas las prendas
            for prenda in prendas:
                prenda["largo_talle"] = 55
        elif operaciones[operacion_actual] == CONTORNO_BUSTO:
            # Actualizar el contorno de busto en todas las prendas
            for prenda in prendas:
                prenda["contorno_busto"] = 115
    class validar_largo_talle:
        def __init__(self, prendas, valor_definido):
            self.prendas = prendas
            self.valor_definido = valor_definido

        def validar(self):
            for prenda in self.prendas:
                if prenda["largo_talle"] < self.valor_definido:
                    return False
            return True

    class validar_diseno_espalda:
        def __init__(self, prendas, diseno_referencia):
            self.prendas = prendas
            self.diseno_referencia = diseno_referencia

        def validar(self):
            for prenda in self.prendas:
                if prenda["diseno_espalda"] != self.diseno_referencia:
                    return False
            return True

    class validar_contorno_busto:
        def __init__(self, prendas, valor_definido):
            self.prendas = prendas
            self.valor_definido = valor_definido

        def validar(self):
            for prenda in self.prendas:
                if prenda["contorno_busto"] < self.valor_definido:
                    return False
            return True

    # Función para validar si las operaciones fueron correctas
    def validar_operaciones(prendas):
        resultado_validacion = False
        validador = None
        validadores = []

        # Validar cada operación según sus criterios de validación
        if operaciones[operacion_actual] == DISENO_FINAL:
            # Criterios de validación para la operación "Diseño Espalda"
            validador = validar_diseno_espalda(prendas, "A")
            print('Validacion 1')
        if operaciones[operacion_actual] == DISENO_FINAL:
            # Criterios de validación para la operación "Largo Talle"
            validador = validar_largo_talle(prendas, 55)
            print('Validacion 2')
        if operaciones[operacion_actual] == DISENO_FINAL:
            # Criterios de validación para la operación "Contorno Busto"
            validador = validar_contorno_busto(prendas, 115)
            print(prendas)
            print('Validacion 3')

            # Realizar todas las validaciones
        for validador in validadores:
            resultado_validacion = validador.validar()
            if not resultado_validacion:
                break

        # Llama al método validar() en el objeto validador y asigna el resultado a la variable resultado_validacion
        if validador is not None:
            # Llama al método validar() en el objeto validador y asigna el resultado a la variable resultado_validacion
            resultado_validacion = validador.validar()

            # Imprimir el mensaje de validación correspondiente
            if resultado_validacion:
                print(f"Validación de {operaciones[operacion_actual]} exitosa")
                resultado_validacion = True
            else:
                print(f"Validación de {operaciones[operacion_actual]} no exitosa")
                resultado_validacion = False

        return resultado_validacion
    # Función para avanzar a la siguiente estación
    def avanzar_a_siguiente_estacion():
        global estacion_actual # Indicar que estacion_actual se modificará en el ámbito superior
        estacion_actual = 0
        estacion_actual += 1
        if estacion_actual == len(estaciones):
            estacion_actual = 0
        print(f"Avanzando a la siguiente estación: {estaciones[estacion_actual]}")

    # Bucle de simulación
    while not operaciones_correctas:
        # Realizar operación actual con su tiempo correspondiente
        tiempo_operacion = random.uniform(tiempos_aleatorios[operacion_actual], tiempos_reales[operacion_actual])
        realizar_operacion(tiempo_operacion)

        # Si no es la última operación, avanzar a la siguiente
        if operacion_actual < len(operaciones) - 1:
            operacion_actual += 1

        # Verificar si todas las operaciones han sido completadas
        if operacion_actual == 14:
            #Validar operaciones
            operaciones_correctas = validar_operaciones(prendas)

            # Si las operaciones fueron correctas, avanzar a la siguiente estación
            if operaciones_correctas:
                avanzar_a_siguiente_estacion()

        # Si la operación actual es la última y todas las operaciones fueron completadas, romper el bucle y finalizar la simulación
        if operacion_actual == len(operaciones) - 1 and operaciones_correctas:
            break

if __name__ == '__main__':
    main()