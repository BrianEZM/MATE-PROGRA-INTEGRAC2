import services.servicios_operaciones as servicios_operaciones

ENTREGA = "TPI-2 Mate-Progra UTN"
NUM_INTEGRANTES = 2
INTEGRANTES = ["Brian Zapata Marin", "Matias Almeida"]

DNI_INTEGRANTE_1 = "35973635"
DNI_INTEGRANTE_2 = "44046088"

ANIO_INTEGRANTE_1 = 1991
ANIO_INTEGRANTE_2 = 2002


# PROGRAMA PRINCIPAL
def main():
    lista_dnis = [DNI_INTEGRANTE_1, DNI_INTEGRANTE_2]
    lista_anios = [ANIO_INTEGRANTE_1, ANIO_INTEGRANTE_2]

    print(f"\nDatos del Grupo: {ENTREGA}")
    for i in range(NUM_INTEGRANTES):
        print(f"  {INTEGRANTES[i]}: DNI = {lista_dnis[i]}, Año de Nacimiento = {lista_anios[i]}")

    servicios_operaciones.realizar_operaciones_dni(lista_dnis)
    servicios_operaciones.realizar_operaciones_anios(lista_anios)


if __name__ == "__main__":
    main()
