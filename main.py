import tkinter as tk
import estacion1
import time
import sys


def main():
    def iniciar_proceso():
        nonlocal contadorTotal, contador_prendas

        # Reiniciar contadores
        contadorTotal = 0
        contador_prendas = 0

        # Vaciar la consola
        limpiar_consola()

        # Obtener la cantidad de prendas del campo de entrada
        prendas = int(entry_cantidad.get())

        # Desactivar el botón de inicio
        btn_iniciar.config(state=tk.DISABLED)

        # Bucle para ejecutar el programa el número de prendas especificado
        while contador_prendas < prendas:
            inicio = time.perf_counter()
            # Incrementar el contador de prendas
            contador_prendas += 1

            # Redirigir la salida estándar a la interfaz de usuario
            text_output.config(state=tk.NORMAL)
            text_output.insert(tk.END, f"Prenda {contador_prendas}:\n")
            text_output.update_idletasks()  # Actualizar la interfaz

            # Redirigir la salida estándar a la interfaz de usuario
            redirect_output(text_output)

            # Comenzar ejecución
            estacion1.main()

            # Detener la redirección de la salida estándar
            restore_output()

            final = (time.perf_counter() - inicio)
            final *= 1000
            contadorTotal += final / 60


        # Mostrar la cantidad de prendas que se realizaron durante la ejecución del programa
        lbl_prendas_var.set(f"Prendas fabricadas: {contador_prendas}.")
        window.update_idletasks()  # Actualizar la interfaz

        # Calcular y mostrar el tiempo total
        mostrar_tiempo_total()

        # Reactivar el botón de inicio
        btn_iniciar.config(state=tk.NORMAL)

    def mostrar_tiempo_total():
        if contadorTotal >= 60:
            horas = contadorTotal // 60  # División entera para obtener las horas
            minutos = contadorTotal % 60  # Obtener el residuo para los minutos
            segundos = (minutos % 1) * 100
            tiempo_total = f"Tiempo total de la fabricación de todas las prendas: {horas:.0f} hora/s {minutos:.0f} minutos {segundos:.0f} segundos."
        else:
            segundos = (contadorTotal % 1) * 100
            tiempo_total = f"Tiempo total de la fabricación de todas las prendas: {contadorTotal:.0f} minutos {segundos:.0f} segundos."
        lbl_tiempo_total_var.set(tiempo_total)

    def redirect_output(text_widget):
        # Redirigir la salida estándar a un widget de texto
        sys.stdout = StdoutRedirector(text_widget)

    def restore_output():
        # Restaurar la salida estándar original
        sys.stdout = sys.__stdout__

    def limpiar_consola():
        # Vaciar el contenido del campo de texto
        text_output.config(state=tk.NORMAL)
        text_output.delete(1.0, tk.END)
        text_output.config(state=tk.DISABLED)

    class StdoutRedirector:
        def __init__(self, text_widget):
            self.text_widget = text_widget

        def write(self, text):
            self.text_widget.insert(tk.END, text)
            self.text_widget.see(tk.END)

        def flush(self):
            pass

    # Crear la ventana principal
    window = tk.Tk()
    window.title("Fabricación de Prendas")

    # Obtener el ancho y alto de la ventana
    window_width = 900
    window_height = 600

    # Obtener el ancho y alto de la pantalla
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calcular la posición x, y para centrar la ventana
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    # Establecer la geometría de la ventana
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Variables para el contador de prendas y el tiempo total
    contador_prendas = 0
    contadorTotal = 0

    # Etiqueta y campo de entrada para la cantidad de prendas
    lbl_cantidad = tk.Label(window, text="Cantidad de prendas:")
    lbl_cantidad.pack()
    entry_cantidad = tk.Entry(window)
    entry_cantidad.pack()

    # Botón de inicio
    btn_iniciar = tk.Button(window, text="Iniciar", command=iniciar_proceso)
    btn_iniciar.pack()

    # Etiqueta para mostrar la cantidad de prendas fabricadas
    lbl_prendas_var = tk.StringVar()
    lbl_prendas_var.set("Prendas fabricadas: 0")
    lbl_prendas = tk.Label(window, textvariable=lbl_prendas_var)
    lbl_prendas.pack()

    # Etiqueta para mostrar el tiempo total de la fabricación
    lbl_tiempo_total_var = tk.StringVar()
    lbl_tiempo_total_var.set("Tiempo total de la fabricación de todas las prendas: 0 minutos")
    lbl_tiempo_total = tk.Label(window, textvariable=lbl_tiempo_total_var)
    lbl_tiempo_total.pack()

    # Campo de texto para mostrar la salida del programa
    text_output = tk.Text(window, state=tk.DISABLED)
    text_output.pack(fill=tk.BOTH, expand=True)

    # Barras de desplazamiento para el campo de texto
    scroll_y = tk.Scrollbar(text_output)
    scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
    scroll_y.config(command=text_output.yview)
    text_output.config(yscrollcommand=scroll_y.set)

    # Centrar la ventana en la pantalla
    window.update_idletasks()

    # Ejecutar la interfaz de usuario
    window.mainloop()


if __name__ == "__main__":
    main()
