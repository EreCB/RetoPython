# DIRECTORIO DE PARTICIPANTES SFWIT ONLINE

directorio = []

print("\nBienvenida al directorio de Skills for Women in Tech en línea\n")
tamaño = int(input("Por favor, indica el número de participantes a registrar: \n"))

for i in range(tamaño):
    print("\nParticipante ", i+1)
    nombre = input("\nNombre completo de participante: ")
    edad = input("Edad: ")
    edad_int = int(edad)
    temas = input("Temas de interés (máx 30 caracteres): ")
    menor_ed = 0

    if edad_int < 18:
        menor_ed = "Menor de edad"
    else:
        menor_ed = "Mayor de edad"

    directorio.append((nombre, edad_int, temas, menor_ed))

print("\nRegistro realizado exitosamente.")
print("\n\nPor favor, elija una opción del sguiente menú:\n")
print("1. Imprimir directorio de participantes")
print("2. Salir")

seleccion = int(input("\nIndique la opción deseada: "))

if seleccion == 1:
    print("\n===========================================================")
    print("= DIRECTORIO DE PARTICIPANTES EN SKILLS FOR WOMEN IN TECH =\n")
    i = 1
    for persona in directorio:
        print("Participante ", i)
        print(". Nombre: ", directorio[i-1][0])
        print(". Edad: ", directorio[i-1][1])
        print(". Temas: ", directorio[i-1][2])
        print(". Menor de edad: ", directorio[i-1][3], ".\n")

        i = i + 1

    print("\n Gracias por consultar el registro de SFWIT")

elif seleccion == 2:
    print("\n Gracias por consultar el sistema de registro de SFWIT!")

else:
    print("\n La opción elegida es incorrecta. Regresa pronto al sistema de registro de SFWIT!")
