######################################  PANDAS ###################################################

# ************************************  019 SERİLER
# ************************************  158 SERİ ELEMAN İŞLEMLERİ
# ************************************  205 DATA FRAME
# ************************************  298 DATA FRAME ELEMAN İŞLEMLERİ
# ************************************  350 GÖZLEM VE DEĞİŞKEN SEÇİMLERİ (LOC- İLOC)
# ************************************  385 KOŞULLU ELEMAN İŞLEMLERİ
# ************************************  425 BİRLEŞTİRME (JOIN) İŞLEMLERİ
# ************************************  523 TOPLULAŞTIRMA VE GRUPLAMA
# ************************************  530 TOPLULAŞTIRMA İŞLEMLERİ
# ************************************  589 GRUPLAMA İŞLEMLERİ
# ************************************  626 İLERİ TOPLULAŞTIRMA İŞLEMLERİ(AGGREGATE,APPLY,FİLTER vs.)
# ************************************  744 PİVOT TABLOLAR
# ************************************  792 DIŞ KAYNAKLI VERİ OKUMA

import pandas as pd

############################# SERİLER
#####SERİ OLUŞTURMA:
pd.Series([2,4,6,8,10])
# 0     2
# 1     4
# 2     6
# 3     8
# 4    10
# dtype: int64

# Listeden Oluşturma:
sayilar = list(np.random.randint(0,20,3))
numpy_dizi =np.random.randint(0,20,10)

seri1 = pd.Series(sayilar)
seri1
# 0     3
# 1     3
# 2    19
# dtype: int64

# Sözlükten Oluşturma:
sozluk = {"5" : 52,
          "10": 62,
          "15": 85}
seri3 = pd.Series(sozluk)
seri3
# 5     52
# 10    62
# 15    85
# dtype: int64

#Veri Seti Üzerinden Oluşturma(Dış kaynaklı veri setini okutma işlemi en aşağıda daha detaylı anlatılmıştır.)
tips_data = pd.read_csv("Data_Sets/tips.csv", nrows = 30)
tips_total_bill = tips_data["total_bill"]
tips_days = tips_data["day"]

# 0     16.99
# 1     10.34
# 2     21.01
# 3     23.68
# Name: total_bill, dtype: float64

##### Tip Sorgulama:
type(tips_total_bill)
# pandas.core.series.Series

seri = pd.Series([2,4,6,8,10])
type(seri)
# pandas.core.series.Series

##### İndex bilgilerine erişme:
seri.axes
# [RangeIndex(start=0, stop=5, step=1)]

##### Seri ile ilgili tip bilgisi için:
seri.dtype
# dtype('int64')

##### Eleman sayısı:
seri.size
#5

##### Boyut bilgisi:
seri.ndim
#1

##### Belirli bir sütuna vektör olarak erişmek(veya array yapısında erişmek)
seri.values
# array([ 2,  4,  6,  8, 10], dtype=int64)

##### Seriye başka veri yapısı şeklinde erişmek istersek:
dict(seri.items())
# {0: 2, 1: 4, 2: 6, 3: 8, 4: 10}
list(seri.items())
# [(0, 2), (1, 4), (2, 6), (3, 8), (4, 10)]

##### İlk 3 gözleme erişmek:
seri.head(3)
# 0    2
# 1    4
# 2    6
# dtype: int64

##### Sondan 2 gözleme erişmek:
seri.tail(2)
# 3     8
# 4    10
# dtype: int64

###### İndex isimlendirmesi:
seri1 = pd.Series([85,222,356,41,25],index= [10,20,30,"Kırk","Elli"])
# 10       85
# 20      222
# 30      356
# Kırk     41
# Elli     25
# dtype: int64

##### İndex ile elemanlara erişmek
seri1["Kırk"]
#41
### Slice
seri1["Kırk":"Elli" ]
# Kırk    41
# Elli    25
# dtype: int64

##### Sözlük üzerinden seri oluşturma:
sozluk = pd.Series({"reg" : 10, "log":22,"cart":54})
sozluk
# reg     10
# log     22
# cart    54
# dtype: int64

# 2. Yol
sozluk = {"reg" : 10, "log":22,"cart":54}
seri2 = pd.Series(sozluk)
seri2
# reg     10
# log     22
# cart    54
# dtype: int64

##### İki seri birleştirerek seri oluşturma:
pd.concat([seri,seri1])
# 0         2
# 1         4
# 2         6
# 3         8
# 4        10
# 10       85
# 20      222
# 30      356
# Kırk     41
# Elli     25
# dtype: int64

############## Eleman İşlemleri ############
import numpy as np
a = np.array([32,258,5,6])
seri = pd.Series(a)
seri

seri[0]
#32

seri[0:2]
# 0     32
# 1    258
# dtype: int32

seri1 = pd.Series([24,35,148,56], index=["ab","bc","cd","de"])
seri1
# ab     24
# bc     35
# cd    148
# de     56
# dtype: int64

seri1.keys
# <bound method Series.keys of ab     24
# bc     35
# cd    148
# de     56
# dtype: int64>

list(seri1.items())
# Out[53]: [('ab', 24), ('bc', 35), ('cd', 148), ('de', 56)]

"ab" in seri1
#True

#Fancy
seri1[["ab","de"]]
# ab    24
# de    56
# dtype: int64

#Değer atama:
seri1["bc"] = 250
seri1[["bc"]]
# bc    250
# dtype: int64

#################################  DATA FRAME  ####################################
# Numpy sabit tipli olduğundan işlem yapmada çok fonksiyonel olmadığından, veri manüplasyonunda pandas df kullanılır.
#Yapılandırılmış bir veri formudur.

#Listeden Oluşturma:
liste = [55,2,3,36,5]
pd.DataFrame(liste, columns=["Sayılar"])
   # Sayılar
# 0       55
# 1        2
# 2        3
# 3       36
# 4        5

#Numpy Arrayden Oluşturma:
m = np.arange(1,28,3).reshape(3,3)
m
pd.DataFrame(m,columns=["var1","var2","var3"])
     # var1  var2  var3
# 0     1     4     7
# 1    10    13    16
# 2    19    22    25

#Sözlükten oluşturma:
degisken_isimleri = ["var1","var2","var3"]
degerler = [np.random.randint(10,size=5)for _ in range(3)]
#-> [array([1, 6, 3, 7, 5]), array([7, 0, 0, 4, 6]), array([4, 5, 6, 6, 5])]
sozluk = dict(zip(degisken_isimleri,degerler))
sozlukten_df= pd.DataFrame(sozluk)
sozlukten_df
   # var1  var2  var3
# 0     2     7     1
# 1     2     8     4
# 2     5     8     1
# 3     0     3     4
# 4     4     9     8

#Seriden oluşturma:
seri = pd.Series([2,4,6,8,10])
df = pd.DataFrame(seri, columns=["Seri"])
df
   # Seri
# 0     2
# 1     4
# 2     6
# 3     8
# 4    10

# Değişken ismi değiştirme:
m = np.arange(1,28,3).reshape(3,3)
m
df = pd.DataFrame(m,columns=["var1","var2","var3"])
df.columns = ("deg1","deg2","deg3")
df.head(1)
   # deg1  deg2  deg3
# 0     1     4     7

df.columns
# Index(['deg1', 'deg2', 'deg3'], dtype='object')

df.dtypes
# deg1    int32
# deg2    int32
# deg3    int32
# dtype: object

df.ndim
#2

df.shape
#(3, 3)

df.size
#9

df.values   #Değerleri çekip array formuna çevirir.
# array([[ 1,  4,  7],
#        [10, 13, 16],
#        [19, 22, 25]])

df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 3 entries, 0 to 2
# Data columns (total 3 columns):
#    Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   deg1    3 non-null      int32
#  1   deg2    3 non-null      int32
#  2   deg3    3 non-null      int32
# dtypes: int32(3)



##### Eleman işlemleri :
s1 = np.random.randint(20, size=5)
s2 = np.random.randint(20, size=5)
s3 = np.random.randint(20, size=5)
sozluk = {"var1": s1 , "var2": s2, "var3" : s3}
df = pd.DataFrame(sozluk)
df

df.index = ["a","b","c","d","e"]
df
   # var1  var2  var3
# a    14    19     4
# b     9     1     9
# c     4    17     7
# d    15    19     3
# e    12     6    11

########  Silme işlemi  ###############
df.drop("c",axis =0)  #KALICI İŞLEM DEĞİL
   # var1  var2  var3
# a    14    19     4
# b     9     1     9
# d    15    19     3
# e    12     6    11

df.drop("c",axis =0, inplace=True) # KALICI OLARAK SİLER

######Fancy ile silme
sil = ["a","b"]
df.drop(sil,axis=0)  # inplace = True yaparsak kalıcı olarak silecektir.
   # var1  var2  var3
# d    15    19     3
# e    12     6    11

###### Değişkenleri silme:
sil2 = ["var1","var2"]
df.drop(sil2, axis=1)  # inplace = True yaparsak kalıcı olarak silecektir.
   # var3
# a     4
# b     9
# d     3
# e    11

# Değişken oluşturma
df["var4"] = df["var1"] * df["var3"]
df
   # var1  var2  var3  var4
# a    14    19     4    56
# b     9     1     9    81
# d    15    19     3    45
# e    12     6    11   132

############ GÖZLEM VE DEĞİŞKEN SEÇİMİ ##############
ma = np.random.randint(1,30, size=(5,3))
df = pd.DataFrame(ma, columns=["deg1","deg2","deg3"])
df
#### loc : Tanımlandığı şekliyle seçim yapmak için kullanılır.

df.loc[0:2]
   # deg1  deg2  deg3
# 0    18    16    18
# 1    26    15     3
# 2    25    24    21

#### iloc : Alışık olduğumuz indeksleme mantığı('e kadar).
df.iloc[0:2]
   # deg1  deg2  deg3
# 0    18    16    18
# 1    26    15     3

df.iloc[0,0]
# 18
df.iloc[:3,:2]
   # deg1  deg2
# 0    18    16
# 1    26    15
# 2    25    24

df.loc[0:3,"deg2"] #iloc değişken veya indexlerde mutlak bir değer işaretlemesi yapacaksak çalışmaz.
# 0    16
# 1    15
# 2    24
# 3     6
# Name: deg2, dtype: int32

# İNDEKSLERE BAĞLI KALACAKSAK LOC KALMAYACAKSAK İLOC

########## Koşullu Eleman İşlemleri  ##############
ma = np.random.randint(1,30, size=(5,3))
df = pd.DataFrame(ma, columns=["deg1","deg2","deg3"])
df

df[0:2][["deg1","deg2"]] #Birden fazla değişken girmek istedğimizde fancy yardımıyla [[deg]] yapılmalı...
   # deg1  deg2
# 0    20    13
# 1     1    28

# 2. değişkendeki değerlerin 10 dan büyük olması:
df[df.deg2 > 15]
   # deg1  deg2  deg3
# 1     7    27    24
# 2     2    20    15
# 3     3    16    12
df[df.deg2 > 15]["deg1"]
# 1    7
# 2    2
# 3    3
# Name: deg1, dtype: int32

# Birden fazla koşul gerçekleştirmek istersek
df[(df.deg2 > 15) & (df.deg3 < 20)]
   # deg1  deg2  deg3
# 2     2    20    15
# 3     3    16    12

df.loc[(df.deg2 > 15), ["deg1","deg2"]]
   # deg1  deg2
# 1     7    27
# 2     2    20
# 3     3    16

df[(df.deg2 > 15)][["deg1","deg3"]]
   # deg1  deg3
# 1     7    24
# 2     2    15
# 3     3    12

# Birleştirme (Join) işlemleri:
ma = np.random.randint(1,30, size=(5,3))
df1 = pd.DataFrame(ma, columns=["deg1","deg2","deg3"])
df1

##  Concat:
df2 = df1+ 85
df2
pd.concat([df1,df2])
# (   deg1  deg2  deg3
#  0    22     1    23
#  1    24    22     2
#  2    19     9     3
#  3    23    20    21
#  4     3     4    19,
#     deg1  deg2  deg3
#  0   107    86   108
#  1   109   107    87
#  2   104    94    88
#  3   108   105   106
#  4    88    89   104)

pd.concat([df1,df2],ignore_index= True)
# ?pd.concat
   # deg1  deg2  deg3
# 0    22     1    23
# 1    24    22     2
# 2    19     9     3
# 3    23    20    21
# 4     3     4    19
# 5   107    86   108
# 6   109   107    87
# 7   104    94    88
# 8   108   105   106
# 9    88    89   104

df2.columns = ["deg1","deg2","var3"]
df2
pd.concat([df1,df2])
   # deg1  deg2  deg3   var3
# 0    22     1  23.0    NaN
# 1    24    22   2.0    NaN
# 2    19     9   3.0    NaN
# 3    23    20  21.0    NaN
# 4     3     4  19.0    NaN
# 0   107    86   NaN  108.0
# 1   109   107   NaN   87.0
# 2   104    94   NaN   88.0
# 3   108   105   NaN  106.0
# 4    88    89   NaN  104.0

pd.concat([df1,df2], join="inner")
   # deg1  deg2
# 0    22     1
# 1    24    22
# 2    19     9
# 3    23    20
# 4     3     4
# 0   107    86
# 1   109   107
# 2   104    94
# 3   108   105
# 4    88    89

# İleri birleştirme işlemleri:

df1 = pd.DataFrame({"Çalışanlar" : ["Ali","Veli","Ayşe","Fatma"],
                    "Grup": ["Muhasebe","Mühendislik","Mühendislik","IK"]})
df1
df2 = pd.DataFrame({"Çalışanlar" : ["Ayşe","Ali","Veli","Fatma"],
                    "Ilk giriş": [2010,2009,2014,2018]})
df2
pd.merge(df1,df2)
  # Çalışanlar         Grup  Ilk giriş
# 0        Ali     Muhasebe       2009
# 1       Veli  Mühendislik       2014
# 2       Ayşe  Mühendislik       2010
# 3      Fatma           IK       2018

#Çoktan teke,
df3 = pd.merge(df1,df2)
df3
df4=pd.DataFrame({"Grup" : ["Muhasebe","Mühendislik","IK"],
                  "Müdür": ["Caner" , "Mustafa","Berkcan"]})
pd.merge(df3,df4)
 # Çalışanlar         Grup  Ilk giriş    Müdür
# 0        Ali     Muhasebe       2009    Caner
# 1       Veli  Mühendislik       2014  Mustafa
# 2       Ayşe  Mühendislik       2010  Mustafa
# 3      Fatma           IK       2018  Berkcan

#Çoktan çoka,
df5= pd.DataFrame({"Grup": ["Muhasebe","Muhasebe","Mühendislik","Mühendislik","IK","IK"],
                   "Yetenekler" : ["mat","excel","kodlama","linux","excel","yönetim"]})
df5
df1
pd.merge(df1,df5)

################### TOPLULAŞTIRMA VE GRUPLAMA ##################
import pandas as pd
import seaborn as sns
df = sns.load_dataset("planets")
df.head(10)
df.shape

####### TOPLULAŞTIRMA İŞLEMLERİ
# count() Gözlem birimlerinin sayısını gösterir.
df.count()
# method            1035
# number            1035
# orbital_period     992
# mass               513
# distance           808
# year              1035
# dtype: int64

# median() Gözlem birimlerinin medyanını gösterir.
df.median()
# number               1.0000
# orbital_period      39.9795
# mass                 1.2600
# distance            55.2500
# year              2010.0000
# dtype: float64

# min() Değişken içindeki minimum değeri getirir.
df["mass"].min()
# 0.0036

# max() Değişken içindeki maximum değer
df["distance"].max()
# 8500.0

# sum() Değişkenlerin değerlerini toplar.
df["mass"].sum()
# 1353.37638

# std() Değişkenlerin Standart sapma değerini gösterir.
df["mass"].std()
# 3.8186166509616046

# var() Değişkenlerin varyans değerini gösterir.
df["mass"].var()
# 14.58183312700122

# mean()  ORTALAMA ALMA İÇİN KULLANILIR.
df.mean()
# number               1.785507
# orbital_period    2002.917596
# mass                 2.638161
# distance           264.069282
# year              2009.070531
# dtype: float64

df["mass"].mean()
# 2.6381605847953233

# describe() Betimsel istatistiklerin tamamına erişmek
df.describe().T
      # count  mean       std   min   25%   50%   75%   max
# deg1    5.0   9.2  5.118594   3.0   7.0   9.0  10.0  17.0
# deg2    5.0  20.2  6.099180  11.0  20.0  20.0  22.0  28.0
# deg3    5.0  18.4  7.668116   5.0  19.0  22.0  23.0  23.0

################# GRUPLAMA İŞLEMLERİ

df = pd.DataFrame({"Gruplar" : ["A","B","C","A","B","C"],
                   "Veri": [10,11,52,23,43,55]}, columns=["Gruplar","Veri"])
df
df.groupby("Gruplar")
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001A9BA6E7160>
df.groupby("Gruplar").mean() #A,B,C gruplarının değerlerinin ortalmasını aldı
         # Veri
# Gruplar
# A        16.5
# B        27.0
# C        53.5

import seaborn as sns
df = sns.load_dataset("planets")
df.head(3)

df.groupby("method")
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001A9BA6E7190>
df.groupby("method")["orbital_period"] #Aggregation fonk yazmamız lazım yoksa alttaki çıktıyı vermeye devam eder.
# <pandas.core.groupby.generic.SeriesGroupBy object at 0x000001A9BA7148E0>
df.groupby("method")["orbital_period"].mean()
# method
# Astrometry                          631.180000
# Eclipse Timing Variations          4751.644444
# Imaging                          118247.737500
# Microlensing                       3153.571429
# Orbital Brightness Modulation         0.709307
# Pulsar Timing                      7343.021201
# Pulsation Timing Variations        1170.000000
# Radial Velocity                     823.354680
# Transit                              21.102073
# Transit Timing Variations            79.783500
# Name: orbital_period, dtype: float64


################### İLERİ TOPLULAŞTIRMA
#AGGREGATE,FİLTER,TRANSFORM,APPLY

df = pd.DataFrame({"Gruplar" : ["A","B","C","A","B","C"],
                   "Degisken1": [10,11,52,23,11,55],
                   "Degisken2" : [100,253,33,262,11,969]},
                  columns=["Gruplar","Degisken1","Degisken2"])
df

# Aggregate:
df.groupby("Gruplar").mean()
         # Degisken1  Degisken2
# Gruplar
# A             16.5      181.0
# B             11.0      132.0
# C             53.5      501.0
# ***************************
import numpy as np
df.groupby("Gruplar").aggregate(["min", np.median,max])
 #                 Degisken1            Degisken2
 #              min median max       min median  max
# Gruplar
# A              10   16.5  23       100    181  262
# B              11   11.0  11        11    132  253
# C              52   53.5  55        33    501  969
#Veri setini gruplara göre bölüp, aggregate fonk sayesinde kendi istediğimiz fonksiyonları çalıştımamızı sağladı.

df.groupby("Gruplar").aggregate({"Degisken1": "min",
                                 "Degisken2": "max"})
         # Degisken1  Degisken2
# Gruplar
# A               10        262
# B               11        253
# C               52        969

# FILTER:
df = pd.DataFrame({"Gruplar" : ["A","B","C","A","B","C"],
                   "Degisken1": [10,11,52,23,85,55],
                   "Degisken2" : [100,253,33,262,11,969]},
                  columns=["Gruplar","Degisken1","Degisken2"])
def filter_func(x):
    return x["Degisken1"].std()>9
df.groupby("Gruplar").std()
         # Degisken1   Degisken2
# Gruplar
# A         9.192388  114.551299
# B        52.325902  171.119841
# C         2.121320  661.851947

df.groupby("Gruplar").filter(filter_func)
  # Gruplar  Degisken1  Degisken2
# 0       A         10        100
# 1       B         11        253
# 3       A         23        262
# 4       B         85         11

#Mevcut pandas fonksiyonlarıiçinde yer almayan,
# bizim tanımladığımız bir fonksiyonu df değişkenlerinin üzerinde sorgulamamızı sağlar.

### TRANSFORM:
df["Degisken1"]*9
# 0     90
# 1     99
# 2    468
# 3    207
# 4    765
# 5    495
# Name: Degisken1, dtype: int64

df_a =df.iloc[:,1:]
df_a.transform(lambda x: x - x.mean())
   # Degisken1   Degisken2
# 0 -29.333333 -171.333333
# 1 -28.333333  -18.333333
# 2  12.666667 -238.333333
# 3 -16.333333   -9.333333
# 4  45.666667 -260.333333
# 5  15.666667  697.666667

df_a.transform(lambda x: (x -x.mean()) / x.std())
   # Degisken1  Degisken2
# 0  -0.986438  -0.478483
# 1  -0.952809  -0.051200
# 2   0.425962  -0.665594
# 3  -0.549267  -0.026065
# 4   1.535705  -0.727033
# 5   0.526848   1.948374

### APPLY:
df = pd.DataFrame({"Degisken1": [10,11,52,23,85,55],
                   "Degisken2" : [100,253,33,262,11,969]},
                  columns=["Degisken1","Degisken2"])
df

df.apply(np.sum)
# Degisken1     236
# Degisken2    1628
# dtype: int64

df.apply(np.mean)
# Degisken1     39.333333
# Degisken2    271.333333
# dtype: float64

df = pd.DataFrame({"Gruplar" : ["A","B","C","A","B","C"],
                   "Degisken1": [10,11,52,23,85,55],
                   "Degisken2" : [100,253,33,262,11,969]},
                  columns=["Gruplar","Degisken1","Degisken2"])

df.groupby("Gruplar").apply(np.sum)
        # Gruplar  Degisken1  Degisken2
# Gruplar
# A            AA         33        362
# B            BB         96        264
# C            CC        107       1002

# df'in değişkenleri üzerinde gezinmeye ve toplulaştırmaya yarayan fonksiyon.

######################### PİVOT TABLOLAR #############################
titanic = sns.load_dataset("titanic")
titanic.head()

titanic.groupby("sex")["survived"].mean()
# sex
# female    0.742038
# male      0.188908
# Name: survived, dtype: float64

titanic.groupby(["sex","class"])["survived"].aggregate("mean").unstack()
# class      First    Second     Third
# sex
# female  0.968085  0.921053  0.500000
# male    0.368852  0.157407  0.135447

# Cinsiyet ve class kategorik değişkenini sınıflarına göre bölüp kesişiminde işlem yapmış olduk.

#Pivot table ile işlem:
titanic.pivot_table("survived", index="sex",columns="class")
# class      First    Second     Third
# sex
# female  0.968085  0.921053  0.500000
# male    0.368852  0.157407  0.135447

titanic.age.head()
# 0    22.0
# 1    38.0
# 2    26.0
# 3    35.0
# 4    35.0
age = pd.cut(titanic["age"],[0,18,90])
age.head()
# 0    (18, 90]
# 1    (18, 90]
# 2    (18, 90]
# 3    (18, 90]
# 4    (18, 90]
# Name: age, dtype: category

titanic.pivot_table("survived", ["sex",age],"class")
# class               First    Second     Third
# sex    age
# female (0, 18]   0.909091  1.000000  0.511628
#        (18, 90]  0.972973  0.900000  0.423729
# male   (0, 18]   0.800000  0.600000  0.215686
#        (18, 90]  0.375000  0.071429  0.133663

###########################  DIŞ KAYNAKLI VERİ OKUMA(PYCHARM) #####
#Ayar işlemi
pd.set_option("display.max_columns",None)  # Bütün sütun isimlerini eksiksiz göster.(None yerine 5 dersek 5sütun gösterir.)
pd.set_option("display.expand_frame_repr",False)  # Bütün değişkenleri yan yana yazdırmak için kullanılır.

#### .csv  #####

tips_data = pd.read_csv("Data_Sets/tips.csv") #Bunu bulamadım diyecektir.
#Project içinden csv dosyasını bulup sağ tık -> Copy Path -> Path From Content Root a basıp yukarı kopyaladık.

tips_data = pd.read_csv("Data_Sets/tips_II.csv")
tips_data.head(2)
  # total_bill;"tip";"sex";"smoker";"day";"time";"size"
# 0          16.99;1.01;"Female";"No";"Sun";"Dinner";2
# 1            10.34;1.66;"Male";"No";"Sun";"Dinner";3

#Bu durumu düzletmek için sep parametresini kullanırız.
tips_data = pd.read_csv("Data_Sets/tips_II.csv", sep= ";")
tips_data.head(2)
   # total_bill   tip     sex smoker  day    time  size
# 0       16.99  1.01  Female     No  Sun  Dinner     2
# 1       10.34  1.66    Male     No  Sun  Dinner     3

# 100 satırını almak:
tips_data_100= pd.read_csv("Data_Sets/tips.csv", nrows=100) #Belirtlien sayı kadar alır
tips_data_100

#100-150 arasına almak istersek:
tips_data_100_150= pd.read_csv("Data_Sets/tips.csv", skiprows=100, nrows=150, header = None)
tips_data_100_150

diabetes = pd.read_csv("Data_Sets/diabetes.csv")
#... lı değerler oluşmuştu. Yukarıdaki ayar kodlarından ilkini çalıştırarak sorunu giderdik.
# Bazı değişkenler aşağı kaymıştı.Yukarıdaki ayar kodlarından ikincisini çalıştırarak sorunu giderdik.
diabetes.head(10)

##Veri setlerindeki boş değerleri veri setini alırken tanıtmak Örn:insulin değerleri 0 gözüküyor.
   # Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  DiabetesPedigreeFunction  Age  Outcome
# 0            6      148             72             35        0  33.6                     0.627   50        1
# 1            1       85             66             29        0  26.6                     0.351   31        0
# 2            8      183             64              0        0  23.3                     0.672   32        1
# 3            1       89             66             23       94  28.1
diabetes = pd.read_csv("Data_Sets/diabetes.csv", na_values={"Glucose": 0,                                                                                                                      "BloodPressure": 0,
                                                           "SkinThickness": 0,
                                                           "Insulin": 0,
                                                           "BMI":0})
diabetes.head(3)
   # Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  DiabetesPedigreeFunction  Age  Outcome
# 0            6    148.0           72.0           35.0      NaN  33.6                     0.627   50        1
# 1            1     85.0           66.0           29.0      NaN  26.6                     0.351   31        0
# 2            8    183.0           64.0            NaN      NaN  23.3                     0.672   32        1

# 0 olan gözlemleri NaN olarak dolduruldu ve boş olarak gözüküyor

#### .xlsx ####
import pandas as pd
online_retail = pd.read_excel("Data_Sets/online_retail_GER.xlsx")
online_retail

#excel üstünde ki sütunların ismine göre çekmek
online_retail = pd.read_excel("Data_Sets/online_retail_GER.xlsx", usecols="B:E, G")
online_retail.head(3)
 # StockCode                     Description  Quantity         InvoiceDate  Customer ID
# 0    85049E       SCANDINAVIAN REDS RIBBONS        12 2009-12-01 11:50:00        12533
# 1     21976  PACK OF 60 MUSHROOM CAKE CASES        24 2009-12-01 11:50:00        12533
# 2     21498                RED SPOTS  WRAP         25 2009-12-01 11:50:00        12533

# Aynı veri setinden İki farklı veri setini birleştime istediğimizde:

online_retail_2009_2010 = pd.read_excel("Data_Sets/online_retail_GER.xlsx", sheet_name="Year 2009-2010")
online_retail_2010_2011 = pd.read_excel("Data_Sets/online_retail_GER.xlsx", sheet_name="Year 2010-2011")

online_retail_all = pd.concat(([online_retail_2009_2010,online_retail_2010_2011]))
online_retail_all

#Döngü aracılığıyla sonda hangi yıl aralığından geldiğini belirtecek bir sütun ile birleştirme

online_retail_all_new = pd.DataFrame()

for sheet_name, frame in pd.read_excel("Data_Sets/online_retail_GER.xlsx", sheet_name=None).items():
    frame["Year"] = sheet_name
    online_retail_all_new = online_retail_all_new.append(frame)
online_retail_all_new.head(2)
# Invoice StockCode                     Description  Quantity         InvoiceDate  Price  Customer ID  Country            Year
# 0  489526    85049E       SCANDINAVIAN REDS RIBBONS        12 2009-12-01 11:50:00   1.25        12533  Germany  Year 2009-2010
# 1  489526     21976  PACK OF 60 MUSHROOM CAKE CASES        24 2009-12-01 11:50:00   0.55        12533  Germany  Year 2009-2010