# saludos.py
from utils.printer import print_message

def saludo(name: str):
    """Genera un saludo simple."""
    message = f"¡Hola, {name}!"
    print_message(message)