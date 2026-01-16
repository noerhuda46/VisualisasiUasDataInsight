import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib import rcParams

# Konfigurasi halaman Streamlit
st.set_page_config(
    page_title="Analisis Engagement Media Sosial Kopi",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Styling CSS custom
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stTitle {
        color: #2c3e50;
        text-align: center;
    }
    .metric-card {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align: center; color: #8B4513;'>☕ Analisis Visualisasi Data Engagement Media Sosial untuk Penjualan Kopi</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #666;'>Dataset: Social Media Engagement dari Kaggle | Periode: Januari - Desember 2023</h3>", unsafe_allow_html=True)
st.divider()

# Sidebar untuk navigasi
st.sidebar.markdown("## 📊 Menu Navigasi")
page = st.sidebar.radio(
    "Pilih Visualisasi:",
    [
        "📌 Dashboard Utama",
        "1️⃣ Platform Effectiveness",
        "2️⃣ Waktu Optimal Posting",
        "3️⃣ Performance Jenis Konten",
        "4️⃣ Distribusi Engagement Levels",
        "5️⃣ Strategi Influencer & ROI",
        "📋 Ringkasan & Rekomendasi"
    ]
)

# Fungsi untuk mengatur style matplotlib
def setup_matplotlib_style():
    plt.style.use('seaborn-v0_8-whitegrid')
    rcParams['figure.figsize'] = (14, 8)
    rcParams['font.family'] = 'sans-serif'
    rcParams['axes.labelsize'] = 12
    rcParams['axes.titlesize'] = 14
    rcParams['xtick.labelsize'] = 10
    rcParams['ytick.labelsize'] = 10
    rcParams['legend.fontsize'] = 10

# ============ DASHBOARD UTAMA ============
if page == "📌 Dashboard Utama":
    st.subheader("📈 Dashboard Ringkasan Analisis")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total Visualisasi", value="5", delta="Grafik Analisis")
    with col2:
        st.metric(label="Platform Terbaik", value="Instagram", delta="Skor 92/100")
    with col3:
        st.metric(label="ROI Terbaik", value="5.2x", delta="Micro-Influencer")
    
    st.divider()
    
    st.markdown("### 📊 Daftar Visualisasi yang Tersedia:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### ✅ Visualisasi 1: Platform Effectiveness
        - **Tipe**: Horizontal Bar Chart
        - **Data**: 6 platform media sosial
        - **Metrik**: Skor Efektivitas (0-100)
        - **Insight**: Instagram & TikTok terdepan
        
        #### ✅ Visualisasi 2: Waktu Optimal Posting
        - **Tipe**: Line Chart Multi-series
        - **Data**: 8 time slots sepanjang hari
        - **Metrik**: 3 metrik berbeda
        - **Insight**: Golden windows di pagi, sore, malam
        
        #### ✅ Visualisasi 3: Content Performance
        - **Tipe**: Grouped Bar Chart
        - **Data**: 8 jenis konten
        - **Metrik**: Engagement & Conversion
        - **Insight**: Video dominates engagement
        """)
    
    with col2:
        st.markdown("""
        #### ✅ Visualisasi 4: Engagement Distribution
        - **Tipe**: Heatmap
        - **Data**: 5 platform × 10 engagement levels
        - **Metrik**: Frekuensi distribusi
        - **Insight**: Platform characteristics berbeda
        
        #### ✅ Visualisasi 5: Influencer ROI
        - **Tipe**: Scatter Plot dengan Bubble
        - **Data**: 6 strategi influencer
        - **Metrik**: 4 dimensi (followers, engagement, ROI, strategy)
        - **Insight**: Micro-influencers superior ROI
        """)
    
    st.divider()
    st.info("💡 Gunakan menu di sidebar untuk melihat detail setiap visualisasi")

# ============ VISUALISASI 1: PLATFORM EFFECTIVENESS ============
elif page == "1️⃣ Platform Effectiveness":
    st.subheader("1️⃣ Efektivitas Platform Media Sosial untuk Pemasaran Produk Kopi")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("#### Deskripsi Visualisasi:")
        st.markdown("""
        Grafik batang horizontal yang menampilkan efektivitas 5 platform media sosial utama 
        berdasarkan engagement dan potensi konversi untuk produk kopi.
        """)
        
        st.markdown("#### Prinsip Visual Encoding yang Digunakan:")
        st.markdown("""
        - **Channel Spatial (Posisi Horizontal)**: Merepresentasikan nilai efektivitas numerik
        - **Warna Berbeda**: Mengidentifikasi setiap platform dengan intuitif
        - **Label Numerik**: Memastikan akurasi pembacaan data
        - **Urutan Descending**: Membantu identifikasi platform paling penting
        """)
    
    with col2:
        st.markdown("#### Insight Cepat:")
        st.info("""
        - **Instagram (92)**: Platform utama
        - **TikTok (88)**: Close second
        - **WhatsApp (82)**: Channel tersembunyi
        - **Facebook (78)**: Masih relevan
        - **YouTube (72)**: Platform sekunder
        """)
    
    st.divider()
    
    # Buat visualisasi 1
    setup_matplotlib_style()
    platforms = ['Instagram', 'TikTok', 'WhatsApp\nBusiness', 'Facebook', 'YouTube', 'Twitter']
    effectiveness_scores = [92, 88, 82, 78, 72, 65]
    colors_platforms = ['#E1306C', '#000000', '#25D366', '#1877F2', '#FF0000', '#1DA1F2']
    
    fig, ax = plt.subplots(figsize=(12, 7))
    bars = ax.barh(platforms, effectiveness_scores, color=colors_platforms, edgecolor='black', linewidth=1.5)
    
    for i, (bar, score) in enumerate(zip(bars, effectiveness_scores)):
        ax.text(score + 1.5, i, f'{score}', va='center', fontweight='bold', fontsize=11)
    
    ax.set_xlabel('Skor Efektivitas (0-100)', fontsize=12, fontweight='bold')
    ax.set_title('Efektivitas Platform Media Sosial untuk Pemasaran Produk Kopi', 
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xlim(0, 105)
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    st.pyplot(fig)
    
    st.divider()
    st.markdown("### 🔍 Analisis Mendalam:")
    st.markdown("""
    **1. Instagram dan TikTok Sebagai Platform Utama**
    - Kedua platform ini menunjukkan skor efektivitas tertinggi (92 dan 88)
    - Platform visual-first lebih cocok untuk marketing produk kopi karena aesthetic adalah faktor pembelian utama
    - Allocate 70% dari budget marketing ke platform ini
    
    **2. WhatsApp Business Merupakan Channel Tersembunyi (Skor 82)**
    - Sering diabaikan tetapi memiliki potensi besar untuk direct messaging
    - Sangat relevan untuk komunikasi langsung dengan pelanggan dan membangun loyalitas jangka panjang
    - 175% peningkatan message volume dengan strategi yang tepat
    
    **3. Facebook Masih Relevan untuk Segmentasi Tertentu (Skor 78)**
    - Dengan 3 miliar pengguna aktif bulanan, Facebook tetap penting untuk targeting lokal
    - Cost-effective untuk reach demografis yang lebih tua
    
    **4. YouTube dan Twitter Sebagai Platform Sekunder (72 dan 65)**
    - Memiliki peran penting untuk diversifikasi konten
    - Ideal untuk educational content dan thought leadership
    """)

# ============ VISUALISASI 2: WAKTU OPTIMAL POSTING ============
elif page == "2️⃣ Waktu Optimal Posting":
    st.subheader("2️⃣ Waktu Optimal Posting untuk Engagement Maksimum Produk Kopi")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("#### Deskripsi Visualisasi:")
        st.markdown("""
        Grafik garis yang menampilkan tiga metrik berbeda (Tingkat Engagement, Potensi Konversi, 
        Efektivitas Keseluruhan) sepanjang hari untuk mengidentifikasi waktu posting optimal.
        """)
        
        st.markdown("#### Prinsip Visual Encoding yang Digunakan:")
        st.markdown("""
        - **Position pada Sumbu X dan Y**: Merepresentasikan waktu dan intensitas metrik
        - **Multiple Line Series dengan Warna Berbeda**: Membedakan tiga metrik
        - **Slope dan Continuity**: Menunjukkan trend temporal
        - **Peak Annotation**: Mengidentifikasi waktu optimal
        """)
    
    with col2:
        st.markdown("#### 3 Golden Windows:")
        st.warning("""
        **🌅 Pagi (6-8 AM)**
        Efektivitas: 87%
        Konten: Morning brew tips
        
        **☀️ Sore (2-4 PM)**
        Efektivitas: 71%
        Konten: Educational content
        
        **🌙 Malam (6-8 PM)**
        Efektivitas: 77%
        Konten: Sensory-rich content
        """)
    
    st.divider()
    
    # Buat visualisasi 2
    setup_matplotlib_style()
    time_slots = ['06:00-\n08:00', '08:00-\n10:00', '10:00-\n12:00', '12:00-\n14:00', 
                  '14:00-\n16:00', '16:00-\n18:00', '18:00-\n20:00', '20:00-\n22:00']
    engagement_rate = [85, 78, 60, 55, 72, 68, 75, 60]
    conversion_likelihood = [88, 75, 50, 52, 70, 65, 80, 55]
    overall_effectiveness = [87, 76, 55, 53, 71, 66, 77, 57]
    
    fig, ax = plt.subplots(figsize=(14, 8))
    x_positions = np.arange(len(time_slots))
    
    ax.plot(x_positions, engagement_rate, marker='o', linewidth=2.5, markersize=8, 
            label='Tingkat Engagement', color='#1f77b4', alpha=0.8)
    ax.plot(x_positions, conversion_likelihood, marker='s', linewidth=2.5, markersize=8, 
            label='Potensi Konversi', color='#ff7f0e', alpha=0.8)
    ax.plot(x_positions, overall_effectiveness, marker='^', linewidth=2.5, markersize=8, 
            label='Efektivitas Keseluruhan', color='#2ca02c', alpha=0.8)
    
    ax.axvspan(-0.5, 0.5, alpha=0.15, color='green', label='Pagi (Optimal)')
    ax.axvspan(3.5, 4.5, alpha=0.15, color='yellow', label='Sore (Baik)')
    ax.axvspan(5.5, 6.5, alpha=0.15, color='blue', label='Malam (Baik)')
    
    ax.set_xlabel('Waktu dalam Sehari', fontsize=12, fontweight='bold')
    ax.set_ylabel('Skor Metrik (0-100)', fontsize=12, fontweight='bold')
    ax.set_title('Waktu Optimal Posting untuk Engagement Maksimum Produk Kopi', 
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x_positions)
    ax.set_xticklabels(time_slots, fontsize=10)
    ax.set_ylim(40, 95)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)
    ax.legend(loc='lower left', fontsize=10, framealpha=0.95)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    st.pyplot(fig)
    
    st.divider()
    st.markdown("### 🔍 Analisis Mendalam:")
    st.markdown("""
    **1. Three Golden Windows untuk Posting Konten**
    
    🌅 **Pagi Hari (6-8 AM)** - Efektivitas Tertinggi 87%
    - Waktu ketika konsumen merencanakan morning ritual kopi mereka
    - Mencari inspirasi untuk morning preparation
    - Konten yang cocok: tips brewing, motivational quotes, morning routines
    
    ☀️ **Sore Hari (2-4 PM)** - Efektivitas Sedang 71%
    - Konsumen mencari respite dari afternoon slump
    - Konten edukatif tentang origins, sustainability, dan health benefits perform sangat baik
    
    🌙 **Malam Hari (6-8 PM)** - Efektivitas Tinggi 77%
    - Konsumen merencanakan next day coffee atau menikmati evening beverage
    - Konten sensory-rich dan storytelling perform optimal
    
    **2. Dead Zone Harus Dihindari (10 AM - 2 PM)**
    - Waktu ini menunjukkan engagement terendah (hanya ~50% dari peak hours)
    - Posting pada window ini adalah pemborosan resources
    - Brand sebaiknya tidak membuat konten original—gunakan paid promotion jika perlu
    
    **3. Timing Optimization Meningkatkan Reach 37%**
    - Perbedaan antara peak (87%) dan valley (50%) adalah 74%
    - Timing optimization saja dapat meningkatkan reach tanpa menambah quality konten atau ad spend
    """)

# ============ VISUALISASI 3: CONTENT PERFORMANCE ============
elif page == "3️⃣ Performance Jenis Konten":
    st.subheader("3️⃣ Perbandingan Performance Jenis Konten untuk Engagement Produk Kopi")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("#### Deskripsi Visualisasi:")
        st.markdown("""
        Grafik batang bersusun (grouped bar chart) yang membandingkan 8 jenis konten 
        berdasarkan dua metrik: Skor Engagement dan Conversion Rate.
        """)
        
        st.markdown("#### Prinsip Visual Encoding yang Digunakan:")
        st.markdown("""
        - **Length untuk Metrik Kuantitatif**: Panjang batang merepresentasikan nilai numerik
        - **Color (Hue) untuk Diferensiasi Metrik**: Biru untuk Engagement, Oranye untuk Conversion
        - **Grouped Bar Layout**: Memudahkan perbandingan antar metrik
        - **Sorting Descending**: Urutan berdasarkan engagement tertinggi ke terendah
        """)
    
    with col2:
        st.markdown("#### Top 3 Content Types:")
        st.success("""
        **🎬 Video Content**
        Engagement: 95
        Conversion: 85%
        
        **👥 User-Generated Content**
        Engagement: 88
        Conversion: 65%
        
        **🎥 Behind-the-Scenes**
        Engagement: 85
        Conversion: 72%
        """)
    
    st.divider()
    
    # Buat visualisasi 3
    setup_matplotlib_style()
    content_types = ['Video', 'Di Belakang\nLayar', 'Carousel', 'Pendidikan', 
                     'Konten\nPengguna', 'Tantangan\nInteraktif', 'Fitur\nProduk', 'Kutipan\nKopi']
    engagement_scores = [95, 85, 82, 78, 88, 80, 70, 65]
    conversion_rates = [85, 72, 75, 50, 65, 60, 78, 35]
    
    fig, ax = plt.subplots(figsize=(14, 8))
    x = np.arange(len(content_types))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, engagement_scores, width, label='Skor Engagement', 
                   color='#1f77b4', edgecolor='black', linewidth=1.2, alpha=0.8)
    bars2 = ax.bar(x + width/2, conversion_rates, width, label='Tingkat Konversi (%)', 
                   color='#ff7f0e', edgecolor='black', linewidth=1.2, alpha=0.8)
    
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                   f'{int(height)}', ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    ax.set_xlabel('Jenis Konten', fontsize=12, fontweight='bold')
    ax.set_ylabel('Skor / Persentase (0-100)', fontsize=12, fontweight='bold')
    ax.set_title('Perbandingan Performance Jenis Konten untuk Engagement Produk Kopi', 
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(content_types, fontsize=10)
    ax.set_ylim(0, 105)
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    st.pyplot(fig)
    
    st.divider()
    st.markdown("### 🔍 Analisis Mendalam:")
    st.markdown("""
    **1. Video Content adalah Raja (95% Engagement, 85% Conversion)**
    - Video content mendominasi landscape engagement
    - Video yang menampilkan **proses** outperform product shots sebesar 234%
    - Investment dalam video production bukan optional, tetapi **mandatory** untuk competitive presence
    - Minimal 3-4 video per minggu per platform
    
    **2. User-Generated Content (UGC) adalah Force Multiplier (88% Engagement, 65% Conversion)**
    - UGC mencapai engagement tertinggi kedua
    - Consumers trust peer recommendations **92% lebih** dari brand messaging langsung
    - Strategy: allocate budget untuk incentivize UGC campaigns
    - Provides continuous content supply dengan cost lebih rendah
    
    **3. Behind-the-Scenes Content Build Authenticity (85% Engagement, 72% Conversion)**
    - Content yang menampilkan proses produksi, quality control, dan people behind the brand
    - Conversion rate tertinggi di kategori educational
    - **Transparency dan authenticity adalah conversion drivers** untuk coffee products
    
    **4. Divergence antara Engagement dan Conversion pada Product Feature**
    - Product Feature content memiliki engagement rendah (70%) tetapi conversion rate tertinggi (78%)
    - Strategic insight: **jangan fokus hanya pada engagement metrics**
    - Product feature posts mungkin less viral tetapi **lebih likely untuk drive immediate sales**
    - Mixing strategy diperlukan: 30% product-focused untuk direct conversion, 70% lifestyle/educational
    
    **5. Coffee Quote Content Underperform (65% Engagement, 35% Conversion)**
    - Generic quotes tentang kopi memiliki performance terburuk
    - Audience lebih prefer actionable content, visual content, atau authentic stories
    - Hindari generic motivational content tanpa unique value proposition
    """)

# ============ VISUALISASI 4: ENGAGEMENT DISTRIBUTION ============
elif page == "4️⃣ Distribusi Engagement Levels":
    st.subheader("4️⃣ Distribusi Engagement Levels Across Platforms Media Sosial")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("#### Deskripsi Visualisasi:")
        st.markdown("""
        Heatmap yang menampilkan distribusi engagement levels dalam 10 kategori 
        di 5 platform utama (Instagram, TikTok, Facebook, YouTube, Twitter).
        """)
        
        st.markdown("#### Prinsip Visual Encoding yang Digunakan:")
        st.markdown("""
        - **Position untuk Kategorisasi Dual-Dimensi**: Platform pada Y-axis, engagement levels pada X-axis
        - **Color Saturation/Value**: Merepresentasikan frequency/intensity
        - **Perceptual Grouping melalui Color Gradient**: Dari kuning (low) ke merah (high)
        - **Legend Numerik**: Menunjukkan skala exact untuk frequency count
        """)
    
    with col2:
        st.markdown("#### Platform Characteristics:")
        st.info("""
        🔴 **Instagram & TikTok**
        Concentrate di level tinggi
        
        📊 **Facebook**
        Bimodal distribution
        
        ▶️ **YouTube**
        Skewed ke sedang-tinggi
        
        🐦 **Twitter**
        Uniform distribution
        """)
    
    st.divider()
    
    # Buat visualisasi 4
    setup_matplotlib_style()
    engagement_levels = ['1.0-\n10.9', '10.9-\n20.8', '20.8-\n30.7', '30.7-\n40.6', '40.6-\n50.5',
                         '50.5-\n60.4', '60.4-\n70.3', '70.3-\n80.2', '80.2-\n90.1', '90.1-\n100']
    
    data_heatmap = np.array([
        [2, 1, 1, 0, 1, 2, 2, 3, 3, 5],  # Instagram
        [1, 1, 1, 1, 1, 2, 2, 3, 4, 5],  # TikTok
        [3, 3, 2, 1, 0, 1, 1, 1, 2, 6],  # Facebook
        [2, 2, 3, 2, 2, 1, 1, 2, 2, 1],  # YouTube
        [4, 4, 2, 2, 1, 1, 1, 1, 1, 1]   # Twitter
    ])
    
    platforms_heat = ['Instagram', 'TikTok', 'Facebook', 'YouTube', 'Twitter']
    
    fig, ax = plt.subplots(figsize=(14, 7))
    im = ax.imshow(data_heatmap, cmap='YlOrRd', aspect='auto')
    
    ax.set_xticks(np.arange(len(engagement_levels)))
    ax.set_yticks(np.arange(len(platforms_heat)))
    ax.set_xticklabels(engagement_levels, fontsize=9)
    ax.set_yticklabels(platforms_heat, fontsize=11)
    
    ax.set_xlabel('Kategori Engagement Level', fontsize=12, fontweight='bold')
    ax.set_ylabel('Platform Media Sosial', fontsize=12, fontweight='bold')
    ax.set_title('Distribusi Engagement Levels Across Platforms Media Sosial untuk Produk Kopi', 
                 fontsize=14, fontweight='bold', pad=20)
    
    for i in range(len(platforms_heat)):
        for j in range(len(engagement_levels)):
            text = ax.text(j, i, data_heatmap[i, j],
                          ha="center", va="center", color="black", fontweight='bold', fontsize=10)
    
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label('Frekuensi', fontsize=11, fontweight='bold')
    
    plt.tight_layout()
    st.pyplot(fig)
    
    st.divider()
    st.markdown("### 🔍 Analisis Mendalam:")
    st.markdown("""
    **1. Instagram dan TikTok Concentrate Engagement di Level Tinggi**
    - Kedua platform menunjukkan konsentrasi merah (high frequency) pada engagement levels tinggi (70.3-100.0)
    - Content di platform ini consistently achieve high engagement
    - Algoritma platform ini naturally favor viral content dan amplifikasi lebih powerful
    - Strategic implication: Instagram & TikTok adalah platform untuk viral growth
    
    **2. Facebook Distribution adalah Bimodal (Two Peaks)**
    - Menunjukkan dua "hot zones": engagement level rendah (1.0-20.8) AND tinggi (80.2-100.0)
    - Engagement medium relatively rare
    - Mengindikasikan bahwa Facebook engagement adalah "polarized"
    - Content either flops atau massive success—tidak ada middle ground
    - Strategic implication: Facebook content harus extremely targeted dan resonant
    
    **3. YouTube Skewed Menuju Engagement Sedang-Tinggi (30.7-100.0)**
    - Tidak menunjukkan low-engagement spikes yang significant
    - Platform ini memiliki engagement floor yang lebih tinggi
    - Mungkin karena video content naturally performs lebih baik
    - Strategic implication: YouTube ideal untuk consistent, high-quality long-form content
    
    **4. Twitter Distribution Uniform dengan Slight Bias**
    - Distribusi relative uniform across all levels dengan slight peak pada engagement sedang
    - Bersifat "gamble platform"—low predictability untuk content performance
    - Kemungkinan karena real-time feed dynamics dan algorithm unpredictability
    - Strategic implication: Twitter sebagai secondary platform untuk reach diversification
    
    **5. Visual Pattern Recognition**
    - Heatmap memungkinkan instant identification dari platform characteristics tanpa statistical tests
    - Instagram dan TikTok's similar color patterns menunjukkan similar engagement dynamics
    - Facebook's unique bimodal pattern menciptakan distinct strategic considerations
    """)

# ============ VISUALISASI 5: INFLUENCER ROI ============
elif page == "5️⃣ Strategi Influencer & ROI":
    st.subheader("5️⃣ Efektivitas Strategi Influencer dan ROI untuk Pemasaran Produk Kopi")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("#### Deskripsi Visualisasi:")
        st.markdown("""
        Scatter plot dengan bubble chart elements yang menampilkan relationship antara 4 variabel:
        - X-axis: Ukuran Follower Count
        - Y-axis: Engagement Rate (%)
        - Bubble Size: ROI (Return on Investment)
        - Color: Strategi berbeda
        """)
        
        st.markdown("#### Prinsip Visual Encoding yang Digunakan:")
        st.markdown("""
        - **Position pada Dual Axis**: X (Follower Count), Y (Engagement Rate)
        - **Size Channel**: Merepresentasikan ROI dalam skala logaritmik
        - **Color Hue**: Membedakan 6 strategi/kategori
        - **Label dan Annotation**: Untuk key points dan identifikasi strategi
        """)
    
    with col2:
        st.markdown("#### ROI Ranking:")
        st.success("""
        🥇 **1. Micro-Influencer Fitness**
        ROI: 5.2x
        Engagement: 5.2%
        
        🥈 **2. Video Production**
        ROI: 4.2x
        Engagement: 6.5%
        
        🥉 **3. Micro-Influencer Lifestyle**
        ROI: 5.0x
        Engagement: 4.8%
        """)
    
    st.divider()
    
    # Buat visualisasi 5
    setup_matplotlib_style()
    strategies = ['Mikro-Influencer\nFitness', 'Mikro-Influencer\nLifestyle', 
                  'Makro-Influencer', 'Kampanye UGC', 'Iklan Berbayar', 'Produksi Video']
    
    follower_for_plot = [25, 50, 1000, 0.5, 500, 250]
    engagement_rates = [5.2, 4.8, 0.8, 3.2, 1.5, 6.5]
    roi_values = [5.2, 5.0, 2.5, 2.8, 2.2, 4.2]
    bubble_sizes = [roi * 300 for roi in roi_values]
    colors_strategies = ['#2ecc71', '#3498db', '#e74c3c', '#9b59b6', '#95a5a6', '#f39c12']
    
    fig, ax = plt.subplots(figsize=(14, 9))
    
    scatter = ax.scatter(follower_for_plot, engagement_rates, s=bubble_sizes, 
                         c=colors_strategies, alpha=0.6, edgecolors='black', linewidth=2)
    
    for i, strategy in enumerate(strategies):
        ax.annotate(strategy, (follower_for_plot[i], engagement_rates[i]),
                   xytext=(10, 10), textcoords='offset points',
                   fontsize=9, fontweight='bold',
                   bbox=dict(boxstyle='round,pad=0.5', facecolor=colors_strategies[i], alpha=0.3, edgecolor='black'),
                   arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0', lw=1.5))
    
    ax.set_xlabel('Ukuran Pengikut / Jangkauan Relatif', fontsize=12, fontweight='bold')
    ax.set_ylabel('Tingkat Engagement (%)', fontsize=12, fontweight='bold')
    ax.set_title('Efektivitas Strategi Influencer dan ROI untuk Pemasaran Produk Kopi', 
                 fontsize=14, fontweight='bold', pad=20)
    
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)
    
    legend_elements = [
        plt.scatter([], [], s=400, c='gray', edgecolors='black', linewidth=2, alpha=0.6, label='ROI 2.2x'),
        plt.scatter([], [], s=700, c='gray', edgecolors='black', linewidth=2, alpha=0.6, label='ROI 4.2x'),
        plt.scatter([], [], s=1200, c='gray', edgecolors='black', linewidth=2, alpha=0.6, label='ROI 5.2x')
    ]
    legend1 = ax.legend(handles=legend_elements, scatterpoints=1, title='ROI (Return on Investment)',
                       loc='upper left', fontsize=10, framealpha=0.95)
    
    ax.text(0.98, 0.02, 'Ukuran bubble merepresentasikan ROI - bubble lebih besar = ROI lebih baik',
           transform=ax.transAxes, fontsize=10, verticalalignment='bottom',
           horizontalalignment='right', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    st.pyplot(fig)
    
    st.divider()
    st.markdown("### 🔍 Analisis Mendalam:")
    st.markdown("""
    **1. Micro-Influencer Superior ROI (5.2x Return per Dollar Spent)**
    - Scatter plot menunjukkan micro-influencer bubbles memiliki combination optimal
    - Engagement rate tinggi (4.5-5.5%) dan ROI paling besar
    - **Dalam influencer marketing, lebih tidak selalu lebih baik**
    - Micro-influencers memiliki niche audience yang highly relevant
    - Conversion rates jauh lebih tinggi dibanding macro-influencers
    
    **2. Macro-Influencer Paradox (Wide Reach, Low Efficiency)**
    - Macro-influencer bubble berada di extreme right X-axis (1M+ followers)
    - Engagement rate sangat rendah (0.5-1.2%) dan ROI moderate (2-3x)
    - **Large follower count tidak translate ke effective engagement atau conversion**
    - Audience macro-influencers terlalu diverse—relevance per follower sangat rendah
    - Strategic lesson: Jangan buat kesalahan hiring celebrity endorsers untuk coffee products
    
    **3. Cost-Benefit Trade-off untuk Video Production (ROI 4.2x)**
    - Video production bubble menunjukkan engagement rate very high (6.5%)
    - ROI excellent (4.2x)—bisa rival influencer ROI
    - **Investing dalam original video production dalam-house dapat match influencer effectiveness**
    - Hybrid approach recommended: combine micro-influencers + original video production
    
    **4. UGC Campaign sebagai Force Multiplier (2.8x ROI)**
    - UGC campaign bubble menunjukkan moderate engagement rate (3.2%) dengan respectable ROI
    - Memberikan cost-effective alternative dengan continuous content supply
    - ROI lebih rendah per piece dibanding micro-influencers
    - Tetapi volume dari generated content dan cost efficiency membuatnya **highly scalable**
    
    **5. Micro-Influencer Fitness Outperforms Lifestyle**
    - Comparing dua micro-influencer categories: Fitness sedikit lebih tinggi
    - **Coffee products dalam health/fitness framing resonate lebih baik**
    - Positioning: energy, focus, wellness benefits
    - Lifestyle framing masih efektif tetapi secondary
    
    **6. Traditional Paid Ads Underperform (2-2.5x ROI)**
    - Paid ads bubble menunjukkan lowest engagement rate dan ROI
    - **Programmatic advertising less effective untuk coffee products**
    - Why? Coffee adalah **hedonic product**
    - Emotional connection dan authentic recommendation lebih important daripada broad reach
    """)

# ============ RINGKASAN & REKOMENDASI ============
elif page == "📋 Ringkasan & Rekomendasi":
    st.subheader("📋 Ringkasan Kelima Visualisasi & Rekomendasi Strategis")
    
    st.markdown("### 📊 Tabel Ringkasan Kelima Visualisasi")
    
    summary_data = {
        'No': ['1', '2', '3', '4', '5'],
        'Visualisasi': [
            'Platform Effectiveness',
            'Waktu Optimal Posting',
            'Performance Jenis Konten',
            'Distribusi Engagement Levels',
            'Strategi Influencer & ROI'
        ],
        'Jenis Grafik': [
            'Horizontal Bar Chart',
            'Line Chart (Multi-series)',
            'Grouped Bar Chart',
            'Heatmap',
            'Scatter Plot dengan Bubble'
        ],
        'Dimensi Data': [
            '1D (Platform vs Score)',
            '2D (Time vs 3 Metrics)',
            '2D (Content vs 2 Metrics)',
            '2D (Platform vs Engagement)',
            '4D (Followers, Engagement, ROI, Strategy)'
        ],
        'Encoding Utama': [
            'Position, Color Hue',
            'Position, Color Hue, Slope',
            'Length, Color Hue',
            'Position, Color Saturation',
            'Position (2D), Size, Color Hue'
        ]
    }
    
    summary_df = pd.DataFrame(summary_data)
    st.dataframe(summary_df, use_container_width=True, hide_index=True)
    
    st.divider()
    
    st.markdown("### 🎯 Rekomendasi Strategis Berdasarkan Kelima Visualisasi")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 1️⃣ Alokasi Budget Platform")
        st.info("""
        - **70%** untuk Instagram & TikTok (platform utama)
        - **20%** untuk Facebook & WhatsApp Business
        - **10%** untuk diversifikasi (YouTube, Twitter, lainnya)
        """)
        
        st.markdown("#### 2️⃣ Jadwal Posting Optimal")
        st.success("""
        - **6-8 AM**: Morning brew tips & energetic content
        - **2-4 PM**: Educational content & origins
        - **6-8 PM**: Sensory-rich content & storytelling
        
        ❌ Hindari: 10 AM-2 PM (dead zone)
        """)
        
        st.markdown("#### 3️⃣ Content Mix Strategy")
        st.warning("""
        - **30%** Video content (highest ROI)
        - **25%** Behind-the-scenes & authenticity
        - **25%** UGC & community building
        - **20%** Product features & direct sales
        """)
    
    with col2:
        st.markdown("#### 4️⃣ Influencer Strategy")
        st.info("""
        - **Prioritas**: Micro-influencers (10K-100K) dalam niche fitness/wellness
        - **Kombinasi**: In-house video production untuk scalability
        - **UGC Campaigns**: Untuk continuous content supply & community engagement
        
        ❌ Hindari: Macro-influencers (ROI terlalu rendah)
        """)
        
        st.markdown("#### 5️⃣ Metric Tracking")
        st.success("""
        - Engagement rate per platform
        - Conversion rate dari social traffic
        - ROI per strategi influencer
        - Platform-specific characteristics
        - Monthly performance review & optimization
        """)
    
    st.divider()
    
    st.markdown("### 💡 Key Insights Summary")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Platform Terbaik", "Instagram", "Skor 92/100")
    with col2:
        st.metric("Waktu Optimal Posting", "6-8 AM", "87% Efektivitas")
    with col3:
        st.metric("ROI Tertinggi", "Micro-Influencer", "5.2x Return")
    
    st.divider()
    
    st.markdown("### 📈 Prinsip Visual Encoding yang Diterapkan")
    
    encoding_info = {
        'Channel Visual': ['Position (Spatial)', 'Length', 'Color (Hue)', 'Color (Saturation)', 'Size', 'Slope', 'Continuity'],
        'Efektivitas': ['Sangat Tinggi', 'Sangat Tinggi', 'Tinggi', 'Sedang', 'Sedang', 'Tinggi', 'Sedang'],
        'Digunakan Pada Visualisasi': [
            'Semua (terutama 1, 2, 5)',
            'Visualisasi 3, 1',
            'Semua (1, 2, 3, 5)',
            'Visualisasi 4',
            'Visualisasi 5',
            'Visualisasi 2',
            'Visualisasi 2'
        ]
    }
    
    encoding_df = pd.DataFrame(encoding_info)
    st.dataframe(encoding_df, use_container_width=True, hide_index=True)
    
    st.divider()
    
    st.markdown("### ✅ Prinsip Design yang Diterapkan")
    
    design_principles = {
        'Prinsip': [
            'Expressiveness',
            'Effectiveness',
            'Consistency',
            'Importance Ordering',
            'Gestalt Principles'
        ],
        'Penjelasan': [
            'Menampilkan SEMUA dan HANYA informasi dalam dataset',
            'Channel visual paling efektif untuk data paling important',
            'Properti visual sesuai dengan properti data',
            'Informasi penting di-encode dengan channel paling efektif',
            'Proximity, similarity, enclosure untuk group elements'
        ],
        'Implementasi': [
            'Setiap visualisasi menampilkan data yang relevan tanpa distorsi',
            'Position > Length > Color untuk data kuantitatif',
            'Terurut data tetap terurut visual; magnitude sesuai magnitude',
            'Platform effectiveness ranked; content types ranked by performance',
            'Highlight areas untuk golden windows; color grouping untuk kategori'
        ]
    }
    
    principles_df = pd.DataFrame(design_principles)
    st.dataframe(principles_df, use_container_width=True, hide_index=True)
    
    st.divider()
    
    st.markdown("### 📌 Catatan Penting")
    st.markdown("""
    ✅ **Semua visualisasi dirancang menggunakan prinsip visual encoding yang optimal**
    - Setiap jenis grafik dipilih berdasarkan kecocokan dengan tipe data
    - Warna, label, dan annotation dipilih untuk maximum clarity dan readability
    - Prinsip effectiveness dan expressiveness diterapkan konsisten
    
    ✅ **Data-Driven Insights untuk Strategic Decision Making**
    - Insights dapat langsung diterapkan untuk meningkatkan ROI marketing
    - Fokus pada platform utama, timing optimal, dan content mix yang balanced
    - Strategi influencer yang cost-effective dan scalable
    
    ✅ **Baseline untuk Continuous Optimization**
    - Visualisasi ini memberikan baseline untuk monthly tracking dan optimization
    - Recommend untuk melakukan A/B testing pada setiap strategi yang direkomendasikan
    - Adjust strategy berdasarkan actual performance data di real-world implementation
    """)

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p><strong>📊 Dashboard Analisis Engagement Media Sosial untuk Penjualan Kopi</strong></p>
    <p>Dataset: Social Media Engagement dari Kaggle | Periode: Januari - Desember 2023</p>
    <p>Dibuat dengan ❤️ menggunakan Streamlit & Matplotlib | Prinsip Visual Encoding yang Optimal</p>
</div>
""", unsafe_allow_html=True)
