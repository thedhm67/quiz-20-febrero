class Nodo:
    def __int__(self, cedula, nombre, habitación, orden):
        self.cedula = cedula
        self.nombre=nombre
        self.habitación=habitación
        self.orden=orden
        self.siguiente=None

class listaSE:
    def __init__(self, total_habitaciones):
        self.cabeza=None
        self.entradas=None
        self.salidas=None
        self.total_habitaciones=total_habitaciones
        self.habitaciones_ocupadas = set()
        self.contador_llegadas = 0

def registrar_entrada(self, cedula, nombre, habitación):
    if habitación in self.habitaciones_ocupadas:
        print("Habitación ocupada")
        return

    self.contador_llegadas+=1

    nuevo=Nodo(cedula,nombre,habitación, self.contador_llegadas)

    nuevo.siguiente=self.cabeza
    self.cabeza=nuevo

    nuevo_entrada=Nodo(cedula, nombre, nuevo_entrada.siguiente)
    nuevo_entrada.siguiente=self.entradas
    self.entradas=nuevo_entrada

    self.habitaciones_ocupadas.add(habitación)
    print("Entrada registrada")

def registar_salidas(self, cedula):
    actual=self.cabeza
    anterior=None

def _eliminar(nodo, cedula, self):
    if nodo is None:
        print("huesped no encontrado")
        return None
    
    if nodo.cedula==cedula:
        self.habitaciones_ocupadas.remove(nodo.habitación)

    nuevo_salida=Nodo(nodo,cedula,nodo.nombre,nodo.habitacion,nodo.orden)
    nuevo_salida.siguiente=self.salidas

    print("salida registrada")
    return nodo.siguiente


def consultar_por_cedula(self, cedula):
    actual = self.cabeza
    if nodo is None:
        nodo=self.cabeza
    
    if nodo is None:
        print("no encontrado")
        return
    
