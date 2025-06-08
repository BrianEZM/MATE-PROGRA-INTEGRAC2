AÑO_ACTUAL = 2025
INTEGRANTES = ["Brian Zapata Marin", "Matias Almeida"]

# FUNCIONES DE OPERACIONES CON DNIS
def generar_conjunto_digitos_dni(dni_str):
    """
    Genera un conjunto de dígitos únicos a partir de una cadena de DNI.
    Args:
        dni_str (str): El DNI como cadena de texto.
    Returns:
        set: Un conjunto con los dígitos únicos del DNI.
    """
    return set(int(d) for d in dni_str if d.isdigit())


def calcular_frecuencia_digitos(dni_str):
    """
    Calcula la frecuencia de cada dígito (0-9) en un DNI.
    Args:
        dni_str (str): El DNI como cadena de texto.
    Returns:
        dict: Un diccionario donde la clave es el dígito y el valor es su frecuencia.
    """
    frecuencias = {str(i): 0 for i in range(10)}  # Inicializa todas las frecuencias en 0
    for digito in dni_str:
        if digito.isdigit():
            frecuencias[digito] += 1
    return frecuencias


def sumar_digitos_dni(dni_str):
    """
    Suma todos los dígitos de un DNI.
    Args:
        dni_str (str): El DNI como cadena de texto.
    Returns:
        int: La suma total de los dígitos.
    """
    return sum(int(d) for d in dni_str if d.isdigit())


def realizar_operaciones_dni(lista_dni_str):
    """
    Orquesta y muestra los resultados de todas las operaciones relacionadas con los DNIs.
    Args:
        lista_dni_str (list): Una lista de cadenas de texto con los DNIs.
    """
    print("\n" + "=" * 20)
    print("OPERACIONES CON DNIs")
    print("=" * 20)

    conjuntos_dnis = []
    print("\nGeneración de Conjuntos de Dígitos Únicos")
    for i, dni_str in enumerate(lista_dni_str):
        conjunto = generar_conjunto_digitos_dni(dni_str)
        conjuntos_dnis.append(conjunto)
        print(f"DNI {dni_str} ({INTEGRANTES[i]}) -> Conjunto {i+1}: {conjunto}")

    # Cálculo y visualización de operaciones de conjuntos
    print("\nOperaciones de Conjuntos")

    if len(conjuntos_dnis) >= 2:
        # Unión de todos los conjuntos
        union_total = set()
        for c in conjuntos_dnis:
            union_total = union_total.union(c)
        print(f"Unión de todos los conjuntos: {union_total}")

        # Intersección de todos los conjuntos
        # Se toma una copia del primer conjunto para iniciar la intersección
        interseccion_total = conjuntos_dnis[0].copy()
        for i in range(1, len(conjuntos_dnis)):
            interseccion_total = interseccion_total.intersection(conjuntos_dnis[i])
        print(f"Intersección de todos los conjuntos: {interseccion_total}")

        # Diferencias y Diferencias Simétricas (entre pares)
        print("\nDiferencias y Diferencias Simétricas (Entre Pares)")
        for i in range(len(conjuntos_dnis)):
            for j in range(i + 1, len(conjuntos_dnis)):
                conjunto1 = conjuntos_dnis[i]
                conjunto2 = conjuntos_dnis[j]

                print(f"\nEntre {INTEGRANTES[i]} ({lista_dni_str[i]}) y {INTEGRANTES[j]} ({lista_dni_str[j]}):")
                print(f"  Diferencia (Conjunto {i + 1} - Conjunto {j + 1}): {conjunto1.difference(conjunto2)}")
                print(f"  Diferencia (Conjunto {j + 1} - Conjunto {i + 1}): {conjunto2.difference(conjunto1)}")
                print(f"  Diferencia Simétrica (Conjunto {i + 1} Δ Conjunto {j + 1}): {conjunto1.symmetric_difference(conjunto2)}")
    else:
        print("Se necesitan al menos 2 DNI para realizar operaciones de unión, intersección y diferencias entre pares.")
        if conjuntos_dnis:  # Si hay al menos un DNI
            print(f"Conjunto del DNI único: {conjuntos_dnis[0]}")

    # Conteo de frecuencia de cada dígito y Suma total de dígitos
    print("\nFrecuencia y Suma de Dígitos por DNI:")
    for i, dni_str in enumerate(lista_dni_str):
        frecuencias = calcular_frecuencia_digitos(dni_str)
        suma = sumar_digitos_dni(dni_str)
        print(f"\nDNI de {INTEGRANTES[i]} ({dni_str}):")
        print(f"  Frecuencia de dígitos: {frecuencias}")
        print(f"  Suma total de dígitos: {suma}")

    # Evaluación de condiciones lógicas (condicionales)
    print("\nEvaluación de Condiciones Lógicas (DNIs):")

    # CONDICION1: Si algún dígito aparece en todos los conjuntos
    if len(conjuntos_dnis) > 0:
        if len(conjuntos_dnis) >= 2:
            interseccion_todos = conjuntos_dnis[0].copy()
            for i in range(1, len(conjuntos_dnis)):
                interseccion_todos = interseccion_todos.intersection(conjuntos_dnis[i])
        elif len(conjuntos_dnis) == 1:
            interseccion_todos = conjuntos_dnis[0]
        else:
            interseccion_todos = set()

        if interseccion_todos:
            print(
                f"CONDICION1: Dígitos compartidos: Los siguientes dígitos aparecen en todos los conjuntos: {interseccion_todos}")
        else:
            print("CONDICION1: Ningún dígito aparece en todos los conjuntos.")
    else:
        print("CONDI1CION: No hay conjuntos de DNI para evaluar dígitos compartidos.")

    # CONDICION2: Si algún conjunto tiene más de 6 elementos (ejemplo original de consigna)
    diversidad_alta = False
    for i, conjunto in enumerate(conjuntos_dnis):
        if len(conjunto) > 6:
            print(
                f"CONDICION2: Diversidad numérica alta: El conjunto de la Persona {i + 1} tiene {len(conjunto)} elementos.")
            diversidad_alta = True
    if not diversidad_alta and len(conjuntos_dnis) > 0:
        print("CONDICION2: Ningún conjunto tiene más de 6 elementos (diversidad numérica no alta).")
    elif len(conjuntos_dnis) == 0:
        print("CONDICION2: No hay conjuntos de DNI para evaluar diversidad numérica.")

    # CONDICION3: Si la intersección entre todos los conjuntos tiene exactamente un elemento
    if len(conjuntos_dnis) >= 1:
        if len(interseccion_todos) == 1:
            digito_representativo = list(interseccion_todos)[0]
            print(
                f"CONDICION3: Dígito representativo del grupo: La intersección de todos los conjuntos es: {{{digito_representativo}}}")
        else:
            print(
                f"CONDICION3: La intersección de todos los conjuntos no tiene exactamente un elemento. (Elementos: {interseccion_todos})")
    else:
        print("CONDICION3: No hay conjuntos de DNI para evaluar intersección.")

    # CONDICION4: Si ninguno de los conjuntos de DNI contiene el dígito 0
    grupo_sin_ceros = True
    if not conjuntos_dnis:
        grupo_sin_ceros = False  # No hay conjuntos, la condición no aplica
    else:
        for i, conjunto in enumerate(conjuntos_dnis):
            if 0 in conjunto:
                grupo_sin_ceros = False
                print(
                    f"CONDICION4: El grupo NO es 'sin ceros' porque el conjunto de {INTEGRANTES[i]} contiene el "
                    f"dígito 0.")
                break

    if grupo_sin_ceros and conjuntos_dnis:  # Si la bandera sigue True y hay conjuntos
        print("CONDICION4: Grupo 'sin ceros': Ninguno de los conjuntos de DNI contiene el dígito 0.")
    elif not conjuntos_dnis:
        print("CONDICION4: No hay conjuntos de DNI para evaluar la condición 'sin ceros'.")


# FUNCIONES DE OPERACIONES CON AÑOS DE NACIMIENTO
def es_bisiesto(year):
    """
    Determina si un año es bisiesto.
    Un año es bisiesto si es divisible por 4, excepto si es divisible por 100
    pero no por 400.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def calcular_edad(year_nacimiento, current_year=AÑO_ACTUAL):
    """
    Calcula la edad aproximada dado un año de nacimiento y el año actual.
    Args:
        year_nacimiento (int): El año de nacimiento.
        current_year (int): El año actual (por defecto usa AÑO_ACTUAL del servicio).
    Returns:
        int: La edad calculada.
    """
    return current_year - year_nacimiento


def realizar_operaciones_anios(lista_anios_nacimiento):
    """
    Orquesta y muestra los resultados de todas las operaciones relacionadas con los años de nacimiento.
    Args:
        lista_anios_nacimiento (list): Una lista de números enteros con los años de nacimiento.
    """
    print("\n" + "=" * 35)
    print("OPERACIONES CON AÑOS DE NACIMIENTO:")
    print("=" * 35)

    # Contar cuántos nacieron en años pares e impares
    anios_pares = 0
    anios_impares = 0
    for anio in lista_anios_nacimiento:
        if anio % 2 == 0:
            anios_pares += 1
        else:
            anios_impares += 1

    print(f"\nConteo de Años Pares e Impares")
    print(f"Cantidad de años de nacimiento pares: {anios_pares}")
    print(f"Cantidad de años de nacimiento impares: {anios_impares}")

    # Evaluación de condiciones lógicas (Años)
    print("\nEvaluación de Condiciones Lógicas (Años)")

    # CONDICION5: Si todos nacieron después del 2000
    todos_despues_2000 = True
    if not lista_anios_nacimiento:
        todos_despues_2000 = False

    for anio in lista_anios_nacimiento:
        if anio <= 2000:
            todos_despues_2000 = False
            break

    if todos_despues_2000 and lista_anios_nacimiento:
        print("CONDICION5: ¡Grupo Z! Todos nacieron después del año 2000.")
    elif lista_anios_nacimiento:
        print("CONDICION5: No todos nacieron después del año 2000.")
    else:
        print("CONDICION5: No hay años de nacimiento para evaluar.")

    # CONDICION6: Si alguno nació en año bisiesto
    hay_bisiesto = False
    anios_bisiestos_encontrados = []
    for anio in lista_anios_nacimiento:
        if es_bisiesto(anio):
            hay_bisiesto = True
            anios_bisiestos_encontrados.append(anio)

    if hay_bisiesto:
        print(
            f"CONDICION6: Al menos uno nació en un año bisiesto: {anios_bisiestos_encontrados}.")
    elif lista_anios_nacimiento:
        print("CONDICION6: Ninguno nació en un año bisiesto.")
    else:
        print("CONDICION6: No hay años de nacimiento para evaluar años bisiestos.")

    # Producto Cartesiano (Años y Edades)
    print("\nProducto Cartesiano (Años y Edades):")
    if lista_anios_nacimiento:
        conjunto_anios = set(lista_anios_nacimiento)
        conjunto_edades = set()
        for anio in lista_anios_nacimiento:
            edad = calcular_edad(anio, AÑO_ACTUAL)
            conjunto_edades.add(edad)

        print(f"Conjunto de Años de Nacimiento: {conjunto_anios}")
        print(f"Conjunto de Edades Actuales: {conjunto_edades}")

        producto_cartesiano_anios_edades = set()
        for anio in sorted(list(conjunto_anios)):
            for edad in sorted(list(conjunto_edades)):
                producto_cartesiano_anios_edades.add((anio, edad))

        print(f"Producto Cartesiano (Años x Edades): {producto_cartesiano_anios_edades}")
    else:
        print("No hay años de nacimiento para calcular el producto cartesiano.")
