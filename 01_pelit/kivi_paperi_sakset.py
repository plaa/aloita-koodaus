# Tämä ohjelma pelaa kivi-paperi-sakset tietokonetta vastaan.
# Kokeile muuttaa näitä:
# - lisää pisteet
# - pelaa monta kierrosta
# - lisää hassu voittoviesti

import random

vaihtoehdot = ["kivi", "paperi", "sakset"]
pelaaja = input("Valitse kivi, paperi tai sakset: ").lower()
kone = random.choice(vaihtoehdot)

print(f"Tietokone valitsi: {kone}")

if pelaaja not in vaihtoehdot:
    print("Tuota valintaa ei ollut pelissä mukana.")
elif pelaaja == kone:
    print("Tasapeli!")
elif (
    (pelaaja == "kivi" and kone == "sakset")
    or (pelaaja == "paperi" and kone == "kivi")
    or (pelaaja == "sakset" and kone == "paperi")
):
    print("Sinä voitit!")
else:
    print("Tietokone voitti tällä kertaa.")
