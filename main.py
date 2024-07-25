
def saludar(nombre):
    return f"Hola, {nombre}! Estamos probando una nueva versión del saludo."

def dividir(a, b):
    if b == 0:
        return "Error: División por cero no permitida"
    return a / b

if __name__ == "__main__":
    print(saludar("Tester"))
    print(dividir(10, 2))
    print(dividir(5, 0))
