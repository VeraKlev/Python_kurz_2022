import pandas

adopce = pandas.read_csv("adopce-zvirat.csv", sep=";", index_col="nazev_cz") #Načti znovu data, ale tentokrát nastav parametr index_col na název sloupce, který obsahuje název zvířete v češtině. 

print(adopce.index.is_unique) # Pomocí <tvoje-promenna>.index.is_unique ověř, zda je nový index unikátní.

adopce = adopce.sort_index() # Seřazený index je efektivnější a přehlednější. Seřaď index pomocí metody .sort_index().

# print(adopce)

print(adopce.loc["Outloň váhavý"]) # Vyhledej řádek indexovaný názvem "Outloň váhavý". Namísto metody .iloc využij .loc.

print(adopce.loc["Želva Smithova":"Želva žlutočelá"]) # Vyhledej záznamy mezi "Želva Smithova" a "Želva žlutočelá".
