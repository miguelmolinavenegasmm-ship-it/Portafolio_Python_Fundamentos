# Requerimiento 4: Sentencias Iterativas (Bucles for y while)

def generar_tabla_for(base: int, limite: int):
    print(f"\n--- Tabla de Multiplicar del {base} (usando FOR) ---")
    # Bucle for para iterar un rango conocido
    for i in range(1, limite + 1):
        resultado = base * i
        print(f"{base} x {i} = {resultado}")

def calcular_factorial_while(n: int):
    print(f"\n--- Cálculo de Factorial de {n} (usando WHILE) ---")
    # Inicialización de variables de control
    factorial: int = 1
    contador: int = 1
    
    # Bucle while para repetir hasta que se cumpla una condición
    while contador <= n:
        factorial = factorial * contador
        contador = contador + 1 # Incremento
        
    print(f"El factorial de {n} es: {factorial}")

if __name__ == "__main__":
    num_base = 7
    limite = 10
    num_factorial = 5
    
    generar_tabla_for(num_base, limite)
    calcular_factorial_while(num_factorial)
