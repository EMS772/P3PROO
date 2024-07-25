# main.py en la rama dev

# Importamos la nueva funcionalidad
from nueva_funcionalidad import saludar

# Importamos la función de corrección de error
from correccion_error import dividir

def main():
    # Probamos la nueva funcionalidad
    print(saludar("Desarrollador"))
    
    # Probamos la función corregida
    print(dividir(10, 2))
    print(dividir(5, 0))
    
    # Aquí podrías añadir más funciones en desarrollo
    print("Otras funcionalidades en desarrollo...")

if __name__ == "__main__":
    main()
