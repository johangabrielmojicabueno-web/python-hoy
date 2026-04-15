import tkinter as Ventana

class Formulario:

    def __init__(self):

        self.color = "rojo"

        self.entry_nombre = ""
        self.entry_apellido = ""
        self.entry_edad = ""
        self.entry_correo = ""
        self.entry_telefono = ""

        self.label_resultado = ""
        self.formulario = ""

        self.datos = []  

    def iniciar_ventana(self):

        self.formulario = Ventana.Tk()

        self.formulario.title("Registro de usuario")
        self.formulario.geometry("800x400")
        self.formulario.resizable(False, True)
        self.formulario.config(bg="red", cursor="hand2")

        return self.formulario

    def iniciar_preguntas(self):

    
        Ventana.Label(self.formulario, text="Nombre:").pack()
        self.entry_nombre = Ventana.Entry(self.formulario)
        self.entry_nombre.pack()

       
        Ventana.Label(self.formulario, text="Apellido:").pack()
        self.entry_apellido = Ventana.Entry(self.formulario)
        self.entry_apellido.pack()

        
        Ventana.Label(self.formulario, text="Edad:").pack()
        self.entry_edad = Ventana.Entry(self.formulario)
        self.entry_edad.pack()

        
        Ventana.Label(self.formulario, text="Correo:").pack()
        self.entry_correo = Ventana.Entry(self.formulario)
        self.entry_correo.pack()

        
        Ventana.Label(self.formulario, text="Teléfono:").pack()
        self.entry_telefono = Ventana.Entry(self.formulario)
        self.entry_telefono.pack()

        
        self.label_resultado = Ventana.Label(self.formulario, text="")
        self.label_resultado.pack()

      
        boton_enviar = Ventana.Button(
            self.formulario,
            text="Registrar",
            command=self.funcion_general
        )
        boton_enviar.pack()

  
    def validar_campos(self):
        if (self.entry_nombre.get() == "" or
            self.entry_apellido.get() == "" or
            self.entry_edad.get() == "" or
            self.entry_correo.get() == "" or
            self.entry_telefono.get() == ""):

            return False
        return True

   
    def capturar_datos(self):
        datos_cliente = [
            self.entry_nombre.get(),
            self.entry_apellido.get(),
            self.entry_edad.get(),
            self.entry_correo.get(),
            self.entry_telefono.get()
        ]

        return datos_cliente


    def guardar_datos(self, datos):
        self.datos.append(datos)

   
    def funcion_general(self):

        if self.validar_campos():

            datos = self.capturar_datos()
            self.guardar_datos(datos)

            self.label_resultado.config(
                text="Registro exitoso",
                fg="green"
            )

            print("Datos almacenados:", self.datos)

        else:
            self.label_resultado.config(
                text="Hay campos vacíos",
                fg="white"
            )


if __name__ == "__main__":

    app = Formulario()

    ventana = app.iniciar_ventana()

    app.iniciar_preguntas()

    ventana.mainloop()
