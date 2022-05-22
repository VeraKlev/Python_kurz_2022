import re

with open('posta.html', encoding='utf-8') as vstup:
  posta = vstup.read()

# při využití metody read se \n znaky se nezobrazují, proto je nenahrazuji

reg_vyraz_mezery = re.compile(r"\s{2,}")
posta_nova = reg_vyraz_mezery.sub(" " * 1, posta)
# print(posta_nova)

reg_vyraz_adresa = re.compile(r"\d{3}\s{1}\d{2}\s[\w+ ]+")
mesta_psc = reg_vyraz_adresa.findall(posta_nova)
print(mesta_psc)