import random


def kies_woord():
    with open('C:/Users/tufan/PycharmProjects/nano_app_store/woordenlijst.txt', 'r') as file:
        woorden = file.read().splitlines()

    return random.choice(woorden)


def galgje():
    print("Welkom bij Galgje!")
    naam = input("Wat is je naam? ")
    woord = kies_woord()
    geraden_letters = []
    aantal_raden = 6

    while aantal_raden > 0:
        print("Geraden letters:", " ".join(geraden_letters))
        print("Huidig woord:", " ".join([letter if letter in geraden_letters else "_" for letter in woord]))

        letter = input("Raad een letter: ").lower()

        if letter in geraden_letters:
            print(f"Je hebt de letter '{letter}' al geraden.")
            continue

        geraden_letters.append(letter)

        if letter not in woord:
            aantal_raden -= 1
            print(f"Fout! Je hebt nog {aantal_raden} kansen over.")

        if all(letter in geraden_letters for letter in woord):
            print(f"Gefeliciteerd {naam}! Je hebt het woord '{woord}' geraden!")
            break
    else:
        print(f"Helaas, je hebt verloren. Het woord was '{woord}'.")



galgje()
