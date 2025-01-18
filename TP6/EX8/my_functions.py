import logging

class NegativeAgeError(Exception):
    """Exception levée lorsque l'âge est négatif."""
    pass

def log_error(message):
    logging.error(message)

def safe_division(a, b):
    if b == 0:
        raise ZeroDivisionError("La division par zéro n'est pas autorisée.")
    return a / b

def convert_to_int(value):
    return int(value)

def set_age(age):
    if age < 0:
        raise NegativeAgeError("L'âge ne peut pas être négatif.")
    return age

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
