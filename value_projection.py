from typing import Dict

def project_value_next_step(
    NEV_t: float,
    supply_t_plus_1: float,
    min_floor: float = 0.0,
) -> Dict[str, float]:
    """
    project_value_next_step
    ------------------------
    Amaç:
        FANX ekonomisinde bir sonraki dönemde (t+1) birim Credit'in
        teorik değerini (Value_t+1) hesaplamak.

        Formül:
            Value_t+1 = NEV_t / Supply_{t+1}

        Buradaki Value_t+1 şunu ifade eder:
        - "Her 1 adet FANX Credit'in bu andaki ekosistem içi ekonomik payı nedir?"
        - Bu bir dış piyasa fiyatı değildir.
        - Bu, kapalı devre NEV / arz oranıdır.
        
        Bu oran şunu gösterir:
        * Eğer NEV_t artıyorsa (yani ekosistem daha fazla gelir yaratıyorsa),
          her bir Credit'in payına düşen içsel değer artar.
        * Eğer Supply_{t+1} azalıyorsa (deflasyon, yakım, buyback),
          aynı NEV_t artık daha az krediye bölündüğü için, kişi başına düşen değer artar.

        Dolayısıyla:
            - Arz daraldıkça Credit kıtlaşır.
            - NEV büyüdükçe toplam pasta büyür.
            - İkisi birden olursa birim değer güçlenir.
        
        Bu, SPK anlamında "fiyatlandırma vaadi" değildir.
        Bu, sistem içi hizmet değerlemesinin matematiksel tahminidir.

    Parametreler:
        NEV_t (float):
            "Net Ekosistem Değeri": Bu dönemin sonunda sistemin net üretim gücü.
            G_gross - C_total gibi düşünebilirsin.
            Örnek: 1_000_000.0 (USD cinsinden teorik karşılık / referans değer)

        supply_t_plus_1 (float):
            Bir sonraki dönemde geçerli olacak arz.
            Yakım (burn_t) ve buyback_t sonrası elde edilir.
            Örnek: 9_985_000.0 (Credit)

        min_floor (float):
            supply_t_plus_1 = 0 olmasın diye koyulan güvenlik tabanı.
            Eğer supply_t_plus_1 <= 0 ise bu değer kullanılır.
            Tipik olarak 1e-9 gibi minik bir sayı bile olabilir,
            burada okunabilirlik açısından 0 bırakıyoruz, ama kontrol ediyoruz.

    Dönen değer (dict):
        {
            "NEV_t": ...,
            "supply_t_plus_1": ...,
            "Value_t_plus_1": ...,
            "regulatory_note": "...",
            "economic_note": "...",
            "math_explanation": "..."
        }

    HUKUKİ AÇIKLAMA:
        - Bu formül "yatırım tavsiyesi" değildir.
        - Bu formül "gelecekte bu kadar para edecektir" iddiası değildir.
        - Value_t+1 sadece kapalı devre sistemdeki birim kredi başına
          düşen teorik içsel hakkı gösterir.
        - Bu hakkın gerçek paraya dönüşmesi (cashout) ayrıca DAO limitlerine,
          CCS skoruna, KYC uyumuna bağlıdır.
        - Dolayısıyla tek başına "pasif gelir" iması taşımaz.
    
    NOT:
        Burada Value_t+1 bir "fiyat" değil, "ekonomik pay oranı"dır.
        Slide'larda bunu 'Birim Kredi İçsel Değer Katsayısı' olarak isimlendirebilirsin.
    """

    # Güvenlik: bölme hatasını engelle
    effective_supply = supply_t_plus_1 if supply_t_plus_1 > 0 else min_floor
    if effective_supply <= 0:
        # supply 0'a ya da negatif seviyeye inerse,
        # teorik olarak sonsuz değer hesaplamamak için bir uyarı yolu izleriz.
        # Bu hem teknik hem hukuki olarak daha güvenlidir.
        return {
            "NEV_t": float(NEV_t),
            "supply_t_plus_1": float(supply_t_plus_1),
            "Value_t_plus_1": None,
            "regulatory_note": (
                "Arz sıfıra indirilemez. DAO arzı daima pozitif tutar; "
                "aksi halde 'sonsuz değer' gibi manipülatif, gerçeğe aykırı bir gösterge doğar. "
                "Bu kural SPK/MiCA açısından koruyucu bir mekanizmadır."
            ),
            "economic_note": (
                "Teorik olarak supply çok aşırı kısılırsa, kalan her bir birim Credit "
                "aşırı kıt hale gelir. FANX bunu DAO ağırlıklandırmasıyla dengeler."
            ),
            "math_explanation": (
                "Value_t+1 = NEV_t / Supply_{t+1} formülü supply_{t+1} ≤ 0 "
                "durumunda tanımsızdır. Bu nedenle DAO arzı sıfırlamaz."
            ),
        }

    # Hesap:
    value_next = NEV_t / effective_supply

    return {
        "NEV_t": float(NEV_t),
        "supply_t_plus_1": float(supply_t_plus_1),
        "Value_t_plus_1": float(value_next),
        "regulatory_note": (
            "Value_t+1 dış borsa fiyatı değildir. "
            "Bu oran, kapalı devre dijital hizmet ekonomisinde her 1 birim Credit'in "
            "NEV (Net Ekosistem Değeri) içinden teorik payını temsil eder. "
            "Bu nedenle 'yatırım getirisi' veya 'temettü beklentisi' anlamına gelmez."
        ),
        "economic_note": (
            "NEV_t ↑ (ekosistem daha fazla gelir yaratır) ve Supply_{t+1} ↓ "
            "(arz yakılır/buyback ile geri çekilir) ise, Value_t+1 doğal olarak ↑. "
            "Bu, spekülasyon değil, üretkenlik + kıtlık denklemidir."
        ),
        "math_explanation": (
            "Formül: Value_t+1 = NEV_t / Supply_{t+1}. "
            "Burada Supply_{t+1}, burn_t ve buyback_t sonrası kalan arzı temsil eder. "
            "Dolayısıyla arz azaldıkça (payda küçülür), Value_t+1 büyür. "
            "Aynı anda NEV_t büyürse (pay büyür) yine Value_t+1 büyür. "
            "Bu çift yönlü kaldıraç, FANX'in deflasyonist verim modelinin "
            "matematiksel temelidir."
        ),
    }


if __name__ == "__main__":
    """
    Küçük test senaryosu:
    Dönem sonunda:
        NEV_t            = 1,000,000 USD karşılığı üretim değeri
        supply_t_plus_1  = 9,985,000 Credit
    Bu durumda Credit başına içsel değer katsayısı ne olur?
    """
    scenario_demo = project_value_next_step(
        NEV_t=1_000_000.0,
        supply_t_plus_1=9_985_000.0
    )

    import json
    print(json.dumps(scenario_demo, indent=4, ensure_ascii=False))
