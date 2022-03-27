import math
telefonni_cislo = input("Jaké je vaše telefonní číslo? ")
 
def delka_cisla(t_cislo):
    t_cislo = t_cislo.replace(" ", "")
    pocet_znaku = len(t_cislo)
    if pocet_znaku == 9:
        return True
    elif pocet_znaku == 13:
        if "+420"in t_cislo:
            return True
        else:
            return False
    else:
        return False
 
# delka_cisla(telefonni_cislo)
 
if delka_cisla(telefonni_cislo) == False:
    print("Toto číslo není správně.")
else:
    text_zpravy = input("Napište text vaší SMS zprávy: ")
 
def cena_sms(text_sms):
    pocet_znaku_sms = len(text_sms)
    vypocet = pocet_znaku_sms / 180
    vysledek = math.ceil(vypocet) * 3
    print(f"Cena vaší SMS je {vysledek} Kč.")
 
if delka_cisla(telefonni_cislo) == True:
    cena_sms(text_zpravy)