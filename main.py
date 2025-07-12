from funciones import*
import os

print("!!Hola bienvenido!!, por favor seleccione una de las siguientes opciones: ")
print()
participantes = []
puntaje = []
while True:
    mostrar_menu()
    opcion = int(input("Su opcion: "))
    while opcion > 10 or opcion < 0:
        opcion = int(input("Reingrese su opcion (1-10): "))
    if opcion == 1:
        participantes = cargar_participantes()
        print("cargando la lista de los participantes: ")
        print()
        print(participantes)
        print()
    elif opcion == 2:
             puntaje = cargar_puntuacion(participantes)
             print()
    elif opcion == 3:
        if not participantes or not puntaje:
            print("Debe cargar los participantes y las puntuaciones primero (opciones 1 y 2).")
        else: 
            mostrar_puntuaciones(puntaje)
            print()
    elif opcion == 4:
        if not participantes or not puntaje:
            print("Debe cargar los participantes y las puntuaciones primero (opciones 1 y 2).")
        else: 
            mostrar_promedios_mayores_a(puntaje, 4)
            print()
    elif opcion == 5:
        if not participantes or not puntaje:
            print("Debe cargar los participantes y las puntuaciones primero (opciones 1 y 2).")
        else:         
            mostrar_promedios_mayores_a(puntaje, 7)
            print()
    elif opcion == 6:
        if not participantes or not puntaje:
                print("Debe cargar los participantes y las puntuaciones primero (opciones 1 y 2).")
        else:             
            print("mostrando promedios: ")
            mostrar_promedio_por_jurados(puntaje)
            print()
    elif opcion == 7:
        if not participantes or not puntaje:
                print("Debe cargar los participantes y las puntuaciones primero (opciones 1 y 2).")
        else:                        
            print("mostrando al jurado mas estricto: ")
            mostrar_jurado_mas_estricto(puntaje)
            print()
    elif opcion == 8:
        if not participantes or not puntaje:
                print("Debe cargar los participantes y las puntuaciones primero (opciones 1 y 2).")
        else:                        
            print("buscando por nombre.")
            buscar_participante_por_nombre(puntaje)
            print()
    elif opcion == 9:
        if not participantes or not puntaje:
                print("Debe cargar los participantes y las puntuaciones primero (opciones 1 y 2).")
        else:            
            print("buscando el top con mayor puntaje: ")
            lista_top = generar_lista_TOP3(puntaje)
            lista = ordenar_por_promedio_top3(lista_top)
            mostrar_top_3(lista)
            print()
    elif opcion == 10:
        if not participantes or not puntaje:
                print("Debe cargar los participantes y las puntuaciones primero (opciones 1 y 2).")
        else:            
            print("ordenando los participantes en orden alfabetico: ")
            lista = ordenar_participantes_alfabeticamente(puntaje)
            mostrar_participantes(lista)
            print()
    elif opcion == 0:
            print("cerrando el sistema... ")
            break

    else:
            print("ERROR: Opción no válida. Intente nuevamente.")

    input("toque cualquier boton para continuar. ")
    print("regresando.")
    os.system("cls")