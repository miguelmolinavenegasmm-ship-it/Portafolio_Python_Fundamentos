# Requerimiento 6: Modularización con Funciones para Reutilización de Código

PI: float = 3.14159

# Función 1: Cálculo del área de un rectángulo
def calcular_area_rectangulo(largo: float, ancho: float) -> float:
    # Retorna el resultado
    return largo * ancho

# Función 2: Cálculo del área de un triángulo
def calcular_area_triangulo(base: float, altura: float) -> float:
    # Reutilización de lógica (operadores)
    return (base * altura) / 2

# Función 3: Cálculo del área de un círculo
def calcular_area_circulo(radio: float) -> float:
    # Uso de una constante global
    return PI * (radio ** 2)

def mostrar_calculos():
    # Uso de la función 1
    area_rect = calcular_area_rectangulo(10.5, 5.0)
    print(f"Área del Rectángulo (10.5x5.0): {area_rect:.2f}")

    # Uso de la función 2
    area_tri = calcular_area_triangulo(8.0, 4.0)
    print(f"Área del Triángulo (base 8, altura 4): {area_tri:.2f}")

    # Uso de la función 3
    area_circ = calcular_area_circulo(3.0)
    print(f"Área del Círculo (radio 3): {area_circ:.2f}")

if __name__ == "__main__":
    mostrar_calculos()