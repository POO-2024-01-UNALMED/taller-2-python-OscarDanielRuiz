class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if(color == "rojo" or color == "verde" or color == "amarillo" or color == "negro" or color == "blanco"):
            self.color = color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if(tipo == "electrico" or tipo == "gasolina"):
            self.tipo = tipo
    
class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1
    
    def cantidadAsientos(self):
        cantidad = 0
        for i in range(0, len(self.asientos)):
            if (type(self.asientos[i]) == Asiento):
                cantidad += 1
        return cantidad
    
    def verificarIntegridad(self):
        original = False
        if (self.registro == self.motor.registro):
            original = True
            asientosvalidos = []
            for i in range(0, len(self.asientos)):
                if (type(self.asientos[i]) == Asiento):
                    asientosvalidos.append(i)
            for i in range(0, len(asientosvalidos)):
                if (self.registro != self.asientos[i]):
                    original = False
        if (original == True):
            return "Auto original"
        else:
            return "Las piezas no son originales"