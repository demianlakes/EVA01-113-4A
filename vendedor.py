class Vendedor:
    def __init__(self,nombre,rut,telefono):
        self.nombre = nombre
        self.rut = rut
        self.telefono = telefono
    def mostrar_datos(self):
        print(f"nombre: {self.nombre} - rut: {self.rut} - self.telefono : {self.telefono}")
        pass

    def calcular_comision(self,monto_venta):
        if monto_venta >= 5000000:
            print(f"el venddor ha ganado {monto_venta /100 * 10}")
        else:
            print((f"el vendedor ha ganado {monto_venta /100 * 5}"))