"""
reward_engine.py
-----------------
FanPool dağıtımı (temettü değildir!).

Reward_i = FanPool * (CCS_i / ΣCCS)

- FanPool tipik olarak toplam havuzun %40'ıdır.
- CCS_i, kullanıcının Composite Contribution Score değeridir.
  (Aktiflik, kalite, ağ etkisi).
- Bu ödeme pasif yatırım getirisi değildir;
  ifa edilmiş dijital hizmet bedelinin paylaştırılmasıdır (TBK m.393).
"""

def compute_reward(user_ccs: float, all_ccs_sum: float, fan_pool_amount: float) -> float:
    if all_ccs_sum <= 0:
        return 0.0
    return fan_pool_amount * (user_ccs / all_ccs_sum)
