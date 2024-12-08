# utils.py

def input_int(prompt):
    """
    Solicita un número entero al usuario y valida la entrada.
    :param prompt: Mensaje para el usuario.
    :return: Un número entero válido.
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Por favor, ingresa un número entero válido.")


def input_float(prompt):
    """
    Solicita un número flotante al usuario y valida la entrada.
    :param prompt: Mensaje para el usuario.
    :return: Un número flotante válido.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Por favor, ingresa un número válido.")
