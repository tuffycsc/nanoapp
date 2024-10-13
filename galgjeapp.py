import random

def kies_woord():
    woorden = {"makkelijk": ["bal", "kat", "huis"],
               "gemiddeld": ["fiets", "computer", "school"],
               "moeilijk": ["programmeren", "algoritme", "database"]}
    moeilijkheid = input("Kies een moeilijkheidsgraad (makkelijk/gemiddeld/moeilijk): ")
    return random.choice(woorden[moeilijkheid])

def galgje():
    print("Welkom bij Galgje!")
    naam = input("Wat is je naam? ")
    woord = kies_woord()
    geraden_letters = []
    aantal_raden = 6

    while aantal_raden > 0:
        print("Geraden letters:", " ".join(geraden_letters))
        print("Huidig woord:", " ".join([letter if letter in geraden_letters else "_" for letter in woord]))

        letter = input("Raad een letter: ")
        geraden_letters.append(letter)

        if letter not in woord:
            aantal_raden -= 1
            print(f"Fout! Je hebt nog {aantal_raden} kansen over.")

        if all(letter in geraden_letters for letter in woord):
            print(f"Gefeliciteerd {naam}! Je hebt het woord '{woord}' geraden!")
            break
    else:
        print(f"Helaas, je hebt verloren. Het woord was '{woord}'.")

if __name__ == "__main__":
    galgje()
