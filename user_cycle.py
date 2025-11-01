import math
from typing import Dict

# Görev katsayıları (w_j), Bölüm 3.2 tablosundan
TASK_WEIGHTS = {
    "WATCH": 1.0,      # Video / içerik izleme (min. 20 sn)
    "SHARE": 2.0,      # İçerik paylaşımı / repost
    "MESSAGE": 1.2,    # Mesaj / etkileşim
    "UPLOAD": 3.0,     # Kendi içeriğini yükleme
    "CREATE": 5.0,     # Orijinal eser / NFT üretimi
    "SPONSOR": 3.5,    # Sponsor görevine katılım
    "PLAY": 2.5,       # Mini-game / quiz / etkinlik
    "INVITE": 2.0,     # Yeni kullanıcı daveti
    "LIVE": 4.0,       # Canlı yayına katılım / etkinlik
}


def simulate_user_cycle(
    watch_count: int,
    share_count: int,
    message_count: int,
    upload_count: int,
    create_count: int,
    sponsor_count: int,
    play_count: int,
    invite_count: int,
    live_count: int,
    ai_quality_score: float,
    bot_risk_score: float,
    xp_cap_daily: int = 10_000,
) -> Dict[str, float]:
    """
    FANX Kullanıcı Döngüsü Simülasyonu
    ---------------------------------
    Amaç:
        Tek bir kullanıcının bir gün içindeki faaliyetlerinden ne kadar XP ürettiğini
        ve bu XP'nin "gerçek XP"ye (XP_real) nasıl dönüştüğünü hesaplamak.
        Bu değer daha sonra Credit'e dönüşür (XP → Credit → Burn → Value → Reward).

    Girdi Parametreleri:
        watch_count      : Kullanıcının o gün izlediği içerik sayısı (WATCH)
        share_count      : Paylaşım / repost sayısı (SHARE)
        message_count    : Mesaj sayısı (MESSAGE)
        upload_count     : Yüklenen içerik (UPLOAD)
        create_count     : Orijinal eser / NFT üretimi (CREATE)
        sponsor_count    : Sponsor görevi tamamlama sayısı (SPONSOR)
        play_count       : Mini-game / quiz / görev sayısı (PLAY)
        invite_count     : Davet edilen yeni kullanıcı sayısı (INVITE)
        live_count       : Canlı yayın / etkinlik katılımı sayısı (LIVE)

        ai_quality_score : 0.0 – 1.0 arası kalite faktörü
                           - İçerik özgünlüğü
                           - Topluluk etkileşiminin organikliği
                           - Şikâyet / spam oranı
                           Yüksekse: gerçek insan ve kaliteli katkı.
                           Düşükse: spam / bot davranışı şüphesi.

        bot_risk_score   : 0.0 – 1.0 arası risk faktörü
                           0.0 = kesin insan
                           1.0 = kesin bot
                           Bu skor arttıkça sistem seni otomatik düşürür.

        xp_cap_daily     : Günlük XP tavanı (anti-farm politikası)

    Çıktı:
        {
            "XP_raw": ...,
            "XP_capped": ...,
            "XP_real": ...,
            "AI_effective_multiplier": ...,
            "Breakdown": {...},
            "Notes": {...}
        }

    Hukuki Not:
        XP ücretin ölçüsüdür; yatırım getirisi değildir (TBK m.393).
        Bu hesaplama, kullanıcının ifa ettiği dijital hizmetin nicel/nitel karşılığıdır.
    """

    # 1) Her görev için XP hesapla (nicelik × katsayı)
    xp_watch   = watch_count   * TASK_WEIGHTS["WATCH"]
    xp_share   = share_count   * TASK_WEIGHTS["SHARE"]
    xp_msg     = message_count * TASK_WEIGHTS["MESSAGE"]
    xp_upload  = upload_count  * TASK_WEIGHTS["UPLOAD"]
    xp_create  = create_count  * TASK_WEIGHTS["CREATE"]
    xp_sponsor = sponsor_count * TASK_WEIGHTS["SPONSOR"]
    xp_play    = play_count    * TASK_WEIGHTS["PLAY"]
    xp_invite  = invite_count  * TASK_WEIGHTS["INVITE"]
    xp_live    = live_count    * TASK_WEIGHTS["LIVE"]

    xp_raw = (
        xp_watch   +
        xp_share   +
        xp_msg     +
        xp_upload  +
        xp_create  +
        xp_sponsor +
        xp_play    +
        xp_invite  +
        xp_live
    )

    # 2) Günlük XP tavanını uygula (anti-farm koruması)
    xp_capped = min(xp_raw, xp_cap_daily)

    # 3) Yapay zekâ kalite filtresi uygula
    #    - ai_quality_score: 0.0 → 1.0
    #    - bot_risk_score : 0.0 → 1.0
    #    multiplier = ai_quality_score * (1 - bot_risk_score)
    ai_effective_multiplier = max(0.0, ai_quality_score * (1.0 - bot_risk_score))

    xp_real = xp_capped * ai_effective_multiplier

    # 4) Dönüş sözlüğü
    return {
        "XP_raw": xp_raw,
        "XP_capped": xp_capped,
        "AI_effective_multiplier": ai_effective_multiplier,
        "XP_real": xp_real,
        "Breakdown": {
            "WATCH": xp_watch,
            "SHARE": xp_share,
            "MESSAGE": xp_msg,
            "UPLOAD": xp_upload,
            "CREATE": xp_create,
            "SPONSOR": xp_sponsor,
            "PLAY": xp_play,
            "INVITE": xp_invite,
            "LIVE": xp_live,
        },
        "Notes": {
            "XP_cap_daily": xp_cap_daily,
            "Legal": (
                "XP yatırım geliri değildir; TBK m.393 uyarınca ifa edilen dijital hizmet "
                "karşılığıdır. Kullanıcı burada pasif yatırımcı değil, dijital hizmet sağlayıcıdır."
            ),
            "RiskControls": (
                "ai_quality_score düşük veya bot_risk_score yüksek ise XP_real kesilir; "
                "bu, bot / farm / spam kazancını engeller."
            ),
        },
    }


if __name__ == '__main__':
    # Küçük bir örnek: normal, organik bir kullanıcı
    example = simulate_user_cycle(
        watch_count=5,
        share_count=2,
        message_count=10,
        upload_count=1,
        create_count=1,
        sponsor_count=1,
        play_count=3,
        invite_count=0,
        live_count=1,
        ai_quality_score=0.9,
        bot_risk_score=0.05,
    )

    import json
    print(json.dumps(example, indent=4, ensure_ascii=False))
