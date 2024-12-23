from validation import validate_task
from file_handler import load_data, save_update
from decorators import log
class Task():

    @log("Creating task")
    def __init__(self, ProjectParent, id, name, description, status, start_date, end_date, priority, users):
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.start_date = start_date
        self.end_date = end_date
        self.priority = priority
        self.users = users
        self.project = ProjectParent.project_id

    @log("Collecting task data")
    def show_task(self):
        output = "\n".join(f"{key}: {value}" for key, value in self.__dict__.items())
        print(output)
        return output
    
    @log("Updating task field")
    def update_task_field(self, field, new_data):
        try:
            self.__dict__[field] = new_data
            if validate_task(self): 
                print(f"{field} from the task {self[field]} changed to {new_data}.")
                save_update(self)
        except:
            print("Unexpected error")

    @log("Adding user to task")
    def add_user(self, user_id):
        self.users.append(user_id)
        save_update(self)
        print(f"User {user_id} added to the task.")
    
    @log("Removing user from task")
    def remove_user(self, user_id):
        self.users.remove(user_id)
        save_update(self)
        print(f"User {user_id} removed from the task.")

    @log("collecting users in task")
    def show_users(self):
        return self.users

    def __str__(self):
        return f"Task {self.id}: {self.name}"
    

class TaskManager():
    def __init__(self):
        self.tasks = load_data("tasks.json")
        
    @log("Adding task")
    def add_task(self, new_task):
        tasks = load_data("tasks.json")
        if validate_task(new_task):
            tasks.append(new_task)
            save_update(tasks)
            print("Task added successfully.")
            return True
        else:
            print("Task data is invalid. Task was not added.")
    
    @log("Getting all data")
    def get_all(self):
        return self.tasks  # Devuelve la lista de tareas
    
    @log("showing tasks")
    def show_tasks(self):
        tasks = load_data()
        for task in tasks:
            output = "\n".join(f"{key}: {value}" for key, value in task.items())
            print(output)
        return output

    @log("Finding data from the tasks")
    def find_data(self, field, data_to_find, tasks):
        for task in tasks:
            if task.get(field) == data_to_find:
                return True
        return False

    @log("Updating task field")
    def update_task_field(self, field, data, new_data):
        tasks = load_data("tasks.json")
        try:
            if self.find_data(field, data, tasks):
                for task in tasks:
                    if task.get(field) == data:
                        task[field] = new_data
                        if validate_task(task):
                            print(f"{field} from the task {task[field]} changed to {new_data}.")
                            save_update(tasks)
                        else:
                            print("Task data is invalid. Changes were not saved.")
                        return
                print(f"{field} {data} not found.")
        except:
            print("Unexpected error")
            
    @log("Geting user tasks")
    def get_user_tasks(self, user_id):
        tasks = load_data("tasks.json")
        user_tasks = [task for task in tasks if user_id in task["users"]]
        return user_tasks

