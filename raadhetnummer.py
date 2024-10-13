import random

def raad_het_nummer():
    # Kies een willekeurig nummer tussen 1 en 10
    te_raden_nummer = random.randint(1, 10)
    max_pogingen = 5  # Totale aantal pogingen
    poging_teller = 0  # Aantal gemaakte pogingen

    print("Welkom bij het 'Raad het Nummer' spel!")
    print("Ik heb een nummer tussen 1 en 10 gekozen. Kun jij het raden?")
    print(f"Je hebt {max_pogingen} pogingen om het nummer te raden.")

    # Loop voor het aantal pogingen
    while poging_teller < max_pogingen:
        # Vraag de gebruiker om een gok
        gok = int(input("Voer je gok in: "))
        poging_teller += 1  # Verhoog het aantal pogingen

        # Controleer of de gok juist is
        if gok < te_raden_nummer:
            print("Hoger! Probeer het nog eens.")
        elif gok > te_raden_nummer:
            print("Lager! Probeer het nog eens.")
        else:
            print(f"Gefeliciteerd! Je hebt het nummer {te_raden_nummer} geraden in {poging_teller} pogingen.")
            break  # Stop de loop bij een juiste gok

    # Controleer of het aantal pogingen op is
    if poging_teller == max_pogingen:
        print(f"Helaas, je hebt geen pogingen meer. Het juiste nummer was {te_raden_nummer}.")

if __name__ == "__main__":
    raad_het_nummer()
