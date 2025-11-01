"""
deflation.py
-----------------
Arz dinamiği (deflasyonist model):
    Supply_{t+1} = Supply_t - Burn_t + Buyback_t

Burn_t = alpha_t * Volume_t
Buyback_t = DAO_reserve_(t-1) * rho_t

Not:
- alpha_t (yakım oranı) DAO tarafından belirlenir.
- rho_t (buyback oranı) DAO tarafından belirlenir.
- Buyback, dış borsada fiyat manipülasyonu değildir çünkü dış piyasa yoktur;
  kapalı devre arz dengelemesidir.
"""

from dataclasses import dataclass

@dataclass
class DeflationInputs:
    supply_t: float        # mevcut arz
    volume_t: float        # dönemsel işlem hacmi (toplam FANX hareketi)
    alpha_t: float         # yakım oranı (0.0 - 0.05 tipik)
    dao_reserve_prev: float# DAO rezervi (t-1)
    rho_t: float           # buyback oranı (0.0 - 0.10 tipik)

def compute_burn(volume_t: float, alpha_t: float) -> float:
    return volume_t * alpha_t

def compute_buyback(dao_reserve_prev: float, rho_t: float) -> float:
    return dao_reserve_prev * rho_t

def next_supply(params: DeflationInputs) -> float:
    burn_t = compute_burn(params.volume_t, params.alpha_t)
    buyback_t = compute_buyback(params.dao_reserve_prev, params.rho_t)
    return params.supply_t - burn_t + buyback_t
