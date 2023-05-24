import estacion1


def main():

    # Preguntar al usuario cuántas prendas desea fabricar
    prendas = int(input("Ingrese la cantidad de prendas que desea fabricar: "))

    # Variable para contar la cantidad de prendas
    contador_prendas = 0

    # Bucle para ejecutar el programa el número de prendas especificado
    while contador_prendas < prendas:
        # Incrementar el contador de prendas
        contador_prendas += 1

        # Comenzar ejecución
        estacion1.main()

    # Mostrar la cantidad de prendas que se realizaron durante la ejecución del programa
    print(f"Prendas fabricadas: {contador_prendas}.")


if __name__ == '__main__':
    main()
