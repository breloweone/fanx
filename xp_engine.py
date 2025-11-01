"""
xp_engine.py
-----------------
Kullanıcı eylemlerinden XP üretir ve XP'den Credit hesaplar.

Hukuki sınıf: TBK m.393 kapsamındaki dijital hizmet ifasıdır.
Bu bir yatırım getirisi DEĞİLDİR.
"""

from dataclasses import dataclass

@dataclass
class UserActivity:
    watch_minutes: float      # izleme süresi
    share_count: float        # paylaşım adedi
    message_count: float      # mesaj adedi
    content_created: float    # üretilen içerik sayısı
    ai_quality_score: float   # 0-1 arası kalite puanı (AI_score)

# Görev katsayıları (DAO tarafından belirlenir ve şeffaf ilan edilir)
WEIGHTS = {
    "WATCH": 1.0,      # G2
    "SHARE": 2.0,      # G1
    "MESSAGE": 1.2,    # G6
    "CONTENT": 5.0     # G5 (orijinal eser üretimi)
}

def compute_xp_raw(activity: UserActivity) -> float:
    """Ham XP (AI kalite öncesi)."""
    xp_watch   = activity.watch_minutes  * WEIGHTS["WATCH"]
    xp_share   = activity.share_count    * WEIGHTS["SHARE"]
    xp_message = activity.message_count  * WEIGHTS["MESSAGE"]
    xp_content = activity.content_created* WEIGHTS["CONTENT"]

    xp_total = xp_watch + xp_share + xp_message + xp_content
    return xp_total

def apply_ai_quality(xp_raw: float, ai_quality_score: float) -> float:
    """AI kalite katsayısı uygular.
    Kalite puanı (0-1). Spam/bot tespitinde kalite 0'a iner.
    """
    return xp_raw * ai_quality_score

def xp_to_credit(xp_real: float, R_conv: float) -> float:
    """XP -> Credit dönüşümü.
    R_conv DAO tarafından belirlenir. Ekonomik teşvik / enflasyon dengesi aracıdır.
    """
    return xp_real * R_conv
