#Henger térfogat és súly számítás!

print("\nÜdvözöllek! Ez itt a henger térfogat számláló!")
print("Szabályok: A tizedes vessző (',') helyett pontot ('.') használj! Minden megadott válasz után üss entert!\n")

rules = str(input("Ha a szabályokat megértetted nyomj 'y' betűt ha nem, akkor 'n' betűt "))
if(rules == "y"):
    r = float(input("Add meg a henger sugarát(cm)\n"))
    m = float(input("Add meg a henger magasságát!(cm)\n"))
    PI = float(3.14)
    hengerTerfogata = float(r*r*m*PI)
    print("\nA henger térfogata (köb cm): ")
    hengerTerfogatKiir = print(round(hengerTerfogata,2))
    #FA (LucFenyő) sűrűsége 0.47 g/köbCentiMéter
    #forrás: https://tudasbazis.sulinet.hu/hu/szakkepzes/epiteszet/epitoanyagok/az-altalanos-vizsgalatok-faanyagokra-alkalmazott-valtozatainak-tartalma-modszerei-mente/a-faanyagok-suruseg-testsuruseg-vizsgalata
    print("Tömör fa henger (LucFenyő) esetén a henger súlya (gramm) : ")
    print(round(float(hengerTerfogata*0.47),2))
    #Vas sűrűsége: 7,86 g/cm3
    #Forrás: https://tudasbazis.sulinet.hu/hu/termeszettudomanyok/kemia/szervetlen-kemia/a-femek/a-vas-es-az-aluminium-osszehasonlitasa
    print("Tömör vas henger esetén a henger súlya(gramm) : ")
    print(round(float(hengerTerfogata*7.86),2))
else:
    print("A játék véget ért")
    print("Szabályok: A tizedes vessző (',') helyett pontot ('.') használj! Minden megadott válasz után üss entert!\n")
    print("Futtatsd újra a programot, ha most már világosak a szabályok!")
