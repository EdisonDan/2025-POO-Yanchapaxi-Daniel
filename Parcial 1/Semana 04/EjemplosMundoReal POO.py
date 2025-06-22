# archivo: cine.py

class Pelicula:
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion

    def mostrar_info(self):
        print(f"Título: {self.titulo}, Duración: {self.duracion} minutos")

class Sala:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.ocupados = 0

    def reservar_asiento(self):
        if self.ocupados < self.capacidad:
            self.ocupados += 1
            print("Asiento reservado correctamente.")
        else:
            print("Lo sentimos, no hay asientos disponibles.")

    def mostrar_disponibilidad(self):
        disponibles = self.capacidad - self.ocupados
        print(f"Asientos disponibles: {disponibles}")

class Funcion:
    def __init__(self, pelicula, sala, hora):
        self.pelicula = pelicula
        self.sala = sala
        self.hora = hora

    def mostrar_funcion(self):
        print(f"Función de '{self.pelicula.titulo}' a las {self.hora} en sala {self.sala.numero}")
        self.sala.mostrar_disponibilidad()

# Código de prueba
if __name__ == "__main__":
    # Crear objetos
    pelicula1 = Pelicula("Spider-Man", 120)
    sala1 = Sala(1, 5)
    funcion1 = Funcion(pelicula1, sala1, "18:30")

    # Mostrar información
    funcion1.mostrar_funcion()
    sala1.reservar_asiento()
    sala1.reservar_asiento()
    funcion1.mostrar_funcion()