# Tämä ohjelma piirtää kuvion merkeillä.
# Kokeile muuttaa näitä:
# - vaihda merkki
# - muuta kokoa
# - tee talo tai naama

merkki = "#"
koko = 5

print("Neliö:")
for _ in range(koko):
    print(merkki * koko)

print()
print("Kolmio:")
for rivi in range(1, koko + 1):
    print(merkki * rivi)
