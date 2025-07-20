import os


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        # Intentar abrir con diferentes codificaciones
        for encoding in ['utf-8', 'latin-1', 'cp1252']:
            try:
                with open(ruta_script_absoluta, 'r', encoding=encoding) as archivo:
                    print(f"\n--- Código de {ruta_script} ---\n")
                    print(archivo.read())
                    return  # Si se lee correctamente, salir de la función
            except UnicodeDecodeError:
                continue  # Probar con la siguiente codificación
            except FileNotFoundError:
                break  # Salir del bucle si el archivo no existe
        
        # Verificar si el archivo existe
        if not os.path.exists(ruta_script_absoluta):
            print("El archivo no se encontró.")
        else:
            print("No se pudo leer el archivo con ninguna codificación compatible.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Parcial1/Semana02/Semana2.py',
        '2': 'Parcial1/Semana03/POO.py',
        '3': 'Parcial1/Semana03/ProgramaciónTradicional.py',
        '4': 'Parcial1/Semana04/EjemplosMundoRealPOO.py',
        '5': 'Unidad2/Semana5/TiposDeDatosIdentificadoresImplementacion.py',
        '6': 'Unidad2/Semana6/ClasesObjetosHerenciaEncapsulamientoPolimorfismo.py',
        '7': 'Unidad2/Semana7/ImplementacionDeConstructoresYDestructoresEnPython.py',
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()