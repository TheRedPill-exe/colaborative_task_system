from decorators import log 
from task_manager import Task
from user_manager import User
from validation import validate_project
from file_handler import save_update, load_data
class Project():
    @log("Creating project")
    def __init__(self, id, name, description, priority, tasks, users):
        self.id = id
        self.name = name
        self.description = description
        self.tasks = tasks
        self.users = users
        self.priority = priority
    
    @log("Adding task to project")
    def add_task(self, task):
        self.tasks.append(task)
    
    @log("Adding user to project")
    def add_user(self, user):
        self.users.append(user)
    
    @log("Getting task from project")
    def get_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                return task
        
        print("Task not found.")
        return None

    @log("Getting user from project")
    def get_user(self, user_name):
        for user in self.users:
            if user.name == user_name:
                return user
        
        print("User not found.")
        return None
    
    @log("Showing project data")
    def show_project(self):
        output = "\n".join(f"{key}: {value}" for key, value in self.__dict__.items())
        print(output)
        return output

    @log("Updating project field")
    def update_project_field(self, field, new_data):
        try:
            self.__dict__[field] = new_data
            if validate_project(self):
                print(f"{field} from the project {self[field]} changed to {new_data}.")
                save_update(self)
        except:
            print("Unexpected error")
    
class ProjectManager():
    @log("Adding project")
    def add_project(self, new_project):
        projects = load_data("projects.json")
        if validate_project(new_project):
            projects.append(new_project)
            save_update(projects, "projects.json")
            print("Project added successfully.")
            return True
        else:
            print("Project data is invalid. Project was not added.")
    
    @log("Showing data")
    def show_data(self, field, data_to_find):
        projects = load_data("projects.json")
        if self.find_data(field, data_to_find, projects):
            for project in projects:
                if project[field] == data_to_find:
                    output = "\n".join(f"{key}: {value}" for key, value in project.items())
                    print(output)
                    return output  # Asegúrate de retornar la salida
        else:
            print(f"{field} '{data_to_find}' not found.")
    
    @log("Finding data")
    def find_data(self, field, data, projects):
        for project in projects:
            if project[field] == data:
                return True
        return False
    
    @log("Deleting project")
    def delete_project(self, project_id):
        projects = load_data("projects.json")
        if self.find_data("id", project_id, projects):
            for project in projects:
                if project["id"] == project_id:
                    projects.remove(project)
                    save_update(projects, "projects.json")
                    print("Project deleted successfully.")
                    return True
        else:
            print(f"Project with id {project_id} not found.")
            return False
    

        