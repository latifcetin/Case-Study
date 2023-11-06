#######################################################################
# GÖREV 1: Veri Yapılarının Tiplerini İnceleyiniz.
#######################################################################

x = 8
print(type(x))

y = 3.2
print(type(y))

z = (8j + 18)
print(type(z))

a = "Hello AI Era"
print(type(a))

b = True
print(type(b))

c = 23 < 22
print(type(c))

l = [1, 2, 3 ,4, "String", 3.2, False]
print(type(l))
# Sıralıdır
# Kapsayıcıdır
# Değiştirilebilir

d = {"Name": "Jake",
     "Age": [27, 56],
     "Adress": "Downtown"}
print(type(d))
# Değiştirilebilir
# Kapsayıcı
# Sıralı

t = ("Machine Learning", "Data Science")
print(type(t))
# Değiştirilemez
# Kapsayacı
# Sıralı

s = {"Python", "Machine Learning", "Data Science", "Python"}
print(type(s))
# Değiştirilebilir
# Sırasız + Eşsiz
# Kapsayıcı

#######################################################################
# GÖREV 2: Verilen String İfadenin Tüm Harflerini Büyük Harfe Çeviriniz. Virgül ve Nokta Yerine Space Koyunuz, Kelime Kelime Ayırınız.
#######################################################################

text = "The goal is to turn data into information, and information into insight."
print(text.upper().replace(",", " ").replace(".", " ").split())

#######################################################################
# GÖREV 3: Verilen Liste İçin Aşağıdaki Görevleri Yapınız.
#######################################################################
 
lst = ['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'N', 'C', 'E']

# Adım 1: Verilen listenin eleman sayısına bakınız.
print(len(lst))

# Adım 2: Sıfırıncı ve onuncu index'teki elemanları çağırın.
print(lst[0])
print(lst[10])

# Adım 3: Veilen liste üzerinden ['D', 'A', 'T', 'A'] listesi oluşturun.
new_list = lst[:4]
print(new_list) 

# Adım 4: Sekizinci index'teki elemanı silin.
lst.pop(8)
print(lst)

# Adım 5: Yeni bir eleman ekleyin.
lst.append(101)
print(lst)

# Adım 6: Sekizinci elemana 'N' elemanını tekrar ekleyin.
lst.insert(8, 'N')
print(lst)


#######################################################################
# Görev 4: Verilen Sözlük Yapısına Aşağıdaki Adımları Uygulayınız.
#######################################################################

dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}

# Adım 1: Key değerlerine erişiniz.
print(dict.keys())

# Adım 2: Value değerlerine erişiniz.
print(dict.values())  

# Adım 3: Daisy key'ine ait 12 değerini 12 olarak güncelleyinzi.
dict['Daisy'][1] = 13

dict.update({'Daisy': ["England", 13]})
print(dict)

# Adım 4: Key değeri Ahmet, value değeri ["Turkey", 24] olan yeni bir değer ekleyiniz.
dict.update({'Ahmet': ["Turkey", 24]})
print(dict)

# Adım 5: Antonio'yu dictionary'den siliniz.
dict.pop('Antonio')
print(dict)

#######################################################################
# Görev 5: Argüman Olarak Bir Liste Alan, Listenin İçerisindeki Tek ve Çift Sayıları Ayrı Listelere Atayan ve Bu Listeleri Return Eden Fonksiyon Yazınız.
#######################################################################

l = [2, 13, 18, 93, 22]

def func(list):
    even_number_list = []
    odd_number_list = []
    for number in list:
        if number % 2 == 0:
            even_number_list.append(number)
        else:
            odd_number_list.append(number)
    return even_number_list, odd_number_list

even, odd = func(l)
print(even, odd)


#######################################################################
# Görev 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır. 
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir. 
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
#######################################################################

students = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for index, student in enumerate(students):
    if index < 3:
        index+=1
        print("Mühendislik Fakültesi", index, ". öğrenci:", student)
    else:
        print("Tıp Fakültesi", index, ". öğrenci:", student)  

#######################################################################
# Görev 7: Aşağıda 3 adet liste verilmiştir. 
# Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. 
# Zip kullanarak ders bilgilerini bastırınız.
#######################################################################

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

for ders_kodu, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
    print(f"Kredisi {kredi} olan {ders_kodu}, kodlu dersin kontenjanı {kontenjan} kişidir.")


#######################################################################
# Görev 8: Aşağıda 2 adet set verilmiştir. 
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
#######################################################################

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def kume(set1, set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))

print(kume(kume1, kume2))
print(kume(kume2, kume1))    