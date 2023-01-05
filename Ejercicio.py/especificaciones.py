from persona import Persona
from celular import Celular
from celular import Info
from marca import Marca
from gama import Gama

class Especificaciones:
    procesador      = str
    almacenamiento  = str
    RAM             = str
    celular         = Info("","","","","")
    persona         = Persona("","")
    marca           = Marca("","")
    gama            = Gama("","")
    
    
    #Herencia dentro de otro archivo
    
    def __init__(self, procesador, almacenamiento, RAM, celular, persona, marca, gama):
        self.procesador     = procesador
        self.almacenamiento = almacenamiento
        self.RAM            = RAM
        self.celular        = celular
        self.persona        = persona
        self.marca          = marca
        self.gama           = gama