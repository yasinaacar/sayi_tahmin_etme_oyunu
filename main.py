from ast import While
import time
import random

def tahminet():
    sayi=random.randint(1,100) #programın rastgele bir sayı oluşturması için tanımladığımız değişken
    can=3 #oyun için default olarak gelen can sayımız 

    while True: #programın break komutuna getirine kadar devam etmesini sağlayan döngü

        try: #hata yakalam için yazdığımız alan. Eğer kullanıcı integer değer dışında bir değer girerse programın çökmemesini sağlıyor
            tahmin=int(input("1 ile 100 arasında bir sayı giriniz:\t")) #kullanıcıdan alınan tahmini sayı girdisi
        except:
            print("Lütfen sadece 1 ile 100 arasında bir tam sayı değeri giriniz..") #integer dışında bir değer girildiğinde ekrana basılacak uyarı
            continue
        
        if tahmin==sayi:
            print("Tebrikler DOĞRU tahmin...")
            devam=input("Devam Etmek İstiyor Musunuz? E/H:\t").upper()
            if (devam=="E"): #cevap doğru olursa ve kullanıcı devam etmek isterse tüm oyun değişkenlerini başa alıyoruz
                can=3
                sayi=random.randint(1,100)
                print(sayi)
                continue
            elif (devam=="H"):
                print("Oyun sonladırılıyor...")
                time.sleep(0.5)
                print("OYUN SONLANDIRILDI")
                break

            
        
        elif tahmin<sayi:
            print("Tahmininiz YANLIŞ. Daha büyük bir sayı giriniz:\t")
            can=can-1
            print("Kalan CAN SAYISI {}".format(can))
            if can==0:
                print("Canlarınız tükendi. Doğru cevap = {}".format(sayi))
                devam=input("Devam Etmek İstiyor Musunuz? E/H:\t").upper()
                if (devam=="E"):
                    can=3
                    sayi=random.randint(1,100)
                    print(sayi)
                    continue
                elif (devam=="H"):
                    print("Oyun sonladırılıyor...")
                    time.sleep(0.5)
                    print("OYUN SONLANDIRILDI")
                    break

            elif can>0:
                continue

        elif tahmin>sayi:
            print("Tahmininiz YANLIŞ. Daha küçük bir sayı seçin:\t")
            can=can-1
            print("Kalan CAN SAYISI {}".format(can))
            if can==0:
                print("Canlarınız tükendi. Doğru cevap = {}".format(sayi))
                devam=input("Devam Etmek İstiyor Musunuz? E/H:\t").upper()
                if (devam=="E"):
                    can=3
                    sayi=random.randint(1,100)
                    print(sayi)
                    continue
                elif (devam=="H"):
                    print("Oyun sonladırılıyor...")
                    time.sleep(0.5)
                    print("OYUN SONLANDIRILDI")
                    break
            elif can>0:
                continue

        

def gerisayim(): #bu kısım program çalıştırıldığında geri sayım yaparak oyunu başlatan fonksiyon
    zaman=3
    for i in range(3):
        time.sleep(1)
        anlik=i+1
        print(anlik)
        if anlik==3:
            print("Oyun başlıyor...")

print("Sayı tahmin etme oyununa hoşgeldiniz")
gerisayim()
tahminet()



