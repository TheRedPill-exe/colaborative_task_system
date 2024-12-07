import re

def validate(user):
    fieds = ["id", "name", "email", "birth_date", "password"]
    for field in fieds:
        if not user.get(field):
            print(f"{field} must be present and cannot be empty.")
            return False
    # Si todas las validaciones pasan, retornamos True
    return True

def validate_task(task):
    fieds = ["id", "name", "description", "status", "priority", "deadline"]
    for field in fieds:
        if not task.get(field):
            print(f"{field} must be present and cannot be empty.")
            return False
    # Si todas las validaciones pasan, retornamos True
    return True

def validate_project(project):
    fieds = ["id", "name", "description", "priority", "tasks", "users"]
    for field in fieds:
        if not project.get(field):
            print(f"{field} must be present and cannot be empty.")
            return False
    # Si todas las validaciones pasan, retornamos True
    return True