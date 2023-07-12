import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón Mostrar tomar del campo de texto cantidad de repetir que se desea
repetir el mensaje "Hola UTN FRA" (utilizando el Dialog Alert)
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="MENSAJE")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_repetir = customtkinter.CTkEntry(master=self)
        self.txt_repetir.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        repetir = self.txt_repetir.get()  
        if repetir.isdigit():  
            repetir = int(repetir)
            for i in range(repetir):
                alert("UTN FRA", "Hola UTN FRA")
        else:
            alert("Error", "El numero ingresado es incorrecto, intente nuevamente")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()