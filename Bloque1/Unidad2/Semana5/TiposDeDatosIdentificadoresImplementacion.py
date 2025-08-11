class Lote:
    def __init__(self, largo: float, ancho: float, ubicacion: str):
        self.largo = largo
        self.ancho = ancho
        self.ubicacion = ubicacion

    def calcular_area(self) -> float:
        return self.largo * self.ancho

    def descripcion(self) -> str:
        area = self.calcular_area()
        return f"Ubicación: {self.ubicacion.title()}, Área del lote: {area} m²"


# Programa
print("Calculadora de área de lotes")
print("Ubicaciones disponibles: Quito, Guayaquil, Cuenca\n")

# Entrada de datos
ubicacion_usuario = input("Ingrese la ubicación del lote: ").lower()
largo_usuario = float(input("Ingrese el largo del lote en metros: "))
ancho_usuario = float(input("Ingrese el ancho del lote en metros: "))

lote_usuario = Lote(largo=largo_usuario, ancho=ancho_usuario, ubicacion=ubicacion_usuario)

print("\nResultado:")
print(lote_usuario.descripcion())
