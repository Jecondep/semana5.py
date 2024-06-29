python
# Este programa gestiona información básica de una lista de estudiantes

# Creamos una lista vacía para almacenar la información de los estudiantes
lista_estudiantes = []

# Solicitamos al usuario que ingrese los datos de los estudiantes
while True:
    nombre = input("Ingresa el nombre del estudiante (o 'salir' para terminar): ")
    if nombre.lower() == "salir":
        break
    
    edad = int(input("Ingresa la edad del estudiante: "))
    promedio = float(input("Ingresa el promedio del estudiante: "))
    activo = input("¿El estudiante está activo? (si/no): ").lower() == "si"
    
    # Creamos un diccionario con los datos del estudiante
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "promedio": promedio,
        "activo": activo
    }
    
    # Agregamos el diccionario a la lista de estudiantes
    lista_estudiantes.append(estudiante)

# Mostramos la información de los estudiantes
print("\nInformación de los estudiantes:")
for estudiante in lista_estudiantes:
    print("Nombre:", estudiante["nombre"])
    print("Edad:", estudiante["edad"])
    print("Promedio:", estudiante["promedio"])
    print("Activo:", estudiante["activo"])
    print("-" * 30)

# Datos de ejemplo
estudiante1 = {
    "nombre": "Juan",
    "edad": 18,
    "promedio": 8.5,
    "activo": True
}
estudiante2 = {
    "nombre": "María",
    "edad": 19,
    "promedio": 9.2,
    "activo": False
}
estudiante3 = {
    "nombre": "Carlos",
    "edad": 20,
    "promedio": 7.8,
    "activo": True
}

# Agregamos los datos de ejemplo a la lista de estudiantes
lista_estudiantes.append(estudiante1)
lista_estudiantes.append(estudiante2)
lista_estudiantes.append(estudiante3)

# Mostramos la información de los estudiantes nuevamente
print("\nInformación de los estudiantes (con datos de ejemplo):")
for estudiante in lista_estudiantes:
    print("Nombre:", estudiante["nombre"])
    print("Edad:", estudiante["edad"])
    print("Promedio:", estudiante["promedio"])
    print("Activo:", estudiante["activo"])
    print("-" * 30)


En este programa, hemos agregado datos de ejemplo para tres estudiantes: Juan, María y Carlos. Puedes agregar más estudiantes de la misma manera si lo deseas.

Recuerda que estos datos de ejemplo son ficticios y solo se utilizan para ilustrar cómo se vería el programa con información de estudiantes.

Si tienes alguna otra pregunta o necesitas más ayuda, no dudes en preguntar. ¡Estoy aquí para ayudarte en todo lo relacionado con Python!# Online Python - IDE, Editor, Compiler, Interpreter

def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')
