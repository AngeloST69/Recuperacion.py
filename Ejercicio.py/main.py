from persona import Persona
from celular import Celular
from celular import Info
from especificaciones import Especificaciones
from gama import Gama
from marca import Marca

if __name__ == "__main__":
    
    celular1        = Info(1, "Angelo", 20, "SamsungA53", 2021)
    celular2        = Info(2, "Bryan", 32, "Xiomi Note 7", 2019)
    
    
    celular3        = Celular(3, " Samanta", 24, "Shark 7")
    
    gama1           = Gama(32, "Media")
    gama2           = Gama(43, "Media alta")
    
    marca1          = Marca(23, "Samsung")
    marca2          = Marca(54, " Xiaomi")
    
    persona1        = Persona("32", "Angelo Lopez")
    persona2        = Persona("41", "Victor Hugo")
    
    especificaciones1 = Especificaciones("Snapdragon 765", "128gb", "6gb", celular1, gama1, marca1, persona1)
    especificaciones2 = Especificaciones("HelioG 96", "128gb", "8gb", celular2, gama2, marca2, persona2)
    
    
    #Clase con metodo
    
    print("CLASE CON METODO")
    print("ESPECIFICACIONES")
    print(vars(celular1))
    print(" ")
    print("CELULAR")
    print(vars(celular3))
    print(" ")
    print("GAMA")
    print(vars(gama1))
    print(" ")
    print("MARCA")
    print(vars(marca1))
    print(" ")
    print("PERSONA")
    print(vars(persona1))
    print(" ")
    
    #Metodo str
    
    print("METODO STR")  
    print(celular1)
    print(" ")
    print(celular2)
    
    #Objetos dentro de objetos
    
    print("OBJETOS DENTRO DE OBJETOS")
    print( vars( especificaciones1))
    print(" ")
    print(vars(especificaciones2))