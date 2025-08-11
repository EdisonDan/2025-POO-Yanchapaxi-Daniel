from ast import Break


class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id
    def get_nombre(self):
        return self.nombre
    def get_cantidad(self):
        return self.cantidad
    def get_precio(self):
        return self.precio

    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad
    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"
        
class Inventario:
    def __init__(self):
        self.productos = []
        

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("El ID del producto ya existe.")
                return
        self.productos.append(producto)
        print("Producto agregado exitosamente.")
        
    def eliminar_producto(self, id):
        for p in self.productos:
            if p.get_id() == id:
                self.productos.remove(p)
                print("Producto eliminado exitosamente.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id, nueva_cantidad=None, nuevo_precio=None):
        for producto in self.productos:
            if producto.get_id() == id:
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                print("Producto actualizado exitosamente.")
                return
            print("Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        for producto in self.productos:
            if producto.get_nombre() == nombre:
                return producto
            return None
        print("Producto no encontrado.")

    def buscar_producto_por_id(self, id):
        for producto in self.productos:
            if producto.get_id() == id:
                return producto
        return None

    def mostrar_todos(self):
        for p in self.productos:
            print(p)


def menu():
    inventario = Inventario()

    while True:
        print("\n=== Sistema de Gestión de Inventarios ===")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id = input("ID: ")
            while True:
                if inventario.buscar_producto_por_id(id) is not None:
                    print("El ID del producto ya existe.")
                    menu()
                else:
                    break
            nombre = input("Nombre: ")
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
            nombre = input("Nombre a buscar: ")
            producto = inventario.buscar_producto_por_nombre(nombre)
            if producto is not None:
                print(producto)

            else:
                print(" No se encontraron productos.")

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print(" Saliendo del sistema...")
            break

        else:
            print(" Opción inválida. Intente de nuevo.")

# Ejecutar el programa

if __name__ == "__main__":
    menu()