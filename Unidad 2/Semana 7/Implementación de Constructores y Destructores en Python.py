class Archivo:
    # Constructor: se ejecuta al crear la instancia
    def __init__(self, nombre_archivo):
        self.nombre = nombre_archivo
        self.abierto = True
        print(f"Archivo '{self.nombre}' abierto.")

    # Metodo que simula escribir en el archivo
    def escribir(self, texto):
        if self.abierto:
            print(f"Escribiendo en '{self.nombre}': {texto}")
        else:
            print(f"No se puede escribir. El archivo '{self.nombre}' está cerrado.")

    # Destructor: se ejecuta cuando el objeto va a ser destruido
    def __del__(self):
        if self.abierto:
            self.abierto = False
            print(f"Archivo '{self.nombre}' cerrado automáticamente.")

# Crear una instancia de Archivo
mi_archivo = Archivo("notas.txt")

# Usar el metodo escribir
mi_archivo.escribir("Línea de ejemplo.")

# Eliminar el objeto manualmente para ver el destructor en acción
del mi_archivo