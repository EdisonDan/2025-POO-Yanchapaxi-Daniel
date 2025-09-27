import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Lista de Tareas")
ventana.geometry("500x400")

# Lista para guardar las tareas
lista_tareas = []

# Función para añadir una tarea nueva
def añadir_tarea():
    # Obtener el texto del campo de entrada
    nueva_tarea = entrada_tarea.get()
    
    # Verificar que no esté vacío
    if nueva_tarea.strip() == "":
        messagebox.showwarning("Advertencia", "¡Por favor escribe una tarea!")
        return
    
    # Añadir la tarea a la lista
    lista_tareas.append({"texto": nueva_tarea, "completada": False})
    
    # Actualizar la lista visual
    actualizar_lista()
    
    # Limpiar el campo de entrada
    entrada_tarea.delete(0, tk.END)

# Función para marcar tarea como completada
def marcar_completada():
    try:
        # Obtener el índice de la tarea seleccionada
        indice = listbox_tareas.curselection()[0]
        
        # Cambiar el estado de la tarea
        lista_tareas[indice]["completada"] = not lista_tareas[indice]["completada"]
        
        # Actualizar la lista visual
        actualizar_lista()
        
    except IndexError:
        messagebox.showwarning("Advertencia", "¡Selecciona una tarea primero!")

# Función para eliminar una tarea
def eliminar_tarea():
    try:
        # Obtener el índice de la tarea seleccionada
        indice = listbox_tareas.curselection()[0]
        
        # Eliminar la tarea de la lista
        del lista_tareas[indice]
        
        # Actualizar la lista visual
        actualizar_lista()
        
    except IndexError:
        messagebox.showwarning("Advertencia", "¡Selecciona una tarea para eliminar!")

# Función para actualizar la lista visual
def actualizar_lista():
    # Limpiar la lista visual
    listbox_tareas.delete(0, tk.END)
    
    # Añadir todas las tareas a la lista visual
    for i, tarea in enumerate(lista_tareas):
        if tarea["completada"]:
            # Si está completada, mostrar con ✓ y tachada
            texto = f"✓ {tarea['texto']}"
        else:
            # Si no está completada, mostrar normal
            texto = f"○ {tarea['texto']}"
        
        listbox_tareas.insert(tk.END, texto)

# Función para manejar la tecla Enter
def manejar_enter(event):
    añadir_tarea()

# Función para doble clic (evento adicional)
def doble_clic(event):
    marcar_completada()

# Crear los elementos de la interfaz

# Título
label_titulo = tk.Label(ventana, text="📝 LISTA DE TAREAS", font=("Arial", 16, "bold"))
label_titulo.pack(pady=10)

# Frame para la entrada de tareas
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10, padx=20, fill="x")

# Campo de entrada para nuevas tareas
label_entrada = tk.Label(frame_entrada, text="Nueva tarea:")
label_entrada.pack(anchor="w")

entrada_tarea = tk.Entry(frame_entrada, font=("Arial", 12), width=40)
entrada_tarea.pack(side="left", padx=(0, 10), fill="x", expand=True)
# Conectar la tecla Enter al campo de entrada
entrada_tarea.bind('<Return>', manejar_enter)

# Botón para añadir tarea
boton_añadir = tk.Button(frame_entrada, text="Añadir", command=añadir_tarea, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
boton_añadir.pack(side="right")

# Frame para los botones de acciones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

# Botón para marcar como completada
boton_completar = tk.Button(frame_botones, text="✓ Completar", command=marcar_completada, bg="#2196F3", fg="white", font=("Arial", 10))
boton_completar.pack(side="left", padx=5)

# Botón para eliminar tarea
boton_eliminar = tk.Button(frame_botones, text="🗑️ Eliminar", command=eliminar_tarea, bg="#f44336", fg="white", font=("Arial", 10))
boton_eliminar.pack(side="left", padx=5)

# Frame para la lista de tareas
frame_lista = tk.Frame(ventana)
frame_lista.pack(pady=10, padx=20, fill="both", expand=True)

# Etiqueta para la lista
label_lista = tk.Label(frame_lista, text="Mis tareas:", font=("Arial", 12, "bold"))
label_lista.pack(anchor="w")

# Lista visual para mostrar las tareas
listbox_tareas = tk.Listbox(frame_lista, font=("Arial", 11), selectmode=tk.SINGLE, height=10)
listbox_tareas.pack(fill="both", expand=True, pady=(5, 0))
# Conectar doble clic a la lista
listbox_tareas.bind('<Double-1>', doble_clic)

# Scrollbar para la lista
scrollbar = tk.Scrollbar(listbox_tareas)
scrollbar.pack(side="right", fill="y")
listbox_tareas.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_tareas.yview)

# Información adicional
label_info = tk.Label(ventana, text="💡 Tip: Presiona Enter para añadir, doble clic para completar", font=("Arial", 9), fg="gray")
label_info.pack(pady=5)

# Iniciar la aplicación
print("🚀 Iniciando aplicación de Lista de Tareas...")
print("📋 Funciones disponibles:")
print("   - Escribir tarea y presionar Enter o clic en 'Añadir'")
print("   - Seleccionar tarea y clic en 'Completar' para marcar/desmarcar")
print("   - Doble clic en una tarea para completarla rápidamente")
print("   - Seleccionar tarea y clic en 'Eliminar' para borrarla")
print("-" * 50)

ventana.mainloop()