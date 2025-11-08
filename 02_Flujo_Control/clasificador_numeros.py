# Requerimiento 3: Sentencias Condicionales para Control de Flujo

def clasificar_numero(numero: int):
    # Uso de sentencias condicionales para la toma de decisiones
    if numero > 0:
        print(f"El número {numero} es POSITIVO.")
    elif numero < 0:
        print(f"El número {numero} es NEGATIVO.")
    else:
        # El caso final
        print(f"El número es CERO.")

if __name__ == "__main__":
    try:
        # Entrada y conversión a entero
        valor = int(input("Ingrese un número entero: "))
        clasificar_numero(valor)
    except ValueError:
        print("ERROR: Ingrese solo números enteros.")