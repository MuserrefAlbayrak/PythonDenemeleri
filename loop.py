# for loop
#for range() bolumu i degerini alir (ornegin 0 ise ki default 0'dir ben herhangi bir şey belirtmemissem)
# i degerini 10'a kadar 1'er arttirir 10 dahil degil.

for i in range(10) :
    print(i);#0, 1, 2, 3, 4, 5, 6, 7, 8, 9

print("********************************************************************")
for i in range(5,10):
    print(i);# 5, 6, 7, 8, 9
print("********************************************************************")

for i in range(0,51,10): # 0 ile 50 arasinda 10 10 arttirarak dongu olustur
    print(i) #0, 10, 20, 30, 40, 50
print("********************************************************************")    

credits = [1, 1.5, 2j, [1,7],(8,9),{"city":"Ankara"}];
for i in credits:
    if  isinstance(i, int):
        print(i)
    
      
print("********************************************************************")    
for i in range(len(credits)):
    print([i]) 

print("********************************************************************")

# "Muserref" text'ini terstten yazdir bir bakayim:)

def tersCevir(string):
    text = ""
    for i in string:
        text = i + text# java'daki text += i burada olmadi. o nedenle boyle yazildi. 
    return text;
name = "Muserref"
print(tersCevir(name));

print("********************************************************************")
def ters_cevirr(string):
    ters_string = ""
    for karakter in string:
        ters_string += karakter
    return ters_string
name2 = "Muserref Albayrak"
ters_ifade = ters_cevirr(name2)
print(ters_ifade)
print("********************************************************************")
def ters_cevir3(string):
    ters_string = string[::-1]
    return ters_string
name3 = "Albayrak"
ters_ifade = ters_cevir3(name3)
print(ters_ifade)

print("********************************************************************")


numbers = [0, 1, 4.5, 8, -7, 89, 7.08]
#SORU: numbers container'indaki tamsayilari print eden code'u yaz.
#1st way
for i in numbers:
    if isinstance(i, int):
        print(i)
print("isinstance() methodu tamsayi mi degil mi onu kontrol ediyor")    
#2nd way
for i in numbers:
    if type(i) == int:
        print(i)

print("type() ile kontrol")   

#3rd way try-except blogu
for i in numbers:
    try:
        if i == int(i):
            print(i)
    except TypeError:
        continue

print("try-except blogu ile. try kismina istenen, istenen olmazsa bir exception atma halinde except ile o hatayi yakaliyoruz ve altindaki code calisir. JAVA'daki try-catch")
#4th way list comprehension 

tamsayilar = [x for x in numbers if isinstance(x, int)]
print(tamsayilar)

print("list comprehension")
#new_list = [expression for item in iterable if condition] list comprehension yapisi
#new_list, oluşturulacak yeni liste.
# "expression", her bir item icin kullanılacak ifade veya deger.
# "item", mevcut liste üzerinde dönerken kullanılan değişken adı.
#"iterable", üzerinde döngü yapılacak olan liste, demet, dize veya başka bir iterable veri yapısı.
# "condition "(opsiyonel), isteğe bağlı bir koşul ifadesi. Eğer koşul sağlanıyorsa, sadece o item işleme dahil edilir.

#5th way filter() function
integers = list(filter(lambda x: isinstance(x, int), numbers))
print(integers)
print("filter() function")

#6th way map() function
tamsayilar1 = list(map(lambda x: x if isinstance(x, int) else None, numbers))
tamsayilar1 = list(filter(lambda x: x is not None, tamsayilar1))
print(tamsayilar1)
print("map() function")


#*******************************************************************
#while-loop

# while True:
#     print("x") infinity loop. alttaki code'a ulasilamaz
# print("y")  

i = 0
while i < 10:
    print("x")
    i += 1;
print("y")

print("*************")

while True:
    print("x")
    break

credits = [1, 1.5, 2j, [1,7],(8,9),{"city":"Ankara"}];

i = 0
while i < len(credits):
    print(credits[i])
    i+=1
    if credits[i] == {"city":"Ankara"}:
        break
