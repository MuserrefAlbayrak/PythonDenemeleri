print("Kodlamaio");
header = "Tasit Kredisi";
print(header);
#String=> JAVA'daki ile ayni anlami ihtiva etmekte:)
header = "Ihtiyac Kredisi";
print(header);
#int, Integer => Yine JAVA'daki gibi.
vade = 36;
ekVade = 12;
#float, decimal, double
aylikOdeme = 200.50;
#bool, boolean
#JAVA'da true or false iken; Python'da 'T'rue or 'F'alse
#-------------------------------------------------
# "/" bolme operatoru Python'da iki tamsayi birbirine bolundugunde cikti tamsayi olsa dahi output float donmekte
print(vade / ekVade); #output => 3.0
print(vade % 5); #output=>1

# or (JAVA'daki || tabii) and (&&)
print(1 > 2 or 5 > 2) #True
print(1 > 2 and 5 > 2) #False

numberOne = 77;
numberTwo = 27;
#indent
if(numberOne > numberTwo) : 
    print("numberOne bigger than numberTwo")
elif numberTwo > numberOne : 
    print("numberTwo bigger than numberOne")
else : 
    print("numberOne equal to numberTwo")
print("if blogunun disinda oldugum kisim bir tab bosluk birakinca if'in icerisinde oluyorum unutma.")    
   
#JAVA'daki gibi bagimsiz if mantigi burada da ayni. 
