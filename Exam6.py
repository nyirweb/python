#Telek négyszögöl számítása

a = float(input("Add meg a telek hosszát!\n"))
b = float(input("Add meg a telek szélét!\n"))

T = float(a*b)

print("A telek területe (négyzetméterben): ",round(T,2))

NegySzogOl = float(T/3.6)

print("A telek területe (négyszögölben: ",round(NegySzogOl,2))