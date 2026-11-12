
def calcular_salario(horas, categoria):
    """
    Calcula el salario de un trabajador según las horas trabajadas y su categoría.
    """

    tarifas = {
        1: 12000,
        2: 17000,
        3: 22000
    }

    if type(categoria) is not int or categoria not in tarifas:
        raise ValueError("La categoría debe ser 1, 2 o 3.")

    if type(horas) not in (int, float) or not 0 <= horas < float("inf"):
        raise ValueError("Las horas deben ser un número finito mayor o igual a 0.")

    tarifa = tarifas[categoria]

    if horas > 40:
        horas_extras = horas - 40
        salario = (40 * tarifa) + (horas_extras * tarifa * 1.25)
    else:
        salario = horas * tarifa

    return salario


if __name__ == "__main__":
    try:
        horas = float(input("Ingrese las horas trabajadas: "))
        categoria = int(input("Ingrese la categoría (1, 2 o 3): "))

        salario = calcular_salario(horas, categoria)

        print(f"Salario del trabajador: ${salario:,.2f} COP")

    except ValueError as error:
        print(f"Error: {error}")
