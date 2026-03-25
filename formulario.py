import tkinter as Ventana

class Formulario:
    def __init__(self):
        self.color = "rojo"
        self.entry_nombre = ""
        self.label_resultado = ""
        self.formulario = ""

    def iniciar_ventana(self):
        self.formulario = Ventana.Tk()  # Widgets
        self.formulario.title("Registro de usuario")
        self.formulario.geometry("800x400")
        self.formulario.resizable(False, True)
        self.formulario.config(bg="red", cursor="hand2")
        return self.formulario

    def iniciar_preguntas(self):
        label_nombre = Ventana.Label(
            self.formulario,
            text="Digite el nombre del cliente: "
        )
        label_nombre.config(padx=10, borderwidth=2, fg="blue")
        label_nombre.pack()

        self.entry_nombre= Ventana.Entry(self.formulario)
        self.entry_nombre.pack()

        boton_enviar = Ventana.Button(self.formulario, text="")

# Ejecución del programa
if __name__ == "__main__":
    app = Formulario()
    ventana = app.iniciar_ventana()
    app.iniciar_preguntas()
    ventana.mainloop()