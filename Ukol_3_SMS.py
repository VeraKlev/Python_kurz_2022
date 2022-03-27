telefonni_cislo = input("Jaké je vaše telefonní číslo? ")

def delka_cisla(cislo):
    pocet_znaku = len(telefonni_cislo)
    if pocet_znaku == 9:
        return True
    elif pocet_znaku == 13:
        if "+420"in telefonni_cislo:
            return True
        else:
            return False
    else:
        return False

delka_cisla(telefonni_cislo)

if delka_cisla(telefonni_cislo) == False:
    print("Toto číslo není správně.")
else:
    text_zpravy = input("Napište text vaší SMS zprávy: ")

def cena_sms(pocet_znaku):
    pocet_znaku = len(text_zpravy)
    if pocet_znaku <= 180:
        vysledek = 3
    else:
        vypocet = pocet_znaku / 180
        import math
        vysledek = math.ceil(vypocet) * 3
    print(f"Cena vaší SMS je {vysledek} Kč.")

if delka_cisla(telefonni_cislo) == True:
    cena_sms(text_zpravy)

    