import random

class Kart():

    def __init__(self,desen,değer):
        self.desen=desen
        self.değer=değer

    def __str__(self):
        return "{} {}\n".format(self.desen,self.değer)

def puanhesaplama(b,puan):
    if (b == "A"):
        if (puan<=10):
            puan = puan + 11
        elif (puan > 10):
            puan = puan + 1
    elif (b == "J"):
        puan = puan + 10
    elif (b == "Q"):
        puan = puan + 10
    elif (b == "K"):
        puan = puan + 10
    else:
        puan = puan + b

    return  puan

deste=[]
desen=["maça","sinek","kupa","karo"]
değer=["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]

for i in desen:
    for j in değer:
        deste.append(Kart(i,j))

print("OYUNCU 1 SEÇİM")
oyuncu1=[]

while True:
    i=0
    puan=0
    while i<2:
        x= random.choice(deste)
        deste.remove(x)
        print(x)
        oyuncu1.append(x)
        puan=puanhesaplama(x.değer,puan)
        i += 1
    print("Puanınız : ", puan)

    while puan<21:
        print("KART SEÇMEK İSTER MİSİNİZ : EVET İSE 'E' HAYIR İSE 'H' TUŞLAYINIZ")
        a=input()
        if(a=="E"):
            x = random.choice(deste)
            deste.remove(x)
            print("Seçtiğiniz Kart : ", x)
            oyuncu1.append(x)
            puan=puanhesaplama(x.değer,puan)
            print("Puanınız : ", puan)
        if(a=="H"):
            print("Puanınız : ", puan)
            break
    break

print("OYUNCU 2 SEÇİM")
oyuncu2=[]

while True:
    i=0
    puan1=0
    while i<2:
        x= random.choice(deste)
        deste.remove(x)
        print(x)
        oyuncu2.append(x)
        puan1=puanhesaplama(x.değer,puan1)
        i += 1
    print("Puanınız : ", puan1)

    while puan1<21:
        print("KART SEÇMEK İSTER MİSİNİZ : EVET İSE 'E' HAYIR İSE 'H' TUŞLAYINIZ")
        a=input()
        if(a=="E"):
            x = random.choice(deste)
            deste.remove(x)
            print("Seçtiğiniz Kart : ", x)
            oyuncu2.append(x)
            puan1=puanhesaplama(x.değer,puan1)
            print("Puanınız : ", puan1)
        if(a=="H"):
            print("Puanınız : ", puan1)
            break
    break

print("KASA SEÇİM")
kasa=[]

while True:
    i=0
    kasapuan=0
    while i<2:
        x= random.choice(deste)
        deste.remove(x)
        print(x)
        oyuncu2.append(x)
        kasapuan=puanhesaplama(x.değer,kasapuan)
        i += 1
    print("Puanınız : ", kasapuan)

    while kasapuan<21:
        if kasapuan<17:
            x = random.choice(deste)
            deste.remove(x)
            print("Seçtiğiniz Kart : ", x)
            oyuncu2.append(x)
            kasapuan = puanhesaplama(x.değer, kasapuan)
            print("Puanınız : ", kasapuan)
        else:
            print("KART SEÇMEK İSTER MİSİNİZ : EVET İSE 'E' HAYIR İSE 'H' TUŞLAYINIZ")
            a=input()
            if(a=="E"):
                x = random.choice(deste)
                deste.remove(x)
                print("Seçtiğiniz Kart : ", x)
                oyuncu2.append(x)
                kasapuan=puanhesaplama(x.değer,kasapuan)
                print("Puanınız : ", kasapuan)
            if(a=="H"):
                print("Puanınız : ", kasapuan)
                break
    break


if(puan1>21 and puan>21 and kasapuan>21):
    print("KAZANAN YOK")
if(puan<=21 and puan1<=21 and kasapuan<=21):
    if(puan>puan1 and puan>kasapuan):
        print("Oyuncu1 Kazandı")
    elif(puan<puan1 and kasapuan<puan1):
        print("Oyuncu2 Kazandı")
    elif(kasapuan>puan and kasapuan>puan1):
        print("KASA KAZANDI...")
    else:
        print("berabere")
elif(puan1>21 and puan<=21 and kasapuan>21):
    print("Oyuncu1 KAZANDI")
elif(puan1<=21 and puan>21 and kasapuan>21):
    print("OYUNCU2 KAZANDI")
elif(kasapuan<=21 and puan>21 and puan1>21):
    print("KASA KAZANDI")
elif(puan1<=21 and puan<=21 and kasapuan>21):
    if(puan1>puan):
        print("OYUNCU2 KAZANDI")
    elif(puan>puan1):
        print("OYUNCU1 KAZANDI")
    else:
        print("BERABERE")

elif(puan1<=21 and puan>21 and kasapuan<=21):
    if(puan1>kasapuan):
        print("OYUNCU2 KAZANDI")
    elif(kasapuan>puan1):
        print("KASA KAZANDI")
    else:
        print("BERABERE")

elif(puan1>21 and puan<=21 and kasapuan<=21):
    if(puan>kasapuan):
        print("OYUNCU1 KAZANDI")
    elif(kasapuan>puan):
        print("KASA KAZANDI")
    else:
        print("BERABERE")

print(len(deste))
