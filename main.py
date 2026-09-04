from auto import Auto
from motocicleta import Motocicleta
from vendedor import Vendedor
from automotora import Automotora


def main():

    # Crear automotora
    automotora_uno = Automotora("Locos por los fierros")

    # Crear 2 automóviles
    Mazda3 = Auto("2USADA","Mazda","Mazda 3",2017,10000000,4,95)
    Miata = Auto("ASDSA","Mazda","Miata",1993,1500000,2,93)

    # Crear motocicleta
    hayabusa = Motocicleta("ADSAD2","YAMAHA","hayabusa",2000,8000000,1000,"deportiva")
    cb190r = Motocicleta("E23DAS","HONDA","cb190r",2026,3000000,190,"ciudad")

    # Agregar vehículos a la automotora 
    automotora_uno.agregarVehiculo(Mazda3)
    automotora_uno.agregarVehiculo(hayabusa)

    # Mostrar vehículos
    print("===== VEHÍCULOS DE LA AUTOMOTORA =====")
    print(automotora_uno.mostrarVehiculos())


    # Probar métodos de un Auto
    print("\n===== AUTO =====")
    print(Mazda3.abrirMaletero())
    print(Mazda3.tieneAireAcondicionado())

    # Calcular años de uso del auto
    print(Mazda3.calcularAñosUso(2026,2017))

    # Probar métodos de Motocicleta
    print("\n===== MOTOCICLETA =====")
    print(hayabusa.esDeAltaCilindrada())
    print(cb190r.esDeAltaCilindrada())
    print(hayabusa.encenderMotor())

    # Calcular años de uso de la motocicleta
    print(hayabusa.calcularAñosUso(2026,2000))

    # Crear vendedor
    vendedor1 = Vendedor(
         "Juan Pérez",
         "12.345.678-9",
         "987654321"
     )

    print("\n===== VENDEDOR =====")
    print(vendedor1.mostrar_datos())
    print(vendedor1.calcular_comision(5000000))
    print(vendedor1.calcular_comision(3000000))

    

if __name__ == "__main__":
    main()