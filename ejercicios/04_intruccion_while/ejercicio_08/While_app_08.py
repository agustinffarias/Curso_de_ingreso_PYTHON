import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera, 
hasta que presione el botón Cancelar (en el prompt) o el usuario ingrese cero. 
Calcular la suma acumulada de los positivos y multiplicar los negativos. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_producto

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_producto = customtkinter.CTkEntry(master=self, placeholder_text="Producto")
        self.txt_producto.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        contador = 0 
        numeros_acumulados = 0
        resultado_prompt = "si"
        negativos = 1
        
        while True: 
            numero =int(prompt("UTN FRA","Ingrese un numero: "))
            if numero == None or numero == 0:
                break
            numero = int(numero)
            if numero > 0:
                numeros_acumulados = numeros_acumulados + numero
            elif numero <0:
                negativos = negativos * numero
  
        # Ingresamos los datos a las cajitas:
        self.txt_suma_acumulada.delete(0,10000)
        self.txt_suma_acumulada.insert(0,numeros_acumulados)      
        self.txt_producto.delete(0,10000)
        self.txt_producto.insert(0,negativos)
            
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
