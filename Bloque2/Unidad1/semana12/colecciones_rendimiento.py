import os

# =========================
# Clase Libro
# =========================
class Libro:
    def __init__(self, isbn, titulo, autor, categoria):
        self.info = (titulo, autor)  # tupla inmutable
        self.isbn = isbn
        self.categoria = categoria

    def get_titulo(self):
        return self.info[0]

    def get_autor(self):
        return self.info[1]

    def get_isbn(self):
        return self.isbn

    def get_categoria(self):
        return self.categoria

    def __str__(self):
        return f"ISBN: {self.isbn}, Título: {self.get_titulo()}, Autor: {self.get_autor()}, Categoría: {self.categoria}"


# =========================
# Clase Usuario
# =========================
class Usuario:
    def __init__(self, user_id, nombre):
        self.user_id = user_id
        self.nombre = nombre
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        for libro in self.libros_prestados:
            if libro.get_isbn() == isbn:
                self.libros_prestados.remove(libro)
                return libro
        return None

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.user_id}, Libros prestados: {[libro.get_titulo() for libro in self.libros_prestados]}"


# =========================
# Clase Biblioteca
# =========================
class Biblioteca:
    def __init__(self):
        directorio = os.path.dirname(os.path.abspath(__file__))
        self.archivo_libros = os.path.join(directorio, "biblioteca.txt")
        self.archivo_usuarios = os.path.join(directorio, "usuarios.txt")
        self.archivo_prestamos = os.path.join(directorio, "prestamos.txt")

        self.libros = {}     # isbn -> libro
        self.usuarios = {}   # id -> usuario
        self.ids_usuarios = set()

        self.cargar_libros()
        self.cargar_usuarios()
        self.cargar_prestamos()

    # ---------- Persistencia de libros ----------
    def guardar_libros(self):
        try:
            with open(self.archivo_libros, "w", encoding="utf-8") as f:
                for libro in self.libros.values():
                    f.write(f"ISBN={libro.isbn}=Titulo={libro.get_titulo()}=Autor={libro.get_autor()}=Categoria={libro.get_categoria()}\n")
        except Exception as e:
            print(f"Error al guardar libros: {e}")

    def cargar_libros(self):
        if not os.path.exists(self.archivo_libros):
            open(self.archivo_libros, "w").close()
            return
        try:
            with open(self.archivo_libros, "r", encoding="utf-8") as f:
                for linea in f:
                    partes = linea.strip().split("=")
                    if len(partes) == 8:
                        isbn = partes[1]
                        titulo = partes[3]
                        autor = partes[5]
                        categoria = partes[7]
                        self.libros[isbn] = Libro(isbn, titulo, autor, categoria)
        except Exception as e:
            print(f"Error al cargar libros: {e}")

    # ---------- Persistencia de usuarios ----------
    def guardar_usuarios(self):
        try:
            with open(self.archivo_usuarios, "w", encoding="utf-8") as f:
                for usuario in self.usuarios.values():
                    f.write(f"ID={usuario.user_id}=Nombre={usuario.nombre}\n")
        except Exception as e:
            print(f"Error al guardar usuarios: {e}")

    def cargar_usuarios(self):
        if not os.path.exists(self.archivo_usuarios):
            open(self.archivo_usuarios, "w").close()
            return
        try:
            with open(self.archivo_usuarios, "r", encoding="utf-8") as f:
                for linea in f:
                    partes = linea.strip().split("=")
                    if len(partes) == 4:
                        user_id = partes[1]
                        nombre = partes[3]
                        usuario = Usuario(user_id, nombre)
                        self.usuarios[user_id] = usuario
                        self.ids_usuarios.add(user_id)
        except Exception as e:
            print(f"Error al cargar usuarios: {e}")

    # ---------- Persistencia de préstamos ----------
    def guardar_prestamos(self):
        try:
            with open(self.archivo_prestamos, "w", encoding="utf-8") as f:
                for usuario in self.usuarios.values():
                    for libro in usuario.libros_prestados:
                        f.write(f"UserID={usuario.user_id}=ISBN={libro.get_isbn()}=Titulo={libro.get_titulo()}=Autor={libro.get_autor()}=Categoria={libro.get_categoria()}\n")
        except Exception as e:
            print(f"Error al guardar préstamos: {e}")

    def cargar_prestamos(self):
        if not os.path.exists(self.archivo_prestamos):
            open(self.archivo_prestamos, "w").close()
            return
        try:
            with open(self.archivo_prestamos, "r", encoding="utf-8") as f:
                for linea in f:
                    partes = linea.strip().split("=")
                    if len(partes) == 10:  # UserID=...=ISBN=...=Titulo=...=Autor=...=Categoria=...
                        user_id = partes[1]
                        isbn = partes[3]
                        titulo = partes[5]
                        autor = partes[7]
                        categoria = partes[9]

                        if user_id in self.usuarios:
                            libro = Libro(isbn, titulo, autor, categoria)
                            self.usuarios[user_id].prestar_libro(libro)
        except Exception as e:
            print(f"Error al cargar préstamos: {e}")

    # ---------- Libros ----------
    def añadir_libro(self, libro: Libro):
        if libro.get_isbn() in self.libros:
            print("El libro ya existe en la biblioteca.")
            return
        self.libros[libro.get_isbn()] = libro
        self.guardar_libros()
        print("Libro añadido correctamente.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            self.guardar_libros()
            print("Libro eliminado correctamente.")
        else:
            print("Libro no encontrado.")

    def buscar_libro(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if (criterio == "titulo" and libro.get_titulo() == valor) or \
               (criterio == "autor" and libro.get_autor() == valor) or \
               (criterio == "categoria" and libro.get_categoria() == valor):
                resultados.append(libro)
        return resultados

    def listar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
        for libro in self.libros.values():
            print(libro)

    # ---------- Usuarios ----------
    def registrar_usuario(self, usuario: Usuario):
        if usuario.user_id in self.ids_usuarios:
            print("El ID de usuario ya existe.")
            return
        self.usuarios[usuario.user_id] = usuario
        self.ids_usuarios.add(usuario.user_id)
        self.guardar_usuarios()
        print("Usuario registrado exitosamente.")

    def dar_baja_usuario(self, user_id):
        if user_id in self.usuarios:
            del self.usuarios[user_id]
            self.ids_usuarios.remove(user_id)
            self.guardar_usuarios()
            self.guardar_prestamos()
            print("Usuario dado de baja exitosamente.")
        else:
            print("Usuario no encontrado.")

    def listar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
        for usuario in self.usuarios.values():
            print(usuario)

    # ---------- Préstamos ----------
    def prestar_libro(self, user_id, isbn):
        if user_id not in self.usuarios:
            print("Usuario no registrado.")
            return
        if isbn not in self.libros:
            print("Libro no disponible en la biblioteca.")
            return
        usuario = self.usuarios[user_id]
        libro = self.libros.pop(isbn)
        usuario.prestar_libro(libro)
        self.guardar_libros()
        self.guardar_prestamos()
        print(f"Libro '{libro.get_titulo()}' prestado a {usuario.nombre}.")

    def devolver_libro(self, user_id, isbn):
        if user_id not in self.usuarios:
            print("Usuario no registrado.")
            return
        usuario = self.usuarios[user_id]
        libro = usuario.devolver_libro(isbn)
        if libro:
            self.libros[isbn] = libro
            self.guardar_libros()
            self.guardar_prestamos()
            print(f"Libro '{libro.get_titulo()}' devuelto por {usuario.nombre}.")
        else:
            print("El usuario no tenía prestado este libro.")

    def listar_libros_prestados(self, user_id):
        if user_id not in self.usuarios:
            print("Usuario no registrado.")
            return
        usuario = self.usuarios[user_id]
        if not usuario.libros_prestados:
            print("El usuario no tiene libros prestados.")
        else:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(libro)


# =========================
# Menú Principal
# =========================
def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n=== Sistema de Gestión de Biblioteca Digital ===")
        print("1. Añadir libro")
        print("2. Quitar libro")
        print("3. Buscar libro")
        print("4. Listar todos los libros")
        print("5. Registrar usuario")
        print("6. Dar de baja usuario")
        print("7. Listar todos los usuarios")
        print("8. Prestar libro")
        print("9. Devolver libro")
        print("10. Listar libros prestados de un usuario")
        print("11. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            isbn = input("ISBN: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            libro = Libro(isbn, titulo, autor, categoria)
            biblioteca.añadir_libro(libro)

        elif opcion == "2":
            isbn = input("ISBN del libro a eliminar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":
            criterio = input("Buscar por (titulo/autor/categoria): ").lower()
            valor = input("Ingrese el valor de búsqueda: ")
            resultados = biblioteca.buscar_libro(criterio, valor)
            if resultados:
                for libro in resultados:
                    print(libro)
            else:
                print("No se encontraron libros.")

        elif opcion == "4":
            biblioteca.listar_libros()

        elif opcion == "5":
            user_id = input("ID de usuario: ")
            nombre = input("Nombre: ")
            usuario = Usuario(user_id, nombre)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "6":
            user_id = input("ID de usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(user_id)

        elif opcion == "7":
            biblioteca.listar_usuarios()

        elif opcion == "8":
            user_id = input("ID de usuario: ")
            isbn = input("ISBN del libro a prestar: ")
            biblioteca.prestar_libro(user_id, isbn)

        elif opcion == "9":
            user_id = input("ID de usuario: ")
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(user_id, isbn)

        elif opcion == "10":
            user_id = input("ID de usuario: ")
            biblioteca.listar_libros_prestados(user_id)

        elif opcion == "11":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    menu()