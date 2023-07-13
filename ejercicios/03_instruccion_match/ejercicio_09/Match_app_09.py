import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Una agencia de viajes cobra $15.000 por cada estadía como base. 
Luego para calcular las tarifas total realiza el siguiente cálculo, 
en función de la estación del año y del destino elegido:
    Si es invierno: 
        Bariloche tiene un aumento del 20% 
        Cataratas y Córdoba tienen un descuento del 10%
        Mar del plata tiene un descuento del 20%
    Si es Verano:
        Bariloche tiene un descuento del 20%
        Cataratas y Cordoba tienen un aumento del 10%
        Mar del plata tiene un aumento del 20%
    Si es Primavera u Otoño:
        Bariloche tiene un aumento del 10%
        Cataratas tiene un aumento del 10%
        Mar del plata tiene un aumento del 10%
        Córdoba tiene precio sin descuento

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_estaciones = customtkinter.CTkLabel(master=self, text="Estaciones")
        self.label_estaciones.grid(row=0, column=0, padx=20, pady=10)
        estaciones = ['Verano', 'Otoño', 'Invierno', 'Primavera']
        self.combobox_estaciones = customtkinter.CTkComboBox(master=self, values=estaciones)
        self.combobox_estaciones.grid(row=1, column=0, padx=20, pady=(10, 10))

        
        self.label_destinos = customtkinter.CTkLabel(master=self, text="Destinos")
        self.label_destinos.grid(row=2, column=0, padx=20, pady=10)
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Cordoba']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=3, column=0, padx=20, pady=(10, 10))
    
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
        
    def btn_informar_on_click(self):
        estacion = self.combobox_estaciones.get()
        destino = self.combobox_destino.get()
        estadia = 15000
# Logica utilizable en diferentes lenguajes de programacion:
        match estacion:
            case "Invierno":
                match destino:
                    case "Bariloche":
                        mensaje = estadia * 1.2
                    case "Cataratas"|"Cordoba":
                        mensaje = estadia * 1.1
                    case _:
                        mensaje = estadia * .80
            case "Verano":
                match destino:
                    case "Bariloche":
                        mensaje = estadia * 0.8
                    case "Cordoba"|"Cataratas":
                        mensaje = estadia * 1.1
                    case "Mar del plata":
                        mensaje = estadia * 1.2
            case "Otoño"|"Primevera":
                match destino:
                    case "Bariloche"|"Cataratas"|"Mar del plata":
                        mensaje = estadia * 1.1
                    case "Cordoba":
                        mensaje = estadia                
        alert(title="UTN FRA",message=mensaje)
        
'''  No sirve para otros lenguajes, si para Python.
        match(estacion, destino):
            case ('Invierno', 'Bariloche'):
                 mensaje = estadia * 1.2
            case ('Invierno', 'Cataratas' | 'Córdoba'):
                mensaje = estadia * 0.9
            case ('Invierno', 'Mar del plata'):
                mensaje = estadia * 0.8
            case ('Verano', 'Bariloche'):
                mensaje = estadia * 0.8
            case ('Verano', 'Cataratas' | 'Córdoba'):
                mensaje = estadia * 1.1
            case ('Verano', 'Mar del plata'):
                mensaje = estadia * 1.2
            case ('Primavera' | 'Otoño', 'Bariloche' | 'Cataratas' | 'Mar del plata'):
                mensaje = estadia * 1.1
            case ('Primavera' | 'Otoño', 'Córdoba'):
                mensaje = estadia
                    
        alert(title="UTN FRA",message=f'El precio final es: {mensaje}')   
'''
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()