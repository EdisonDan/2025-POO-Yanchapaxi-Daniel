# Importamos las librerías necesarias
import tkinter as tk  # Para crear la interfaz gráfica
from tkinter import ttk  # Para widgets más modernos como TreeView
from tkinter import messagebox  # Para mostrar mensajes de confirmación
from datetime import datetime  # Para trabajar con fechas y horas

class AgendaPersonal:
    """
    Clase principal que maneja toda la aplicación de agenda personal
    """
    
    def __init__(self):
        """
        Constructor: inicializa la aplicación y crea la interfaz
        """
        # Crear la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Agenda Personal")  # Título de la ventana
        self.ventana.geometry("800x600")  # Tamaño de la ventana (ancho x alto)
        self.ventana.configure(bg="#f0f0f0")  # Color de fondo
        
        # Lista para guardar todos los eventos
        self.eventos = []
        
        # Crear todos los elementos de la interfaz
        self.crear_interfaz()
    
    def crear_interfaz(self):
        """
        Método que crea todos los elementos de la interfaz gráfica
        """
        # Título principal de la aplicación
        titulo = tk.Label(
            self.ventana,
            text="📅 MI AGENDA PERSONAL",
            font=("Arial", 18, "bold"),
            bg="#f0f0f0",
            fg="#2c3e50"
        )
        titulo.pack(pady=10)  # pack() coloca el elemento en la ventana
        
        # Frame principal que contendrá todo el contenido
        frame_principal = tk.Frame(self.ventana, bg="#f0f0f0")
        frame_principal.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Crear las tres secciones principales
        self.crear_seccion_entrada(frame_principal)
        self.crear_seccion_botones(frame_principal)
        self.crear_seccion_eventos(frame_principal)
    
    def crear_seccion_entrada(self, contenedor):
        """
        Crea la sección donde el usuario introduce los datos del evento
        """
        # Frame para contener los campos de entrada
        frame_entrada = tk.LabelFrame(
            contenedor,
            text="Agregar Nuevo Evento",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0",
            fg="#34495e",
            padx=10,
            pady=10
        )
        frame_entrada.pack(fill="x", pady=(0, 10))
        
        # Crear una cuadrícula para organizar los campos
        # Fila 0: Campos de fecha y hora
        tk.Label(frame_entrada, text="📅 Fecha (dd/mm/yyyy):", font=("Arial", 10), bg="#f0f0f0").grid(row=0, column=0, sticky="w", padx=(0, 10))
        
        # Simple entry for date input
        self.entrada_fecha = tk.Entry(frame_entrada, width=12)
        self.entrada_fecha.insert(0, datetime.now().strftime("%d/%m/%Y"))
        self.entrada_fecha.grid(row=0, column=1, sticky="w", padx=(0, 20))
        
        tk.Label(frame_entrada, text="🕐 Hora:", font=("Arial", 10), bg="#f0f0f0").grid(row=0, column=2, sticky="w", padx=(0, 10))
        
        # Campo para introducir la hora
        self.entrada_hora = tk.Entry(frame_entrada, width=10)
        self.entrada_hora.insert(0, "09:00")  # Valor por defecto
        self.entrada_hora.grid(row=0, column=3, sticky="w")
        
        # Fila 1: Campo de descripción (más grande)
        tk.Label(frame_entrada, text="📝 Descripción:", font=("Arial", 10), bg="#f0f0f0").grid(row=1, column=0, sticky="nw", pady=(10, 0))
        
        self.entrada_descripcion = tk.Text(frame_entrada, width=50, height=3)
        self.entrada_descripcion.grid(row=1, column=1, columnspan=3, sticky="ew", pady=(10, 0))
    
    def crear_seccion_botones(self, contenedor):
        """
        Crea la sección con los botones de acción
        """
        frame_botones = tk.Frame(contenedor, bg="#f0f0f0")
        frame_botones.pack(fill="x", pady=10)
        
        # Botón para agregar evento
        boton_agregar = tk.Button(
            frame_botones,
            text="✅ Agregar Evento",
            command=self.agregar_evento,  # Función que se ejecuta al hacer clic
            font=("Arial", 11, "bold"),
            bg="#27ae60",
            fg="white",
            padx=20,
            pady=5,
            cursor="hand2"  # Cambia el cursor al pasar el mouse
        )
        boton_agregar.pack(side="left", padx=(0, 10))
        
        # Botón para eliminar evento seleccionado
        boton_eliminar = tk.Button(
            frame_botones,
            text="🗑️ Eliminar Seleccionado",
            command=self.eliminar_evento,
            font=("Arial", 11, "bold"),
            bg="#e74c3c",
            fg="white",
            padx=20,
            pady=5,
            cursor="hand2"
        )
        boton_eliminar.pack(side="left", padx=(0, 10))
        
        # Botón para salir de la aplicación
        boton_salir = tk.Button(
            frame_botones,
            text="🚪 Salir",
            command=self.salir_aplicacion,
            font=("Arial", 11, "bold"),
            bg="#95a5a6",
            fg="white",
            padx=20,
            pady=5,
            cursor="hand2"
        )
        boton_salir.pack(side="right")
    
    def crear_seccion_eventos(self, contenedor):
        """
        Crea la sección que muestra la lista de eventos
        """
        # Frame para la lista de eventos
        frame_lista = tk.LabelFrame(
            contenedor,
            text="Eventos Programados",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0",
            fg="#34495e",
            padx=10,
            pady=10
        )
        frame_lista.pack(fill="both", expand=True)
        
        # Crear el TreeView (tabla) para mostrar los eventos
        columnas = ("Fecha", "Hora", "Descripción")
        self.tree = ttk.Treeview(frame_lista, columns=columnas, show="headings", height=10)
        
        # Configurar las columnas
        self.tree.heading("Fecha", text="📅 Fecha")
        self.tree.heading("Hora", text="🕐 Hora")
        self.tree.heading("Descripción", text="📝 Descripción")
        
        # Ajustar el ancho de las columnas
        self.tree.column("Fecha", width=100)
        self.tree.column("Hora", width=80)
        self.tree.column("Descripción", width=400)
        
        # Crear scrollbar para la tabla
        scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Colocar la tabla y el scrollbar
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def agregar_evento(self):
        """
        Función que se ejecuta cuando se hace clic en 'Agregar Evento'
        """
        try:
            # Obtener los datos de los campos de entrada
            fecha = self.entrada_fecha.get().strip()
            hora = self.entrada_hora.get().strip()
            descripcion = self.entrada_descripcion.get("1.0", "end-1c").strip()
            
            # Verificar que todos los campos estén llenos
            if not fecha or not hora or not descripcion:
                messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos.")
                return
            
            # Verificar formato de fecha
            try:
                datetime.strptime(fecha, "%d/%m/%Y")
            except ValueError:
                messagebox.showerror("Fecha inválida", "Por favor, introduce la fecha en formato dd/mm/yyyy")
                return
            
            # Verificar formato de hora
            if not self.validar_hora(hora):
                messagebox.showerror("Hora inválida", "Por favor, introduce la hora en formato HH:MM (ejemplo: 14:30)")
                return
            
            # Crear un diccionario con los datos del evento
            evento = {
                "fecha": fecha,
                "hora": hora,
                "descripcion": descripcion
            }
            
            # Agregar el evento a nuestra lista
            self.eventos.append(evento)
            
            # Actualizar la tabla con el nuevo evento
            self.actualizar_tabla()
            
            # Limpiar los campos después de agregar
            self.limpiar_campos()
            
            # Mostrar mensaje de éxito
            messagebox.showinfo("¡Éxito!", "Evento agregado correctamente.")
            
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")
    
    def eliminar_evento(self):
        """
        Función que elimina el evento seleccionado
        """
        # Obtener el elemento seleccionado en la tabla
        seleccion = self.tree.selection()
        
        if not seleccion:
            messagebox.showwarning("Sin selección", "Por favor, selecciona un evento para eliminar.")
            return
        
        # Confirmar la eliminación
        respuesta = messagebox.askyesno(
            "Confirmar eliminación",
            "¿Estás seguro de que quieres eliminar este evento?"
        )
        
        if respuesta:  # Si el usuario confirma
            # Obtener el índice del elemento seleccionado
            item = seleccion[0]
            indice = self.tree.index(item)
            
            # Eliminar de la lista de eventos
            del self.eventos[indice]
            
            # Actualizar la tabla
            self.actualizar_tabla()
            
            messagebox.showinfo("Eliminado", "Evento eliminado correctamente.")
    
    def actualizar_tabla(self):
        """
        Actualiza la tabla con todos los eventos actuales
        """
        # Limpiar la tabla
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Agregar todos los eventos a la tabla
        for evento in self.eventos:
            self.tree.insert("", "end", values=(
                evento["fecha"],
                evento["hora"],
                evento["descripcion"]
            ))
    
    def limpiar_campos(self):
        """
        Limpia todos los campos de entrada
        """
        self.entrada_fecha.delete(0, tk.END)
        self.entrada_fecha.insert(0, datetime.now().strftime("%d/%m/%Y"))
        self.entrada_hora.delete(0, tk.END)
        self.entrada_hora.insert(0, "09:00")  # Valor por defecto
        self.entrada_descripcion.delete("1.0", tk.END)
    
    def validar_hora(self, hora):
        """
        Valida que la hora tenga el formato correcto HH:MM
        """
        try:
            # Intentar convertir la hora al formato correcto
            datetime.strptime(hora, "%H:%M")
            return True
        except ValueError:
            return False
    
    def salir_aplicacion(self):
        """
        Función para cerrar la aplicación
        """
        respuesta = messagebox.askyesno(
            "Salir",
            "¿Estás seguro de que quieres salir de la aplicación?"
        )
        
        if respuesta:
            self.ventana.quit()  # Cerrar la aplicación
    
    def ejecutar(self):
        """
        Método que inicia la aplicación
        """
        self.ventana.mainloop()  # Inicia el bucle principal de la interfaz

# Función principal que se ejecuta cuando corres el programa
def main():
    """
    Función principal del programa
    """
    print("🚀 Iniciando Agenda Personal...")
    print("📋 Instrucciones:")
    print("   • Ingresa la fecha en formato dd/mm/yyyy")
    print("   • Introduce la hora en formato HH:MM (ej: 14:30)")
    print("   • Escribe una descripción del evento")
    print("   • Haz clic en 'Agregar Evento'")
    print("   • Para eliminar, selecciona un evento y haz clic en 'Eliminar'")
    print("=" * 50)
    
    # Crear y ejecutar la aplicación
    app = AgendaPersonal()
    app.ejecutar()

# Esta línea hace que el programa se ejecute solo cuando corres este archivo directamente
if __name__ == "__main__":
    main()