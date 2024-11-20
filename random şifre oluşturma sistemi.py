import random
import string


def sifre_uret(uzunluk=12, buyuk_harf=True, kucuk_harf=True, rakam=True, sembol=True):
    karakter_havuzu = ""
    if buyuk_harf:
        karakter_havuzu += string.ascii_uppercase
    if kucuk_harf:
        karakter_havuzu += string.ascii_lowercase
    if rakam:
        karakter_havuzu += string.digits
    if sembol:
        karakter_havuzu += string.punctuation

    if not karakter_havuzu:
        raise ValueError("şifre oluşturmak için en az bir karakter türü seçmelisiniz.")


    sifre = "".join(random.choice(karakter_havuzu) for _ in range(uzunluk))
    return sifre


def girdi_al(mesaj):
    while True:
        cevap = input(mesaj).strip().lower()
        if cevap == 'y':
            return True
        elif cevap == 'n':
            return False
        else:
            print("Hatalı giriş yaptınız! Yes için 'y', no için 'n' yazın.")


def sifre_olusturucu_arayuz(uzunluk=12, buyuk_harf=True, kucuk_harf=True, sembol=True, rakam=True):
    print("şifre üretici uygulamasına hoş geldiniz.")

    try:
        uzunluk = int(input("şifre uzunluğunu giriniz.(max uzunluk=12)"))
        buyuk_harf = girdi_al("büyük harf içersin mi? (y/n): ")
        kucuk_harf = girdi_al("küçük harf içersin mi? (y/n):")
        rakam = girdi_al("Rakam içersin mi? (y/n): ")
        sembol = girdi_al("sembol içersin mi? (y/n): ")

        sifre = sifre_uret(uzunluk, buyuk_harf, kucuk_harf, rakam, sembol)
        print(f"oluşturulan sifre: {sifre} ")
    except ValueError as y:
        print(f"hata: {y} ")


if __name__ == "__main__":
    sifre_olusturucu_arayuz()
