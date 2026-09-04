class Vehiculo:
    def __init__(self, patente, marca, modelo, año, precio):
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    def mostrarInfo(self):
        print(f"Patente: {self.patente} - Marca: {self.marca} - Modelo: {self.modelo} - Año: {self.año} - Precio: {self.precio}")

    def calcularAñosUso(self, año_actual,año_fabricacion):
        self.calcularAñosUso = año_actual - año_fabricacion
        return f"los años de usos son {self.calcularAñosUso}"