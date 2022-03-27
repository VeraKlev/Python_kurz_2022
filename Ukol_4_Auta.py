class Auto():
  def __init__(self, registr_znacka, znacka, typ, pocet_km, k_dispozici=True):
    self.registr_znacka = registr_znacka
    self.znacka = znacka
    self.typ = typ
    self.pocet_km = pocet_km
    self.k_dispozici = k_dispozici

  def pujc_auto(self):
    if self.k_dispozici == True:
      self.k_dispozici = False
      return f"Potvrzuji zapůjčení vozidla."
    else:
      return f"Vozidlo není k dispozici."

  def get_info(self):
    return f"Auto má registrační značku {self.registr_znacka}, značku {self.znacka}. Je to auto typu {self.typ} a má najeto {self.pocet_km} km."

peugeot = Auto('4A2 3020', 'Peugeot', '403 Cabrio', 47534)
octavia = Auto('1P3 4747', 'Škoda', 'Octavia', 41253)

booking = input("Jaké auto si chcete rezervovat? ")

if booking == "Peugeot":
  print(peugeot.get_info())
  print(peugeot.pujc_auto())
elif booking == "Škoda":
  print(octavia.get_info())
  print(octavia.pujc_auto())
else:
  print("Toto auto není v naší nabídce.")

booking = input("Jaké auto si chcete rezervovat? ")
if booking == "Peugeot":
  print(peugeot.get_info())
  print(peugeot.pujc_auto())
elif booking == "Škoda":
  print(octavia.get_info())
  print(octavia.pujc_auto())
else:
  print("Toto auto není v naší nabídce.")