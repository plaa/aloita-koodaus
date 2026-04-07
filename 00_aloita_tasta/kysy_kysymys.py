# Tämä ohjelma kysyy muutaman kysymyksen ja vastaa niihin.
# Kokeile muuttaa näitä:
# - lisää uusi kysymys
# - keksi hauskempi vastaus
# - vaihda aihe omiin kiinnostuksiin

nimi = input("Mikä sinun nimesi on? ")
elain = input("Mikä eläin olisi hauska lemmikki? ")
herkku = input("Mikä on paras herkku? ")

print()
print(f"Hei {nimi}!")
print(f"Ai että, {elain} olisi kyllä erikoinen lemmikki.")

if herkku == "jäätelö":
    print("Jäätelö on klassikko. Hyvä valinta.")
elif herkku == "pizza":
    print("Pizza herkuksi? Rohkea ja maukas päätös.")
else:
    print(f"{herkku} kuulostaa hyvältä minustakin.")

if elain == "lohikäärme":
    print("Muista vain tehdä sille extra-suuri peti.")
elif elain == "koira":
    print("Koira on uskollinen ystävä, mutta vaatii paljon huomiota.")
else:
    print("Ehkä sille voisi keksiä myös hauskan nimen.")
