import logging

logging.basicConfig(level=logging.INFO)

def dividir_seguro(a, b):
    try:
        result = a / b
        logging.info(f"División exitosa: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logging.error(f"Intento de división por cero: {a} / {b}")
        return "Error: No se puede dividir por cero"

if __name__ == "__main__":
    print(dividir_seguro(10, 2))
    print(dividir_seguro(5, 0))
