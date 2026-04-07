# Tämä ohjelma kertoo satunnaisen vitsin tai hassun viestin.
# Kokeile muuttaa näitä:
# - lisää omia vitsejä
# - tee useampi kierros
# - jaa vitsit eri ryhmiin

import random

vitsit = [
    "Mitä nolla sanoi kasille? Hieno vyö!",
    "Miksi kana ylitti tien? Koska se halusi päästä toiselle puolelle.",
    "Miksi tietokone meni lääkäriin? Koska sillä oli virus.",
    "Mitkä ovat käytetyimmät sanat koulussa? – En tiedä.",
    "Jos dinosaurus söisi karkkia, sitä voisi kutsua mässysaurukseksi.",
    "Osaatteko nimetä viisi tuotetta, jotka sisältävät maitoa? opettaja kysyi. - Jäätelö, juusto, viili, voi ja lehmä.",
]

print("Vitsikone käynnistyy...")
print()
print(random.choice(vitsit))
