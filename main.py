from task_manager import Task, TaskManager
from user_manager import User, UserManager
from project_manager import Project, ProjectManager
from decorators import log

class CollaborativeTaskSystem():
    def __init__(self):
        self.users = UserManager()
        self.tasks = TaskManager()
        self.projects = ProjectManager()
    
    @log("Creating user")
    def create_user(self, id, name, email, password):
        new_user = User(id, name, email, password)
        return self.users.add_user(new_user)
    
    @log("Creating task")
    def create_task(self, ProjectParent, id, name, description, status, start_date, end_date, priority, users):
        new_task = Task(ProjectParent, id, name, description, status, start_date, end_date, priority, users)
        return self.tasks.add_task(new_task)
    
    @log("Creating project")
    def create_project(self, id, name, description, priority, tasks, users):
        new_project = Project(id, name, description, priority, tasks, users)
        return self.projects.add_project(new_project)
    
    @log("Showing user data")
    def show_user_data(self, field, data_to_find):
        return self.users.show_data(field, data_to_find)
    
    @log("Showing task data")
    def show_task_data(self, field, data_to_find):
        return self.tasks.show_data(field, data_to_find)
    
    @log("Showing project data")
    def show_project_data(self, field, data_to_find):
        return self.projects.show_data(field, data_to_find)
    
    @log("Updating user field")
    def update_user_field(self, field, data, new_data):
        return self.users.update_user_field(field, data, new_data)
    
    @log("Updating task field")
    def update_task_field(self, field, data, new_data):
        return self.tasks.update_task_field(field, data, new_data)
    
    @log("Updating project field")
    def update_project_field(self, field, data, new_data):
        return self.projects.update_project_field(field, data, new_data)
    
    @log("Deleting user")
    def delete_user(self, user_id):
        return self.users.delete_user(user_id)
    
    @log("Deleting task")
    def delete_task(self, task_id):
        return self.tasks.delete_task(task_id)
    
    @log("Deleting project")
    def delete_project(self, project_id):
        return self.projects.delete_project(project_id)
    
    @log("Adding user to task")
    def add_user_to_task(self, task_id, user_id):
        return self.tasks.add_user_to_task(task_id, user_id)