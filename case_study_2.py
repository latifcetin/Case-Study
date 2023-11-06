# ######################################################################
# GÖREV 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM_ ekleyiniz. 
# ######################################################################
#
# # Beklenen Çıktı
#
# # ['NUM_TOTAL',
#    'NUM_SPEEDING',
#    'NUM_ALCOHOL',
#    'NUM_NOT_DISTRACTED',
#    'NUM_NO_PREVIOUS',
#    'NUM_INS_PREMIUM',
#    'NUM_IN_LOSSES',
#    'ABBREV']
#
# # Notlar:
# # Numeric olmayan değişkenlerin de isimleri büyümeli. 
# # Tek bir list comprehension yapısı kullanılmalı.

import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
print(df.columns)
print(df.info())

print(["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns])


# ######################################################################
# GÖREV 2: List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan değişkenlerin isimlerinin sonuna "FLAG" yazınız.
# ######################################################################
#
# # Beklenen Çıktı
#
# # ['NUM_TOTAL_FLAG',
#    'NUM_SPEEDING_FLAG',
#    'NUM_ALCOHOL_FLAG',
#    'NUM_NOT_DISTRACTED',
#    'NUM_NO_PREVIOUS',
#    'NUM_INS_PREMIUM_FLAG',
#    'NUM_IN_LOSSES_FLAG',
#    'ABBREV_FLAG']
#
# # Tüm değişkenlerin isimleri büyük harf olmalı. 
# # Tek bir list comprehension yapısı ile yapılmalı.

["_FLAG" + col.upper() if "no" not in col else col.upper() for col in df.columns]


# ######################################################################
#  GÖREV 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerinin seçiniz ve yeni bir dataframe oluşturunuz.
# ######################################################################
#
# # Notlar:
# # Önce verilen listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# # Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz ve adını new_df olarak isimlendiriniz.

og_list = ["abbrev", "no_previous"]

new_cols = [col for col in df.columns if col not in og_list]
new_cols = df[new_cols]
print(df.head())


# ######################################################################
# GÖREV 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
# ######################################################################

df = sns.load_dataset("titanic")
print(df.head())
print(df.shape)


# ######################################################################
# GÖREV 2: Yukarıda tanımlanan Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
# ######################################################################

print(df["sex"].value_counts())  


# ######################################################################
# GÖREV 3: Her bir sütuna ait unique değerlerin sayısını bulunuz.
# ######################################################################

print(df.nunique())


# ######################################################################
# GÖREV 4: pclass değişkeninin unique değerlerini bulunuz.
# ######################################################################

print(df["pclass"].nunique())


# ######################################################################
# GÖREV 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
# ######################################################################

print(df[["pclass", "parch"]].nunique())


# ######################################################################
# GÖREV 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz. Tekrar tipini kontrol ediniz.
# ######################################################################

print(df["embarked"].dtype)
df["embarked"] = df["embarked"].astype("category")
print(df["embarked"].dtype)
print(df.info())


# ######################################################################
# GÖREV 7: embarked değeri C olanların tüm bilgilerini gösteriniz.
# ######################################################################

print(df[df["embarked"] == "C"].head())


# ######################################################################
# GÖREV 8: embarked değeri S olmayanların tüm bilgilerini gösteriniz.
# ######################################################################

print(df[df["embarked"] != "S"].head())

print(df[df["embarked"] != "S"]["embarked"].nunique())


# ######################################################################
# GÖREV 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
# ######################################################################

print(df[(df["age"] < 30) & (df["sex"] == "female")].head())


# ######################################################################
# GÖREV 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
# ######################################################################

print(df[(df["fare"] > 500) | (df["age"] > 70)].head())


# ######################################################################
# GÖREV 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
# ######################################################################

print(df.isnull().sum())


# ######################################################################
# GÖREV 12: who değişkenini dataframe'den düşürün.
# ######################################################################

print(df.drop("who", axis=1, inplace=True))

# ######################################################################
# GÖREV: 13: deck değişkenşndeki boş değerleri deck değişkeninin en çok tekrar eden değeri(mod) ile doldurunuz.
# ######################################################################

df["deck"].mode()
print(df["deck"].mode()[0])
print(df["deck"].fillna(df["deck"].mode()[0], inplace=True))
print(df.isnull().sum())


# ######################################################################
# GÖREV 14: age değişkenindeki boş değerleri age değişkeninin medyanı ile doldurun
# ######################################################################

df["age"].fillna(df["age"].median(), inplace=True)
print(df["age"].isnull().sum())


# ######################################################################
# GÖREV 15: survived değişkeninin pclass ve sex değişkenleri kırılımında sum, count, mean değerlerini bulunuz.
# ######################################################################

print(df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "count", "mean"]}))


# ######################################################################
# GÖREV 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın. 
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
# ######################################################################

def age_30(age):
    if age < 30:
        return 1
    else:
        return 0

df["age_flag"] = df["age"].apply(lambda x: age_30(x))

df["age_flag"] = df["age"].apply(lambda x: 1 if x < 30 else 0)


# ######################################################################
# GÖREV 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
# ######################################################################

df = sns.load_dataset("tips")
df.head()
df.shape


# ######################################################################
# GÖREV 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
# ######################################################################

print(df.groupby("time").agg({"total_bill": ["sum", "min", "mean", "max"]}))

# ######################################################################
# GÖREV 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
# ######################################################################

print(df.groupby(["day", "time"]).agg({"total_bill": ["sum", "min", "mean", "max"]}))


# ######################################################################
# GÖREV 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
# ######################################################################

df[(df["time"] == "Lunch") & df["sex"] == "Female"].groupby({"total_bill": ["sum", "min", "mean", "max"],
                                                             "tip": ["sum", "min", "mean", "max"]})

# ######################################################################
# GÖREV 21: size', 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir?
# ######################################################################

df.loc[(df["size"] < 3) & (df["total_bill"] > 10), "total_bill"].mean()


# ######################################################################
# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturun. Her bir müşterinin ödediği totalbill ve tip'in toplamını versin.
# ######################################################################

df["total_bill_tip_sum"] == df["total_bill"] + df["tip"]
df.head()


# ######################################################################
# GÖREV 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
# ######################################################################

new_df = df.sort_values("total_bill_tip_sum", ascending=False)[:30]
new_df.shape