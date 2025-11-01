# DAO_GOVERNANCE.md

## 💠 DAO Yönetim Modeli – FANX Ekosistemi

### “Kimse tek başına sistemi yönetmez. Değer, katılımın ortak kararıyla yönetilir.”

DAO (Decentralized Autonomous Organization), FANX ekonomisinin **yönetişim merkezi**dir.  
Bu yapı bir **patron** değil, bir **topluluk denetim organı**dır.

---

## 🔹 1. DAO’nun Rolü

DAO; arz, görev katsayıları, havuz oranları ve dönüşüm katsayılarını belirleyen şeffaf bir kuruldur.  
Fakat bu kurul yatırımcılara “getiri dağıtmaz”, yalnızca sistem parametrelerini yönetir.

**DAO’nun ana görevleri:**
- αₜ : Yakım oranlarını belirler (burn ratio)
- ρₜ : DAO buyback oranını belirler (rezerv geri alım oranı)
- wⱼ : Görev katsayılarını belirler (hangi görev ne kadar XP kazandırır)
- R_conv : XP → Credit dönüşüm katsayısını tanımlar
- Havuz oranları : Fan Pool / Creator Pool / DAO Pool / Platform Pool yüzdeleri

Her yeni dönem bu parametreler **DAO panelinde şeffaf biçimde yayınlanır.**
Bu şeffaflık, regülatör açısından “kapalı karar alma” riskini ortadan kaldırır.

---

## 🔹 2. VotePower Formülü

Her kullanıcının DAO oylamalarında sahip olduğu etki gücü şu şekilde hesaplanır:

\`\`\`text
VotePowerᵢ = FTXᵢ + (RSᵢ × Weight)
\`\`\`

| Sembol | Tanım | Açıklama |
|:--|:--|:--|
| **FTXᵢ** | Governance puanı | Kullanıcının uzun dönemli katkısı (devredilemez, satılamaz) |
| **RSᵢ** | Reputation Score | Katkı kalitesi + topluluk etkisi |
| **Weight** | Denge katsayısı | Balina etkisini sınırlayan DAO parametresi |

**Amaç:**  
- Parası çok olanın değil, katkısı çok olanın gücü artsın.  
- “Balina kilidi” (Weight) ile büyük hesapların tek başına sistemi kontrol etmesi engellensin.  

**Hukuki dayanak:**  
FTXᵢ satılamadığı için bir “yatırım aracı” değildir.  
Oy hakkı bir “mülkiyet” değil, bir “katılım yetkisidir.”  
Bu yüzden DAO oylaması SPK anlamında “menkul kıymet oylaması” sayılmaz.

---

## 🔹 3. CCS (Composite Contribution Score)

DAO, kullanıcı itibarını ve katkı kalitesini ölçmek için **CCS_i** sistemini kullanır.

\`\`\`text
CCSᵢ = (Aktiflikᵢ × α) + (Kaliteᵢ × β) + (AğEtkisiᵢ × γ)
\`\`\`

| Bileşen | Tanım | Etkisi |
|:--|:--|:--|
| Aktiflikᵢ | Kullanıcının görev, mesaj, içerik üretim sıklığı | +XP puanı üretir |
| Kaliteᵢ | İçeriğin izlenme oranı, şikâyet puanı, AI kalite skoru | Kalite + güven puanı |
| AğEtkisiᵢ | Yeni kullanıcı daveti, paylaşım zinciri etkisi | Topluluk büyümesi katkısı |

**Katsayılar:** α / β / γ  
→ DAO tarafından belirlenir ve panelde açıklanır.

**RSᵢ = normalize(CCSᵢ)**  
Yani RSᵢ, sadece “çok içerik atmak” değil, “değerli içerik üretmek” ile artar.

---

## 🔹 4. Weight – Balina Kilidi

Bazı kullanıcılar (örneğin ünlü Creator veya büyük topluluk sahibi) yüksek RSᵢ puanına ulaşabilir.  
Bu durumda Weight çarpanı devreye girer:

\`\`\`text
VotePowerᵢ = FTXᵢ + (RSᵢ × Weight)
\`\`\`

**Weight < 1** ise, bu hesapların etki gücü sınırlanır.  
Amaç: “demokratik denge”.

**Hukuki ve regülasyon avantajı:**
- DAO tek kişiye bağlı hale gelmez.
- Piyasa manipülasyonu / kartel riski ortadan kalkar.
- Regülatör için bu yapı “topluluk koruma mekanizması” olarak görülür.

---

## 🔹 5. DAO’nun Yayınladığı Parametreler

DAO şeffaflık panelinde aşağıdaki değerler düzenli olarak yayımlanır:

| Parametre | Tanım | Periyot | Hukuki Önemi |
|:--|:--|:--|:--|
| **αₜ** | Yakım oranı | Dönemsel | Deflasyon dengesinin yasal temeli |
| **ρₜ** | Buyback oranı | Dönemsel | Arz daraltma politikasının şeffaf ilanı |
| **wⱼ** | Görev katsayıları | Günlük/Haftalık | Katılım ödül katsayısı, iç dengeyi korur |
| **R_conv** | XP → Credit dönüşüm oranı | Dönemsel | Emek-karşılık oranı; ücret değil yatırım |
| **Havuz oranları** | Fan/Creator/DAO/Platform payları | Dönemsel | Adil paylaşımın kanıtı |

Tüm bu değerler **off-chain ledger üzerinde hash’lenmiş kayıtlarla** arşivlenir.  
Bu sayede “DAO manipülasyon yaptı mı?” sorusu gerektiğinde matematiksel olarak ispatlanabilir.

---

## 🔹 6. Hukuki Çerçeve

| Kriter | DAO Statüsü | Açıklama |
|:--|:--|:--|
| SPK | Yatırım sözleşmesi değil | Oy hakkı devredilemez, gelir payı yok |
| MASAK | Uyumlu | DAO işlemleri KYC + kayıtlı ledger ile izlenir |
| MiCA / VARA | Uyumlu | Transferable token yok; DAO dış borsada işlem yapmaz |
| TBK m.393 | Hizmet sözleşmesi | Katkı, hizmetin ifasıdır, getiri beklentisi değildir |

**Sonuç:**  
DAO bir “patron” değildir.  
DAO, “topluluk içinde ekonomik adaleti ve regülasyon uyumunu denetleyen mekanizmadır.”

---

## 🔹 7. Tek Cümlelik Özet

> **“FANX DAO, yatırımcıya getiri dağıtan bir yapı değil; topluluk emeğini dengeleyen, uyum ve şeffaflığı garanti altına alan otonom bir denetim sistemidir.”**
