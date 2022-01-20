janne = "Janne Porkka 1"
janne = 'Janne Porkka 2'
pituus = 190
liukuluku = 190.0
joku_lista = ["arvo 1", 1234, 456.7, "moi"]
tyhja_lista = []
sanakirja = {"avain1": "arvo1", "avain2": "arvo2"}
sanakirja = {
    "avain1": "arvo1",
    "avain2": "arvo2",
    "nelkyt kaks": 42,
    42: "nelikakkonen"
}

# # Käy sanakirjan kaikki avain-arvo-parit läpi
# for avain in sanakirja:
#     print(avain, " => ", sanakirja[avain])

# for luku in [55, 66, 13, 4]:
#     print(luku * 2)
#     print("Moi!")
#     print("No moi moi!")

# def tulosta_kaksi_arvoa(parametri1, parametri2):
#     # funktion koodi
#     print(parametri1, " --- ", parametri2)
#     return parametri1 * 10

# paluuarvo = tulosta_kaksi_arvoa(32, "jee")

# if paluuarvo > 100:
#     print("Suurempi kuin 100")
#     print(paluuarvo)
# else:
#     print("Pienempi tai yhtäsuuri kuin 100")
#     print(paluuarvo)


# nimet = [
#     "Piia",
#     "Petra",
#     "Jussi",
#     "Ville",
# ]

# for nimi in nimet:
#     print("Henkilö:", nimi)
#     if nimi.startswith("P"):
#         print("Alkaa P:llä, aloitetaan alusta.")
#         continue
#     if nimi == "Jussi":
#         print("Nimi ei alkunut P:llä.")
#         break

# Vaihtoehto 1

import nimet

pitka_nimi = nimet.kysy_nimi(5)
print(pitka_nimi)
print("Puhdistettu:", nimet.puhdista_nimi(pitka_nimi))

# Vaihtoehto 2

# from nimet import kysy_nimi

# pitka_nimi = kysy_nimi(5)
# print(pitka_nimi)


# nimi = "nimi"

# while True:
#     print("Kysytään nimi.")
#     nimi = input("Kirjoita nimi:")
#     if not nimi:
#         print("Nimi oli tyhjä. Kysytään uudestaan.")
#         continue
#     print("Saatiin nimi", nimi)
#     if nimi:
#         break

# print("Annettu nimi oli:", nimi)
