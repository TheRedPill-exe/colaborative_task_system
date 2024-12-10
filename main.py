from task_manager import Task, TaskManager
from user_manager import User, UserManager
from project_manager import Project, ProjectManager
from decorators import log


class CollaborativeTaskSystem():
    def __init__(self):
        self.users = UserManager()
        self.tasks = TaskManager()
        self.projects = ProjectManager()

    # Funcionalidad para crear usuarios
    def create_user(self):
        print("\n-- Create User --")
        user_id = input("Enter User ID: ")
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        birth_date = input("Enter Birth Date: ")

        new_user = User(user_id, name, email, password, birth_date, [], [])
        if self.users.add_user(new_user):
            print("User created successfully!")
        else:
            print("Failed to create user. ID may already exist.")

    # Funcionalidad para crear tareas
    def create_task(self):
        print("\n-- Create Task --")
        task_id = input("Enter Task ID: ")
        name = input("Enter Task Name: ")
        description = input("Enter Description: ")

        new_task = Task(None, task_id, name, description, "Pending", "", "", "Normal", [])
        if self.tasks.add_task(new_task):
            print("Task created successfully!")
        else:
            print("Failed to create task. ID may already exist.")

    # Funcionalidad para crear proyectos
    def create_project(self):
        print("\n-- Create Project --")
        project_id = input("Enter Project ID: ")
        name = input("Enter Project Name: ")
        description = input("Enter Description: ")
    
        # Mostrar tareas disponibles y seleccionar una
        print("\nAvailable Tasks:")
        tasks = self.tasks.get_all()  # Método que devuelve todas las tareas
        if not tasks:
            print("No tasks available. Please create a task first.")
            return
    
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
        task_choice = int(input("Select a task by number: ")) - 1
        if task_choice < 0 or task_choice >= len(tasks):
            print("Invalid task selection.")
            return
        selected_task = tasks[task_choice]
    
        # Mostrar usuarios disponibles y seleccionar uno
        print("\nAvailable Users:")
        users = self.users.get_all()  # Método que devuelve todos los usuarios
        if not users:
            print("No users available. Please create a user first.")
            return
    
        for i, user in enumerate(users):
            print(f"{i + 1}. {user}")
        user_choice = int(input("Select a user by number: ")) - 1
        if user_choice < 0 or user_choice >= len(users):
            print("Invalid user selection.")
            return
        selected_user = users[user_choice]
    
        # Crear proyecto con la tarea y el usuario seleccionados
        new_project = Project(project_id, name, description, "Normal", [selected_task], [selected_user])
        if self.projects.add_project(new_project):
            print("Project created successfully!")
        else:
            print("Failed to create project. ID may already exist.")
    

    # Funcionalidad para mostrar usuarios
    def show_users(self):
        print("\n-- Show Users --")
        field = input("Search by field (e.g. ID, name): ")
        value = input("Enter the value to search: ")
        users = self.users.show_data(field, value)
        if users:
            print("User(s) found:")
            for user in users:
                print(user)
        else:
            print("No users found.")

    # Funcionalidad para mostrar tareas
    def show_tasks(self):
        print("\n-- Show Tasks --")
        field = input("Search by field (e.g. ID, name): ")
        value = input("Enter the value to search: ")
        tasks = self.tasks.show_data(field, value)
        if tasks:
            print("Task(s) found:")
            for task in tasks:
                print(task)
        else:
            print("No tasks found.")

    # Funcionalidad para mostrar proyectos
    def show_projects(self):
        print("\n-- Show Projects --")
        field = input("Search by field (e.g. ID, name): ")
        value = input("Enter the value to search: ")
        projects = self.projects.show_data(field, value)
        if projects:
            print("Project(s) found:")
            for project in projects:
                print(project)
        else:
            print("No projects found.")

    # Funcionalidad principal para ejecutar el sistema
    def menu(self):
        while True:
            print("\n== Collaborative Task System Menu ==")
            print("1. Create User")
            print("2. Create Task")
            print("3. Create Project")
            print("4. Show Users")
            print("5. Show Tasks")
            print("6. Show Projects")
            print("7. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.create_user()
            elif choice == "2":
                self.create_task()
            elif choice == "3":
                self.create_project()
            elif choice == "4":
                self.show_users()
            elif choice == "5":
                self.show_tasks()
            elif choice == "6":
                self.show_projects()
            elif choice == "7":
                print("\nExiting system. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please try again.")


# Instanciar y ejecutar la aplicación
if __name__ == "__main__":
    system = CollaborativeTaskSystem()
    system.menu()
