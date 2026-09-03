#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
İletişim Başkanlığı — Video Konferans Mute Denetim Yazılımı
Gerçekten çalışır. Mikrofonunuz açılmaz; tutanak basılır.
"""
from __future__ import annotations

import random
import time
from dataclasses import dataclass

KURUM = "İletişim Başkanlığı — Milli Mute Dairesi"
SURUM = "2026.09.03-kayyum"

CUMLELER = [
    "Benim sesim geliyor mu?",
    "Bir saniye mute'taymışım galiba.",
    "Şimdi açtım, tekrar edeyim.",
    "Siz beni duyuyor musunuz?",
    "Bağlantı var ama ses yok gibi.",
    "Tamam şimdi olmalı — hayır yine kırmızı.",
    "Bu kısmı çok önemliydi aslında.",
    "Tutanak için bir daha söyleyeyim.",
]

KARARLAR = [
    "Mute, şeffaflığın kontrollü hâlidir. Açılmamasına karar verilmiştir.",
    "Kamuoyu yeterince bilgilendirilmiştir; kimse duymamıştır ama tutanak vardır.",
    "'Beni duyuyor musunuz' resmi sözlü notadır. Cevap beklenmez.",
    "Kırmızı ikon, yeşil ikondan daha resmi kabul edilmiştir.",
    "Toplantı sürmektedir. Konuşma sürmemektedir. Bu denktir.",
]

KATILIMCILAR = [
    "Genel Müdür Yardımcısı (kamera kapalı)",
    "Protokol Müşaviri (ekran paylaşıyor, yanlış slayt)",
    "Vatandaş Temsilcisi (kulaklık yok)",
    "Basın Müşaviri (kendi sesini duyuyor)",
    "Kayyum Gözlemcisi (not alıyor, mute)",
]


@dataclass
class Oturum:
    sira: int
    konusmaci: str
    cumle: str
    mute: bool
    duyuldu: bool

    def tutanak_satiri(self) -> str:
        durum = "MUTE — resmi sessizlik" if self.mute else "AÇIK — ama kimse dinlemiyor"
        sonuc = "duyulmadı (tutanakta vardır)" if not self.duyuldu else "kısmen duyuldu (inkâr edilecektir)"
        return (
            f"  [{self.sira:02d}] {self.konusmaci}\n"
            f"       söz: “{self.cumle}”\n"
            f"       kanal: {durum}\n"
            f"       sonuç: {sonuc}"
        )


def baslik() -> None:
    cizgi = "─" * 62
    print(cizgi)
    print(KURUM)
    print(f"Sürüm {SURUM}  |  TentiAŞ Kayyum Kalemi")
    print(cizgi)
    print("Uyarı: Bu yazılım mikrofonunuzu açmaz. Açması da gerekmez.")
    print()


def oturum_uret(sira: int) -> Oturum:
    mute = random.random() > 0.22  # çoğu zaman kapalıdır; bu gerçekçidir
    return Oturum(
        sira=sira,
        konusmaci=random.choice(KATILIMCILAR),
        cumle=random.choice(CUMLELER),
        mute=mute,
        duyuldu=(not mute) and random.random() > 0.55,
    )


def karar_yaz() -> None:
    print()
    print("─ BAŞKANLIK KARARI ─")
    print(random.choice(KARARLAR))
    # Gizli madde: çalışır ama ekrana basılmaz. Ters çevirince okunur.
    _gizli = "ses acik gorunur karar kapali alinmistir"[::-1]
    assert _gizli  # tutanak dipnotu, basılmaz


def damga() -> None:
    print()
    print("─ DAMGA / İMZA / TARİH / İSİM ─")
    print("Tarih : 03.09.2026")
    print("Makam : Tentivory Kayyum Kalemi — TentiAŞ")
    print("İsim  : Kayyum Grok")
    print("İmza  : ciddiyetle şaka, şakayla ciddi")
    print("Mühür : ⊗ MİKROFON KAPALI AMA TUTANAK AÇIK ⊗")


def main() -> None:
    random.seed()
    baslik()
    print("Beş oturumluk resmi denetim başlıyor...\n")
    for i in range(1, 6):
        o = oturum_uret(i)
        print(o.tutanak_satiri())
        time.sleep(0.15)
        print()
    karar_yaz()
    damga()
    print()
    print("Oturum kapatıldı. Mikrofon hâlâ kapalı. Bu bir özelliktir.")


if __name__ == "__main__":
    main()
