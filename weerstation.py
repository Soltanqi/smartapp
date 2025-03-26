def fahrenheit(temp_celsius):
    fahrenheit = (temp_celsius * 1.8) + 32
    return fahrenheit
    print("\nCelsius naar fahrenheit berekenen...")
    temperatuur = float(input("Hoeveel graden is het? (celsius): "))
    print(f"{fahrenheit(temperatuur)} graden Fahrenheit")

def gevoelstemperatuur(temp_celcius1, windsnelheid, luchtvochtigheid):
    gevoelstemperatuur = temp_celcius1 - (luchtvochtigheid / 100 * windsnelheid)
    return gevoelstemperatuur
    print("\nGevoelstemperatuur berekenen...")
    temperatuur2 = float(input("Wat is de temperatuur in Celsius?: "))
    wind = float(input("Wat is de windsnelheid (in km/h)?: "))
    vocht = float(input("Wat is de luchtvochtigheid (in %): "))

    print(f"De gevoelstemperatuur is {gevoelstemperatuur(temperatuur2, wind, vocht)} graden Celsius.")


def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    gevoel = gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid)

    if gevoel < 0 and windsnelheid > 10:
        return ('Het is heel koud en het stormt! Verwarming helemaal aan!')
    elif gevoel < 0 and windsnelheid <= 10:
        return ('Het is behoorlijk koud! Verwarming aan op de benedenverdieping!')
    elif 0 <= gevoel <10 and windsnelheid > 12:
        return ('Het is best koud en het waait; verwarming aan en roosters dicht!')
    elif 0 <= gevoel < 10 and windsnelheid <= 12:
        return ('Het is een beetje koud, elektrische kachel op de benedenverdieping aan!')
    elif 10 <= gevoel < 22:
        return ( 'Heerlijk weer, niet te koud of te warm.')
    else:
        return ('Warm! Airco aan!')
    print("\nWeerrapport berekenen...")


    temp = float(input("Wat is de temperatuur in Celsius?: "))
    wind = float(input("Wat is de windsnelheid (in km/h)?: "))
    vocht = float(input("Wat is de luchtvochtigheid (in %): "))

    print(weerrapport(temp, wind, vocht))

def weerstation():
    print("\nWeerstation berekenen...")
    totaal_temp1 = 0
    dagen = 0

    while dagen < 7:
        temperatuur = float(input("Voer de temperatuur in (in Celsius): "))
        if temperatuur == " ":
            break
        windsnelheid = float(input("Voer de windsnelheid in (in m/s): "))
        luchtvochtigheid = int(input("Voer de luchtgevoeligheid in (als geheel percentage van 0 tot 100): "))

        temp_fahrenheit = fahrenheit(temperatuur)
        totaal_temp1 += temp_fahrenheit
        dagen += 1

        print(f"Het is {temperatuur}C ({temp_fahrenheit}F")
        print(weerrapport(temperatuur, windsnelheid, luchtvochtigheid))
        print(f"Gemmidelde temp tot nu toe is {totaal_temp1 / dagen}")

        if luchtvochtigheid < 0 or luchtvochtigheid > 100:
            print("Fout: Luchtvochtigheid moet tussen 0 en 100 zijn.")
            continue

