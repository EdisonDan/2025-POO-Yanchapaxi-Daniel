# Mi primera aplicación GUI con Tkinter
# Tarea de programación - Lista de tareas simple
# Autor: Estudiante principiante

import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Lista de Tareas - Aplicación GUI Básica")
ventana.geometry("500x400")
ventana.config(bg="lightblue")

# Variables globales (las aprendí en clase)
lista_tareas = []

# Funciones para los botones
def agregar_tarea():
    """Función que agrega una tarea a la lista"""
    # Obtener el texto del campo de entrada
    tarea = entrada_texto.get()
    
    # Verificar que no esté vacío (esto me ayudó el profesor)
    if tarea.strip() == "":
        messagebox.showwarning("Advertencia", "Por favor escribe una tarea")
        return
    
    # Agregar la tarea a nuestra lista
    lista_tareas.append(tarea)
    
    # Actualizar la lista en la pantalla
    actualizar_lista()
    
    # Limpiar el campo de texto
    entrada_texto.delete(0, tk.END)

def limpiar_todo():
    """Función que limpia toda la lista"""
    # Limpiar la lista de tareas
    lista_tareas.clear()
    # Actualizar la pantalla
    actualizar_lista()
    # También limpiar el campo de texto
    entrada_texto.delete(0, tk.END)

def actualizar_lista():
    """Función que actualiza lo que se muestra en la lista"""
    # Primero borro todo lo que está en la lista visual
    lista_visual.delete(0, tk.END)
    
    # Luego agrego todas las tareas una por una
    for i, tarea in enumerate(lista_tareas):
        lista_visual.insert(tk.END, f"{i+1}. {tarea}")

# Crear los componentes de la interfaz (widgets)

# Título principal (etiqueta)
titulo = tk.Label(ventana, text="📝 MI LISTA DE TAREAS", 
                  font=("Arial", 16, "bold"), 
                  bg="lightblue", 
                  fg="darkblue")
titulo.pack(pady=10)

# Instrucciones (otra etiqueta)
instrucciones = tk.Label(ventana, text="Escribe una tarea y presiona 'Agregar'", 
                        font=("Arial", 10), 
                        bg="lightblue")
instrucciones.pack(pady=5)

# Campo de texto para escribir tareas
entrada_texto = tk.Entry(ventana, font=("Arial", 12), width=40)
entrada_texto.pack(pady=10)

# Frame para los botones (para que queden uno al lado del otro)
frame_botones = tk.Frame(ventana, bg="lightblue")
frame_botones.pack(pady=10)

# Botón para agregar tareas
boton_agregar = tk.Button(frame_botones, text="Agregar", 
                         command=agregar_tarea,
                         bg="green", fg="white",
                         font=("Arial", 10, "bold"),
                         width=10)
boton_agregar.pack(side=tk.LEFT, padx=5)

# Botón para limpiar
boton_limpiar = tk.Button(frame_botones, text="Limpiar", 
                         command=limpiar_todo,
                         bg="red", fg="white",
                         font=("Arial", 10, "bold"),
                         width=10)
boton_limpiar.pack(side=tk.LEFT, padx=5)

# Etiqueta para la lista
etiqueta_lista = tk.Label(ventana, text="Mis tareas:", 
                         font=("Arial", 12, "bold"), 
                         bg="lightblue")
etiqueta_lista.pack(pady=(20,5))

# Lista para mostrar las tareas (Listbox)
lista_visual = tk.Listbox(ventana, font=("Arial", 10), 
                         width=50, height=10,
                         bg="white")
lista_visual.pack(pady=10, padx=20)

# Hacer que funcione la tecla Enter en el campo de texto
entrada_texto.bind('<Return>', lambda event: agregar_tarea())

# Iniciar la aplicación
if __name__ == "__main__":
    # Mensaje de bienvenida (opcional)
    messagebox.showinfo("Bienvenido", "¡Bienvenido a tu lista de tareas!\n\nPuedes agregar tareas y limpiar la lista.")
    
    # Ejecutar el loop principal de la ventana
    ventana.mainloop()