def saludar_personalizado(nombre, idioma="es"):
    saludos = {
        "es": f"¡Hola, {nombre}!",
        "en": f"Hello, {nombre}!",
        "fr": f"Bonjour, {nombre}!"
    }
    return saludos.get(idioma, saludos["es"])

if __name__ == "__main__":
    print(saludar_personalizado("María"))
    print(saludar_personalizado("John", "en"))
