import pandas

ukol = pandas.read_csv("temperature.csv")

print(ukol.iloc[0:10]) # Vypiš si prvních několik řádků, ať si prohlédneš strukturu tabulky.

print(ukol[ukol["City"]=="Prague"]) # Dotaz na měření, která byla provedena v Praze.

print(ukol[ukol["AvgTemperature"] > 80]) # Dotaz na měření, ve kterých je teplota (sloupec AvgTemperature) vyšší než 80 stupňů.

teplota_pod_sedesat = ukol["AvgTemperature"] < 60
staty_v_Evrope = ukol["Region"] == "Europe"

print(ukol[teplota_pod_sedesat & staty_v_Evrope]) # Dotaz na měření, ve kterých je teplota vyšší než 60 stupňů a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe).

teplota_nad_osmdesat = ukol["AvgTemperature"] > 80
teplota_pod_minus_dvacet = ukol["AvgTemperature"] < -20

print(ukol[teplota_nad_osmdesat | teplota_pod_minus_dvacet]) # Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 80 stupňů nebo menší než -20 stupňů.





