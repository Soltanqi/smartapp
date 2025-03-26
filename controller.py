import os


def aantal_dagen(inputFile):
    if not os.path.exists(inputFile):
        print("Fout: Bestand niet gevonden.")
        return -1
    with open(inputFile, 'r') as file:
        regels = file.readlines()
    return len(regels) - 1


def auto_bereken(inputFile, outputFile):
    if not os.path.exists(inputFile):
        print("Fout: Bestand niet gevonden.")
        return
    with open(inputFile, 'r') as infile, open(outputFile, 'w') as outfile:
        lines = infile.readlines()[1:]
        for line in lines:
            try:
                date, numPeople, tempSetpoint, tempOutside, precip = line.strip().split()
                numPeople, tempSetpoint, tempOutside, precip = int(numPeople), float(tempSetpoint), float(tempOutside), float(precip)

                cv_ketel = 100 if (tempSetpoint - tempOutside) >= 20 else 50 if (tempSetpoint - tempOutside) >= 10 else 0
                ventilatie = min(numPeople + 1, 4)
                bewatering = "True" if precip < 3 else "False"

                outfile.write(f"{date};{cv_ketel};{ventilatie};{bewatering}\n")
            except ValueError:
                print(f"Fout bij verwerken van regel: {line.strip()}")


def overwrite_settings(outputFile):
    if not os.path.exists(outputFile):
        print("Fout: Bestand niet gevonden.")
        return -1

    date = input("Voer de datum in (bijv. 08-10-2024): ").strip()
    system = input("Kies een van de systemen (1: CV ketel, 2: ventilatie, 3: bewatering): ").strip()
    value = input("Voer de nieuwe waarde in: ").strip()

    if system not in ['1', '2', '3']:
        print("Fout: Ongeldig systeem gekozen.")
        return -3

    try:
        with open(outputFile, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Fout: Bestand niet gevonden.")
        return -1

    updated = False
    new_lines = []
    for line in lines:
        parts = line.strip().split(';')
        if parts[0] == date:
            if system == '1' and value.isdigit() and 0 <= int(value) <= 100:
                parts[1] = value
            elif system == '2' and value.isdigit() and 0 <= int(value) <= 4:
                parts[2] = value
            elif system == '3' and value in ('0', '1'):
                parts[3] = "True" if value == '1' else "False"
            else:
                print("Fout: Ongeldige invoer voor het geselecteerde systeem.")
                return -3
            updated = True
        new_lines.append(";".join(parts) + "\n")

    if not updated:
        print("Fout: Datum niet gevonden.")
        return -1

    with open(outputFile, 'w') as file:
        file.writelines(new_lines)

    print("Waarde succesvol bijgewerkt.")
    return 0


def smart_home_controller():
    while True:
        print("\nSmart Home Controller Menu:")
        print("1. Aantal dagen in het bestand?")
        print("2. Bereken en sla actuatoren op")
        print("3. Waarde overschrijven")
        print("4. Stoppen")

        keuze = input("Maak een keuze (1-4): ").strip()
        if keuze == '1':
            dagen = aantal_dagen('smart_home_input.txt')
            if dagen != -1:
                print(f"Aantal dagen: {dagen}")
        elif keuze == '2':
            auto_bereken('smart_home_input.txt', 'smart_home_output.txt')
            print("Berekeningen opgeslagen in smart_home_output.txt")
        elif keuze == '3':
            overwrite_settings('smart_home_output.txt')
        elif keuze == '4':
            break
        else:
            print("Fout: Ongeldige keuze.")








