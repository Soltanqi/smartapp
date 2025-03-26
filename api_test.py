import requests

API_KEY = "02ebc3af515bb8a533761a86fd22eb93"

def weer_app():
    print("🌤 WeerApp 🌍")

    stad = input("Voer een stad in: ").strip()

    if stad:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={stad}&appid={API_KEY}&units=metric&lang=nl"

        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                temperatuur = data["main"]["temp"]
                weer_omschrijving = data["weather"][0]["description"]

                print(f"\nPlaats: {stad.capitalize()}")
                print(f" Temperatuur: {temperatuur}°C")
                print(f" Weer: {weer_omschrijving}\n")
            else:
                print("️ Stad niet gevonden. Probeer opnieuw.")

        except requests.exceptions.RequestException:
            print("️ Er is een probleem met de verbinding.")





