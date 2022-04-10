class Polozka:
  def __init__(self, nazev, zanr):
    self.nazev = nazev
    self.zanr = zanr
  def get_info(self):
    return f"Položka má název {self.nazev} a její žánr je {self.zanr}. "

class Film(Polozka):
  def __init__(self, nazev, zanr, delka):
    super().__init__(nazev, zanr)
    self.delka = delka
  def get_info(self):
    return f"Film se jmenuje {self.nazev}, jeho žánr je {self.zanr} a délka filmu je {self.delka} minut. "

class Serial(Polozka):
  def __init__(self, nazev, zanr, pocet_epizod, delka_epizody):
    super().__init__(nazev, zanr)
    self.pocet_epizod = pocet_epizod
    self.delka_epizody = delka_epizody
  def get_info(self):
    return f"Seriál se jmenuje {self.nazev}, jeho žánr je {self.zanr}, má {self.pocet_epizod} epizod a délka epizody je {self.delka_epizody} minut. "

polozka = Polozka('Smrt na Nilu', 'detektivka')
print(polozka.get_info())

film = Film('Po přečtení spalte', 'komedie', 120)
print(film.get_info())

serial = Serial('Kancl', 'komedie', 201, 20)
print(serial.get_info())