import csv
from datetime import datetime, date

afiliados = [] 
ids = set()    

# Identificacion 
def leer_identificacion(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor.lower() == "salir":  
            return None
        if not valor.isdigit():
            print("Debes ingresar solo numeros.")
            continue
        if len(valor) != 10:
            print("La identificación debe tener exactamente 10 dígitos.")
            continue
        return valor

# Validar Fecha
def leer_fecha(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor.lower() == "salir":
            return None
        try:
            return datetime.strptime(valor, "%d/%m/%Y").date()
        except ValueError:
            print("Formato invalido. Usar dd/mm/aaaa.")

# Plan Afiliados
def leer_plan(mensaje):
    while True:
        valor = input(mensaje).upper().strip()
        if valor.lower() == "salir":
            return None
        if valor in ["A", "B", "C"]:
            return valor
        print("Debe ser A, B o C.")

# Validar genero 
def leer_genero(mensaje):
    while True:
        valor = input(mensaje).upper().strip()
        if valor.lower() == "salir":
            return None
        if valor in ["M", "F"]:
            return valor
        print("El genero debe ser M o F.")

# Validar Edad
def calcular_edad(fecha_nacimiento):
    hoy = date.today()
    return hoy.year - fecha_nacimiento.year - (
        (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day)
    )

# Registro de Afiliados
def registrar_afiliado():
    print("\nRegistro de Afiliado")
    id_afiliado = leer_identificacion("Numero de identificacion: ")
    if id_afiliado is None:
        print("Registro cancelado.")
        return
    if id_afiliado in ids:
        print("Este numero de identificación ya esta registrado.")
        return

    nombres = input("Nombres: ").strip()
    apellidos = input("Apellidos: ").strip()

    fecha_nac = leer_fecha("Fecha de nacimiento (dd/mm/aaaa): ")
    if fecha_nac is None:
        print("Registro cancelado.")
        return

    plan = leer_plan("Plan de afiliación (A | B | C): ")
    if plan is None:
        print("Registro cancelado.")
        return

    genero = leer_genero("Género ( M / F ): ")
    if genero is None:
        print("Registro cancelado.")
        return

    correo = input("Correo electronico: ").strip()

    afiliado = {
        "id": id_afiliado,
        "nombres": nombres,
        "apellidos": apellidos,
        "fecha_nacimiento": fecha_nac,
        "plan": plan,
        "genero": genero,
        "correo": correo,
    }
    afiliados.append(afiliado)
    ids.add(id_afiliado)
    print("Afiliado registrado correctamente.")

# Listar Afiliados
def listar_afiliados():
    print("\n Lista de Afiliados")
    for a in sorted(afiliados, key=lambda x: x["apellidos"]):
        print(f"{a['id']} - {a['nombres']} {a['apellidos']} - Plan {a['plan']}")

# Buscar Afiliados
def buscar_afiliado():
    print("\n Buscar Afiliado")
    id_buscar = leer_identificacion("Ingrese numero de identificacion: ")
    if id_buscar is None:
        print("Busqueda cancelada.")
        return
    for a in afiliados:
        if a["id"] == id_buscar:
            print(a)
            return
    print("Afiliado no encontrado.")

# Estadisticas Rapidas
def estadisticas():
    print("\n Estadisticas Rapidas ")
    
    conteo_planes = {"A": 0, "B": 0, "C": 0}
    for a in afiliados:
        conteo_planes[a["plan"]] += 1
    print("Afiliados por plan:", conteo_planes)

    edades_genero = {"M": [], "F": []}
    for a in afiliados:
        edad = calcular_edad(a["fecha_nacimiento"])
        if a["genero"].upper() in edades_genero:
            edades_genero[a["genero"].upper()].append(edad)

    for g, lista in edades_genero.items():
        if lista:
            promedio = sum(lista) / len(lista)
            print(f"Promedio de edad genero {g}: {promedio:.1f} años")

    if afiliados:
        edades = [calcular_edad(a["fecha_nacimiento"]) for a in afiliados]
        print(f"El afiliado mas joven: {min(edades)} años")
        print(f"El afiliado mas Mayor/Adulto: {max(edades)} años")

# Exportacion a csv
def exportar_csv():
    with open("afiliados.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Nombres", "Apellidos", "FechaNacimiento", "Plan", "Genero", "Correo"])
        for a in afiliados:
            writer.writerow([
                a["id"], a["nombres"], a["apellidos"],
                a["fecha_nacimiento"].strftime("%d/%m/%Y"),
                a["plan"], a["genero"], a["correo"]
            ])
    print("Datos exportados a afiliados.csv")

# Menu Principal
def menu():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Registrar afiliado")
        print("2. Listar afiliados")
        print("3. Buscar afiliado por ID")
        print("4. Estadísticas rápidas")
        print("5. Exportar CSV")
        print("6. Salir")

        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            registrar_afiliado()
        elif opcion == "2":
            listar_afiliados()
        elif opcion == "3":
            buscar_afiliado()
        elif opcion == "4":
            estadisticas()
        elif opcion == "5":
            exportar_csv()
        elif opcion == "6":
            exportar_csv()
            print(f"Programa finalizado. Total afiliados guardados: {len(afiliados)}")
            break
        else:
            print("Opción no válida.")

menu()
