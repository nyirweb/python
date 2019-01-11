#Korra válaszol

kor = int(input("Add neg a korod! (Években)\n"))

if(kor<0):
    print("Helytelen választ adtál meg!")
else:
    if(kor>=0 and kor<=13):
        print("Gyermek")
    elif(kor>=14 and kor<=17):
        print("Fiatalkorú")
    elif(kor>=18 and kor<=23):
        print("Ifjú")
    elif(kor>=24 and kor<=59):
        print("Felnőtt")
    elif(kor >= 60):
        print("Idős")
    else:
        print("Helytelen számot adtál meg! Pozitív egész számokat adj meg!")