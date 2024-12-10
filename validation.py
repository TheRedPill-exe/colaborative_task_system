def validate(entity, required_fields):

    for field in required_fields:
        if not getattr(entity, field, None):  # Verifica si el atributo existe y no está vacío
            print(f"{field} must be present and cannot be empty.")
            return False
    return True

def validate_user(user):
    required_fields = ["id", "name", "email", "birth_date", "password"]
    return validate(user, required_fields)

def validate_task(task):
    required_fields = ["id", "name", "description", "status", "priority", "deadline"]
    return validate(task, required_fields)

def validate_project(project):
    required_fields = ["id", "name", "description", "priority", "tasks", "users"]
    return validate(project, required_fields)
