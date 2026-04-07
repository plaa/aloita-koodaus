# Tämä ohjelma on pieni tekstiseikkailu.
# Kokeile muuttaa näitä:
# - lisää uusi paikka
# - tee lisää loppuja
# - vaihda hahmojen nimet

print("Olet mystisessä metsässä.")
print("Edessä näkyy luola ja puumaja.")

paikka = input("Menetkö luolaan vai puumajaan? ").lower()
print()

if paikka == "luolaan" or paikka == "luola":
    print("Luolassa tapaat ystävällisen peikon, jolla on valtava suklaakeksi.")
    teko = input("Pyydätkö keksiä vai juoksetko pois? ").lower()
    print()

    if teko.startswith("pyydä"):
        print("Peikko antaa sinulle keksin ja kruunaa sinut keksiritariksi.")
    else:
        print("Juokset niin kovaa, että löydät salaisen trampoliinin metsän keskeltä.")
elif paikka == "puumajaan" or paikka == "puumaja":
    print("Puumajassa istuu pöllö, joka pitää aurinkolaseja.")
    teko = input("Sanotko hei vai kysytkö salaisuutta? ").lower()
    print()

    if teko == "hei":
        print("Pöllö nyökkää arvokkaasti ja tarjoaa mehua.")
    else:
        print("Salaisuus on tämä: parhaat seikkailut alkavat kummallisesta ideasta.")
else:
    print("Päädyt marjapolulle ja löydät eväsretken. Sekin oli hyvä loppu.")
