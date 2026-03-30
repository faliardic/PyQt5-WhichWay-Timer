import random

# ------------------------- SELAMLAMA CEVAPLARI -------------------------

SELAMLAMA_CEVAPLARI = [
    "Merhaba! Ben Çenebaz, senin sohbet arkadaşın.",
    "Selam! Hazırım, başlayalım mı?",
    "Hey! Sohbet etmeye hazır mısın?",
    "Merhaba dostum! Bugün nasılsın?",
    "Selamlar! Ben Çenebaz v2.0, tanışalım mı?"
]

def rastgele_selamlama() -> str:
    return random.choice(SELAMLAMA_CEVAPLARI)

# -------------------------
# İSİM KATEGORİLERİ
# -------------------------

ERKEK_KLASIK = {"ahmet", "mehmet", "mustafa", "ali", "hüseyin", "hasan", "ibrahim"}
ERKEK_MODERN = {"emre", "burak", "mert", "arda", "atlas", "kerem", "yiğit", "fatih"}

KADIN_KLASIK = {"ayşe", "fatma", "emine", "hatice", "zeynep"}
KADIN_MODERN = {"defne", "ela", "duru", "arya", "mira", "melis", "irem", "azra"}

# -------------------------
# CEVAP HAVUZLARI (TONLU)
# -------------------------

CEVAPLAR = {

    "erkek_klasik": {
        "komik": [
            "{isim}. Bu isimle doğan insanlar genelde direkt ciddiye alınır.",
            "{isim} mi? Bu isimle mahallede saygı otomatik geliyor.",
        ],
        "sarkastik": [
            "{isim}. Klasik. Çok risk almamışsın.",
            "Tabii... {isim}. Sistem bunu bekliyordu zaten.",
        ],
        "dalkavuk": [
            "{isim}. Çok sağlam bir isim seçmişsin.",
            "Valla {isim} ismi karakterli duruyor.",
        ]
    },

    "erkek_modern": {
        "komik": [
            "{isim}. Bu isimle spor salonuna yazılma ihtimali yüksek.",
            "{isim} ha? Ana karakter vibes.",
        ],
        "sarkastik": [
            "{isim}. Modern... biraz fazla modern hatta.",
            "Evet evet {isim}. Trendleri yakalamışsın.",
        ],
        "dalkavuk": [
            "{isim}. Karizmatik isim, net.",
            "Güzel seçim {isim}. Enerji var.",
        ]
    },

    "kadin_klasik": {
        "komik": [
            "{isim}. Bu isimle herkes sana güvenmek zorunda hissediyor.",
            "{isim}... Bu isimde otomatik saygı var.",
        ],
        "sarkastik": [
            "{isim}. Zamansız… yani baya eski ama iyi anlamda.",
            "Tabii {isim}. Klasiklerden şaşmamışsın.",
        ],
        "dalkavuk": [
            "{isim}. Çok zarif bir isim.",
            "Gerçekten {isim} çok güzel duruyor.",
        ]
    },

    "kadin_modern": {
        "komik": [
            "{isim}. Bu isimle influencer olma ihtimali yüksek.",
            "{isim} ha? Estetik algı güçlü belli.",
        ],
        "sarkastik": [
            "{isim}. Modern… hatta biraz fazla havalı.",
            "Evet {isim}. Pinterest seviyesinde bir isim.",
        ],
        "dalkavuk": [
            "{isim}. Çok hoş bir isim seçmişsin.",
            "Gerçekten {isim} kulağa çok iyi geliyor.",
        ]
    },

    "bilinmiyor": {
        "komik": [
            "{isim}. Bu isim veri tabanımı korkuttu.",
            "{isim}? Bu yeni güncellemede mi geldi?",
        ],
        "sarkastik": [
            "{isim}. Bunu çözemedim ama saygı duyuyorum.",
            "İlginç... {isim}. Sistem bunu beklemiyordu.",
        ],
        "dalkavuk": [
            "{isim}. Özgün isimleri severim.",
            "Güzel, seni {isim} olarak kaydettim.",
        ]
    }
}

# -------------------------
# FONKSİYONLAR
# -------------------------

def normalize(isim: str) -> str:
    return isim.strip().lower()


def isim_kategorisi_bul(isim: str) -> str:
    isim = normalize(isim)

    if isim in ERKEK_KLASIK:
        return "erkek_klasik"
    if isim in ERKEK_MODERN:
        return "erkek_modern"
    if isim in KADIN_KLASIK:
        return "kadin_klasik"
    if isim in KADIN_MODERN:
        return "kadin_modern"

    return "bilinmiyor"


def isim_cevabi_uret(isim: str) -> str:
    kategori = isim_kategorisi_bul(isim)

    # rastgele ton seç
    ton = random.choice(["komik", "sarkastik", "dalkavuk"])

    sablon = random.choice(CEVAPLAR[kategori][ton])

    return sablon.format(isim=isim.strip())



# -------------------------
# YAYGIN MESLEKLER
# -------------------------

HIZMET_MESLEKLERI = {
    "garson", "servis elemanı", "komi", "barista",
    "aşçı", "kasiyer", "reyon görevlisi", "market elemanı",
    "satış elemanı", "çağrı merkezi müşteri temsilcisi",
    "müşteri temsilcisi", "turizm elemanı", "otelcilik elemanı",
    "güvenlik görevlisi", "özel güvenlik", "silahsız özel güvenlik"
}

TEKNIK_MESLEKLER = {
    "mühendis", "inşaat mühendisi", "makine mühendisi",
    "elektrik mühendisi", "mimar", "tekniker", "teknisyen",
    "yazılımcı", "programcı", "bilgisayar mühendisi"
}

SAGLIK_MESLEKLERI = {
    "doktor", "hemşire", "ebe", "paramedik", "eczacı",
    "fizyoterapist", "diş hekimi", "psikolog"
}

EGITIM_MESLEKLERI = {
    "öğretmen", "akademisyen", "özel ders öğretmeni",
    "rehber öğretmen"
}

OFIS_MESLEKLERI = {
    "memur", "sekreter", "muhasebeci", "finansçı",
    "insan kaynakları", "bankacı", "avukat", "danışman"
}

URETIM_MESLEKLERI = {
    "işçi", "fabrika işçisi", "konfeksiyon işçisi",
    "usta", "kalfa", "operatör", "şoför", "kurye"
}

def meslek_metninden_anahtar_bul(kullanici_girdisi: str) -> str:
    metin = kullanici_girdisi.strip().lower()

    tum_meslekler = (
        HIZMET_MESLEKLERI
        | TEKNIK_MESLEKLER
        | SAGLIK_MESLEKLERI
        | EGITIM_MESLEKLERI
        | OFIS_MESLEKLERI
        | URETIM_MESLEKLERI
    )

    for meslek in tum_meslekler:
        if meslek in metin:
            return meslek

    return metin


# -------------------------
# TONLU CEVAPLAR
# -------------------------

MESLEK_CEVAPLARI = {
    "hizmet": {
        "komik": [
            "{meslek} ha? İnsanla uğraşma DLC'sini satın almışsın.",
            "{meslek} diyorsun. Sabır seviyen muhtemelen benden yüksek."
        ],
        "sarkastik": [
            "Tabii, {meslek}. İnsanlığın yükünü yine sen çekiyorsun.",
            "{meslek}... demek yine medeniyet senin omuzlarında."
        ],
        "dalkavuk": [
            "{meslek} güzel iş. İletişim becerisi ister, herkeste olmaz.",
            "Valla {meslek} küçümsenecek iş değil. Ciddi emek var."
        ]
    },

    "teknik": {
        "komik": [
            "{meslek} mi? O zaman yanlış bir şey söylersem anında yakalanırım.",
            "{meslek} ha? Demek olaylara cetvelle bakıyorsun."
        ],
        "sarkastik": [
            "Anladım, {meslek}. Dünyayı yine siz ayakta tutuyorsunuz tabii.",
            "{meslek}... tamam, şimdi biraz daha dikkatli konuşayım da beni hesaplamayasın."
        ],
        "dalkavuk": [
            "{meslek} sağlam iş. Zekâ, disiplin, sabır; hepsi gerekiyor.",
            "Güzel meslek {meslek}. Ağırlığı var."
        ]
    },

    "saglik": {
        "komik": [
            "{meslek} mi? O zaman burada en ayakta kişi sensin.",
            "{meslek} ha? İnsanların canına bakıyorsun, ben cümlelere."
        ],
        "sarkastik": [
            "Tabii, {meslek}. Yine en kritik işlerden biri sende.",
            "{meslek}... yani stres seviyen muhtemelen tavanda."
        ],
        "dalkavuk": [
            "{meslek} çok saygı duyulan bir alan. Cidden değerli.",
            "Güzel meslek {meslek}. İnsan hayatına dokunuyorsun."
        ]
    },

    "egitim": {
        "komik": [
            "{meslek} mi? O zaman sabrın endüstriyel seviyededir.",
            "{meslek} ha? Bilgi aktarma işinin boss level'ındasın."
        ],
        "sarkastik": [
            "Tabii, {meslek}. Geleceği yine sessizce siz inşa ediyorsunuz.",
            "{meslek}... emek çok, takdir bazen az. Klasik."
        ],
        "dalkavuk": [
            "{meslek} çok kıymetli iş. Herkes yapamaz.",
            "Güzel meslek {meslek}. Etkisi uzun vadede ortaya çıkar."
        ]
    },

    "ofis": {
        "komik": [
            "{meslek} mi? Demek Excel ve toplantılarla düello yapıyorsun.",
            "{meslek} ha? Masa başı savaşlarının deneyimli tarafısın."
        ],
        "sarkastik": [
            "Anladım, {meslek}. Mail zincirlerinin gizli kahramanı.",
            "{meslek}... kurumsal hayat seni şekillendirmiş olmalı."
        ],
        "dalkavuk": [
            "{meslek} düzen ve dikkat ister. Hafife alınmaz.",
            "Güzel meslek {meslek}. Sistem insanı olduğun belli."
        ]
    },

    "uretim": {
        "komik": [
            "{meslek} mi? Gerçek iş yapan taraftasın yani.",
            "{meslek} ha? Ortamda laf değil iş üreten ekiptesin."
        ],
        "sarkastik": [
            "Tabii, {meslek}. Yine işin yükü sahadakilerde.",
            "{meslek}... masa başındakiler kadar konuşup siz kadar iş yapan az."
        ],
        "dalkavuk": [
            "{meslek} çok net iştir. Emeği görünürdür.",
            "Güzel meslek {meslek}. Gerçek üretim tarafındasın."
        ]
    },

    "bilinmiyor": {
        "komik": [
            "{meslek} mi? Veri tabanım kısa süreli bocaladı.",
            "{meslek}? İlginç. Meslek mi boss title mı çözemedim."
        ],
        "sarkastik": [
            "{meslek}... tamam, bunu sonra ayrıca işlemem gerekecek.",
            "İlginç, {meslek}. Sistem bunu ilk kez duyuyor olabilir."
        ],
        "dalkavuk": [
            "{meslek} güzel duruyor. Özgün bir alan olabilir.",
            "Tamam, seni {meslek} olarak not ettim."
        ]
    }
}

# -------------------------
# YARDIMCI FONKSİYONLAR
# -------------------------

def normalize_metin(metin: str) -> str:
    return metin.strip().lower()


def meslek_kategorisi_bul(meslek: str) -> str:
    temiz = normalize_metin(meslek)

    if temiz in HIZMET_MESLEKLERI:
        return "hizmet"
    if temiz in TEKNIK_MESLEKLER:
        return "teknik"
    if temiz in SAGLIK_MESLEKLERI:
        return "saglik"
    if temiz in EGITIM_MESLEKLERI:
        return "egitim"
    if temiz in OFIS_MESLEKLERI:
        return "ofis"
    if temiz in URETIM_MESLEKLERI:
        return "uretim"

    return "bilinmiyor"


def meslek_cevabi_uret(meslek: str) -> str:
    kategori = meslek_kategorisi_bul(meslek)
    ton = random.choice(["komik", "sarkastik", "dalkavuk"])
    sablon = random.choice(MESLEK_CEVAPLARI[kategori][ton])
    return sablon.format(meslek=meslek.strip())


# -------------------------
# YAŞ CEVAPLARI
# -------------------------

YAS_CEVAPLARI = {
    "cocuk": {
        "komik": [
            "{yas} yaş mı? Daha oyunun eğitim bölümlerindesin.",
            "{yas} ha? Hikâye yeni başlıyor."
        ],
        "sarkastik": [
            "{yas}. Tamam, hayat seni henüz fazla hırpalamamış.",
            "{yas} yaş güzel. Dertler demo sürümde."
        ],
        "dalkavuk": [
            "{yas} yaş harika. Önünde çok alan var.",
            "Güzel yaş {yas}. Enerji tarafı yüksek olur."
        ]
    },
    "genc": {
        "komik": [
            "{yas} yaş... tam ana karakter dönemi.",
            "{yas} mi? Enerji var, kafa biraz karışık olabilir."
        ],
        "sarkastik": [
            "{yas}. Hayatla pazarlıkların başladığı yaşlar.",
            "{yas} yaş... özgüven yüksek, uyku düzeni düşük olabilir."
        ],
        "dalkavuk": [
            "{yas} güzel yaş. Güç ve potansiyel birlikte geliyor.",
            "Harika. {yas} yaş gerçekten güçlü dönemlerden biri."
        ]
    },
    "yetiskin": {
        "komik": [
            "{yas} yaş mı? Sistem seni artık ciddiye almaya başlar.",
            "{yas} ha? Gençlik devam ediyor ama sorumluluklar da masaya oturmuş."
        ],
        "sarkastik": [
            "{yas}. Artık 'vakit hızlı geçiyor' cümlesi anlam kazanmaya başlar.",
            "{yas} yaş... ne tam gençliği bırakırsın ne yetişkinliği tam kabullenirsin."
        ],
        "dalkavuk": [
            "{yas} çok iyi yaş. Denge kurulmaya başlar.",
            "Güzel. {yas} yaş, güçle aklın ortaklığa başladığı dönemdir."
        ]
    },
    "orta_yas": {
        "komik": [
            "{yas} yaş... tecrübe paketini açmışsın.",
            "{yas} ha? Artık gençlere bakıp 'bizim zamanımızda' deme riski başlıyor."
        ],
        "sarkastik": [
            "{yas}. Sistem seni artık deneyimli kullanıcı sınıfına aldı.",
            "{yas} yaş... hata payın azalır ama sabır kotan da test edilir."
        ],
        "dalkavuk": [
            "{yas} çok güçlü yaş. Tecrübe ciddi avantajdır.",
            "Güzel yaş {yas}. İnsan kendini daha net tanımaya başlar."
        ]
    },
    "ileri_yas": {
        "komik": [
            "{yas} yaş mı? Artık olaylara üst katmandan bakıyorsun.",
            "{yas} ha? Tecrübe puanın çoğu sistemi sollamıştır."
        ],
        "sarkastik": [
            "{yas}. Gençlerin anlamsız özgüvenini uzaktan izleme dönemi.",
            "{yas} yaş... artık çoğu konuda 'bunu da gördük' diyebilirsin."
        ],
        "dalkavuk": [
            "{yas} çok kıymetli bir dönem. Tecrübenin ağırlığı büyük olur.",
            "Güzel yaş {yas}. Birikim tarafı çok güçlüdür."
        ]
    },
    "bilinmiyor": {
        "komik": [
            "Bu yaşı çözemedim. Sistem nüfus müdürlüğüne bağlanamadı.",
            "Yaş olarak bunu işleyemedim ama ilginç duruyor."
        ],
        "sarkastik": [
            "Bunu yaş olarak kabul edeyim mi, emin olamadım.",
            "İlginç... bunu yaş hanesine yazmak biraz cesaret ister."
        ],
        "dalkavuk": [
            "Tamam, yaş bilgisini sonra daha net alırız.",
            "Sorun değil, bunu şimdilik es geçiyorum."
        ]
    }
}

def yas_sayisini_bul(kullanici_girdisi: str) -> int | None:
    metin = kullanici_girdisi.strip()
    sayi_metni = ""

    for karakter in metin:
        if karakter.isdigit():
            sayi_metni += karakter

    if sayi_metni:
        return int(sayi_metni)

    return None


def yas_kategorisi_bul(yas: int | None) -> str:
    if yas is None:
        return "bilinmiyor"

    if yas < 13:
        return "cocuk"
    if yas < 20:
        return "genc"
    if yas < 36:
        return "yetiskin"
    if yas < 56:
        return "orta_yas"

    return "ileri_yas"


def yas_cevabi_uret(kullanici_girdisi: str) -> str:
    yas = yas_sayisini_bul(kullanici_girdisi)
    kategori = yas_kategorisi_bul(yas)
    ton = random.choice(["komik", "sarkastik", "dalkavuk"])
    sablon = random.choice(YAS_CEVAPLARI[kategori][ton])

    if yas is None:
        return sablon

    return sablon.format(yas=yas)

# ============================================================
# KAPANIS CEVAPLARI
# ============================================================

KAPANIS_CEVAPLARI = [
    "Tamam, temel verileri aldım. Sohbete geçelim mi?",
    "İyi. Artık seni biraz tanıdım sayılır. Devam edelim.",
    "Güzel. Profil tamamlandı, şimdi gerçek sohbet başlıyor.",
    "Kayıt tamamlandı. Şimdi ne konuşmak istersen.",
    "Anladım. Bunları not ettim. Hazır olduğunda devam edelim.",
]


def rastgele_kapanis() -> str:
    return random.choice(KAPANIS_CEVAPLARI)


# ============================================================
# HOBİ CEVAPLARI
# ============================================================

AKTIF_HOBİLER = {
    "spor", "futbol", "basketbol", "koşu", "yüzme", "bisiklet",
    "voleybol", "tenis", "yürüyüş", "trekking", "dağcılık",
    "fitness", "yoga", "pilates", "dans", "boks", "güreş"
}

SANATSAL_HOBİLER = {
    "müzik", "gitar", "piyano", "keman", "çizim", "resim",
    "heykel", "fotoğrafçılık", "fotoğraf", "yazarlık", "şiir",
    "tiyatro", "sinema", "film izlemek", "dizi izlemek"
}

ENTELEKTUEL_HOBİLER = {
    "kitap okumak", "okumak", "satranç", "bulmaca",
    "tarih", "felsefe", "bilim", "araştırma", "podcast dinlemek"
}

DIJITAL_HOBİLER = {
    "oyun", "oyun oynamak", "video oyunları", "mobil oyun",
    "programlama", "kod yazmak", "youtube", "twitch"
}

HOBİ_CEVAPLARI = {
    "aktif": {
        "komik": [
            "{hobi} ha? Kanepe senin için yapılmamış belli.",
            "{hobi} yapıyorsun. Demek kaslar çalışıyor, metabolizma mutlu."
        ],
        "sarkastik": [
            "{hobi}. Vücut hâlâ itaat ediyor, iyi.",
            "Anladım, {hobi}. Enerji fazlanı bir yere harcıyorsun."
        ],
        "dalkavuk": [
            "{hobi} harika seçim. Hem beden hem zihin için değerli.",
            "Güzel hobi {hobi}. Disiplin ister, herkeste olmaz."
        ]
    },
    "sanatsal": {
        "komik": [
            "{hobi} ha? Demek duygusal derinlik tarafı açık.",
            "{hobi}... yaratıcı ruh var."
        ],
        "sarkastik": [
            "{hobi}. Sanatçı ruhu bari sende kalsın.",
            "Anladım, {hobi}. Dünyanın güzelliğini sen taşıyacaksın."
        ],
        "dalkavuk": [
            "{hobi} çok güzel bir uğraş. Yaratıcılık büyük nimet.",
            "Harika. {hobi} yapan insanlar dünyayı daha iyi hissettiriyor."
        ]
    },
    "entelektuel": {
        "komik": [
            "{hobi} ha? Beyin boş kalmıyor sende hiç.",
            "{hobi}... bu hobinin yanında biraz uyku da önerebilirim."
        ],
        "sarkastik": [
            "{hobi}. Aydın taraf aktif, sistem bunu not etti.",
            "Anladım, {hobi}. Kafa yorulmak istemiyor ama sürekli çalışıyor."
        ],
        "dalkavuk": [
            "{hobi} çok değerli bir uğraş. Zihin gelişimi kolay olmuyor.",
            "Güzel hobi {hobi}. Merak eden insan olmak büyük artı."
        ]
    },
    "dijital": {
        "komik": [
            "{hobi} ha? Ekran süresi raporun muhtemelen cesur rakamlar içeriyor.",
            "{hobi}... parmaklar yorulmaz ama gözler bazen itiraz eder."
        ],
        "sarkastik": [
            "{hobi}. Modern çağın getirisi, kim ne diyebilir.",
            "Anladım, {hobi}. Karanlık odada yaşanabilir aslında."
        ],
        "dalkavuk": [
            "{hobi} günümüzde geçerli bir hobi. Dijital dünya da gerçek dünya.",
            "Güzel. {hobi} de bir beceri, kim ne derse desin."
        ]
    },
    "bilinmiyor": {
        "komik": [
            "{hobi} mi? Kategorize edemedim ama ilginç.",
            "{hobi}... bu veri tabanımda yok ama saygı duyuyorum."
        ],
        "sarkastik": [
            "{hobi}. Özgün seçim, sistemi zorladın.",
            "Anladım, {hobi}. Kalıpların dışına çıkmışsın."
        ],
        "dalkavuk": [
            "{hobi} özgün bir hobi. Herkesin gitmediği yolda ilerliyorsun.",
            "Güzel, {hobi}. Sıradışı hobiler karakteri ortaya koyar."
        ]
    }
}


def hobi_kategorisi_bul(hobi: str) -> str:
    temiz = hobi.strip().lower()
    if any(h in temiz for h in AKTIF_HOBİLER):
        return "aktif"
    if any(h in temiz for h in SANATSAL_HOBİLER):
        return "sanatsal"
    if any(h in temiz for h in ENTELEKTUEL_HOBİLER):
        return "entelektuel"
    if any(h in temiz for h in DIJITAL_HOBİLER):
        return "dijital"
    return "bilinmiyor"


def hobi_cevabi_uret(hobi: str) -> str:
    kategori = hobi_kategorisi_bul(hobi)
    ton = random.choice(["komik", "sarkastik", "dalkavuk"])
    sablon = random.choice(HOBİ_CEVAPLARI[kategori][ton])
    return sablon.format(hobi=hobi.strip())


# ============================================================
# MEMLEKET / ŞEHİR CEVAPLARI
# ============================================================

BUYUK_SEHIRLER = {
    "istanbul", "ankara", "izmir", "bursa", "antalya",
    "adana", "konya", "gaziantep", "mersin", "kayseri"
}

KUCUK_SEHIRLER = {
    "artvin", "ardahan", "bayburt", "tunceli", "sinop",
    "kastamonu", "yozgat", "kırşehir", "aksaray", "niğde",
    "karaman", "ısparta", "burdur"
}

TURISTIK_SEHIRLER = {
    "kapadokya", "bodrum", "marmaris", "fethiye", "pamukkale",
    "trabzon", "rize", "erzurum", "van", "mardin", "hatay",
    "muğla", "çanakkale"
}

SEHIR_CEVAPLARI = {
    "buyuk": {
        "komik": [
            "{sehir} mi? Trafik ve kalabalık paketi dahil, anladık.",
            "{sehir}... demek büyük şehir hayatının tüm nimetlerini yaşıyorsun."
        ],
        "sarkastik": [
            "{sehir}. Kalabalık, pahalı ama 'şehirde yaşıyorum' avantajı var.",
            "Anladım, {sehir}. Metro + trafik + gürültü üçlüsü yanında."
        ],
        "dalkavuk": [
            "{sehir} güzel şehir. İmkânlar açısından avantajlı.",
            "Harika. {sehir} olanaklarıyla fırsatlar da çok olur."
        ]
    },
    "kucuk": {
        "komik": [
            "{sehir} ha? Herkes herkesi tanır, sır saklamak zordur.",
            "{sehir}... sakin hayat, az trafik, çok dedikodu paketi."
        ],
        "sarkastik": [
            "{sehir}. Büyük şehrin gürültüsünden uzak en azından.",
            "Anladım, {sehir}. Huzur var ama 'yok bu şehirde' cümlesi de çok kullanılır."
        ],
        "dalkavuk": [
            "{sehir} samimi bir yer olur genelde. İnsan ilişkileri daha sıcak.",
            "Güzel. {sehir} gibi yerlerde hayat daha nefes alabilir."
        ]
    },
    "turistik": {
        "komik": [
            "{sehir} mi? Yerli halk turistten fazla mı, o soru hep açık.",
            "{sehir}... yaz aylarında yüzde kaç turist yüzde kaç yerel?"
        ],
        "sarkastik": [
            "{sehir}. Tarihin ve turizmin iç içe geçtiği yer. Fiyatlar da ona göre.",
            "Anladım, {sehir}. Güzel ama yazın 'bu şehirde nasıl yaşanır' sorusu meşru."
        ],
        "dalkavuk": [
            "{sehir} değerli bir yer. Hem tarih hem güzellik bir arada.",
            "Harika. {sehir} gibi yerlerde yaşamak ayrı bir his olmalı."
        ]
    },
    "bilinmiyor": {
        "komik": [
            "{sehir} mi? Harita uygulamam tereddüt etti biraz.",
            "{sehir}... bu şehri özgün bırakalım."
        ],
        "sarkastik": [
            "{sehir}. Sistem bunu ilk kez duydu olabilir.",
            "Anladım, {sehir}. Tanımadığım yer ama saygı duyuyorum."
        ],
        "dalkavuk": [
            "{sehir} güzel geliyor. Az bilinen yerler genelde sürpriz çıkar.",
            "Tamam, {sehir}. Keşfedilmemiş güzellikler olabilir."
        ]
    }
}


def sehir_kategorisi_bul(sehir: str) -> str:
    temiz = sehir.strip().lower()
    if temiz in BUYUK_SEHIRLER:
        return "buyuk"
    if temiz in KUCUK_SEHIRLER:
        return "kucuk"
    if temiz in TURISTIK_SEHIRLER:
        return "turistik"
    return "bilinmiyor"


def sehir_cevabi_uret(sehir: str) -> str:
    kategori = sehir_kategorisi_bul(sehir)
    ton = random.choice(["komik", "sarkastik", "dalkavuk"])
    sablon = random.choice(SEHIR_CEVAPLARI[kategori][ton])
    return sablon.format(sehir=sehir.strip())


# ============================================================
# FAVORİ YEMEK & MÜZİK CEVAPLARI
# ============================================================

TURK_YEMEKLERI = {
    "kebap", "döner", "köfte", "lahmacun", "pide", "börek",
    "mantı", "iskender", "çorba", "mercimek", "pilav",
    "dolma", "sarma", "baklava", "künefe", "kadayıf"
}

DUNYA_MUTFAGI = {
    "pizza", "burger", "sushi", "ramen", "pasta", "taco",
    "steak", "salata", "wrap", "sandviç", "makarna"
}

FAVORİ_CEVAPLARI = {
    "yemek_turk": {
        "komik": [
            "{sey} ha? Milli bilinç güçlü, damak vatan sevgisiyle dolu.",
            "{sey}... yerli üretim taraftarısın, anladım."
        ],
        "sarkastik": [
            "{sey}. Klasik tercih. Ama kimse kötü seçmez bunu.",
            "Anladım, {sey}. Dünya mutfağına baktın sonunda 'yok bundan iyisi' dedin."
        ],
        "dalkavuk": [
            "{sey} harika seçim. Türk mutfağı zaten tartışmasız.",
            "Güzel. {sey} seçen insanın lezzet anlayışına güvenilir."
        ]
    },
    "yemek_dunya": {
        "komik": [
            "{sey} ha? Sınırları aşmış, global damak.",
            "{sey}... pasaportsuz tatilleri yemekle yapıyorsun."
        ],
        "sarkastik": [
            "{sey}. Dünya mutfağı keşfedilmiş, iyi.",
            "Anladım, {sey}. Farklı tatlar peşindesin."
        ],
        "dalkavuk": [
            "{sey} güzel seçim. Farklı kültürlere açık olmak iyidir.",
            "Harika. {sey} seçen biri meraklı ve açık fikirlidir genelde."
        ]
    },
    "muzik": {
        "komik": [
            "{sey} ha? Kulaklık olmadan yaşanmaz öyleyse.",
            "{sey}... bu türü yüksek sesle açmak komşu ilişkilerini sınıyor olabilir."
        ],
        "sarkastik": [
            "{sey}. Müzik zevki netleşmiş, iyi.",
            "Anladım, {sey}. Playlist'in belli bir karakteri var demek."
        ],
        "dalkavuk": [
            "{sey} güzel tür. Müzik zevki olan biri belli.",
            "Harika seçim, {sey}. Müzikle geçen zaman boşa gitmiyor."
        ]
    },
    "bilinmiyor": {
        "komik": [
            "{sey} ha? Kategorim bunu kaldırmadı ama not ettim.",
            "{sey}... özgün zevkler her zaman ilginç."
        ],
        "sarkastik": [
            "{sey}. Sistem bunu beklemiyordu ama saygı duyuyor.",
            "Anladım, {sey}. Kalıpların dışına çıkılmış."
        ],
        "dalkavuk": [
            "{sey} güzel tercih. Özgün zevkler karakteri yansıtır.",
            "Tamam, {sey}. Farklı tercihler her zaman ilginç."
        ]
    }
}


def favori_yemek_cevabi_uret(yemek: str) -> str:
    temiz = yemek.strip().lower()
    if any(y in temiz for y in TURK_YEMEKLERI):
        kategori = "yemek_turk"
    elif any(y in temiz for y in DUNYA_MUTFAGI):
        kategori = "yemek_dunya"
    else:
        kategori = "bilinmiyor"
    ton = random.choice(["komik", "sarkastik", "dalkavuk"])
    sablon = random.choice(FAVORİ_CEVAPLARI[kategori][ton])
    return sablon.format(sey=yemek.strip())


def favori_muzik_cevabi_uret(muzik: str) -> str:
    ton = random.choice(["komik", "sarkastik", "dalkavuk"])
    sablon = random.choice(FAVORİ_CEVAPLARI["muzik"][ton])
    return sablon.format(sey=muzik.strip())


# ============================================================
# GÜNDEM / RUH HALİ CEVAPLARI
# ============================================================

IYET_IFADELERI = {
    "iyi", "güzel", "harika", "mükemmel", "süper",
    "çok iyi", "gayet iyi", "pozitif", "mutlu"
}

KOTU_IFADELERI = {
    "kötü", "berbat", "yorgun", "yoruldum", "bıktım",
    "bunaldım", "stresli", "sıkıldım", "üzgün",
    "mutsuz", "sinirli", "gergin", "hasta"
}

NOTR_IFADELERI = {
    "fena değil", "idare eder", "şöyle böyle",
    "normal", "sıradan", "eh", "orta", "karışık"
}

RUH_HALİ_CEVAPLARI = {
    "iyi": {
        "komik": [
            "İyi misin? Şüpheyle yaklaşıyorum ama güzel.",
            "İyi ha? Bu böyle devam ederse hayal kırıklığına hazır ol."
        ],
        "sarkastik": [
            "İyi olduğunu söylüyorsun. Sistem bunu not etti.",
            "Anladım, iyisin. Bari biri iyi olsun."
        ],
        "dalkavuk": [
            "İyi olmak güzel şey. Bu enerjiyi koru.",
            "Güzel! İyi ruh hali bulaşıcıdır, etrafına yayarsın."
        ]
    },
    "kotu": {
        "komik": [
            "Kötü mü? En azından dürüstsün, bu artı.",
            "Kötü ha? Kötü günler de geçiyor, iyi haber bu."
        ],
        "sarkastik": [
            "Kötüsün. Tamam, dürüstlük politikası aktif.",
            "Anladım, kötü. En azından 'iyiyim' yalanını söylemedin."
        ],
        "dalkavuk": [
            "Kötü günler geçici. Yarın daha iyi olur, cidden.",
            "Üzüldüm. Ama konuşmak bazen işe yarar, buradayım."
        ]
    },
    "notr": {
        "komik": [
            "Fena değil mi? Klasik Türk cevabı. Tam orta.",
            "Şöyle böyle ha? En az enerji harcayan ruh hali."
        ],
        "sarkastik": [
            "Orta. Sistem de bazen öyle hissediyor.",
            "Anladım, ne iyi ne kötü. Kararsızlık kendi başına bir durum."
        ],
        "dalkavuk": [
            "Orta da olsa ayaktasın, bu önemli.",
            "Fena değil yeterli bazen. Her gün harika olmak zorunda değil."
        ]
    },
    "bilinmiyor": {
        "komik": [
            "Ruh halini tam çözemedim ama konuşmaya devam edelim.",
            "Bu cevabı sınıflandıramadım, özgün ruh hali."
        ],
        "sarkastik": [
            "Anladım galiba. Ya da anlamadım. Devam edelim.",
            "Sistem bunu işleyemedi ama geçelim."
        ],
        "dalkavuk": [
            "Her ne hissediyorsan, burada konuşabiliriz.",
            "Tamam, nasıl olursan ol sohbet devam eder."
        ]
    }
}


def ruh_hali_kategorisi_bul(ifade: str) -> str:
    temiz = ifade.strip().lower()
    if any(i in temiz for i in IYET_IFADELERI):
        return "iyi"
    if any(i in temiz for i in KOTU_IFADELERI):
        return "kotu"
    if any(i in temiz for i in NOTR_IFADELERI):
        return "notr"
    return "bilinmiyor"


def ruh_hali_cevabi_uret(ifade: str) -> str:
    kategori = ruh_hali_kategorisi_bul(ifade)
    ton = random.choice(["komik", "sarkastik", "dalkavuk"])
    sablon = random.choice(RUH_HALİ_CEVAPLARI[kategori][ton])
    return sablon


# ============================================================
# SERBEST SOHBET — anahtar kelime tabanlı yönlendirme
# ============================================================

SERBEST_HAVUZ = [
    "Anlıyorum. Devam et, dinliyorum.",
    "İlginç. Bunu biraz açar mısın?",
    "Hmm, bunu daha önce duymadım. Devam?",
    "Katılıyorum aslında. Ya da katılmıyorum. İkisi de olabilir.",
    "Bu konuda ne düşündüğümü sorsaydın... sormadın ama söyleyebilirim.",
    "Anladım. Sistem bunu işledi ve devam ediyor.",
    "Evet, mantıklı. Peki ya sen ne düşünüyorsun?",
    "Bu konu açılınca çok şey söylenebilir. Sana bırakıyorum.",
    "Tamam, bunu not ettim. Devam edelim.",
]


def serbest_cevap_uret(girdi: str) -> str:
    temiz = girdi.strip().lower()

    if any(k in temiz for k in ["hobi", "uğraş", "ilgilen"]):
        return hobi_cevabi_uret(girdi)
    if any(k in temiz for k in ["şehir", "memleket", "nereli", "yaşıyor"]):
        return sehir_cevabi_uret(girdi)
    if any(k in temiz for k in ["yemek", "yiyor", "sever", "sevi"]):
        return favori_yemek_cevabi_uret(girdi)
    if any(k in temiz for k in ["müzik", "dinle", "şarkı", "sanatçı"]):
        return favori_muzik_cevabi_uret(girdi)
    if any(k in temiz for k in ["iyi", "kötü", "yorgun", "mutlu", "üzgün", "stres"]):
        return ruh_hali_cevabi_uret(girdi)

    return random.choice(SERBEST_HAVUZ)
