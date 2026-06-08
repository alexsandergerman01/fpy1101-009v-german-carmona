def obtener_entero_positivo(mensaje_input, mensaje_error):
    """
    Solicita un número al usuario iterando hasta que ingrese un entero positivo válido.
    Muestra un mensaje de error personalizado en caso de fallar.
    """
    while True:
        entrada = input(mensaje_input)
        try:
            valor = int(entrada)
            if valor > 0:
                return valor
            else:
                print(mensaje_error)
        except ValueError:
            print(mensaje_error)

def sistema_hospital():
    print("--- Hospital Central Metropolitano: Registro de Médicos ---")

    error_cantidad = "¡Registro médico inválido! Ingresa un entero positivo para continuar."
    cantidad_medicos = obtener_entero_positivo("¿Cuántos médicos deseas registrar?: ", error_cantidad)
    
    especialistas_senior = 0
    residentes_junior = 0
    
    for i in range(cantidad_medicos):
        print(f"--- Registrando Médico {i + 1} de {cantidad_medicos} ---")
        
        while True:
            nombre = input("Ingresa el Nombre Profesional (min. 6 caracteres, sin espacios): ")
            if len(nombre) >= 6 and ' ' not in nombre:
                break
            else:
                print("Error: El nombre debe tener al menos 6 caracteres y no incluir espacios.")
        
        error_experiencia = "¡Error clínico! Ingresa un número entero positivo para la experiencia."
        experiencia = obtener_entero_positivo(f"Años de experiencia clínica para {nombre}: ", error_experiencia)
        
        if experiencia > 5:
            especialistas_senior += 1
            print(f" {nombre} clasificado(a) exitosamente como: Especialista Senior.")
        else:
            residentes_junior += 1
            print(f" {nombre} clasificado(a) exitosamente como: Residente Junior.")
            
    print("="*60)
    print("RESUMEN FINAL DE REGISTRO")
    print("="*60)
    print(f"¡El hospital cuenta con {especialistas_senior} Especialistas Senior y {residentes_junior} Residentes Junior! ¡Sistema listo para operar!")

if __name__ == "__main__":
    sistema_hospital()
