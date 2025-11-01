import math
from typing import Dict, List


def calculate_reward_preview(
    ccs_scores: List[float],
    fan_pool_usd: float,
    user_index: int,
) -> Dict[str, float]:
    """
    FANX Reward Preview Hesaplayıcı
    --------------------------------
    Amacı:
        Bir kullanıcının (örneğin "Ayşe") Fan Pool'dan potansiyel olarak
        ne kadar pay alacağını önizleme olarak hesaplamak.
        Bu "temettü" değildir, bu "katkı payı"dır.

    Hukuki statü:
        - Bu dağıtım SPK anlamında temettü / kâr payı değildir.
        - TBK m.393 uyarınca ifa edilen dijital hizmetin karşılığıdır.
        - Kullanıcı pasif yatırımcı değildir; aktif emek sahibidir.
        - Bu bir "preview"dir, garanti değildir.

    Parametreler:
        ccs_scores   : Tüm kullanıcıların CCS (Composite Contribution Score) listesi.
                       CCS_i = Aktiflik_i * α + Kalite_i * β + AğEtkisi_i * γ
                       Yani katkı kalitesi + topluluk etkisi.
        fan_pool_usd : Fan Pool büyüklüğü ($). Örnek: NEV * 0.40
                       Bu havuz, sistemin o dönemde kullanıcı katkısı için ayırdığı fondur.
        user_index   : Hangi kullanıcıyı hesaplayacağımızın dizini. (0-based)

    Dönen Değerler:
        {
            "user_ccs": ...,
            "ccs_total": ...,
            "raw_share_ratio": ...,
            "reward_estimate_usd": ...,
            "legal_note": "...",
            "safety_note": "...",
        }

    Matematik:
        Kullanıcı pay oranı = user_CCS / sum(CCS_all)
        Kullanıcı pay miktarı ($) = pay oranı * Fan Pool ($)

        reward_estimate_usd = (ccs_i / Σccs_n) * fan_pool_usd

    Çok kritik:
        Bu çıktı, "garanti edilen gelir" değildir.
        Bir "katılım/katkı payı simülasyonu"dur.

    """

    # Güvenlik kontrolleri
    if user_index < 0 or user_index >= len(ccs_scores):
        raise IndexError("user_index geçersiz (listede yok).")

    # Toplam katkı puanı (Σ CCS)
    total_ccs = sum(max(score, 0.0) for score in ccs_scores)

    # Sıfır bölme güvenliği
    if total_ccs <= 0:
        return {
            "user_ccs": 0.0,
            "ccs_total": 0.0,
            "raw_share_ratio": 0.0,
            "reward_estimate_usd": 0.0,
            "legal_note": (
                "Herhangi bir katkı puanı olmadığı için dağıtılabilir katkı karşılığı yoktur. "
                "Bu durum pasif bekleme ile gelir elde edilemeyeceğini doğrular."
            ),
            "safety_note": (
                "Dağıtım yok → Ponzi / pasif kazanç / temettü algısı yok. "
                "Sistem sadece aktif katkıyı ödüller."
            ),
        }

    # İlgili kullanıcının katkı puanı
    user_ccs = max(ccs_scores[user_index], 0.0)

    # Pay oranı
    share_ratio = user_ccs / total_ccs

    # Teorik tahmini katkı karşılığı ödül ($)
    reward_usd = share_ratio * fan_pool_usd

    return {
        "user_ccs": user_ccs,
        "ccs_total": total_ccs,
        "raw_share_ratio": share_ratio,
        "reward_estimate_usd": reward_usd,
        "legal_note": (
            "Bu hesaplanan tutar temettü değildir. "
            "Bu bir 'katkı bedeli önizlemesi'dir. "
            "TBK m.393-394 anlamında ifa edilen dijital hizmet karşılığıdır; "
            "kullanıcı burada pasif yatırımcı değildir."
        ),
        "safety_note": (
            "SPK açısından yatırım sözleşmesi unsurları yoktur çünkü: "
            "1) Kullanıcı sisteme sermaye koymaz, emek koyar. "
            "2) Getiri pasif değildir; CCS tamamen aktif katkıya bağlıdır. "
            "3) Havuz dağıtımı şirket kâr payı değildir, Fan Pool payıdır (~%40). "
        ),
        "regulatory_tags": {
            "SPK_risk": "düşük",
            "MASAK": "KYC + kayıtlı ödeme",
            "MiCA": "non-transferable utility credit",
        },
    }


if __name__ == "__main__":
    # Örnek bir senaryo
    # Diyelim ki sistemde 4 kullanıcı var:
    # - Kullanıcı0 = 120 CCS
    # - Kullanıcı1 = 80 CCS
    # - Kullanıcı2 = 50 CCS
    # - Kullanıcı3 = 10 CCS
    #
    # Fan Pool bu dönem için 10,000 USD değerinde hizmet bedeli ayırmış olsun.
    #
    # calculate_reward_preview(ccs_scores, 10_000, user_index=0)
    # bize Kullanıcı0 için önizlemeyi verecek.

    sample_scores = [120, 80, 50, 10]
    pool_value = 10_000  # USD cinsinden örnek Fan Pool büyüklüğü
    result_for_user0 = calculate_reward_preview(sample_scores, pool_value, user_index=0)

    import json
    print(json.dumps(result_for_user0, indent=4, ensure_ascii=False))
