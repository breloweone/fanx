"""
nev_engine.py
-----------------
NEV (Net Ecosystem Value) = G_gross - C_total

- G_gross: XP görev hacmi, içerik lisansı, sponsor görevleri,
  premium servisler, mesajlaşma ekonomisi.
- C_total: Sunucu gideri, DAO operasyonu, reward dağıtımı,
  cashout (TBK 393 ifa bedeli iadesi), buyback.

NEV ekosistemin içsel GSYH'sidir.
Dışarıdan spekülatif sermaye girişi varsaymaz.
"""

from dataclasses import dataclass

@dataclass
class RevenueComponents:
    G_XP: float         # görev / XP tabanlı işlem hacmi
    G_Content: float    # içerik lisans satışları
    G_Sponsor: float    # sponsor görevleri
    G_Premium: float    # premium abonelikler
    G_Message: float    # mesajlaşma mikro-ödemeleri

@dataclass
class CostComponents:
    C_server: float     # altyapı + AI
    C_ops: float        # DAO / operasyon
    C_reward: float     # dağıtılan ödüller
    C_cashout: float    # hizmet bedeli iadesi
    C_buyback: float    # arz geri alımı / dengeleme

def compute_nev(rev: RevenueComponents, cost: CostComponents) -> float:
    G_gross = (
        rev.G_XP
        + rev.G_Content
        + rev.G_Sponsor
        + rev.G_Premium
        + rev.G_Message
    )
    C_total = (
        cost.C_server
        + cost.C_ops
        + cost.C_reward
        + cost.C_cashout
        + cost.C_buyback
    )
    return G_gross - C_total

def compute_value_per_credit(nev_t: float, supply_t_plus_1: float) -> float:
    """Value_{t+1} = NEV_t / Supply_{t+1}
    Bu "fiyat" değildir.
    Bu, 1 kredi biriminin ekosistem içi hizmet değeridir.
    """
    if supply_t_plus_1 <= 0:
        return 0.0
    return nev_t / supply_t_plus_1
