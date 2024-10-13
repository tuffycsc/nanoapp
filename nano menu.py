import galgjeapp  # Galgje-app importeren
import raadhetnummer  # Raad het Nummer-app importeren

def main_menu():
    while True:  # Oneindige lus voor het hoofdmenu
        # Hoofdmenu weergeven
        print("Welkom bij de Nano App Store!")  # Welkomsbericht voor de Nano App Store
        print("1. Galgje App")  # Keuze voor de Galgje-app
        print("2. Raad het Nummer")  # Keuze voor de Raad het Nummer-app
        print("3. Stoppen")  # Optie om het programma te stoppen
        choice = input("Maak uw keuze: ")  # Gebruiker om een keuze vragen

        if choice == '1':
            galgjeapp.galgje()  # Galgje-app functie aanroepen
        elif choice == '2':
            raadhetnummer.raad_het_nummer()  # Raad het Nummer-app functie aanroepen
        elif choice == '3':
            print("Programma wordt afgesloten...")  # Mededeling dat het programma wordt afgesloten
            exit()  # Het programma beëindigen
        else:
            print("Ongeldige keuze, probeer het opnieuw.")  # Gebruiker waarschuwen bij ongeldige keuze

if __name__ == "__main__":
    main_menu()  # Hoofdmenu weergeven wanneer het programma start
