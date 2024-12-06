import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Directorio raíz del proyecto
filename = os.path.join(BASE_DIR, "colaborative_task_system\\" "data", "log.txt")
#creando un decorador para el logeo de las funciones
def log(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, "a") as file:
                file.write(f"{message} - {func.__name__} executed with args: {args}, and kwargs: {kwargs}\n")
            return result
        return wrapper
    return decorator

@log("Finding data")
def find_data(field, data_to_find, data):
    for object in data:
        if object.get(field) == data_to_find:
            return True
    return False

