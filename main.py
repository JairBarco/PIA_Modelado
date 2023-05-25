import estacion1
import time


def main():
    contadorTotal = 0
    # Preguntar al usuario cuántas prendas desea fabricar
    prendas = int(input("Ingrese la cantidad de prendas que desea fabricar: "))

    # Variable para contar la cantidad de prendas
    contador_prendas = 0

    # Bucle para ejecutar el programa el número de prendas especificado
    while contador_prendas < prendas:
        inicio = time.perf_counter()
        # Incrementar el contador de prendas
        contador_prendas += 1

        # Comenzar ejecución
        estacion1.main()
        final = (time.perf_counter() - inicio)
        final *= 1000
        contadorTotal += final

    # Mostrar la cantidad de prendas que se realizaron durante la ejecución del programa
    print(f"Prendas fabricadas: {contador_prendas}.")
    print(f"Tiempo total de la fabricación de todas las prendas: {(contadorTotal / 60):.2f} minutos.")


if __name__ == '__main__':
    main()
