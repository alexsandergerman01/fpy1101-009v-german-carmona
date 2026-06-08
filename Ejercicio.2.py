def sistema_biblioteca():
    capacidad_maxima = 120
    libros_disponibles = 120
    prestamos_activos = 0
    transacciones_prestamo = 0
    
    print("¡Bienvenido al sistema de gestión de préstamos de la Biblioteca Central!\n")
    
    while True:
        print("===")
        print("MENÚ PRINCIPAL")
        print("===")
        print("1. Libros disponibles")
        print("2. Realizar préstamo")
        print("3. Devolver préstamo")
        print("4. Historial de préstamos")
        print("5. Salir")
        
        opcion = input("\nSelecciona una opción (1-5): ")
        
        if opcion == '1':
            print(f"Libros actualmente libres en la biblioteca: {libros_disponibles}")
            
        elif opcion == '2':
            try:
                cantidad = int(input("\n¿Cuántos libros deseas pedir prestados / reservar?: "))
                if cantidad <= 0:
                    print("Error: La cantidad solicitada debe ser mayor a 0.")
                elif cantidad > libros_disponibles:
                    print(f"Error: No hay suficiente capacidad. Solo quedan {libros_disponibles} libros disponibles.")
                else:
                    libros_disponibles -= cantidad
                    prestamos_activos += cantidad
                    transacciones_prestamo += 1
                    print(f"Préstamo exitoso. Has retirado {cantidad} libro(s).")
            except ValueError:
                print("Error: Por favor, ingresa un número entero válido.")
                
        elif opcion == '3':
            try:
                cantidad = int(input("\n¿Cuántos libros deseas devolver?: "))
                if cantidad <= 0:
                    print("Error: Debes devolver al menos 1 libro.")
                elif (libros_disponibles + cantidad) > capacidad_maxima:
                    limite_devolucion = capacidad_maxima - libros_disponibles
                    print(f"Error: La cantidad supera el stock máximo. Solo puedes devolver hasta {limite_devolucion} libro(s).")
                else:
                    libros_disponibles += cantidad
                    prestamos_activos -= cantidad
                    print(f"Devolución exitosa. Has devuelto {cantidad} libro(s).")
            except ValueError:
                print("Error: Por favor, ingresa un número entero válido.")
                
        elif opcion == '4':
            print("HISTORIAL DE PRÉSTAMOS")
            print(f"* Libros actualmente en préstamo (activos): {prestamos_activos}")
            print(f"* Total de operaciones de préstamo realizadas en esta sesión: {transacciones_prestamo}")
            
        elif opcion == '5':
            print("Gracias por utilizar nuestro software, hasta la próxima.")
            break
            
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 5.")
        
        print("-"*50)

if __name__ == "__main__":
    sistema_biblioteca()

