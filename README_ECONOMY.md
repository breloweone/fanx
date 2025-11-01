# FANX Economy Core Module
(Generated 2025-11-01T00:56:00.836954Z)

Bu paket, FANX Dijital Hizmet Ekonomisi'nin çekirdek ekonomik / matematiksel / hukuki modelini içerir.
Bu klasörü doğrudan GitHub reposuna (`/core`, `/data`, `/legal`) atabilirsiniz.

## İçerik

### 1. XP -> Credit -> Burn -> Value -> NEV Döngüsü
- Kullanıcı eylemi (watch/share/message/content)
- XP hesaplama (`xp_engine.py`)
- XP -> Credit dönüşümü (`R_conv`)
- Burn / Buyback ile arz azaltımı (`deflation.py`)
- NEV hesaplama (`nev_engine.py`)
- Value_t+1 = NEV / Supply formülü
- FanPool dağıtımı ve Reward (`reward_engine.py`)

### 2. Hukuki Çerçeve (legal/audit_log.json)
- TBK m.393-394: Hizmet ifası karşılığı bedel
- SPK kapsamına girmeyen model (yatırım sözleşmesi yok)
- MiCA / VARA uyumu (non-transferable utility credit)
- MASAK uyumu (kapalı devre, KYC zorunlu)

### 3. DAO Parametreleri
- Yakım oranı (alpha_t)
- Buyback oranı (rho_t)
- R_conv (XP -> Credit katsayısı)
- w_j görev katsayıları
- FanPool %40, CreatorPool %30, DAO %20, Platform %10

### 4. JSON State Log (data/state_log.json)
Streamlit / simülatör bu dosyaya özet yazar:
```json
{
    "XP": 153.5,
    "Credit": 15.35,
    "NEV": 281250,
    "Supply": 830584000,
    "Value_t_plus_1": 0.000339,
    "Reward_preview_USD": 0.62,
    "legal_tags": ["@TBK_393","@SPK_Exempt","@MASAK_Compliant","@MiCA_Utility","@VARA_OffChain"]
}
```

## Önemli Hukuki Not
- Bu ekonomi modeli yatırım tavsiyesi, kâr garantisi, temettü taahhüdü değildir.
- Cashout bir "ifa edilmiş dijital hizmet bedeli iadesi"dir.
- Reward pasif gelir değildir; katkı karşılığı hizmet bedelidir.

## Dosya Haritası
- core/models/xp_engine.py
- core/models/nev_engine.py
- core/reward_engine.py
- core/economy/deflation.py
- legal/audit_log.json
- data/state_log.json
