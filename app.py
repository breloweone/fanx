import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(page_title="FANX Digital Service Economy", layout="wide")
st.title("💠 FANX Closed-Loop Economy Simulator")
st.markdown("### XP → Credit → Burn → Value → NEV Döngüsü")

# Initialize state
if "xp" not in st.session_state:
    st.session_state.xp = 0
if "credit" not in st.session_state:
    st.session_state.credit = 0
if "supply" not in st.session_state:
    st.session_state.supply = 1_000_000_000
if "nev" not in st.session_state:
    st.session_state.nev = 100_000

# Section 1: Kullanıcı Etkileşimi
st.header("1️⃣ Kullanıcı Etkileşimi ve XP Üretimi")
col1, col2, col3, col4 = st.columns(4)

watch = col1.number_input("🎥 İzleme (dakika)", min_value=0, max_value=600, value=0)
share = col2.number_input("🔗 Paylaşım (adet)", min_value=0, max_value=100, value=0)
message = col3.number_input("💬 Mesajlaşma (adet)", min_value=0, max_value=200, value=0)
create = col4.number_input("🧠 İçerik Üretimi (adet)", min_value=0, max_value=50, value=0)

# XP hesaplama
xp_new = watch * 0.5 + share * 2 + message * 0.2 + create * 10
st.metric("Yeni XP", round(xp_new, 2))

# XP'den Credit dönüşümü (örnek katsayı: 0.1)
r_conv = 0.1
credit_new = xp_new * r_conv
st.metric("Kazanılan Credit (₣)", round(credit_new, 2))

# Fan Pool Preview
st.header("2️⃣ Fan Pool - Reward Önizleme")
fan_pool_ratio = 0.40
reward_preview = (st.session_state.nev * fan_pool_ratio) / 100_000  # Basit ölçekli gösterim
st.metric("Tahmini Fan Pool Dağıtımı ($)", f"{reward_preview:.2f}")
st.caption("Bu **temettü değil**, hizmet karşılığı bedeldir (TBK m.393).")

# Supply Dynamics
st.header("3️⃣ Burn + Buyback Sonrası Arz Daralması")
burn_rate = st.slider("Yakım Oranı (αₜ)", 0.0, 0.05, 0.025, step=0.005)
buyback_rate = st.slider("Buyback Oranı (ρₜ)", 0.0, 0.10, 0.03, step=0.01)

burn_amount = st.session_state.supply * burn_rate
buyback_amount = st.session_state.supply * buyback_rate
supply_new = st.session_state.supply - burn_amount - buyback_amount
st.metric("Yeni Supply", f"{supply_new:,.0f} ₣")

# NEV ve Değer Hesaplaması
st.header("4️⃣ NEV / Supply Oranından Valueₜ₊₁ Hesaplaması")
nev_growth = st.slider("NEV Büyüme Oranı (%)", 0, 200, 25, step=5)
nev_new = st.session_state.nev * (1 + nev_growth / 100)
value_t1 = nev_new / supply_new
st.metric("Yeni Valueₜ₊₁ (₣ başına değer)", f"${value_t1:.6f}")

# Güncelleme butonu
if st.button("💾 Simülasyonu Güncelle"):
    st.session_state.xp += xp_new
    st.session_state.credit += credit_new
    st.session_state.supply = supply_new
    st.session_state.nev = nev_new
    st.success("Sistem değerleri güncellendi.")

# Son durum özeti
st.header("📊 Ekonomik Özet")
summary = {
    "Toplam XP": st.session_state.xp,
    "Toplam Credit": st.session_state.credit,
    "Mevcut Supply": st.session_state.supply,
    "Güncel NEV": st.session_state.nev,
    "Credit Başına Değer": value_t1,
}
st.json(summary)

st.markdown("---")
st.caption("© 2025 FANX • Dijital Hizmet Ekonomisi • Bu simülasyon yatırım tavsiyesi değildir.")
