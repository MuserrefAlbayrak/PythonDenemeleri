faiz = 1.59;
vade = 36;
krediAdi = "Ihtiyac Kredisi"
#type conversion
print(type(faiz)) #degisken tipini ogrenmek istedigimde type() ile bunu yapabilmekteyim
print(vade + int(faiz)) #faiz float data type idi int() icine aldim 
print(str(faiz)); #string'e dondurmek icin str()
vade = int(input("Lutfen istediginiz vade sayisini giriniz: "));
#Kullanicidan alinan input default olarak String data type'tir. Python'in ozelligi.
#ihtiyaca gore hangi data type olmaliysa input()'u istenilen data type'a donusturebilirsin.
vade = vade + 12
# String Interpolation
#Kullanicinin girdigi deger sonucu elde edilen vade: 
print("sectiginiz vade sonucu elde edilen vade : {vadeSayisi}".format(vadeSayisi=vade));
print(type(f"sectiginiz vade sonucu elde edilen vade : {vade}"));
#string concatination java mantiginda degil burada biraz. simdi; atring ifade icerisinde {} icerisine bir replika name tanimla
#daha sonra o tanimlanan name'i sitring disinda .format() icerisinde istenen container'a esitle.

#2nd way. f-string => yaygin olan
name = "Muserref"
text = f"Welcome {name}"
print(text);

x = 12

#print("Add result = {add}".format(add=(x)))
print(type(x))
metin = f"Welcome {x}"
print(metin); # output=> Welcome 12

number = int(input("Lutfen tam bir sayi giriniz: "))
number = f"girdiginiz sayi = {number}" 
print(type(number)); #output => <class 'str'>
print(number); #girdiginiz sayi = 23