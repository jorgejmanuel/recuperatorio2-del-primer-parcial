#MOSTRAR MENU
def mostrar_menu():
    print("1. cargar nombres\n2. cargar puntuacion\n3. mostrar puntuaciones\n4. ver participantes con promedio mayor a 4\n5. ver participantes con promedio mayor a 7 \n6. ver promedio de jurados\n7. ver jurado más estricto\n8. buscar participante por nombre\n9. mostar el top 3 con mayor promedio\n10. ordenar participantes alfabeticamente\n0. cerrar sistema. ")
#VERIFICACION POR ASCII
def contiene_numeros(cadena) -> bool:
    for caracter in cadena:
        valor = ord(caracter)
        if valor >= 48 and valor <= 57:
            return True
    return False
#PROMEDIO
def calcular_promedio(puntos: list) -> float:
    total = 0
    for p in puntos:
        total += p
    return total / len(puntos)
#CARGA DE DATOS
def cargar_participantes():
    participantes = [None] * 5
    for i in range(5):
        nombre = input(f"Ingrese el nombre del participante {i+1}: ")
        while len(nombre) < 3 or contiene_numeros(nombre):
            if len(nombre) < 3:
                print("Nombre inválido. Debe tener al menos 3 caracteres.")
            if contiene_numeros(nombre):
                print("Nombre inválido. No debe contener números.")
            nombre = input(f"Reingrese el nombre del participante {i+1}: ")
        participantes[i] = nombre
    return participantes

def cargar_puntuacion(participantes) -> list:
    puntos_de_participante = []
    for nombre_participante in participantes:
        print(f"ingrese la puntuacion del participante {nombre_participante}...")
        puntaje = []
        for j in range (1, 4):
            nota = int (input(f"ingresar la puntuacion del jurado {j} (1-10): "))
            print()
            while nota < 1 or nota > 10:
                print("INGRESAR UN NUMERO VALIDO")
                nota = int(input(f"reingrese la puntuacion del jurado {j} (1-10): "))
            puntaje += [nota]
        puntos_de_participante += [[nombre_participante, puntaje]]
    return puntos_de_participante
#MUESTRA DE DATOS
def mostrar_puntuaciones(participantes: list):
    print("\nInformacion de cada participante:\n")
    for participante in participantes:
        nombre = participante[0]
        puntos = participante[1]
        print(f"nombre del participante: {nombre}")
        for i in range(len(puntos)):
            print(f"puntaje del jurado {i+1}: {puntos[i]}")
        promedio = calcular_promedio(puntos)
        print(f"promedio: {promedio:.2f}\n")

def mostrar_promedios_mayores_a(puntos_de_participante: list, promedio_requerido: float):
    print(f"\nParticipantes con un promedio superior a {promedio_requerido}:\n")
    bandera = False
    for participante in puntos_de_participante:
        nombre = participante[0]
        puntos = participante[1]
        promedio = calcular_promedio(puntos)
        if promedio > promedio_requerido:
            print(f"{nombre} promedio: {promedio:.2f}\n")
            bandera = True
    if not bandera:
        print("NO HAY CONCURSANTE CON ESE PROMEDIO.")

def mostrar_promedio_por_jurados(puntos_de_participantes):
    print("\nPromedio de puntuaciones por jurado:\n")
    total_participantes = len(puntos_de_participantes)
    total_jurados = len(puntos_de_participantes[0][1])
    for i in range(total_jurados):
        suma = 0
        for participante in puntos_de_participantes:
            suma += participante[1][i]
        promedio = suma / total_participantes
        print(f"Jurado {i + 1}: {promedio:.2f}")

def mostrar_jurado_mas_estricto(puntos_de_participantes):
    total_participantes = len(puntos_de_participantes)
    total_jurados = len(puntos_de_participantes[0][1])
    promedio_mas_bajo = None
    indice_estricto = -1
    for i in range(total_jurados):
        suma = 0
        for participante in puntos_de_participantes:
            suma += participante[1][i]
        promedio = suma / total_participantes
        if promedio_mas_bajo is None or promedio < promedio_mas_bajo:
            promedio_mas_bajo = promedio
            indice_estricto = i
    print(f"\nEl jurado mas estricto: Jurado {indice_estricto + 1} (promedio {promedio_mas_bajo:.2f})")

#BUSCAR PARTICIPANTE POR NOMBRE
def buscar_participante(puntos_participantes: list, nombre_buscado: str):
    for participante in puntos_participantes:
        if participante[0] == nombre_buscado:
            return participante
    return None

def mostrar_datos_participante(participante: list):
    nombre = participante[0]
    puntajes = participante[1]
    print(f"Nombre: {nombre}")
    for i in range(len(puntajes)):
        print(f"Puntaje del jurado {i+1}: {puntajes[i]}")
    promedio = calcular_promedio(puntajes)
    print(f"Promedio: {promedio:.2f}")

def buscar_participante_por_nombre(puntos_participantes: list):
    nombre = input("Ingrese el nombre del participante a buscar: ")
    participante = buscar_participante(puntos_participantes, nombre)
    print()
    if participante is not None:
        print("Se ha encontrado al participante. Mostrando sus datos:")
        mostrar_datos_participante(participante)
        print()
    else:
        print("No se encontró el participante. Verifique el nombre ingresado.")
#MOSTRAR TOP 3
def generar_lista_TOP3(puntos_de_participantes: list) -> list:
    lista = []
    for i in range(len(puntos_de_participantes)):
        nombre = puntos_de_participantes[i][0]
        puntajes = puntos_de_participantes[i][1]
        promedio = calcular_promedio(puntajes)
        lista = lista + [[nombre, promedio]]
    return lista

def ordenar_por_promedio_top3(lista: list) -> list:
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j][1] < lista[j + 1][1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def mostrar_top_3(lista: list):
    print("\nTop 3 participantes con mayor puntaje promedio:\n")
    limite = min(3, len(lista))
    for i in range(limite):
        nombre = lista[i][0]
        promedio = lista[i][1]
        print(f"{i + 1}. {nombre} - Promedio: {promedio:.2f}")

#ORDENAR ALFEBETICAMENTE
def ordenar_participantes_alfabeticamente(puntos_de_participantes: list) -> list:
    lista = [0] * len(puntos_de_participantes)
    for i in range(len(puntos_de_participantes)):
        lista[i] = [puntos_de_participantes[i][0], puntos_de_participantes[i][1]]

    participantes = len(lista)
    for i in range(participantes - 1):
        for j in range(participantes - i - 1):
            if lista[j][0] > lista[j + 1][0]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def mostrar_participantes(puntos_de_participantes: list):
    print("\nParticipantes ordenados alfabéticamente:\n")
    for nombre, puntajes in puntos_de_participantes:
        promedio = calcular_promedio(puntajes)
        print(f"{nombre}: Puntajes = {puntajes}, Promedio = {promedio:.2f}")