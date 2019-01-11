# Kamatozás banki befektetés esetén
# r=kamat(periódusonként)
# n=periódusok száma
# PV=Present Value (Jelen érték)
# [Tőkésítés nélkül]
# FV = PV *(1+r*n)
# [Tőkésítés Minden Periódus végén]
# FV = PV *(1+r)^n

PV = float(input("Add meg a befektetni kívánt összeget!(HUF)\n"))
kamat = float(input("Add meg az éves kamatlábat! (Csak Számokat írj, hány százalék?!)\n"))
n = float(input("Add meg a hónapok számát, ammeddig ezzel a kamatozással befektetnél!\n"))


r = float((kamat/100)/12)
FV = float(PV*(1+r*n))
print("Tőkésítés nélkül a várható összeg (Kamatadó és SZOCHO levonás nélkül): ")
print(round(FV,2))
#** -> hatványozás a pythonban
FVt = float(PV*(1+r)**n)
print("Tőkésítés havonta történik a várható összeg (Kamatadó és SZOCHO levonás nélkül): ")
print(round(FVt,2))