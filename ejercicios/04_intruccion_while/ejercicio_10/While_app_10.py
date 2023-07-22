import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        contador_numeros_positivos = 0
        contador_numeros_negativos = 0
        suma_numeros_positivos = 0
        suma_numeros_negativos = 0
        ceros = 0
      
        while True:
            numero = prompt("UTN FRA","Ingrese un numero: ")
            if numero == None:
                break
            numero = int(numero)
            if numero > 0:
                suma_numeros_positivos = suma_numeros_positivos + numero
                contador_numeros_positivos = contador_numeros_positivos + 1
            elif numero < 0:
                suma_numeros_negativos = suma_numeros_negativos - numero
                contador_numeros_negativos = contador_numeros_negativos + 1
            elif numero == 0:
                ceros = ceros + 1
        diferencia = suma_numeros_positivos - suma_numeros_negativos
        alert("UTN FRA",f'La suma de positivos es: {suma_numeros_positivos}\nLa suma de negativos es: {suma_numeros_negativos}\nLa cantidad de ceros es: {ceros}\nLa diferencia entre positivos y negativos es: {diferencia}')

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
