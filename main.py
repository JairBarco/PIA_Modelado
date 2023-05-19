import estacion1


def main():

    # Preguntar al usuario cuántas veces desea ejecutar el programa
    prendas = int(input("Ingrese la cantidad de prendas que desea fabricar: "))

    # Variable para contar la cantidad de ejecuciones
    contador_prendas = 0

    # Bucle para ejecutar el programa el número de veces especificado
    while contador_prendas < prendas:
        # Incrementar el contador de ejecuciones
        contador_prendas += 1

        # Comenzar ejecución
        estacion1.main()

    # Mostrar la cantidad de veces que se ejecutó el programa
    print(f"Prendas fabricadas: {contador_prendas}.")


if __name__ == '__main__':
    main()
