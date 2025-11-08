# Requerimiento 5: Estructuras de Datos (Diccionarios para almacenamiento, Listas para gestión)

# Usamos un diccionario para almacenar contactos
# La clave es el nombre, y el valor es un diccionario con los detalles
AGENDA: dict = {
    "Carlos": {"telefono": "555-1234", "email": "carlos@ejemplo.com"},
    "Ana": {"telefono": "555-5678", "email": "ana@ejemplo.com"},
    # Usamos tuplas (estructura inmutable) para datos específicos si fuera necesario
    "Juan": {"telefono": "555-9012", "email": "juan@ejemplo.com", "etiquetas": ("amigo", "trabajo")} 
}

def agregar_contacto(nombre: str, telefono: str, email: str):
    # Uso de diccionarios para organizar datos
    if nombre in AGENDA:
        print(f"Advertencia: El contacto {nombre} ya existe y será actualizado.")
    
    AGENDA[nombre] = {"telefono": telefono, "email": email}
    print(f"Contacto {nombre} agregado/actualizado.")

def listar_contactos():
    print("\n--- AGENDA DE CONTACTOS ---")
    # Iteración sobre las claves del diccionario
    nombres: list = list(AGENDA.keys())
    
    if not nombres:
        print("La agenda está vacía.")
        return

    # Iteración sobre una lista de nombres
    for nombre in nombres:
        detalle = AGENDA[nombre]
        print(f"Nombre: {nombre}")
        print(f"  Teléfono: {detalle['telefono']}")
        print(f"  Email: {detalle['email']}")
        # Ejemplo de manejo de un campo opcional (Tupla)
        if 'etiquetas' in detalle:
             print(f"  Etiquetas: {', '.join(detalle['etiquetas'])}")
    print("----------------------------")

if __name__ == "__main__":
    agregar_contacto("Sofia", "555-4321", "sofia@ejemplo.com")
    listar_contactos()