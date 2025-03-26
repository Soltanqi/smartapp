#hoofdmenu
import weerstation as weerstation
import controller as controller
import api_test as api_test


while True:
    print("\nWelkom bij Spinzo!")
    print("kies het spel dat je wilt spelen: ")
    print("1. ⛅️ weerstation 🚉")
    print("2. controller 🎮 ")
    print("3. 🌤 WeerApp 🌍")
    print("4. Afsluiten.")

    keuze = input("maak een keuze tussen 1 en 4:")
    if keuze == "1":
            weerstation.weerstation()
    elif keuze == "2":
        controller.smart_home_controller()
    elif keuze == "3":
        api_test.weer_app()
    elif keuze == "4":
        print("Tot ziens!")
    else:
        print("Kies uit 1,2, 3 of 4.")