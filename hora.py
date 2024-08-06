def convertir_a_12_horas(hora_24):
    hora, minutos = map(int, hora_24.split(':'))
    
    if hora >= 12:
        sufijo = 'PM'
        if hora > 12:
            hora_12 = hora - 12
        else:
            hora_12 = 12
    else:
        sufijo = 'AM'
        if hora == 0:
            hora_12 = 12
        else:
            hora_12 = hora
    
    return f"{hora_12}:{minutos:02d} {sufijo}"


hora_24 = input("Introduce la hora en formato 24 horas (HH:MM): ")
hora_12 = convertir_a_12_horas(hora_24)
print(hora_12)