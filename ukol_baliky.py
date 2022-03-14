baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

kod_baliku = input('Jaký je váš kód balíku? ')

if baliky[kod_baliku] == True:
  print("Balík ", kod_baliku, " byl předán kurýrovi.")

else:
  print("Balík ", kod_baliku, " zatím nebyl předán kurýrovi.")