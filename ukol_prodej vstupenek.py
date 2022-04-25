from datetime import datetime

termin = input("V jakém termínu chcete jít do kina? ")

datum_navstevy_kina = datetime.strptime(termin, "%d. %m. %Y")

prvni_datum = datetime(2021, 7, 1)
druhe_datum = datetime(2021, 8, 11)
treti_datum = datetime(2021, 8, 31)

if datum_navstevy_kina < prvni_datum:
    print("Kino je v tomto termínu uzavřeno.")

elif datum_navstevy_kina < druhe_datum:
    pocet_osob = int(input("Kolik lístků si přejete? "))
    cena_listku = 250
    cena = pocet_osob * cena_listku
    print(f"Cena vašich lístků je {cena} Kč.")
    
elif datum_navstevy_kina <= treti_datum:
    pocet_osob_novy = int(input("Kolik lístků si přejete? "))
    cena_listku_nova = 180
    cena_nova = pocet_osob_novy * cena_listku_nova
    print(f"Cena vašich lístků je {cena_nova} Kč.")

else:
    print("Kino je v tomto termínu uzavřeno.")

