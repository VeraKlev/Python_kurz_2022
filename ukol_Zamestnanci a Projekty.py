import pandas

zam_liberec = pandas.read_csv("zam_liberec.csv")
zam_plzen = pandas.read_csv("zam_plzeň.csv")
zam_praha = pandas.read_csv("zam_praha.csv")

zam_liberec["mesto"] = "Liberec"
zam_plzen["mesto"] = "Plzen"
zam_praha["mesto"] = "Praha"

vsichni_zamestnanci = pandas.concat([zam_liberec, zam_plzen, zam_praha], ignore_index=True)
# print(vsichni_zamestnanci)

platy_2021_02 = pandas.read_csv("platy_2021_02.csv")
# print(platy_2021_02)

vsichni_zamestnanci = vsichni_zamestnanci.merge(platy_2021_02, on="cislo_zamestnance", how="left")
print(vsichni_zamestnanci)

vyhozeni = vsichni_zamestnanci[vsichni_zamestnanci["plat"].isnull()]
print(vyhozeni.shape) #13
print(vsichni_zamestnanci.shape) #56

print(vsichni_zamestnanci.groupby("mesto")["plat"].mean())


vykazy = pandas.read_csv("vykazy.csv")
# print(vykazy)

print(vykazy.groupby("project")["hours"].sum())