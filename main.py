
def saludar(nombre):
    return f"Bienvenido, {nombre}! Esta es la versión estable del proyecto."

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

if __name__ == "__main__":
    print(saludar("Usuario"))
    print(dividir(10, 2))
