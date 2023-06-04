# lists
credits = ["Ihtiyac Kredisi","Tasit Kredisi","Konut Kredisi"];
print(type(credits)); #<class 'list'>
print(credits[0]); #list logic, java'daki ile ayni.
#print(credits[5]); # IndexError: list index out of range
print(len(credits)); #list'in uzunlugu 3. java'daki length, python'da len() 

arrays = ["Ihtiyac Kredisi", True, 10, 10.5];
print(arrays); #output = > ['Ihtiyac Kredisi', True, 10, 10.5]. farkli data type yazilabiliyor. 
credits.append("Ozel Krediler"); # append() fonksiyonu credits list'ine en sona eleman ekliyor. 
print(credits);
credits.pop();
print(credits);
credits.pop(1);
print(credits);
#pop() methodu default olarak son elemani algilar ve siler. eger methodun icine silmek istedigin elemanin index'ini girersen o elemani siler.

credits.remove("Ihtiyac Kredisi");
print(credits);
# remove() method'u ise pop() gibi index degil de deger bazli ilerler ve girilen degeri ilk gordugu anda siler. 
credits.extend(["X Kredisi","Y Kredisi","Z Kredisi"])
print(credits)
# extend() methodu ile tek satirda birden fazla eleman eklenebiliyor. 

#Python'da liste icinde elemanlar ayni data type'ta olmak zorunda degildir.
list = [1, 1.5, 2j, [1,7],(8,9),{"city":"Ankara"}]
print(list); #integer, float, complex,list,  tuple, dictonary
# tuple; list veri tipi gibi sirali elemanlardan olusur. aralarindaki fark ise;
# tuple degistirilemez (immutable), list ise degistirilebilir (mutable)

print(type(list[4]))
tuple = (0,1, "Ankara",True);
print(tuple)
dictionary = {"city":"Ankara","id":11,1:12}
print(dictionary)
# dictionary = dictionary.keys()
# print(dictionary) # dict_keys(['city', 'id', 1])
dictionary = dictionary.values()
print(dictionary) # dict_values(['Ankara', 11, 12])

# note: string ve tuple veri tiplerinde araya eleman ekleme ve cikarma islemlerini yapamiyoruz. ustte yazdin:) 


newList = [0, 1, 2, 3, 4, 5, 6, 7]
newList2 = ["Ankara", "Balikesir", 8]
newList = newList + newList2
print(newList); # output => [0, 1, 2, 3, 4, 5, 6, 7, 'Ankara', 'Balikesir', 8]

del newList[0] # del komutu ile istedigin indexteki elemani silebilirsin. 
print(newList) # [1, 2, 3, 4, 5, 6, 7, 'Ankara', 'Balikesir', 8]

newList.insert(7,"Tandogan");# insert() methodu eklenen elemanla birlikte bu eklenen elemanin istenen indexteki yerini belirterek kullandigimiz yardimci functiondir.

print(newList)
newList.reverse();#list elemanlarini ters ceviren method
print(newList);
#2nd way
newList[::-1] #burada da list elemanlarini bu syntax ile ters cevirmekteyim.
print(newList)


print(newList.index("Balikesir")); # index() girilen degerin bulundugu en dusuk index nosunu verir. buradaki icin 1. 

newList3 = [2, 3, "Edremit", "Yenimahalle", 7];
newList4 = newList3.copy();
newList3[0] = 5;

print(newList4)
