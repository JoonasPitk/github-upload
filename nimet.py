def kysy_nimi(minimipituus):
    print("Anna nimi,joka on vähintään", minimipituus, "merkkiä pitkä.")
    while True:
        nimi = input("Nimi: ")
        if len(nimi) >= minimipituus:
            break
    return nimi


def puhdista_nimi(nimi):
    turhat_valilyonnit_poistettu = nimi.strip()
    alkukirjaimet_korjattu = turhat_valilyonnit_poistettu.title()   # pEKKA vIrtAneN -> Pekka Virtanen
    return alkukirjaimet_korjattu
