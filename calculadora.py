def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir por cero"

# Menú de la calculadora
while True:
    print("Calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Seleccione una opción (1/2/3/4/5): ")

    if opcion == "5":
        print("Saliendo de la calculadora. ¡Hasta luego!")
        break

    if opcion in ("1", "2", "3", "4"):
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == "1":
            print("Resultado: ", suma(num1, num2))
        elif opcion == "2":
            print("Resultado: ", resta(num1, num2))
        elif opcion == "3":
            print("Resultado: ", multiplicacion(num1, num2))
        elif opcion == "4":
            print("Resultado: ", division(num1, num2))
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
