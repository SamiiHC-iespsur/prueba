# saludos.py
from utils.printer import print_message

def saludo-informal(name: str):
    """Genera un saludo informal."""
    message = f"¡Hey {name}! ¿Qué tal?"

def saludo-formal(name: str):
    """Genera un saludo formal."""
    message = f"Buenos días, {name}. Espero que tengas un excelente día."
    print_message(message)

def greet_in_english(name: str):
    """Genera un saludo simple en inglés."""
    message = f"Hello, {name}!"
    print_message(message)