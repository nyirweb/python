#Fizetés kiiratás

salary = int(input("Add meg a fizetésed számokban!\n"))

if(salary < 100000):
    currentSalary = int(salary*1.25)
    print("Az alkalmazott fizetése: ")
    print(round(currentSalary,2))
else:
    print("Az alkalmazott fizetése:")
    print(round(salary, 2))

