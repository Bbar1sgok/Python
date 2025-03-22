hesaplar = [
    {
        "ad": "Barış",
        "bakiye": 20000,
        "kullanıcı_adı":"bayrambarisgok",
        "şifre": "1234"
    },
    {
        "ad": "Diyar",
        "bakiye": 25000,
        "kullanıcı_adı": "diyaraydın",
        "şifre": "1234"
    },
    {
        "ad": "Yusuf",
        "bakiye": 30000,
        "kullanıcı_adı": "yusuf_kaan_arslan",
        "şifre": "1234"
    },
    {
        "ad": "Filik",
        "bakiye": 40000,
        "kullanıcı_adı": "filik_gardiyan",
        "şifre": "1234"
    },
    {
        "ad": "Kemalettin",
        "bakiye": 50000,
        "kullanıcı_adı": "kemalettin_kocakurt",
        "şifre": "1234"
    }
]

def login():
    kullanici_adi = input("Lütfen Kullanıcı adınızı giriniz: ").strip()
    parola = input("Lütfen parolanızı giriniz: ").strip()

    for hesap in hesaplar:
        if hesap["kullanıcı_adı"] == kullanici_adi and hesap["şifre"] == parola:
            print("Başarılı şekilde giriş yapıldı")
            menu(hesap)
            break
    else:
        print("Kullanıcı bilgisi doğru değil")

def menu(hesap):
    while True:
        print("\n")
        print(f"Merhaba {hesap['ad']}\n")
        print("Lütfen yapmak istediğiniz işlemi seçiniz.")
        print("""
        ********************************
        1-> Bakiye Sorgulama
        2-> Para Çekme
        3-> Para Yatırma
        4-> Çıkış
        ********************************
        """)
        islem = input("Lütfen yapmak istediğiniz işlemi seçiniz: ")

        if islem == "1":
            bakiye_sorgulama(hesap)
        elif islem == "2":
            para_cekme(hesap)
        elif islem == "3":
            para_yatirma(hesap)
        elif islem == "4":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Lütfen belirtilen işlemlerden birini seçiniz.")

def bakiye_sorgulama(hesap):
    print(f"Hesabınızda bulunan bakiye {hesap['bakiye']} TL")

def para_cekme(hesap):
    try:
        cekilen_tutar = float(input("Lütfen hesabınızdan çekmek istediğiniz tutarı giriniz: "))
        if cekilen_tutar <= hesap["bakiye"]:
            hesap["bakiye"] -= cekilen_tutar
            print(f"Para çekme işleminiz başarılı. Hesabınızda kalan para {hesap['bakiye']} TL")
        else:
            print(f"Hesabınızda yeterince para yok. Maksimum çekebileceğiniz para {hesap['bakiye']} TL")
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz.")

def para_yatirma(hesap):
    try:
        yatirilicak_tutar = float(input("Lütfen yatırmak istediğiniz tutarı giriniz: "))
        hesap["bakiye"] += yatirilicak_tutar
        print(f"Hesabınıza {yatirilicak_tutar} TL yatırılmıştır. Hesabınızdaki yeni tutar {hesap['bakiye']} TL")
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz")

login()
