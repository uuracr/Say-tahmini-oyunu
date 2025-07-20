import random as r
print("sayı tahmin oyunu".upper())
tutulan = r. randint(1,100)
min = 1
max = 100
hak= 7
tutulan =r.randint(min, max)
print("1 ile 100 arasında bir sayı tuttum. Tahmin et bakalım!")
for a in range(hak):
    tahmin = int(input("tahminin nedir?"))
    if tahmin == tutulan:
        print("Tebrikler! Doğru tahmin ettin.")
        break
    elif tahmin < tutulan:
        print("Daha yüksek bir sayı dene.")
        min = tahmin + 1   
    elif tahmin > tutulan:
        print("Daha düşük bir sayı dene.")
        max = tahmin - 1
    if a == hak - 1:
        print(f"Üzgünüm, hakkın bitti. Tutulan sayı {tutulan} idi.")
        

    
    
