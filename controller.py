def aantal_dagen(inputFile):
    with open(inputFile, 'r') as file:
        regels = file.readlines()
    return len(regels) - 1


def auto_bereken(inputFile, outputFile):
    with open(inputFile, 'r') as infile, open(outputFile, 'w') as outfile:
        lines = infile.readlines()[1:]  #
        for line in lines:
            date, numPeople, tempSetpoint, tempOutside, precip = line.split()
            numPeople, tempSetpoint, tempOutside, precip = int(numPeople), float(tempSetpoint), float(
                tempOutside), float(precip)

            cv_ketel = 100 if (tempSetpoint - tempOutside) >= 20 else 50 if (tempSetpoint - tempOutside) >= 10 else 0
            ventilatie = min(numPeople + 1, 4)
            bewatering = precip < 3

            outfile.write(f"{date};{cv_ketel};{ventilatie};{bewatering}\n")


def overwrite_settings(inputFile, outputFile):
    date = input("Voer de datum in (bijv. 08-10-2024): ")
    system = input("Kies een van de geldige systemen (1: CV ketel, 2: ventilatie, 3: bewatering): ")
    value = input("Voer de nieuwe waarde in (bijv. 70, zodat de CV ketel op 70% wordt gezet) : ")

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
        parts = line.split(';')
        if parts[0] == date:
            if system == '1' and value.isdigit() and 0 <= int(value) <= 100:
                parts[1] = value
            elif system == '2' and value.isdigit() and 0 <= int(value) <= 4:
                parts[2] = value
            elif system == '3' and value in ('0', '1'):
                parts[3] = "True" if value == '1' else "False"
            else:
                return -3
            updated = True
        new_lines.append(";".join(parts) + "\n")

    if not updated:
        return -1

    with open(outputFile, 'w') as file:
        file.writelines(new_lines)

    return 0


def smart_home_controller():
    while True:
        print("\nSmart Home Controller Menu:")
        print("1. Aantal dagen in het bestand?")
        print("2. Bereken en sla actuatoren op")
        print("3. Waarde overschrijven")
        print("4. Stoppen")

        keuze = input("Maak een keuze (1-4): ")
        if keuze == '1':
            print(f"Aantal dagen: {aantal_dagen('smart_home_input.txt')}")
        elif keuze == '2':
            auto_bereken('smart_home_input.txt', 'smart_home_output.txt')
            print("Berekeningen opgeslagen in smart_home_output.txt")
        elif keuze == '3':
            overwrite_settings('smart_home_output.txt')
        elif keuze == '4':
            break
        else:
            print("Fout: ongeldige keuze.")

smart_home_controller()


"""
Bronnen:
http://w3schools.com/python/ref_string_isdigit.asp
https://www.w3schools.com/python/python_file_open.asp
https://www.w3schools.com/python/python_file_write.asp
https://www.youtube.com/watch?v=Uh2ebFW8OYM&t=709s&pp=ygUfcHl0aG9uIHJlYWQgYW5kIHdyaXRlIHRleHQgZmlsZQ%3D%3D
"""