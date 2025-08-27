import os

# Clase Producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id
    def get_nombre(self):
        return self.nombre
    def get_cantidad(self):
        return self.cantidad
    def get_precio(self):
        return self.precio

    # Setters
    def set_id(self, id):
        self.id = id
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad
    def set_precio(self, precio):
        self.precio = precio

    @classmethod
    def from_dict(cls, data):
        return cls(data['id'], data['nombre'], int(data['cantidad']), float(data['precio']))

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"	


# Clase Inventario
class Inventario:
    def __init__(self):
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        self.archivo = os.path.join(directorio_actual, "inventario.txt")
        self.productos = dict()
        self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                for producto in self.productos.values():
                    f.write(f"ID={producto.id}=Nombre={producto.nombre}=Cantidad={producto.cantidad}=Precio={producto.precio}\n")
        except Exception as e:
            print(f"Error al guardar el inventario en archivo: {e}")
        return self.productos

    def cargar_desde_archivo(self):
        try:
            if not os.path.exists(self.archivo):
                open(self.archivo, "w").close()
                return
            with open(self.archivo, "r") as f:
                for linea in f:
                    partes = linea.strip().split("=")
                    if len(partes) == 8:  # ID=valor=Nombre=valor=Cantidad=valor=Precio=valor
                        id = partes[1]
                        nombre = partes[3]
                        cantidad = int(partes[5])
                        precio = float(partes[7])
                        self.productos[id] = Producto(id, nombre, cantidad, precio)
            print("Inventario cargado desde archivo.")
        except ValueError as e:
            print(f"Error al cargar el inventario desde archivo: {e}")
        except FileNotFoundError as e:
            print(f"Error al cargar el inventario desde archivo: {e}")
        except PermissionError as e:
            print(f"Error al cargar el inventario desde archivo: {e}")
        self.guardar_en_archivo()

    def agregar_producto(self, producto: Producto):
        if self.id_existe(producto.get_id()):
            print("El ID del producto ya existe.")
            return
        self.productos[producto.get_id()] = producto 
        self.guardar_en_archivo()
        print("Producto agregado exitosamente.")
        
    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print("Producto eliminado exitosamente.")
            self.guardar_en_archivo()
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id, nueva_cantidad=None, nuevo_precio=None):
        if id in self.productos:
            producto = self.productos[id]
            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)
            print("Producto actualizado exitosamente.")
            self.guardar_en_archivo()
        else:
            print("Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        for p in self.productos.values():
            if p.get_nombre() == nombre:
                return p
        print("Producto no encontrado.")
        return None

    def buscar_producto_por_id(self, id):
        if id in self.productos:
            return self.productos[id]
        print("Producto no encontrado.")
        return None

    def id_existe(self, id):
        return id in self.productos

    def nombre_existe(self, nombre):
        for p in self.productos.values():
            if p.get_nombre() == nombre:
                return p
        return None

    def mostrar_todos(self):
        for p in self.productos.values():
            print(p)

    def eliminar_inventario(self, confirmacion):
        if confirmacion == "si":
            self.productos = {}
            self.guardar_en_archivo()
            print("Inventario eliminado exitosamente.")
        else:
            print("Operación cancelada.")

# Función principal (Menú)
def menu():
    inventario = Inventario()

    while True:
        print("\n=== Sistema de Gestión de Inventarios ===")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por ID")
        print("5. Buscar producto por nombre")
        print("6. Mostrar todos los productos")
        print("7. Eliminar TODO el inventario")
        print("8. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id = input("ID: ")        
            if inventario.id_existe(id):
                print("El ID del producto ya existe.")                     
            else: 
                nombre = input("Nombre: ")
                if inventario.nombre_existe(nombre):
                    print("El nombre del producto ya existe.")
                else:
                    cantidad = int(input("Cantidad: "))
                    precio = float(input("Precio: "))
                    producto = Producto(id, nombre, cantidad, precio)
                    inventario.agregar_producto(producto)

        elif opcion == "2":
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
           
        elif opcion == "3":
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío si no cambia): ")
            precio = input("Nuevo precio (dejar vacío si no cambia): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == "4":
            id = input("ID a buscar: ")
            producto = inventario.buscar_producto_por_id(id)
            if producto is not None:
                print(producto)

        elif opcion == "5":
            nombre = input("Nombre a buscar: ")
            producto = inventario.buscar_producto_por_nombre(nombre)
            if producto is not None:
                print(producto)

        elif opcion == "6":
            if len(inventario.productos) == 0:
                print(" No hay productos en el inventario.")
            else:
                inventario.mostrar_todos()

        elif opcion == "7":
            confirmacion = input("¿Está seguro de eliminar todo el inventario? (si/no): ")
            inventario.eliminar_inventario(confirmacion)

        elif opcion == "8":
            print(" Saliendo del sistema...")
            break        
        
        else:
            print(" Opción inválida. Intente de nuevo.")


# Ejecutar el programa
if __name__ == "__main__":
    menu()