
# FANX – Digital Service Economy
“Power to the Time, Value to the People.”  
Zaman senin sermayendir. Dikkatin değerindir.

---

## 1. Proje Özeti (Ne Bu Sistem?)

FANX; para yatıran yatırımcıyı değil, katkı sunan kullanıcıyı ödüllendiren kapalı devre (closed-loop) dijital hizmet ekonomisidir.

- Kullanıcı sisteme zaman / içerik / etkileşim verir → bu emek **XP (Experience Points)** olarak ölçülür.
- XP, belirli katsayılarla **FANX Credit**’e dönüşür.
- Fan, içerik satın aldığında / mesaj attığında / görev tamamladığında her işlemde küçük miktarda yakım (**burn**) olur.
- Yakım arzı azaltır → kalan Credit daha değerli hale gelir (**Value ↑**).
- Sistem içi gelir (sponsor görevleri, içerik lisansları, mesajlaşma vb.) minus giderler (sunucu, operasyon, cashout vb.) = **NEV (Net Ekosistem Değeri)**.
- NEV büyüdükçe, katkı yapan topluluk daha güçlü Reward alır.

Bu döngü tamamen platform içinde kalır. Dış borsa yoktur. Dışarı spekülasyon yoktur. Bu yüzden FANX:
- Menkul kıymet değildir.
- Kripto listing / pump-dump modeli değildir.
- Ponzi değildir (ödül dışarıdan gelen yeni para ile değil, içeride yaratılan değerle oluşur).

**Kısa formül:**  
> “Değer, yatırım parasıyla değil; insan emeğiyle üretilir.”


---

## 2. XP → Credit → Burn → Value → NEV Döngüsü

Aşağıdaki zincir FANX ekonomisinin motorudur:

`User → XP → Credit → Burn → Value↑ → NEV↑ → Reward↑ → User↑`

Adımlar:

1. **XP (Experience Point)**  
   - Kullanıcının yaptığı katkıların puanıdır.  
   - Görev tamamlama, içerik yükleme, izleme, etkileşim, topluluğu büyütme vb.
   - XP = fiilen ifa edilmiş dijital hizmettir (TBK m.393-394).

2. **Credit (FANX Credit)**  
   - XP belirli bir dönüşüm katsayısı ile FANX Credit’e çevrilir.  
   - Credit = platform içi dijital hizmet kredisi.  
   - Dışarı transfer edilemez, borsaya çıkamaz → MiCA / SPK açısından yatırım aracı değil.

3. **Burn (Yakım)**  
   - Her işlemde küçük bir miktar Credit yakılır.  
   - Böylece toplam arz (Supply) sürekli azalır → sistem deflasyonisttir.  
   - Formül:  
     `Supply_{t+1} = Supply_t − Burn_t + Buyback_t`

4. **Value (Birim Değer)**  
   - Değer, dış piyasa “fiyatı” ile belirlenmez.  
   - Değer = `NEV / Supply`  
   - NEV yükselirse veya Supply azalırsa Value yükselir.

5. **NEV (Net Ekosistem Değeri)**  
   - NEV = Ekosistemin toplam net üretim değeri.  
   - Formül:  
     `NEV = G_gross − C`  
     - G_gross = içerik lisans gelirleri + sponsor görevleri + mesajlaşma hacmi + premium servisler
     - C = operasyon / altyapı / ödül / cashout / buyback

6. **Reward (Katkı Payı)**  
   - NEV içindeki Fan Pool (%40 civarı) katkıya göre dağıtılır.  
   - Bu dağıtım “temettü” değildir çünkü:
     - pasif sermayeye ödeme yoktur,
     - yalnızca katkı (CCS skoru) varsa ödeme vardır.
   - Yani bu “çalıştın / katkı verdin / değer yarattın → karşılığını al” mekanizmasıdır.

Bu döngü kendi kendini fonlar.  
Yeni para girmese bile döner çünkü değer **etkileşimden** doğar.


---

## 3. Lokal Çalıştırma Rehberi / Streamlit Cloud Dağıtımı

Bu depo tipik olarak şu dosyalarla çalışır:
- `app/streamlit_app.py` → Arayüz
- `core/economics.py` → XP / Credit / Burn / NEV modelleri
- `core/compliance.py` → hukuki sınıflandırma ve risk bayrakları
- `core/dao.py` → DAO voting ve parametre kontrolü
- `data/demo_users.json` → örnek kullanıcı katkıları
- `requirements.txt` → bağımlılıklar

### A) Lokal Çalıştırma (bilgisayarında deneme)
1. Python 3.10+ kurulu olsun.
2. Proje klasörüne gir.
3. Gerekli paketleri kur:
   ```bash
   pip install -r requirements.txt
   ```
4. Uygulamayı başlat:
   ```bash
   streamlit run app/streamlit_app.py
   ```
5. Tarayıcıda otomatik açılır (genelde http://localhost:8501).

Bu arayüz sana şunları gösterir:
- Bir kullanıcının yaptığı görevlerden ne kadar XP ürettiği
- XP → Credit dönüşümü
- Burn sonrası arzın nasıl azaldığı
- NEV ve Value’nun nasıl değiştiği
- Reward’ın nasıl hesaplandığı

### B) Streamlit Cloud Dağıtımı (herkese açık web)
1. Github deposu herkese açık olmalı (Public).
2. https://share.streamlit.io adresine gir ve GitHub hesabınla bağlan.
3. Repo adı olarak: `kullanici_adi/FANX-DigitalServiceEconomy`
4. Branch: `main`
5. Main file path: `app/streamlit_app.py`
6. Deploy’e bas.

Streamlit kendi kendine:
- `requirements.txt` içindeki paketleri kurar,
- `streamlit_app.py` dosyasını çalıştırır,
- Sana public bir URL verir.

Artık yatırımcıya / regülatöre canlı simülasyon gösterebilirsin.  
(Sadece test verisi göster, gerçek kullanıcı verisi asla.)


---

## 4. Hukuki Çerçevenin Kısa Özeti

### 4.1 Bu sistem yatırım ürünü değil.
- FANX Credit dış borsada satılamaz, transfer edilemez.  
- Kullanıcının kazandığı şey “pasif getiri” değil, ifa ettiği dijital hizmetin karşılığıdır.  
- TBK m.393-394: Hizmet ifasında ücret doğar. Bu, temettü değildir.

### 4.2 Cashout = Hizmet Bedeli İadesi
- Kullanıcı zamanını/emek/katılımını verdi.  
- Sistem bu hizmeti geri alıyor ve bedelini ödüyor.  
- Bu, SPK anlamında “yatırım sözleşmesi” değil.  
- Bu, 6493 anlamında “elektronik para” da değil; çünkü platform dışına ödeme aracı olarak kullanılamaz.

### 4.3 Telif / FSEK
- Creator, içerik üzerindeki mali haklarını (FSEK m.21–25) korur.  
- Fan sadece “non-exclusive kullanım lisansı” alır (FSEK m.52).  
- Platform, aracı hizmet sağlayıcıdır (FSEK m.77/A).  
- Her satın alma aynı anda hem telif geliridir hem de arzı azaltan bir yakım olayıdır.

### 4.4 DAO ve Şeffaflık
- DAO; yakım oranı (αₜ), görev katsayıları (wⱼ), buyback oranı, havuz yüzdeleri gibi ekonomik parametreleri belirler.  
- Oy gücü formülü parasal ağırlığa değil katkı-itibar skoruna (CCS) dayanır.  
- Bu yüzden “balina gelip yönetimi ele geçirdi” argümanı engellenmiştir.

### 4.5 Regülasyon uyumu – özet
- **Türkiye (SPK / 6493):** Kapalı devre dijital hizmet kredisi → yatırım ürünü değil → lisans zorunluluğu yoktur.  
- **AB (MiCA / PSD2):** Non-transferable utility credit → kripto varlık lisans tanımının dışında.  
- **Dubai (VARA):** Dış borsaya çıkmayan, transfer edilemeyen kredi → “Virtual Asset Service Provider” kapsamına girmez.  
- **MASAK / FATF:** KYC + kapalı devre nakit dönüş → AML uyumlu.

**Savunma cümlesi (slide altına koymalık):**  
> “FANX, yatırım ürünü sunmaz; kullanıcı emeğini ölçer, bu emeğin dijital hizmet karşılığını hesaplar ve kapalı devre içinde iade eder. Tüm değer üretimi içeride gerçekleşir; dış spekülasyon yoktur.”


---

## 5. Bu Depo Ne İçin Var?

- Topluluğa / yatırımcıya / regülatöre aynı anda tek dilden anlatılabilir bir referans sağlamak.
- Ekonomi matematiğini (XP → Credit → Burn → Value → NEV) şeffaflaştırmak.
- Hukuki konumlandırmayı (SPK / MiCA / VARA / MASAK / FSEK) tek yerde netleştirmek.
- Streamlit arayüzüyle:  
  “Bak, bu kişi şu kadar görev yaptı → şu kadar XP üretti → sistem bu kadar yaktı → arz şu kadar düştü → NEV şu kadar büyüdü” demeyi görsel hale getirmek.

---

## 6. Tek Cümlelik Özet

**FANX, dışarıdan para pompalayan bir yatırım ürünü değil; zamanını veren herkesin emeğini ölçüp, arzı yakarak kıtlık yaratan, telif ve hizmet sözleşmesi hukukuna tam oturan kapalı devre dijital ekonomi modelidir.**
