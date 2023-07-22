import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        contador_femenino = 0
        acumulador_edad_fem = 0
        contador_masculino = 0 
        flag_primer_votante_gianni = False
        contador_votos_giovanni = 0
        contador_votos_gianni = 0
        contador_votos_facu = 0
        for i in range(100):
            #ingreso de nombre:
            nombre = prompt("Votacion","Ingrese su nombre: ")
            for i in range(0,100,1):
                #inicio de los pasos: 
                if nombre != "" and nombre != None:
                    break
                nombre = prompt("ERROR","Reingrese su nombre")
                
            # ingreso de edad:
            for i in range(0,100,1):
                edad = prompt("Votacion","Ingre su edad, usted debe ser mayor a 13 años")
                edad = int(edad)
                if edad > 13:
                    break    
                
            #ingreso de genero:
            for i in range(0,100,1):
                genero = prompt("UTN FRA","Ingrese su genero: ")
                if genero == "Masculino" or genero == "Femenino" or genero == "Otro":
                    break
        
            #ingreso de votacion:
            for i in range(0,100,1):
                nominado = prompt("Votacion","Ingrese a quien desea votar: (Giovanni,Gianni o Facundo)")
                if nominado == "Giovanni" or nominado == "Gianni" or nominado == "Facundo":
                    break
            
            match genero:
                case "Femenino":
                    contador_femenino = contador_femenino + 1
                    acumulador_edad_fem = acumulador_edad_fem + edad
                    
                case "Masculino":
                    if (edad >= 25 or edad <= 40) and (nominado == "Facundo" or nominado =="Giovanni"):
                        contador_masculino = contador_masculino + 1
                case _:
                    pass
            match nominado:
                case "Giovanni":
                    contador_votos_giovanni += 1
                case "Gianni":
                    contador_votos_gianni += 1
                case _:
                    contador_votos_facu += 1
                    
            if nominado == "Gianni":
                if flag_primer_votante_gianni == False or edad > edad_votante_gianni_joven:
                    edad_votante_gianni_joven = edad
                    edad_votante_gianni_joven = nombre
                    flag_primer_votante_gianni = True
            
            respuesta = question("Nominados","Desea continuar?")
            if respuesta == False:
                break
        
        ## A)
        if contador_femenino > 0: 
            promedio = 0
        else:
            promedio = acumulador_edad_fem / contador_femenino  
        alert("PROMEDIO",f"El promedio de edad femenino es: {promedio}")
        ## B)
        alert("UTN FRA",f"Hubieron {contador_masculino} hombres que votaron a Facundo o Giovanni")
        
        ## C)
        if flag_primer_votante_gianni !=False:
            mensaje_c = f"El nombre del votante mas joven de Gianni es : {edad_votante_gianni_joven}"
        else:
            mensaje_c = "Nadie voto por Gianni"
        alert("UTN FRA",mensaje_c)
        
        ## D)
        
        contador_votos_total = contador_votos_gianni + contador_votos_facu + contador_votos_giovanni
        porcentaje_giovanni = (contador_votos_gianni * 100) / contador_votos_total
        porcentaje_facu = (contador_votos_facu * 100) / contador_votos_total
        porcentaje_gianni = (contador_votos_facu *100) / contador_votos_total
        mensaje_d = f'Hubieron {contador_votos_total}votos, el {porcentaje_giovanni}% voto por Giovanni, el {porcentaje_gianni}% voto por Gianni, y el {porcentaje_facu}% voto por Facundo'
        alert("UTN FRA",mensaje_d)
        
        ## E)
        
        if contador_votos_gianni > contador_votos_giovanni and contador_votos_gianni > contador_votos_facu:
            nombre_participante_eliminado = "Gianni"
        elif contador_votos_giovanni > contador_votos_facu:
            nombre_participante_eliminado = "Giovanni"
        else:
            nombre_participante_eliminado = "Facu"
        mensaje_e = f"El participante eliminado es... {nombre_participante_eliminado}"
        alert("Uteniano", mensaje_e)
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()