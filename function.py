fiyat = 100
indirim = 20
# def keyword'u ile function tanimliyoruz 
def calculateWithParams(x, y):
    print(x-y) # java'daki void gibi bu method
calculateWithParams(fiyat, indirim)    


def calculateAndReturn(price, discount):
    return price - discount;
newPrice = calculateAndReturn(fiyat, indirim);
print(newPrice);