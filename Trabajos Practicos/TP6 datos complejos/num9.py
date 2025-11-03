def crear_agenda():
    agenda = {
        ("lunes", "10:00"): "Reunión",
        ("martes", "15:00"): "Clase de inglés",
        ("miércoles", "18:30"): "Gimnasio",
        ("viernes", "09:00"): "Consulta médica"
    }
    return agenda


def consultar_agenda(agenda, dia, hora):
    clave = (dia.lower(), hora)
    if clave in agenda:
        return f"Actividad: {agenda[clave]}"
    else:
        return "No hay ninguna actividad registrada en ese día y hora."


def main():
    agenda = crear_agenda()

    print("=== CONSULTA DE AGENDA ===")
    dia = input("Ingresá el día: ").strip().lower()
    hora = input("Ingresá la hora (formato HH:MM): ").strip()

    resultado = consultar_agenda(agenda, dia, hora)
    print(resultado)


if __name__ == "__main__":
    main()
