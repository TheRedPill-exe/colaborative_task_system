import os

# Directorio raíz del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
filename = os.path.join(BASE_DIR, "colaborative_task_system", "data", "log.txt")

# Creando un decorador para el logeo de las funciones
def log(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            # Usando la variable global filename
            with open(filename, "a") as file:
                file.write(f"{message} - {func.__name__} executed with args: {args}, and kwargs: {kwargs}\n")
            return result
        return wrapper
    return decorator

@log("Finding data")
def find_data(field, data_to_find, data):
    for obj in data:
        if obj.get(field) == data_to_find:
            return True
    return False
