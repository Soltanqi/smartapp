#hoofdmenu
import api_test
import weerstation as weerstation
import controller as controller
import api_test as api_test


while True:
    print("\nWelkom bij Spinzo!")
    print("kies het spel dat je wilt spelen: ")
    print("1. ⛅️ weerstation 🚉")
    print("2. controller 🎮 ")
    print("3. 🌤 WeerApp 🌍")

    keuze = input("maak een keuze tussen 1 en 3:")
    if keuze == "1":
            weerstation.weerstation()
    elif keuze == "2":
        controller.controller()
    elif keuze == "3":
        api_test.weer_app()
    elif keuze == "4":
        print("Tot ziens!")
    else:
        print("Kies uit 1,2, 3 of 4.")