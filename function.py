fiyat = 100
indirim = 20
# def keyword'u ile function tanimliyoruz 
def calculateWithParams(x, y):
    print(x-y) # java'daki void gibi bu method
calculateWithParams(fiyat, indirim)  
print(calculateWithParams(fiyat, indirim)) # output = > None. Java'da boyle bir sey yaptiginda compile time error aliyordun. 
#***********************************************************************
def calculateAndReturn(price, discount):
    return price - discount;
newPrice = calculateAndReturn(fiyat, indirim);
print(newPrice);
#***********************************************************************
def textConcat(text1, text2):
    return text1 + text2;
concat = textConcat("mu", "serref")
print(concat);
print(textConcat("muserref" , f" {17}"))
#***********************************************************************
str = {"id":1, "city":"Ankara", "job title": "SDET"}
str2 = {"userId":2, "country":"Turkey", "company": "ASIS"}
def mergedMap(x, y):
    newMap = dict(x, **y)
    return newMap
print(mergedMap(str, str2))