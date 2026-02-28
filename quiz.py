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

        while actual:
            if actual.cedula == cedula:
                print("Cédula:", actual.cedula)
                print("Nombre:", actual.nombre)
                print("Habitación:", actual.habitacion)
                print("Orden llegada:", actual.orden)
                return
            actual = actual.siguiente

        print("No encontrado.")

 def listar_por_llegada(self):
        actual = self.cabeza
        lista = []

        while actual:
            lista.append(actual)
            actual = actual.siguiente

        lista.sort(key=lambda x: x.orden)

        for h in lista:
            print(h.cedula, h.nombre, h.habitacion, h.orden)  




 def habitaciones_disponibles(self):
        disponibles = []

        for i in range(1, self.total_habitaciones + 1):
            if i not in self.habitaciones_ocupadas:
                disponibles.append(i)

        print("Disponibles:", disponibles)


 def habitaciones_ocupadas_lista(self):
        print("Ocupadas:", list(self.habitaciones_ocupadas))



hotel = Hotel(5)

hotel.registrar_entrada("123", "Juan", 1)
hotel.registrar_entrada("456", "Ana", 2)

hotel.consultar_por_cedula("123")

hotel.listar_por_llegada()

hotel.habitaciones_disponibles()
hotel.habitaciones_ocupadas_lista()

hotel.registrar_salida("123")

hotel.habitaciones_disponibles()

