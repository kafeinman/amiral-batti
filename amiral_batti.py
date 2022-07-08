import numpy as np
import pandas as pd
import random as rd

# Oyun matrisinin olusturulmasi
mx = np.full((10, 10), "0")
df = pd.DataFrame(mx, index=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], columns=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
cf = pd.DataFrame(mx, index=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], columns=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])

#print(df)

# Gemilerin rastgele atanmasi
list = [(0,0), (0,5), (5,0), (5,5)]
amiral_matrisi = rd.choice(list)
list.remove(amiral_matrisi)
muhrip_matrisi = rd.choice(list)
list.remove(muhrip_matrisi)
firkateyn_matrisi = rd.choice(list)
list.remove(firkateyn_matrisi)
denizalti_matrisi = rd.choice(list)
list.remove(denizalti_matrisi)

# Gemilerin pozisyonlarinin belirlenmesi
amiral_pozisyon = rd.randint(0, 9)
muhrip_pozisyon = rd.randint(0, 19)
firkateyn_pozisyon = rd.randint(0, 29)
denizalti_pozisyon = rd.randint(0, 39)

#print(amiral_matrisi, amiral_pozisyon)
#print(muhrip_matrisi, muhrip_pozisyon)
#print(firkateyn_matrisi, firkateyn_pozisyon)
#print(denizalti_matrisi, denizalti_pozisyon)

# Amiralin konumu
if(amiral_matrisi == (0, 0)):
    if(amiral_pozisyon < 5):
        amiral_baslangic = [amiral_pozisyon, 0]
        amiral_bitis = [amiral_pozisyon, 4]
    else:
        amiral_baslangic = [0, amiral_pozisyon - 5]
        amiral_bitis = [4, amiral_pozisyon - 5]
elif(amiral_matrisi == (0, 5)):
    if(amiral_pozisyon < 5):
        amiral_baslangic = [amiral_pozisyon, 5]
        amiral_bitis = [amiral_pozisyon, 9]
    else:
        amiral_baslangic = [0, amiral_pozisyon]
        amiral_bitis = [4, amiral_pozisyon]
elif(amiral_matrisi == (5, 0)):
    if(amiral_pozisyon < 5):
        amiral_baslangic = [5 + amiral_pozisyon, 0]
        amiral_bitis = [5 + amiral_pozisyon, 4]
    else:
        amiral_baslangic = [5, amiral_pozisyon - 5]
        amiral_bitis = [9, amiral_pozisyon - 5]
elif(amiral_matrisi == (5, 5)):
    if(amiral_pozisyon < 5):
        amiral_baslangic = [5+ amiral_pozisyon, 5]
        amiral_bitis = [5+ amiral_pozisyon, 9]
    else:
        amiral_baslangic = [5, amiral_pozisyon]
        amiral_bitis = [9, amiral_pozisyon]

#print(amiral_baslangic[0], amiral_baslangic[1])
#print(amiral_bitis[0], amiral_bitis[1])

if(amiral_baslangic[1] == amiral_bitis[1]):
    df.iloc[amiral_baslangic[0]:amiral_bitis[0]+1, amiral_bitis[1]] = 5
else:
    df.iloc[amiral_baslangic[0], amiral_baslangic[1]:amiral_bitis[1]+1] = 5


# Muhripin konumu
if(muhrip_matrisi == (0, 0)):
    if(muhrip_pozisyon < 5):
        muhrip_baslangic = [muhrip_pozisyon, 0]
        muhrip_bitis = [muhrip_pozisyon, 3]
    elif(muhrip_pozisyon < 10):
        muhrip_baslangic = [muhrip_pozisyon - 5, 1]
        muhrip_bitis = [muhrip_pozisyon - 5, 4]
    elif(muhrip_pozisyon < 15):
        muhrip_baslangic = [0, muhrip_pozisyon - 10]
        muhrip_bitis = [3, muhrip_pozisyon - 10]
    else:
        muhrip_baslangic = [1, muhrip_pozisyon - 15]
        muhrip_bitis = [4, muhrip_pozisyon - 15]
if(muhrip_matrisi == (0, 5)):
    if(muhrip_pozisyon < 5):
        muhrip_baslangic = [muhrip_pozisyon, 5]
        muhrip_bitis = [muhrip_pozisyon, 8]
    elif(muhrip_pozisyon < 10):
        muhrip_baslangic = [muhrip_pozisyon - 5, 6]
        muhrip_bitis = [muhrip_pozisyon - 5, 9]
    elif(muhrip_pozisyon < 15):
        muhrip_baslangic = [0, muhrip_pozisyon - 5]
        muhrip_bitis = [3, muhrip_pozisyon - 5]
    else:
        muhrip_baslangic = [1, muhrip_pozisyon - 10]
        muhrip_bitis = [4, muhrip_pozisyon - 10]
if(muhrip_matrisi == (5, 0)):
    if(muhrip_pozisyon < 5):
        muhrip_baslangic = [muhrip_pozisyon + 5, 0]
        muhrip_bitis = [muhrip_pozisyon + 5, 3]
    elif(muhrip_pozisyon < 10):
        muhrip_baslangic = [muhrip_pozisyon, 1]
        muhrip_bitis = [muhrip_pozisyon, 4]
    elif(muhrip_pozisyon < 15):
        muhrip_baslangic = [5, muhrip_pozisyon - 10]
        muhrip_bitis = [8, muhrip_pozisyon - 10]
    else:
        muhrip_baslangic = [6, muhrip_pozisyon - 15]
        muhrip_bitis = [9, muhrip_pozisyon - 15]
if(muhrip_matrisi == (5, 5)):
    if(muhrip_pozisyon < 5):
        muhrip_baslangic = [muhrip_pozisyon + 5, 5]
        muhrip_bitis = [muhrip_pozisyon + 5, 8]
    elif(muhrip_pozisyon < 10):
        muhrip_baslangic = [muhrip_pozisyon, 6]
        muhrip_bitis = [muhrip_pozisyon, 9]
    elif(muhrip_pozisyon < 15):
        muhrip_baslangic = [5, muhrip_pozisyon - 5]
        muhrip_bitis = [8, muhrip_pozisyon - 5]
    else:
        muhrip_baslangic = [6, muhrip_pozisyon - 10]
        muhrip_bitis = [9, muhrip_pozisyon - 10]


#print(muhrip_baslangic[0], muhrip_baslangic[1])
#print(muhrip_bitis[0], muhrip_bitis[1])

if(muhrip_baslangic[1] == muhrip_bitis[1]):
    df.iloc[muhrip_baslangic[0]:muhrip_bitis[0]+1, muhrip_bitis[1]] = 4
else:
    df.iloc[muhrip_baslangic[0], muhrip_baslangic[1]:muhrip_bitis[1]+1] = 4


# Firkateynin konumu
if(firkateyn_matrisi == (0, 0)):
    if(firkateyn_pozisyon < 5):
        firkateyn_baslangic = [firkateyn_pozisyon, 0]
        firkateyn_bitis = [firkateyn_pozisyon, 2]
    elif(firkateyn_pozisyon < 10):
        firkateyn_baslangic = [firkateyn_pozisyon - 5, 1]
        firkateyn_bitis = [firkateyn_pozisyon - 5, 3]
    elif(firkateyn_pozisyon < 15):
        firkateyn_baslangic = [firkateyn_pozisyon - 10, 2]
        firkateyn_bitis = [firkateyn_pozisyon - 10, 4]
    elif(firkateyn_pozisyon < 20):
        firkateyn_baslangic = [0, firkateyn_pozisyon - 15]
        firkateyn_bitis = [2, firkateyn_pozisyon - 15]
    elif(firkateyn_pozisyon < 25):
        firkateyn_baslangic = [1, firkateyn_pozisyon - 20]
        firkateyn_bitis = [3, firkateyn_pozisyon - 20]
    elif(firkateyn_pozisyon < 30):
        firkateyn_baslangic = [2, firkateyn_pozisyon - 25]
        firkateyn_bitis = [4, firkateyn_pozisyon - 25]
if(firkateyn_matrisi == (0, 5)):
    if(firkateyn_pozisyon < 5):
        firkateyn_baslangic = [firkateyn_pozisyon, 5]
        firkateyn_bitis = [firkateyn_pozisyon, 7]
    elif(firkateyn_pozisyon < 10):
        firkateyn_baslangic = [firkateyn_pozisyon - 5, 6]
        firkateyn_bitis = [firkateyn_pozisyon - 5, 8]
    elif(firkateyn_pozisyon < 15):
        firkateyn_baslangic = [firkateyn_pozisyon - 10, 7]
        firkateyn_bitis = [firkateyn_pozisyon - 10, 9]
    elif(firkateyn_pozisyon < 20):
        firkateyn_baslangic = [0, firkateyn_pozisyon - 10]
        firkateyn_bitis = [2, firkateyn_pozisyon - 10]
    elif(firkateyn_pozisyon < 25):
        firkateyn_baslangic = [1, firkateyn_pozisyon - 15]
        firkateyn_bitis = [3, firkateyn_pozisyon - 15]
    elif(firkateyn_pozisyon < 30):
        firkateyn_baslangic = [2, firkateyn_pozisyon - 20]
        firkateyn_bitis = [4, firkateyn_pozisyon - 20]
if(firkateyn_matrisi == (5, 0)):
    if(firkateyn_pozisyon < 5):
        firkateyn_baslangic = [firkateyn_pozisyon + 5, 0]
        firkateyn_bitis = [firkateyn_pozisyon + 5, 2]
    elif(firkateyn_pozisyon < 10):
        firkateyn_baslangic = [firkateyn_pozisyon, 1]
        firkateyn_bitis = [firkateyn_pozisyon, 3]
    elif(firkateyn_pozisyon < 15):
        firkateyn_baslangic = [firkateyn_pozisyon - 5, 2]
        firkateyn_bitis = [firkateyn_pozisyon - 5, 4]
    elif(firkateyn_pozisyon < 20):
        firkateyn_baslangic = [5, firkateyn_pozisyon - 15]
        firkateyn_bitis = [7, firkateyn_pozisyon - 15]
    elif(firkateyn_pozisyon < 25):
        firkateyn_baslangic = [6, firkateyn_pozisyon - 20]
        firkateyn_bitis = [8, firkateyn_pozisyon - 20]
    elif(firkateyn_pozisyon < 30):
        firkateyn_baslangic = [7, firkateyn_pozisyon - 25]
        firkateyn_bitis = [9, firkateyn_pozisyon - 25]
if(firkateyn_matrisi == (5, 5)):
    if(firkateyn_pozisyon < 5):
        firkateyn_baslangic = [firkateyn_pozisyon + 5, 5]
        firkateyn_bitis = [firkateyn_pozisyon + 5, 7]
    elif(firkateyn_pozisyon < 10):
        firkateyn_baslangic = [firkateyn_pozisyon, 6]
        firkateyn_bitis = [firkateyn_pozisyon, 8]
    elif(firkateyn_pozisyon < 15):
        firkateyn_baslangic = [firkateyn_pozisyon - 5, 7]
        firkateyn_bitis = [firkateyn_pozisyon - 5, 9]
    elif(firkateyn_pozisyon < 20):
        firkateyn_baslangic = [5, firkateyn_pozisyon - 10]
        firkateyn_bitis = [7, firkateyn_pozisyon - 10]
    elif(firkateyn_pozisyon < 25):
        firkateyn_baslangic = [6, firkateyn_pozisyon - 15]
        firkateyn_bitis = [8, firkateyn_pozisyon - 15]
    elif(firkateyn_pozisyon < 30):
        firkateyn_baslangic = [7, firkateyn_pozisyon - 20]
        firkateyn_bitis = [9, firkateyn_pozisyon - 20]


#print(firkateyn_baslangic[0], firkateyn_baslangic[1])
#print(firkateyn_bitis[0], firkateyn_bitis[1])

if(firkateyn_baslangic[1] == firkateyn_bitis[1]):
    df.iloc[firkateyn_baslangic[0]:firkateyn_bitis[0]+1, firkateyn_bitis[1]] = 3
else:
    df.iloc[firkateyn_baslangic[0], firkateyn_baslangic[1]:firkateyn_bitis[1]+1] = 3


# Denizaltinin konumu
if(denizalti_matrisi == (0, 0)):
    if(denizalti_pozisyon < 5):
        denizalti_baslangic = [denizalti_pozisyon, 0]
        denizalti_bitis = [denizalti_pozisyon, 1]
    elif(denizalti_pozisyon < 10):
        denizalti_baslangic = [denizalti_pozisyon - 5, 1]
        denizalti_bitis = [denizalti_pozisyon - 5, 2]
    elif(denizalti_pozisyon < 15):
        denizalti_baslangic = [denizalti_pozisyon - 10, 2]
        denizalti_bitis = [denizalti_pozisyon - 10, 3]
    elif(denizalti_pozisyon < 20):
        denizalti_baslangic = [denizalti_pozisyon - 15, 3]
        denizalti_bitis = [denizalti_pozisyon - 15, 4]
    elif(denizalti_pozisyon < 25):
        denizalti_baslangic = [0, denizalti_pozisyon - 20]
        denizalti_bitis = [1, denizalti_pozisyon - 20]
    elif(denizalti_pozisyon < 30):
        denizalti_baslangic = [1, denizalti_pozisyon - 25]
        denizalti_bitis = [2, denizalti_pozisyon - 25]
    elif(denizalti_pozisyon < 35):
        denizalti_baslangic = [2, denizalti_pozisyon - 30]
        denizalti_bitis = [3, denizalti_pozisyon - 30]
    elif(denizalti_pozisyon < 40):
        denizalti_baslangic = [3, denizalti_pozisyon - 35]
        denizalti_bitis = [4, denizalti_pozisyon - 35]
if(denizalti_matrisi == (0, 5)):
    if(denizalti_pozisyon < 5):
        denizalti_baslangic = [denizalti_pozisyon, 5]
        denizalti_bitis = [denizalti_pozisyon, 6]
    elif(denizalti_pozisyon < 10):
        denizalti_baslangic = [denizalti_pozisyon - 5, 6]
        denizalti_bitis = [denizalti_pozisyon - 5, 7]
    elif(denizalti_pozisyon < 15):
        denizalti_baslangic = [denizalti_pozisyon - 10, 7]
        denizalti_bitis = [denizalti_pozisyon - 10, 8]
    elif(denizalti_pozisyon < 20):
        denizalti_baslangic = [denizalti_pozisyon - 15, 8]
        denizalti_bitis = [denizalti_pozisyon - 15, 9]
    elif(denizalti_pozisyon < 25):
        denizalti_baslangic = [0, denizalti_pozisyon - 15]
        denizalti_bitis = [1, denizalti_pozisyon - 15]
    elif(denizalti_pozisyon < 30):
        denizalti_baslangic = [1, denizalti_pozisyon - 20]
        denizalti_bitis = [2, denizalti_pozisyon - 20]
    elif(denizalti_pozisyon < 35):
        denizalti_baslangic = [2, denizalti_pozisyon - 25]
        denizalti_bitis = [3, denizalti_pozisyon - 25]
    elif(denizalti_pozisyon < 40):
        denizalti_baslangic = [3, denizalti_pozisyon - 30]
        denizalti_bitis = [4, denizalti_pozisyon - 30]
if(denizalti_matrisi == (5, 0)):
    if(denizalti_pozisyon < 5):
        denizalti_baslangic = [denizalti_pozisyon + 5, 0]
        denizalti_bitis = [denizalti_pozisyon + 5, 1]
    elif(denizalti_pozisyon < 10):
        denizalti_baslangic = [denizalti_pozisyon, 1]
        denizalti_bitis = [denizalti_pozisyon, 2]
    elif(denizalti_pozisyon < 15):
        denizalti_baslangic = [denizalti_pozisyon - 5, 2]
        denizalti_bitis = [denizalti_pozisyon - 5, 3]
    elif(denizalti_pozisyon < 20):
        denizalti_baslangic = [denizalti_pozisyon - 10, 3]
        denizalti_bitis = [denizalti_pozisyon - 10, 4]
    elif(denizalti_pozisyon < 25):
        denizalti_baslangic = [5, denizalti_pozisyon - 20]
        denizalti_bitis = [6, denizalti_pozisyon - 20]
    elif(denizalti_pozisyon < 30):
        denizalti_baslangic = [6, denizalti_pozisyon - 25]
        denizalti_bitis = [7, denizalti_pozisyon - 25]
    elif(denizalti_pozisyon < 35):
        denizalti_baslangic = [7, denizalti_pozisyon - 30]
        denizalti_bitis = [8, denizalti_pozisyon - 30]
    elif(denizalti_pozisyon < 40):
        denizalti_baslangic = [8, denizalti_pozisyon - 35]
        denizalti_bitis = [9, denizalti_pozisyon - 35]
if(denizalti_matrisi == (5, 5)):
    if(denizalti_pozisyon < 5):
        denizalti_baslangic = [denizalti_pozisyon + 5, 5]
        denizalti_bitis = [denizalti_pozisyon + 5, 6]
    elif(denizalti_pozisyon < 10):
        denizalti_baslangic = [denizalti_pozisyon, 6]
        denizalti_bitis = [denizalti_pozisyon, 7]
    elif(denizalti_pozisyon < 15):
        denizalti_baslangic = [denizalti_pozisyon - 5, 7]
        denizalti_bitis = [denizalti_pozisyon - 5, 8]
    elif(denizalti_pozisyon < 20):
        denizalti_baslangic = [denizalti_pozisyon - 10, 8]
        denizalti_bitis = [denizalti_pozisyon - 10, 9]
    elif(denizalti_pozisyon < 25):
        denizalti_baslangic = [5, denizalti_pozisyon - 15]
        denizalti_bitis = [6, denizalti_pozisyon - 15]
    elif(denizalti_pozisyon < 30):
        denizalti_baslangic = [6, denizalti_pozisyon - 20]
        denizalti_bitis = [7, denizalti_pozisyon - 20]
    elif(denizalti_pozisyon < 35):
        denizalti_baslangic = [7, denizalti_pozisyon - 25]
        denizalti_bitis = [8, denizalti_pozisyon - 25]
    elif(denizalti_pozisyon < 40):
        denizalti_baslangic = [8, denizalti_pozisyon - 30]
        denizalti_bitis = [9, denizalti_pozisyon - 30]


#print(denizalti_baslangic[0], denizalti_baslangic[1])
#print(denizalti_bitis[0], denizalti_bitis[1])

if(denizalti_baslangic[1] == denizalti_bitis[1]):
    df.iloc[denizalti_baslangic[0]:denizalti_bitis[0]+1, denizalti_bitis[1]] = 2
else:
    df.iloc[denizalti_baslangic[0], denizalti_baslangic[1]:denizalti_bitis[1]+1] = 2


# Mayin gemisinin konumu
while True:
    x = rd.randint(0, 9)
    y = rd.randint(0, 9)
    k = int(df.iloc[x, y])
    if(k == 0):
        df.iloc[x, y] = 1
        #print(df)
        break


# Kullanici girisi
check_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

j = 0
def kullanici_girisi():
    global j
    j += 1
    girdi = input(str(j) + '.Atış lütfen tahminizi giriniz: ')

    if(girdi_kontrol(girdi) == True):
        if len(girdi) == 1:

            if(girdi == 'r'):
                j -= 1

                print("------------------------------------")
                print(str(j) + ' atış denemesi yaptınız.')

                if(mayin_count == -1):
                    print('Mayın gemisi battı.')
                else:
                    print('Mayın gemisi hiç isabet almadı.')
                if(denizalti_count == -1):
                    print('Denizaltı battı.')
                elif(denizalti_count == 1):
                    print("Denizaltı hiç isabet almadı.")
                else:
                    print('Denizaltı ' + str(1 - denizalti_count) + ' isabet aldı.')
                if(firkateyn_count == -1):
                    print('Fırkateyn battı.')
                elif(firkateyn_count == 2):
                    print("Fırkateyn hiç isabet almadı.")
                else:
                    print('Fırkateyn ' + str(2 - firkateyn_count) + ' isabet aldı.')
                if(muhrip_count == -1):
                    print('Muhrip gemisi battı.')
                elif(muhrip_count == 3):
                    print("Muhrip gemisi hiç isabet almadı.")
                else:
                    print('Muhrip ' + str(3 - muhrip_count) + ' isabet aldı.')
                if(amiral_count == -1):
                    print('Amiral gemisi battı.')
                elif(amiral_count == 4):
                    print("Amiral gemisi hiç isabet almadı.")
                else:
                    print('Amiral gemisi ' + str(4 - amiral_count) + ' isabet aldı.')

                print("------------------------------------")
                kullanici_girisi()

            elif(girdi == 'q'):
                print("Programdan çıkıldı.")
                quit()

            else:
                j -= 1
                print("Hata : sayılar 1 ile 10 harfler de A ile J arasında olmalıdır. Tekrar giriniz.")
                kullanici_girisi()

        elif len(girdi) == 2:
            a = girdi[0]
            b = girdi[1]
            atis_kontol(a, b)

        else:
            a = girdi[0] + girdi[1]
            b = girdi[2]
            atis_kontol(a, b)

    elif(girdi_kontrol(girdi) == False):
        print("Hata : sayılar 1 ile 10 harfler de A ile J arasında olmalıdır. Tekrar giriniz.")
        kullanici_girisi()

def girdi_kontrol(girdi):
    if len(girdi) == 1 and girdi == 'r' or 'q':
        return True

    elif len(girdi) == 2:
        a = girdi[0]
        b = girdi[1]
        if (a in check_list and b in check_list):
            return True
        else:
            return False
    elif len(girdi) == 3:
        a = girdi[0] + girdi[1]
        b = girdi[2]
        if (a in check_list and b in check_list):
            return True
        else:
            return False
    else:
        return False

#print(df)
print(cf)

mayin_count = 0
denizalti_count = 1
firkateyn_count = 2
muhrip_count = 3
amiral_count = 4

def atis_kontol(a, b):

    global mayin_count
    global denizalti_count
    global firkateyn_count
    global muhrip_count
    global amiral_count

    atis = int(df.loc[a, b])

    if(mayin_count > 0 or denizalti_count > 0 or firkateyn_count > 0 or muhrip_count > 0 or amiral_count > 0):
        if (atis == 0):
            print("Atış Başarısız. Lütfen tekrar deneyiniz.")
            cf.loc[a, b] = 'X'
            df.loc[a, b] = '6'
            print(cf)
            kullanici_girisi()
        elif(atis == 1):
            mayin_count -= 1
            cf.loc[a, b] = '*'
            df.loc[a, b] = '6'
            print(cf)
            print("Mayın gemisi battı!")
            kullanici_girisi()
        elif(atis == 2):
            denizalti_count -= 1
            cf.loc[a, b] = '*'
            df.loc[a, b] = '6'
            print(cf)
            if(denizalti_count == -1):
                print("Denizaltı battı!")
            else:
                print("Denizaltı vuruldu!")
            kullanici_girisi()
        elif(atis == 3):
            firkateyn_count -= 1
            cf.loc[a, b] = '*'
            df.loc[a, b] = '6'
            print(cf)
            if(firkateyn_count == -1):
                print("Fırkateyn battı!")
            else:
                print("Fırkateyn vuruldu!")
            kullanici_girisi()
        elif(atis == 4):
            muhrip_count -= 1
            cf.loc[a, b] = '*'
            df.loc[a, b] = '6'
            print(cf)
            if(muhrip_count == -1):
                print("Muhrip battı!")
            else:
                print("Muhrip vuruldu!")
            kullanici_girisi()
        elif(atis == 5):
            amiral_count -= 1
            cf.loc[a, b] = '*'
            df.loc[a, b] = '6'
            print(cf)
            if(amiral_count == -1):
                print("Amiral battı!")
            else:
                print("Amiral vuruldu!")
            kullanici_girisi()
        else:
            print("Aynı yere atış yapamazsınız! Lütfen tekrar deneyin.")
            kullanici_girisi()

    else:
        cf.loc[a, b] = '*'
        df.loc[a, b] = '6'
        print(cf)
        print('Tebrikler! ' + str(j) + '.atışta oyunu kazandınız.')


kullanici_girisi()




