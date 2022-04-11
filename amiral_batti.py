import numpy as np
import pandas as pd
import random as random

# Oyun matrisinin olusturulmasi
mx = np.full((10, 10), "O")
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

print(amiral_matrisi, amiral_pozisyon)
print(muhrip_matrisi, muhrip_pozisyon)
print(firkateyn_matrisi, firkateyn_pozisyon)
print(denizalti_matrisi, denizalti_pozisyon)

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
















print(muhrip_baslangic[0], muhrip_baslangic[1])
print(muhrip_bitis[0], muhrip_bitis[1])

if(muhrip_baslangic[1] == muhrip_bitis[1]):
    df.iloc[muhrip_baslangic[0]:muhrip_bitis[0]+1, muhrip_bitis[1]] = 4
else:
    df.iloc[muhrip_baslangic[0], muhrip_baslangic[1]:muhrip_bitis[1]+1] = 4



print(df)

































