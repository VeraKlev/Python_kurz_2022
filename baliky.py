baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

kod_baliku = input('Jaký je váš kód balíku? ')


if kod_baliku == "B541X" or "B501X":
    print(f"Balík byl předán kurýrovi.")

else:
    print(f"Balík zatím nebyl předán kurýrovi.")
    









