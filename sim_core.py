import numpy as np
import pandas as pd

class FanxEconomy:
    def __init__(self, supply_t=10_000_000, nev_t=1_000_000, alpha=0.025, buyback_ratio=0.02, fanpool_ratio=0.4):
        self.supply_t = supply_t
        self.nev_t = nev_t
        self.alpha = alpha
        self.buyback_ratio = buyback_ratio
        self.fanpool_ratio = fanpool_ratio

    def xp_to_credit(self, xp, r_conv=0.2):
        return xp * r_conv

    def burn(self, credit):
        return credit * self.alpha

    def buyback(self):
        return self.supply_t * self.buyback_ratio

    def update_supply(self, burn_t, buyback_t):
        return self.supply_t - burn_t - buyback_t

    def value(self, supply_t1):
        return self.nev_t / supply_t1

    def reward(self, credit, value_t1):
        return credit * value_t1 * self.fanpool_ratio

    def simulate(self, xp, r_conv=0.2):
        credit = self.xp_to_credit(xp, r_conv)
        burn_t = self.burn(credit)
        buyback_t = self.buyback()
        supply_t1 = self.update_supply(burn_t, buyback_t)
        value_t1 = self.value(supply_t1)
        reward = self.reward(credit, value_t1)

        return {
            "XP": xp,
            "Credit": credit,
            "Burn": burn_t,
            "Buyback": buyback_t,
            "Supply_t+1": supply_t1,
            "Value_t+1": value_t1,
            "Reward": reward
        }

# Example batch simulation
if __name__ == "__main__":
    engine = FanxEconomy()
    xp_values = np.arange(100, 1001, 100)
    results = [engine.simulate(xp) for xp in xp_values]
    df = pd.DataFrame(results)
    print(df)
