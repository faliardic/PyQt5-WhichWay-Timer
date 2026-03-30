import time
import beyin

CIKIS_KOMUTLARI = {"çık", "cik", "çıkış", "cikis", "q", "quit", "exit"}


def dusunme_efekti():
    print("Çenebaz: ...")
    time.sleep(1)


def bot_yaz(metin: str):
    dusunme_efekti()
    print(f"Çenebaz: {metin}")


def kullanici_girdisi_al(etiket="Sen"):
    veri = input(f"{etiket}: ").strip()

    if veri.lower() in CIKIS_KOMUTLARI:
        bot_yaz("Görüşürüz. Sohbet güzeldi.")
        raise SystemExit

    return veri


def tanisma_akisi():
    kullanici = {}

    print("ÇENEBAZ v2.0")
    print("Çıkmak için istediğin zaman 'çık' yaz.\n")

    bot_yaz(beyin.rastgele_selamlama())

    bot_yaz("Önce adını alayım.")
    isim = kullanici_girdisi_al()
    kullanici["isim"] = isim
    bot_yaz(beyin.isim_cevabi_uret(isim))

    bot_yaz("Peki ne iş yapıyorsun?")
    meslek = kullanici_girdisi_al()
    kullanici["meslek"] = meslek
    bot_yaz(beyin.meslek_cevabi_uret(meslek))

    bot_yaz("Bir de yaşını söyle bakalım.")
    yas = kullanici_girdisi_al()
    kullanici["yas"] = yas
    bot_yaz(beyin.yas_cevabi_uret(yas))

    isim_gosterim = kullanici["isim"].strip() or "dostum"
    bot_yaz(f"Tamam {isim_gosterim}, temel bilgileri kaptım.")
    bot_yaz(beyin.rastgele_kapanis())

    return kullanici


def devam_sorulari_akisi(kullanici: dict):
    """Tanışma bittikten sonra sıralı ek sorular."""

    isim = kullanici.get("isim", "dostum").strip() or "dostum"

    # Hobi
    bot_yaz(f"Peki {isim}, boş zamanlarında ne yapıyorsun? Bir hobin var mı?")
    hobi = kullanici_girdisi_al()
    kullanici["hobi"] = hobi
    bot_yaz(beyin.hobi_cevabi_uret(hobi))

    # Memleket
    bot_yaz("Nerelisin? Memleketin neresi?")
    sehir = kullanici_girdisi_al()
    kullanici["sehir"] = sehir
    bot_yaz(beyin.sehir_cevabi_uret(sehir))

    # Favori yemek
    bot_yaz("Favori yemeğin ne?")
    yemek = kullanici_girdisi_al()
    kullanici["yemek"] = yemek
    bot_yaz(beyin.favori_yemek_cevabi_uret(yemek))

    # Favori müzik
    bot_yaz("Müzik dinliyor musun? Hangi türü seversin?")
    muzik = kullanici_girdisi_al()
    kullanici["muzik"] = muzik
    bot_yaz(beyin.favori_muzik_cevabi_uret(muzik))

    # Ruh hali
    bot_yaz("Son olarak, bugün kendini nasıl hissediyorsun?")
    ruh_hali = kullanici_girdisi_al()
    kullanici["ruh_hali"] = ruh_hali
    bot_yaz(beyin.ruh_hali_cevabi_uret(ruh_hali))

    bot_yaz(f"Güzel {isim}, artık seni epey tanıdım.")
    bot_yaz("İstersen sohbete devam edebiliriz. Ne aklına gelirse yaz.")


def serbest_sohbet_dongusu(kullanici: dict):
    """Kullanıcı ne yazarsa yazsın, bot cevaplar."""

    while True:
        girdi = kullanici_girdisi_al()
        if not girdi:
            continue
        cevap = beyin.serbest_cevap_uret(girdi)
        bot_yaz(cevap)


if __name__ == "__main__":
    kullanici = tanisma_akisi()
    devam_sorulari_akisi(kullanici)
    serbest_sohbet_dongusu(kullanici)