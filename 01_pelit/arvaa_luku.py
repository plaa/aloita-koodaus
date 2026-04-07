# Tämä ohjelma on arvauspeli, jossa etsit salaisen luvun.
# Kokeile muuttaa näitä:
# - vaihda lukuväli
# - laske arvausten määrä
# - tee pelistä vaikeampi

import random

salainen_luku = random.randint(1, 20)
arvaukset = 0

print("Arvaa luku väliltä 1-20.")

while True:
    arvaus_teksti = input("Anna arvaus: ")

    if not arvaus_teksti.isdigit():
        print("Kirjoita numero.")
        continue

    arvaus = int(arvaus_teksti)
    arvaukset = arvaukset + 1

    if arvaus < salainen_luku:
        print("Liian pieni!")
    elif arvaus > salainen_luku:
        print("Liian suuri!")
    else:
        print(f"Oikein! Löysit luvun {salainen_luku}.")
        print(f"Arvauksia tuli {arvaukset}.")
        break
