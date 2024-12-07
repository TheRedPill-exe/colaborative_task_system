import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from main import CollaborativeTaskSystem

class CollaborativeTaskSystemGUI:
    def __init__(self, root, task_system):
        self.task_system = task_system
        self.root = root
        self.root.title("Collaborative Task System")
        self.root.geometry("800x600")
        self.root.style = ttk.Style("darkly")  # Tema oscuro minimalista
        
        self.setup_main_interface()
    
    def setup_main_interface(self):
        # Frame principal
        self.main_frame = ttk.Frame(self.root, padding=20)
        self.main_frame.pack(fill=BOTH, expand=TRUE)

        # Botones de navegación
        nav_frame = ttk.Frame(self.main_frame)
        nav_frame.pack(fill=X, pady=10)

        ttk.Button(nav_frame, text="Usuarios", command=self.show_users).pack(side=LEFT, padx=5)
        ttk.Button(nav_frame, text="Tareas", command=self.show_tasks).pack(side=LEFT, padx=5)
        ttk.Button(nav_frame, text="Proyectos", command=self.show_projects).pack(side=LEFT, padx=5)
        ttk.Button(nav_frame, text="Salir", command=self.root.quit).pack(side=RIGHT, padx=5)
        
        # Contenido dinámico
        self.content_frame = ttk.Frame(self.main_frame)
        self.content_frame.pack(fill=BOTH, expand=TRUE, pady=10)
        
        # Mostrar la pantalla inicial
        self.show_welcome()

    def show_welcome(self):
        self.clear_content()
        ttk.Label(self.content_frame, text="Bienvenido al Sistema de Tareas", font=("Helvetica", 18)).pack(pady=50)

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_users(self):
        self.clear_content()
        ttk.Label(self.content_frame, text="Gestión de Usuarios", font=("Helvetica", 16)).pack(pady=10)
        
        # Campos para crear un usuario
        user_frame = ttk.Frame(self.content_frame)
        user_frame.pack(pady=20)

        ttk.Label(user_frame, text="ID").grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(user_frame, text="Nombre").grid(row=1, column=0, padx=5, pady=5)
        ttk.Label(user_frame, text="Email").grid(row=2, column=0, padx=5, pady=5)
        ttk.Label(user_frame, text="Contraseña").grid(row=3, column=0, padx=5, pady=5)

        user_id = ttk.Entry(user_frame)
        user_name = ttk.Entry(user_frame)
        user_email = ttk.Entry(user_frame)
        user_password = ttk.Entry(user_frame, show="*")
        
        user_id.grid(row=0, column=1, padx=5, pady=5)
        user_name.grid(row=1, column=1, padx=5, pady=5)
        user_email.grid(row=2, column=1, padx=5, pady=5)
        user_password.grid(row=3, column=1, padx=5, pady=5)

        def add_user():
            # Llamar al método del sistema para crear usuario
            try:
                self.task_system.create_user(user_id.get(), user_name.get(), user_email.get(), user_password.get())
                messagebox.showinfo("Éxito", "Usuario creado correctamente")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        ttk.Button(user_frame, text="Crear Usuario", command=add_user).grid(row=4, column=0, columnspan=2, pady=10)

    def show_tasks(self):
        self.clear_content()
        ttk.Label(self.content_frame, text="Gestión de Tareas", font=("Helvetica", 16)).pack(pady=10)
        # Aquí se pueden añadir formularios y botones para crear, mostrar y actualizar tareas

    def show_projects(self):
        self.clear_content()
        ttk.Label(self.content_frame, text="Gestión de Proyectos", font=("Helvetica", 16)).pack(pady=10)
        # Aquí se pueden añadir formularios y botones para gestionar proyectos


if __name__ == "__main__":
    from task_manager import TaskManager
    from user_manager import UserManager
    from project_manager import ProjectManager

    # Instancia del sistema
    task_system = CollaborativeTaskSystem()
    
    # Iniciar la GUI
    root = ttk.Window(themename="darkly")
    app = CollaborativeTaskSystemGUI(root, task_system)
    root.mainloop()
