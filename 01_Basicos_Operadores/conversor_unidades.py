# Requerimiento 1 & 2: Variables, Operadores y Tipos de Datos
# Ejemplo: Conversor de unidades de temperatura (Celsius a Fahrenheit)

def conversor_temperatura():
    # Distinguir Tipos de Datos: Usamos float para la temperatura
    celsius: float = 0.0
    
    # Solicitar información (Tipo string/cadena)
    print("--- Conversor de Temperatura (C a F) ---")
    entrada = input("Ingrese la temperatura en Celsius (ej: 25.5): ")

    try:
        # Conversión explícita a float
        celsius = float(entrada)
        
        # Uso de Operadores: Multiplicación, división y suma
        fahrenheit: float = (celsius * 9/5) + 32
        
        # Imprimir resultados
        print(f"\nTemperatura Ingresada: {celsius}°C")
        # Sentencia básica: Uso de f-strings
        print(f"Temperatura Convertida: {fahrenheit}°F")
        
    except ValueError:
        # Manejo simple de error de tipo de dato
        print("ERROR: El valor ingresado no es un número válido.")

if __name__ == "__main__":
    conversor_temperatura()