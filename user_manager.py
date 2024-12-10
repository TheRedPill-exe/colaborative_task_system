from validation import validate_user as validate
from file_handler import load_data, save_update
from decorators import log

class User():

    def __init__(self, TaskParent, ProjectParent, id, name, email, birth_date, password):
        self.id = id
        self.name = name
        self.email = email
        self.birth_date = birth_date
        self.password = password
        self.tasks = TaskParent.get_user_tasks(id)
        self.projects = ProjectParent.get_user_projects(id)
    
    @log("Updating user data")
    def update_user_field(self, field, data, new_data):
        
        users = load_data("users.json")

        try:
            if self.find_data(field, data, users):
                for user in users:
                    if user.get(field) == data:
                        user[field] = new_data
                        if validate(user):
                            print(f"{field} from the user {user[field]} changed to {new_data}.")
                            save_update(users)
                        else:
                            print("User data is invalid. Changes were not saved.")
                        return
                print(f"{field} {data} not found.")
        except:
            print("Unexpected error")

class UserManager():

    def __init__(self):
        self.users = load_data("users.json")

    @log("Collecting all users data")
    def get_all(self):
        return self.users  # Devuelve la lista de usuarios
    
    @log("Adding user")
    def add_user(self, new_user):
        users = load_data("users.json")
        if validate(new_user):
            users.append(new_user)
            save_update(users, "users.json")
            print("User added successfully.")
            return True
        else:
            print("User data is invalid. User was not added.")

    @log("Showing data")
    def show_data(self, field, data_to_find):
        users = load_data()
        if self.find_data(field, data_to_find, users):
            for user in users:
                if user[field] == data_to_find:
                    output = "\n".join(f"{key}: {value}" for key, value in user.items())
                    print(output)
                    return output  # Asegúrate de retornar la salida
        else:
            print(f"{field} '{data_to_find}' not found.")

    @log("Deleting user")
    def delete_user(self, user_id):
        users = load_data("users.json")
        if self.find_data("id", user_id, users):
            for user in users:
                if user["id"] == user_id:
                    users.remove(user)
                    save_update(users)  # Asegúrate de que esto se ejecute
                    print(f"User with id {user_id} deleted.")
                    return
        else:
            print("User not found.")

