# Tämä ohjelma vastaa kysymykseen kuin taikapallo.
# Kokeile muuttaa näitä:
# - lisää uusia vastauksia
# - tee oudompia vastauksia
# - lisää eri vastausryhmiä

import random

vastaukset = [
    "Kyllä varmasti.",
    "Ehkä pian.",
    "Kokeile uudestaan hetken päästä.",
    "Tänään näyttää hyvältä.",
    "En olisi siitä ihan varma.",
    "Kuulostaa seikkailulta. Tee se.",
]

kysymys = input("Kysy taikapallolta jotain: ")

print()
print(f"Kysymyksesi oli: {kysymys}")
print(f"Taikapallo sanoo: {random.choice(vastaukset)}")
