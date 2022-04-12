import numpy as np
import pandas as pd
import random as random

# Oyun matrisinin olusturulmasi
mx = np.full((10, 10), "0")
df = pd.DataFrame(mx, index=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], columns=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
#print(df)

# Gemilerin rastgele atanmasi
list = [(0,0), (0,5), (5,0), (5,5)]
amiral_matrisi = random.choice(list)
list.remove(amiral_matrisi)
muhrip_matrisi = random.choice(list)
list.remove(muhrip_matrisi)
firkateyn_matrisi = random.choice(list)
list.remove(firkateyn_matrisi)
denizalti_matrisi = random.choice(list)
list.remove(denizalti_matrisi)

# Gemilerin pozisyonlarinin belirlenmesi
amiral_pozisyon = random.randint(0, 9)
muhrip_pozisyon = random.randint(0, 19)
firkateyn_pozisyon = random.randint(0, 29)
denizalti_pozisyon = random.randint(0, 39)

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


#Muhripin konumu
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


# Firkateyn konumu
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


#Denizaltinin konumu
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





















#print(df)




































