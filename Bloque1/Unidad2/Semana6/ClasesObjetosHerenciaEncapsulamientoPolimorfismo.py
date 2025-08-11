# Clase base: DispositivoElectronico
class DispositivoElectronico:
    def __init__(self, marca, modelo):
        self.marca = marca  # atributo público
        self.__modelo = modelo  # atributo privado (encapsulación)

    # Metodo getter para modelo (encapsulación)
    def get_modelo(self):
        return self.__modelo

    # Metodo setter para modelo (encapsulación)
    def set_modelo(self, nuevo_modelo):
        self.__modelo = nuevo_modelo

    def encender(self):
        print(f"El dispositivo {self.marca} {self.__modelo} está encendiendo (mensaje genérico).")


# Clase derivada: Telefono, hereda de DispositivoElectronico
class Telefono(DispositivoElectronico):
    def __init__(self, marca, modelo, numero):
        super().__init__(marca, modelo)  # llamar al constructor de la clase base
        self.numero = numero  # atributo específico de Telefono

    # Metodo sobrescrito (polimorfismo)
    def encender(self):
        print(f"El teléfono {self.marca} {self.get_modelo()} con número {self.numero} está encendiendo.")


# Clase derivada: Computadora, hereda de DispositivoElectronico
class Computadora(DispositivoElectronico):
    def __init__(self, marca, modelo, sistema_operativo):
        super().__init__(marca, modelo)
        self.sistema_operativo = sistema_operativo

    # Metodo sobrescrito (polimorfismo)
    def encender(self):
        print(f"La computadora {self.marca} {self.get_modelo()} con {self.sistema_operativo} está encendiendo.")


# Función principal para probar las clases y demostrar POO
def main():
    # Crear instancia de DispositivoElectronico
    disp = DispositivoElectronico("GenericBrand", "X100")
    disp.encender()

    # Crear instancia de Telefono (clase derivada)
    mi_telefono = Telefono("Samsung", "Galaxy S21", "+123456789")
    mi_telefono.encender()

    # Crear instancia de Computadora (clase derivada)
    mi_computadora = Computadora("Dell", "Inspiron 15", "Windows 10")
    mi_computadora.encender()

    # Mostrar encapsulación: acceso controlado a atributo privado
    print(f"Modelo original de mi teléfono: {mi_telefono.get_modelo()}")
    mi_telefono.set_modelo("Galaxy S22")
    print(f"Modelo modificado de mi teléfono: {mi_telefono.get_modelo()}")


if __name__ == "__main__":
    main()
