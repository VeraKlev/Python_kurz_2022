import pandas

adopce = pandas.read_csv("adopce-zvirat.csv", sep=";")

print(adopce.shape) #513 radku, 6 sloupcu

print(adopce.columns) #nazvy sloupcu

print(adopce.iloc[34]) #ibis bily, white ibis



