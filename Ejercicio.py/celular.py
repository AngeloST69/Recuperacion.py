from persona import Persona

class Celular(Persona):
    id_c                = int
    nombre_c            = str
    
    def __init__(self, id_p, nombre, id_c, nombre_c):
        super().__init__(id_p, nombre)
        self.id_c       = id_c
        self.nombre_c   = nombre_c
    
    
#Herencia dentro del mismo archivo

class Info(Celular):
    fecha_salida = int
    
    def __init__(self, id_p, nombre, id_c, nombre_c, fecha_salida):
        super().__init__(id_p, nombre, id_c, nombre_c)
        self.fecha_salida = fecha_salida
        
    def __str__(self):
        return f'El celular: {self.nombre_c} con un id: {self.id_c} fue sacado en el: {self.fecha_salida}, le pertenece a: {self.nombre}, con id: {self.id_p} ' 
    
    

    