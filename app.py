import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import base64
import os
import warnings

from plotly.colors import n_colors
from PIL import Image

# Suppress warnings
warnings.filterwarnings('ignore')

# Set page configuration
st.set_page_config(page_title="ENERGY MANAGEMENT DASHBOARD", page_icon=":bar_chart:", layout="wide")

# Load your own logo or image
image = Image.open('mrt-jakarta-logo-vertical.png')  

# Create two columns for the logo and the title
col1, col2 = st.columns([1,10])  # Adjust column width ratio as needed

# Display the logo in the first column
with col1:
    st.image(image, width=100)  # You can adjust the width

# Display the title in the second column
with col2:
    st.title("ENERGY MANAGEMENT DASHBOARD")

# Styling for the dashboard
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

# Initialize session state for menu selection
if 'menu_choice' not in st.session_state:
    st.session_state['menu_choice'] = 'About'

# Define background images for each menu choice
background_images = {
    'About': 'https://example.com/about_background.jpg',
    'Summary': 'https://example.com/summary_background.jpg',
    'Report': 'https://example.com/report_background.jpg'
}

# Update CSS for the current menu choice
st.markdown(
    f"""
    <style>
    body {{
        background-color: #4169E1;
        background-image: url('{background_images[st.session_state.menu_choice]}');
        background-size: cover;
        background-position: center;
    }}

    .stButton>button {{
        background-color: #4169E1;
        color: white;
        padding: 10px 24px;
        font-size: 16px;
        border: none;
        cursor: pointer;
        border-radius: 12px;
        transition: background-color 0.3s ease;
    }}
    
    .stButton>button:hover {{
        background-color: #45a049;
    }}

    /* Change background for the selected button */
    .stButton.selected>button {{
        background-color: #4169E1;
    }}

    .stButton>button:active {{
        background-color: #4169E1;
    }}
    </style>
    """, unsafe_allow_html=True
)

# Create a horizontal menu using buttons with custom styling
col1, col2, col3 = st.columns(3)

def button_with_style(label):
    return st.button(label, key=label, use_container_width=True)

with col1:
    if button_with_style("About"):
        st.session_state['menu_choice'] = 'About'

with col2:
    if button_with_style("Summary"):
        st.session_state['menu_choice'] = 'Summary'

with col3:
    if button_with_style("Report"):
        st.session_state['menu_choice'] = 'Report'
        
# Display content based on the selected menu
if st.session_state['menu_choice'] == 'About':
    # Function to set a background image from a URL (optional)
    def set_background_image(url):
        page_bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] > .main {{
        background-image: url("{url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        }}
        [data-testid="stAppViewContainer"]::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(20, 10, 150, 0.3); /* White overlay */
        z-index: 1;
        }}
        .main > div {{
        position: relative;
        z-index: 2;
        }}
        </style>
        """
        st.markdown(page_bg_img, unsafe_allow_html=True)
     
    # Setting one of the Unsplash images as the background
    set_background_image("https://images.unsplash.com/photo-1688525138876-652b04859861")
    st.session_state.setdefault('page', 'main_menu')
    
    # Gambar untuk About Section
    image1 = Image.open('bf2b0a8426f47402de57109b9f75a7d1.jpg')  # Ganti dengan path gambar Anda
    image2 = Image.open('52879710795_497ffd31f3_k.jpg')  # Ganti dengan path gambar Anda
    image3 = Image.open('52879602218_a2a1d781a3_k.jpg')  # Ganti dengan path gambar Anda
    image4 = Image.open('52487355637_93dd5dad8a_k.jpg')  # Ganti dengan path gambar Anda
    
    # Fungsi untuk menampilkan konten sesuai pilihan
    def show_about():
        st.header("Sistem Manajemen Energi (SME)")
        col1, col2 = st.columns([2, 3])

        with col1:
            st.image(image1, use_column_width=True)

        with col2:
            st.markdown(
                """
                <style>
                    .section1 {
                        background-color: rgba(25, 50, 200, 0.3);
                        padding: 15px;
                        border-radius: 10px;
                        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
                    }
                </style>
                <div class='section1'>
                Sistem Manajemen Energi atau SME adalah sistem tata kelola untuk membuat kebijakan energi, 
                tujuan, sasaran dan rencana kerja energi dan proses-proses yang dibutuhkan untuk mencapai tujuan dan sasaran energi. Dengan latar belakang berdasarkan Peraturan Pemerintah No. 33 tahun 2023 tentang konservasi energi dan
                sejalan dengan Rencana Jangka Panjang Perusahaan (RJPP) PT MRT Jakarta (Perseroda) terkait 
                dengan sustainability energy maka dibutuhkan dokumen panduan dan pedoman dalam 
                bentuk SOP (Standard Operation Procedure) yang akan digunakan menjadi dasar dalam 
                penerapan program kerja energy consumption monitoring dan rencana implementasi ISO 
                50001 yang sedang dijalankan pada saat ini. Ruang lingkup dari prosedur ini yaitu mengatur kebijakan Perusahaan yang terkait dengan 
                Sistem Manajemen Energi (SME) dan proses-proses yang berkaitan dengan pemakaian energi 
                seperti energi listrik dan bahan bakar. Prosedur ini berlaku di seluruh wilayah PT MRT Jakarta 
                (Perseroda) yang mengimplementasikan Sistem Manajemen Energi (SME) atau ISO 50001
    
                Implementasi dari Sistem Manajemen Energi ini bertujuan untuk :
                1. Mengatur pengelolaan energi melalui pendekatan Sistem Manajemen Energi ISO 50001:2018
                2. Memberikan tahapan - tahapan yang diperlukan untuk mengurangi biaya energi serta meningkatkan kinerja perusahaan
                3. Mengendalikan proses dan kegiatan terkait operasional dan pemeliharaan peralatan dan sistem.
                
                Untuk mencapai hal tersebut maka diperlukannya beberapa faktor pendukung diantarnya adalah :
                1. Kebijakan Energi yaitu sebuah pernyataan perusahaan terkait niat dan arahan organisasi 
                tentang energi yang dinyatakan secara formal oleh BoD (Board of Director) PT MRT Jakarta (Perseroda)
                2. Indikator Kinerja Energi (Energy Performance Indicator) yaitu adalah sebuah ukuran atau satuan kinerja energi yang ditetapkan oleh perusahaan.
                Dan juga sebuah, 
                3. Batasan Energi (Energy Baseline) yaitu referensi kuantitatif yang menjadi dasar 
                perbandingan kinerja energi yang telah ditetapkan per bulan, per tahun atau per 
                kWh/m2 dari setiap area atau kWh/penumpang dari setiap area.
                
                Dalam pelaksanaannya tim manajemen energi terdiri dari manager energi, auditor energi dan perwakilan 
                karyawan pada setiap departemen yang ditunjuk oleh top management untuk
                bertanggung jawab dalam mengawasi, mengelola, dan mengoptimalkan penggunaan 
                energi pada area MRT Jakarta serta meningkatkan efisiensi energi, mengurangi biaya 
                operasional, dan meminimalkan dampak lingkungan. 

                Source: SOP Tata Kelola Energi
                </div>
                """,
                unsafe_allow_html=True
            )
        if st.button("Kembali ke Menu Utama"):
            st.session_state['page'] = 'main_menu'
            
    def show_procedure():
        st.header("Tahapan Prosedur")
        col1, col2 = st.columns([3, 2])

        with col1:
            st.markdown(
                """
                <style>
                    .section2 {
                        background-color: rgba(25, 50, 200, 0.3);
                        padding: 15px;
                        border-radius: 10px;
                        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
                    }
                </style>
                <div class='section2'>
                
                Dalam implementasinya, tata kelola energi memiliki standar operasional prosedurnya tersendiri diantanya adalah :
                1. Energy Review
                2. Proses Penentuan Energi Performance Indikator (EnPI)
                3. Penentuan Energy Baseline (EnB)
                4. Pengukuran Energi 
                5. Penentuan Jangka Waktu atau Frekuensi Pengukuran
                6. Kualifikasi Sumber Daya
                7. Kalibrasi Peralatan Pada SME
                8. Investigasi Penyimpangan Penggunaan energi
                9. Program Penghematan Energi
                10. Ketentuan Umum Tata Kelola Energi MRT Jakarta
                
                Semua tahapan prosedur yang dilakukan tidak akan mendapatkan hasil yang baik jika semua aspek yang ada pada PT. MRT Jakarta (PERSERODA) 
                seperti karyawan, penumpang, peralatan dan sistem tidak memiliki kesadaran tentang pentingnya penghematan energi dan dampaknya terhadap lingkungan
                terutama pada area authority diseluruh PT. MRT Jakarta (PERSERODA).
                
                Source: SOP Tata Kelola Energi
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.image(image2, use_column_width=True)
        if st.button("Kembali ke Menu Utama"):
            st.session_state['page'] = 'main_menu'
            
    def show_program():
        st.header("Program Penghematan Energi")
        col1, col2 = st.columns([1, 3])

        with col1:
            st.image(image3, use_column_width=True)

        with col2:
            st.markdown(
                """
                <style>
                    .section3 {
                        background-color: rgba(25, 50, 200, 0.3);
                        padding: 15px;
                        border-radius: 10px;
                        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
                    }
                </style>
                <div class='section3'>
                MRT Jakarta melakukan program penghematan energi yang terbagi menjadi 4 cara diantaranya adalah : 
                
                1. No Cost adalah langkah-langkah yang dapat diambil untuk mengurangi konsumsi 
                    energi tanpa memerlukan investasi finansial. Sesuai dengan Permen ESDM No. 14 
                    Tahun 2012 : Potensi penghematan energi tidak membutuhkan biaya (Biaya Rp0).
                2. Low Cost adalah langkah-langkah yang memerlukan sedikit investasi tetapi dapat 
                    menghasilkan penghematan energi yang signifikan. Sesuai dengan Permen ESDM No. 
                    14 Tahun 2012 : Potensi penghematan energi sampai dengan 10% dan/atau payback
                    kurang dari 2 tahun.                
                3. Medium Cost melibatkan investasi yang lebih besar dibandingkan dengan program 
                    no cost atau low cost, namun masih dalam kategori yang terjangkau. Sesuai dengan 
                    Permen ESDM No. 14 Tahun 2012 : Potensi penghematan energi 10%—20% dan/atau
                    payback 2—4 tahun)                
                4. High Cost melibatkan investasi signifikan tetapi memberikan penghematan energi 
                    yang besar dan berkelanjutan dalam jangka panjang. Sesuai dengan Permen ESDM 
                    No. 14 Tahun 2012 : Potensi penghematan lebih dari 20% dan/atau payback lebih dari 4 tahun.
                    
                Source: SOP Tata Kelola Energi
                </div>
                """,
                unsafe_allow_html=True
            )
        if st.button("Kembali ke Menu Utama"):
            st.session_state['page'] = 'main_menu'
            
    def show_efficiency():
        st.header("Upaya Efisiensi Energi dan Pemanfaatan Energi Terbarukan")
        col1, col2 = st.columns([3, 1])

        with col1:
            st.markdown(
                """
                <style>
                    .section4 {
                        background-color: rgba(25, 50, 200, 0.3);
                        padding: 15px;
                        border-radius: 10px;
                        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
                    }
                </style>
                <div class='section4'>
                
                Efisiensi listrik oleh MRT Jakarta antara lain: 
                1. Dilakukan dengan mendesain ulang kantor dengan konsep yang terbuka sehingga 
                    meminimalkan penggunaan lampu/listrik, menggunakan lampu hemat energi LED, dan engoptimalkan penggunaan lampu 
                    dengan mengimplementasi  teknologi motion dan thermal sensor di beberapa lokasi publik, 
                    seperti toilet publik wanita dan laki-laki.
                2. Mode grouping pada lampu stasiun. Khusus stasiun elevated, 50% 
                    pada siang hari dan 100% pada malam hari. Pada stasiun underground
                    menggunakan mode 100% selama jam operasi. Pada saat kereta berhenti 
                    operasi (window time), maka menggunakan mode 50% untuk stasiun elevated 
                    dan underground. hal tersebut dilakukan untuk menghemat konsumsi listrik untuk pencahayaan, terutama pada stasiun 
                    elevated dikarenakan pada siang hari dapat memanfaatkan pencahayaan 
                    langsung dari matahari.
                3. Pemakaian unit chiller dengan teknologi dual compressor. Apabila beban pendinginan rendah maka dapat mengaktifkan hanya salah 
                    satu dari kompresor, sehingga konsumsi pemakaian listrik lebih rendah
                4. Eskalator dan elevator dalam keadaan mati saat window time.
                5. Terdapat teknologi sensor proximity pada eskalator, yaitu kecepatan normal eskalator hanya pada saat digunakan dan mode lambat bila tidak digunakan.
                
                **Pemanfaatan EBT (Energi Baru Terbarukan)**
                
                PT MRT Jakarta (Perseroda) telah menyusun sembilan tahapan transisi menuju 25 persen energi terbaru periode 2021—2025. Hal ini merupakan bagian dari mendukung 
                komitmen Indonesia mewujudkan net zero emission maksimal pada 2060. Langkah nyata yg dilakukan perseroan untuk mengurangi 
                emisi dilakukan dengan mengoptimalkan efisiensi energi, khusus untuk fasilitas dan kegiatan pendukung. Selain melakukan otomatisasi dan 
                digitaliasi menggunakan teknologi yang lebih hemat energi, perseroan juga berinisiatif untuk memanfaatkan energi baru dan terbarukan (EBT).
                
                Pemanfaatan EBT pada PT. MRT Jakarta sudah melakukan dengan beberapa cara diantaranya :
                1. penggunaan listrik MRT Jakarta berasal dari sumber energi terbarukan. 
                    pada tahun 2022 sebesar 5.000 MWh berasal dari  Pembangkit Listrik Tenaga Panas Bumi (PLTP) Kamojang
                2. Pada tahun 2022 pengelolaan limbah dari waste management di Stasiun Blok M BCA bekerja sama dengan Rekosistem telah mendaur ulang 99,7 persen dari 31,5 ton 
                    sampah anorganik yang disetor masyarakat. PT MRT Jakarta (Perseroda) juga menanam lima ribu lebih pohon sebagai kompensasi pembangunan jaringan MRT Jakarta.
                    Angka ini naik dari 860-an pohon pada 2021.
                3. Pembuatan stasiun pengisi daya berbasis panel surya di Stasiun Dukuh Atas BNI seperti pada foto di samping.  
                
                Source: Sustainability Report dan Jakartamrt.co.id
                </div>
                """,
                unsafe_allow_html=True
            ) 

        with col2:
            st.image(image4, use_column_width=True)
        if st.button("Kembali ke Menu Utama"):
            st.session_state['page'] = 'main_menu'
    
    # Daftar path gambar
    image_paths = [
        "C:/Users/MUHAMMAD ALI RIDHA/Documents/KULIAH/PI DAN MAGANG/MSIB/PT. MRT JAKARTA/PROYEK SME/New project!.jpg",
        "C:/Users/MUHAMMAD ALI RIDHA/Documents/KULIAH/PI DAN MAGANG/MSIB/PT. MRT JAKARTA/PROYEK SME/Power Ideas Ice.jpg",
        "C:/Users/MUHAMMAD ALI RIDHA/Documents/KULIAH/PI DAN MAGANG/MSIB/PT. MRT JAKARTA/PROYEK SME/Public Service Announcement Energy Saving Poster _ Canva Template.jpg"
    ]
                
    def main_menu():
        # Tambahkan gaya CSS untuk memperbesar tombol
        st.markdown("""
            <style>
            .button-container {
                display: flex;
                justify-content: center;
                gap: 20px; /* Jarak antar tombol */
                flex-wrap: wrap; /* Agar tombol responsif di layar kecil */
                margin-top: 20px;
            }
            .custom-button {
                font-size: 22px; /* Ukuran teks tombol */
                padding: 20px; /* Ukuran padding tombol */
                text-align: center;
                border-radius: 10px; /* Sudut melengkung */
                background-color: #4CAF50;
                color: white;
                text-decoration: none; /* Hilangkan underline */
                display: inline-block;
                width: 220px; /* Lebar tombol */
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2); /* Tambahkan bayangan */
            }
            .custom-button:hover {
                background-color: #45a049; /* Warna saat di-hover */
            }
            </style>
        """, unsafe_allow_html=True)

        # Tampilkan judul
        st.markdown("<h2 style='text-align: center;'>Menu Utama</h2>", unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
       
        with col1:
            if st.button("Apa Itu SME?", key="sme", use_container_width=True):
                st.session_state['page'] = 'about'
       
        with col2:
            if st.button("Prosedur", key="procedure", use_container_width=True):
                st.session_state['page'] = 'procedure'
        
        with col3:
            if st.button("Program Penghematan", key="program", use_container_width=True):
                st.session_state['page'] = 'program'
        
        with col4:
            if st.button("Upaya EBT", key="efficiency", use_container_width=True):
                st.session_state['page'] = 'efficiency'
        
        # Layout menggunakan 3 kolom
        col1, col2, col3 = st.columns(3)

        # Tampilkan gambar di kolom-kolom
        with col1:
            st.image(image_paths[0], caption="source : pinterest = Watcharapon Kaewjit", use_column_width=True)
 
        with col2:
            st.image(image_paths[1], caption="source : pinterest = Annabel Muir", use_column_width=True)

        with col3:
            st.image(image_paths[2], caption="source : pinterest = Hydric Template", use_column_width=True)

        # Pesan Tambahan
        st.markdown(
            "<p style='text-align: center; font-size: 50px; font-weight: bold;'>Mari selamatkan energi dengan aksi nyata!</p>",
            unsafe_allow_html=True
        )

    # Logika untuk Navigasi Halaman
    if st.session_state['page'] == 'main_menu':
        main_menu()
    elif st.session_state['page'] == 'about':
        show_about()
    elif st.session_state['page'] == 'procedure':
        show_procedure()
    elif st.session_state['page'] == 'program':
        show_program()
    elif st.session_state['page'] == 'efficiency':
        show_efficiency()
    
                    
elif st.session_state['menu_choice'] == 'Summary':
    
    # Styling for the dashboard
    st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

   # File uploader
    fl = st.file_uploader(":file_folder: Upload a file", type=["csv", "txt", "xlsx", "xls"])

    if fl is not None:
        # Read file based on its type
        if fl.name.endswith(".csv"):
            df = pd.read_csv(fl, encoding="ISO-8859-1")
        elif fl.name.endswith((".xlsx", ".xls")):
            df = pd.read_excel(fl)
    else:
        # Change to your actual directory if needed
        os.chdir(r"C:\Users\MUHAMMAD ALI RIDHA\Documents\KULIAH\PI DAN MAGANG\MSIB\PT. MRT JAKARTA\PROYEK SME")
        df = pd.read_excel("DATA BASE ENERGI.xlsx")
    
    def set_background_image(url):
        page_bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] > .main {{
        background-image: url("{url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        position: relative;
        }}

        [data-testid="stAppViewContainer"]::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(20, 10, 150, 0.3); /* White overlay with 70% opacity */
        z-index: 1;
        }}

        .main > div {{
        position: relative;
        z-index: 2; /* Ensure content stays above the overlay */
        }}

        [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
        }}

        [data-testid="stToolbar"] {{
        right: 2rem;
        }}
        </style>
        """
        st.markdown(page_bg_img, unsafe_allow_html=True)
    
    set_background_image("https://images.unsplash.com/photo-1653798402555-727826cf8e92")
    
    # CSS untuk memodifikasi tampilan judul
    st.markdown("""
        <style>
        .title {
            text-align: center;
            font-size: 58Px;
            font-weight: bold;
            color: WHITE;
        }
        </style>
        """, unsafe_allow_html=True)

    # Menampilkan judul dan deskripsi dengan satu latar belakang transparan
    st.markdown("""
        <div style='background-color: rgba(0, 0, 0, 0.3); padding: 20px; border-radius: 10px;'>
            <h1 style='text-align: center; font-size: 50px; color: white;'>ENERGY EFFICIENCY SUMMARY</h1>
            <p style='text-align: center; font-size: 18px; color: white;'>This section presents a summary of the energy efficiency initiatives undertaken by PT MRT Jakarta (Perseroda) during the 2023 and 2024 periods. It specifically focuses on the scope of all MRT stations, workshops, and administrative buildings, and provides an overview of the electrical energy consumption patterns observed.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Function to clean and convert percentage columns safely 
    def clean_percentage_column(column):
        """Function to clean and convert percentage columns to float safely."""
        column = column.astype(str).str.replace('%', '', regex=False).str.replace(',', '', regex=False)
        return pd.to_numeric(column, errors='coerce') / 100

    # Function to clean numeric columns and handle non-numeric values
    def clean_numeric_column(column):
        """Function to clean numeric columns, removing non-numeric characters."""
        column = column.astype(str).str.replace(',', '', regex=False)
        return pd.to_numeric(column, errors='coerce')

    # Column names based on actual dataset
    column_2023 = ['month', 'Realisasi', 'BASELINE', 'EFISIENSI kWh 2023', 'Persentase']
    column_2024 = ['MONTH', 'REALISASI', 'BASELINE PERBULAN 2024', 'EFISIENSI kWh 2024', 'persentase']
    
    # Define function to display graphs side by side
    def display_side_by_side_charts(data_2023, data_2024, year_2023, year_2024, baseline_col_2023, realization_col_2023, efficiency_col_2023, baseline_col_2024, realization_col_2024, efficiency_col_2024):
        # Create two columns
        col1, col2 = st.columns(2)
        
        # Graph for 2023
        with col1:
            st.markdown(f"<h3 style='text-align: center;'>Energy Savings {year_2023}</h3>", unsafe_allow_html=True)
            fig_2023 = go.Figure()
            fig_2023.add_trace(go.Scatter(x=data_2023['Month'], y=data_2023[realization_col_2023], mode='lines', name='Realization (kWh)', line=dict(color='orange', width=9)))
            fig_2023.add_trace(go.Scatter(x=data_2023['Month'], y=data_2023[baseline_col_2023], mode='lines', name='Baseline (kWh)', line=dict(color='yellow', width=9)))
            fig_2023.update_layout(
                xaxis_title='Month',
                yaxis_title='Energy (kWh)',
                plot_bgcolor='rgba(20, 20, 200, 0)',  # Background color
                paper_bgcolor='rgba(240, 240, 245, 0)',  # Main background color
                margin=dict(t=10)  # Mengurangi jarak dari atas
            )
            st.plotly_chart(fig_2023)

        # Graph for 2024
        with col2:
            st.markdown(f"<h3 style='text-align: center;'>Energy Savings {year_2024}</h3>", unsafe_allow_html=True)
            fig_2024 = go.Figure()
            fig_2024.add_trace(go.Scatter(x=data_2024['Month'], y=data_2024[realization_col_2024], mode='lines', name='Realization (kWh)', line=dict(color='orange', width=9)))
            fig_2024.add_trace(go.Scatter(x=data_2024['Month'], y=data_2024[baseline_col_2024], mode='lines', name='Baseline (kWh)', line=dict(color='yellow', width=9)))
            fig_2024.update_layout(
                xaxis_title='Month',
                yaxis_title='Energy (kWh)',
                plot_bgcolor='rgba(20, 20, 200, 0)',
                paper_bgcolor='rgba(240, 240, 245, 0)',
                margin=dict(t=10)  # Mengurangi jarak dari atas
            )
            st.plotly_chart(fig_2024)

    # Function to display combined summary table
    def display_combined_summary_table(summary_2023, summary_2024):
        # Calculate totals for both years
        total_2023 = {
            'Year': 2023,
            'Total Baseline (kWh)': summary_2023['Baseline (kWh)'].sum(),
            'Total Realization (kWh)': summary_2023['Realization (kWh)'].sum(),
            'Total Savings (kWh)': summary_2023['Efficiency (kWh)'].sum(),
            'Savings Percentage (%)': (summary_2023['Efficiency (kWh)'].sum() / summary_2023['Baseline (kWh)'].sum()) * 100
        }

        total_2024 = {
            'Year': 2024,
            'Total Baseline (kWh)': summary_2024['Baseline (kWh) 2024'].sum(),
            'Total Realization (kWh)': summary_2024['Realization (kWh) 2024'].sum(),
            'Total Savings (kWh)': summary_2024['Efficiency (kWh) 2024'].sum(),
            'Savings Percentage (%)': (summary_2024['Efficiency (kWh) 2024'].sum() / summary_2024['Baseline (kWh) 2024'].sum()) * 100
        }
    
        # Logic to display arrow based on percentage
        def get_arrow(percentage):
            return "⬆️" if percentage > 0 else "⬇️"
        
        # Bar chart styling similar to image reference
        st.markdown(f"""
            <div <div style="background-color: rgba(240, 240, 245, 0.1); padding: 20px; border-radius: 100px; border: 5px solid #ddd; width: 80%; margin: auto;">
                <div style="background-color: rgba(20, 20, 200, 0.3); padding: 2px; border-radius: 100px;">
                    <h3 style="text-align: center; font-size: 35px;">🚆 2023 vs 2024 Energy Savings Summary</h3>
                    <div style="display: flex; justify-content: space-around; padding-top: 5px;">
                        <div style="width: 45%;">
                        <h4 style="color: #ff9800; text-align: center; font-size: 30px;">📅 2023</h4>
                        <p style="text-align: center; font-size: 18px;"><strong>Total Baseline:</strong> <span>{int(total_2023['Total Baseline (kWh)']):,} kWh</span></p>
                        <p style="text-align: center; font-size: 18px;"><strong>Total Realization:</strong> <span>{int(total_2023['Total Realization (kWh)']):,} kWh</span></p>
                        <p style="text-align: center; font-size: 18px;"><strong>Total Savings:</strong> <span>{int(total_2023['Total Savings (kWh)']):,} kWh</span></p>
                        <p style="background-color: #ff9800; border-radius: 100px; border: 2px solid #ddd; padding: 2px; text-align: center; font-size: 30px;"><strong>Savings Percentage:</strong> <span>{total_2023['Savings Percentage (%)']:.2f}%</span> {get_arrow(total_2023['Savings Percentage (%)'])}</p>
                    </div>
                    <!-- 2024 Summary -->
                    <div style="width: 45%;">
                        <h4 style="color: #4caf50; text-align: center; font-size: 30px;">📅 2024</h4>
                        <p style="text-align: center; font-size: 18px;"><strong>Total Baseline:</strong> <span>{int(total_2024['Total Baseline (kWh)']):,} kWh</span></p>
                        <p style="text-align: center; font-size: 18px;"><strong>Total Realization:</strong> <span>{int(total_2024['Total Realization (kWh)']):,} kWh</span></p>
                        <p style="text-align: center; font-size: 18px;"><strong>Total Savings:</strong> <span>{int(total_2024['Total Savings (kWh)']):,} kWh</span></p>
                        <p style="background-color: #4caf50; border-radius: 100px; border: 2px solid #ddd; padding: 2px; text-align: center; font-size: 30px;"><strong>Savings Percentage:</strong> <span>{total_2024['Savings Percentage (%)']:.2f}%</span> {get_arrow(total_2024['Savings Percentage (%)'])}</p>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Note for 2024 data -->
            <div style="text-align: center; font-size: 16px; color: white; margin-top: 10px;">
                <em>Note: Data 2024 baru sampai bulan Agustus</em>
            </div>
        """, unsafe_allow_html=True)
       
            
    # Check and clean data for 2023
    if all(col in df.columns for col in column_2023):
        summary_2023 = df[column_2023].copy()
        summary_2023.columns = ['Month', 'Realization (kWh)', 'Baseline (kWh)', 'Efficiency (kWh)', 'Efficiency Percentage 2023']
        summary_2023['Baseline (kWh)'] = clean_numeric_column(summary_2023['Baseline (kWh)'])
        summary_2023['Realization (kWh)'] = clean_numeric_column(summary_2023['Realization (kWh)'])
        summary_2023['Efficiency (kWh)'] = clean_numeric_column(summary_2023['Efficiency (kWh)'])
        summary_2023['Efficiency Percentage 2023'] = clean_percentage_column(summary_2023['Efficiency Percentage 2023'])
    else:
        st.error("⚠️ Some columns for 2023 data are missing or misnamed.")

    # Check and clean data for 2024
    if all(col in df.columns for col in column_2024):
        summary_2024 = df[column_2024].copy()
        summary_2024.columns = ['Month', 'Realization (kWh) 2024', 'Baseline (kWh) 2024', 'Efficiency (kWh) 2024', 'Efficiency Percentage 2024']
        summary_2024['Baseline (kWh) 2024'] = clean_numeric_column(summary_2024['Baseline (kWh) 2024'])
        summary_2024['Realization (kWh) 2024'] = clean_numeric_column(summary_2024['Realization (kWh) 2024'])
        summary_2024['Efficiency (kWh) 2024'] = clean_numeric_column(summary_2024['Efficiency (kWh) 2024'])
        summary_2024['Efficiency Percentage 2024'] = clean_percentage_column(summary_2024['Efficiency Percentage 2024'])
    else:
        st.error("⚠️ Some columns for 2024 data are missing or misnamed.")

    # Display side-by-side graphs for 2023 and 2024
    if 'summary_2023' in locals() and 'summary_2024' in locals():
        display_side_by_side_charts(summary_2023, summary_2024, 2023, 2024, 'Baseline (kWh)', 'Realization (kWh)', 'Efficiency (kWh)', 'Baseline (kWh) 2024', 'Realization (kWh) 2024', 'Efficiency (kWh) 2024')

    # Display combined summary table for 2023 and 2024
    if 'summary_2023' in locals() and 'summary_2024' in locals():
        display_combined_summary_table(summary_2023, summary_2024)
    
    # Menambahkan gambar atau logo pada sidebar
    st.sidebar.image('MRT_Jakarta_logo.png', use_column_width=100)
    
    # Sidebar for filters 
    st.sidebar.header("Choose Your Summary Report by Month:")

    # Filter for Month - Only keep entries containing valid month names
    valid_months = [
        month for month in df["Bulan"].unique() 
        if isinstance(month, str) and any(sub in month.upper() for sub in [
            'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'
        ])
    ]

    # Add the multiselect option with filtered valid months
    month = st.sidebar.multiselect("Pick your month", valid_months)

   
    # Menampilkan judul dan deskripsi dengan satu latar belakang transparan
    st.markdown("""
        <div style='background-color: rgba(0, 0, 0, 0.3); padding: 20px; border-radius: 10px;'>
            <h1 style='text-align: center; font-size: 50px; color: white;'>ENERGY USAGE GRAPHIC per MONTH</h1>
            <p style='text-align: center; font-size: 18px; color: white;'>The graphical report provides an overview of monthly energy consumption for various locations, with a comparison of consumption with baseline data for 2023 and 2024. To select the months to be displayed, the user may choose the "Select Summary Report by Month" sidebar.</p>
        </div>
        """, unsafe_allow_html=True)

    # Apply filters only if selected, otherwise use the full dataset
    filtered_df = df.copy()
  
    if month:
       filtered_df = filtered_df[filtered_df["Bulan"].isin(month)]
                                 
    # Grouping data for visualization (Summary if no filter is selected)
    pemakaian_df = filtered_df.groupby(by=["LOCATION"], as_index=False)[["Pemakaian", "Baseline"]].sum()
    used_df = filtered_df.groupby(by=["Area"], as_index=False)[["REAL", "BATAS"]].sum()

    # Creating layout with two columns
    col1, col2 = st.columns(2)

    # Set a single color for both charts
    main_color = 'blue'
    baseline_color = 'darkorange'
    
    # Energy consumption in station 2023
    with col1:
        st.markdown("<h2 style='text-align: center;'>MONTHLY ENERGY CONSUMPTION IN 2023</h2>", unsafe_allow_html=True)
        # Convert data to numeric and clean it
        pemakaian_df["Pemakaian"] = pd.to_numeric(
            pemakaian_df["Pemakaian"].astype(str).str.replace(',', '', regex=False), 
            errors='coerce'
        )
        pemakaian_df["Baseline"] = pd.to_numeric(
            pemakaian_df["Baseline"].astype(str).str.replace(',', '', regex=False), 
            errors='coerce'
        )
        # Melt the DataFrame for grouped bar chart
        df_long = pd.melt(pemakaian_df, id_vars=["LOCATION"], value_vars=["Pemakaian", "Baseline"], 
                          var_name="Legends", value_name="Value")

        # Create grouped bar chart for 2023 data
        fig = go.Figure()

        # Add bars for 'Pemakaian'
        fig.add_trace(go.Bar(
            x=df_long[df_long['Legends'] == 'Pemakaian']['LOCATION'],
            y=df_long[df_long['Legends'] == 'Pemakaian']['Value'],
            name='Pemakaian',          
            marker_color=main_color
        ))

        # Add line for 'Baseline'
        fig.add_trace(go.Scatter(
            x=df_long[df_long['Legends'] == 'Baseline']['LOCATION'],
            y=df_long[df_long['Legends'] == 'Baseline']['Value'],
            name='Baseline',
            mode='lines+markers',
            marker_color=baseline_color,
            line=dict(width=5)
        ))

        # Adjust layout
        fig.update_layout(
            barmode='group',
            height=500, 
            xaxis_title="Location",
            yaxis_title="Value",
            legend_title="Legends",
            plot_bgcolor='rgba(20, 20, 200, 0)',  # Transparent background
            paper_bgcolor='rgba(240, 240, 245, 0.1)', 
        )

        st.plotly_chart(fig, use_container_width=True)

    # Total energy consumption in station 2024
    with col2:
        st.markdown("<h2 style='text-align: center;'>MONTHLY ENERGY CONSUMPTION IN 2024</h2>", unsafe_allow_html=True)

        if "REAL" in used_df.columns and "BATAS" in used_df.columns and "Area" in used_df.columns:
            # Convert 'REAL' and 'BATAS' to numeric
            used_df["REAL"] = pd.to_numeric(
                used_df["REAL"].astype(str).str.replace(',', '', regex=False), 
                errors='coerce'
            )
            used_df["BATAS"] = pd.to_numeric(
                used_df["BATAS"].astype(str).str.replace(',', '', regex=False), 
                errors='coerce'
            )

            # Melt the DataFrame for the 2024 bar chart
            df_long_2024 = pd.melt(used_df, id_vars=["Area"], value_vars=["REAL", "BATAS"], 
                                   var_name="Legends", value_name="Value")

            # Create grouped bar chart for 2024 data
            fig2 = go.Figure()

            # Add bars for 'REAL'
            fig2.add_trace(go.Bar(
                x=df_long_2024[df_long_2024['Legends'] == 'REAL']['Area'],
                y=df_long_2024[df_long_2024['Legends'] == 'REAL']['Value'],
                name='REAL',          
                marker_color=main_color
            ))

            # Add line for 'BATAS'
            fig2.add_trace(go.Scatter(
                x=df_long_2024[df_long_2024['Legends'] == 'BATAS']['Area'],
                y=df_long_2024[df_long_2024['Legends'] == 'BATAS']['Value'],
                name='BATAS',
                mode='lines+markers',
                marker_color=baseline_color,
                line=dict(width=5)
            ))

            # Adjust layout
            fig2.update_layout(
                barmode='group',
                height=500,  # Set to the same height as 2023 chart
                xaxis_title="Area",
                yaxis_title="Value",
                legend_title="Legends",
                plot_bgcolor='rgba(20, 20, 200, 0)',  # Transparent background
                paper_bgcolor='rgba(240, 240, 245, 0.1)',
            )
        
            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.error("The 'REAL', 'BATAS', or 'Area' columns are missing or empty for 2024 data.")

    ## Data viewing and downloading
    cl1, cl2 = st.columns(2)
    with cl1:
        with st.expander("Energy consumption 2023_ViewData"):
            csv = filtered_df.to_csv(index=False).encode('utf-8')
            st.download_button("Download Data", data=csv, file_name="Station 2023_ViewData.csv", mime="text/csv",
                               help='Click here to download the data as a CSV file')
    with cl2:
        with st.expander("Energy consumption 2024_ViewData"):
            csv = filtered_df.to_csv(index=False).encode('utf-8')
            st.download_button("Download Data", data=csv, file_name="Station 2024_ViewData.csv", mime="text/csv",
                               help='Click here to download the data as a CSV file')   
     

    # Optional: Download summaries as CSV files
    if 'summary_2024' in locals():
        csv_2024 = summary_2024.to_csv(index=False).encode('utf-8')
        st.download_button("Download 2024 Summary Data", data=csv_2024, file_name="Summary_2024.csv", mime="text/csv")

    # Data setup
    data = {
        'LOKASI': ['WORKSHOP', 'ADMINISTRATION', 'LEBAK BULUS', 'FATMAWATI', 'CIPETE RAYA', 'HAJI NAWI', 'BLOK A', 'BLOK M', 
                   'ASEAN', 'SENAYAN', 'ISTORA', 'BENDUNGAN HILIR', 'SETIABUDI', 'DUKUH ATAS', 'BUNDARAN HI', 'RSS'],
        'Total Pemakaian 2024': [1089370, 1391680, 472097, 587190, 568535, 306075, 313882, 505624, 500114, 2023519, 
                                 2237369, 2533930, 2266823, 4039365, 3783705, 142820],
        'Total Pemakaian 2023': [1917276, 2041357, 821653, 819435, 568535, 497914, 476775, 692974, 781334, 3081851, 
                                 3509003, 3791445, 3782881, 5767925, 5987235, 220350],
        'Total Baseline 2023': [1911870, 2075025, 816140, 822710, 904105, 520855, 507350, 717955, 811395, 3075855, 
                                 3496335, 3783590, 3761690, 5757145, 5987460, 219365]
    }

    # Convert data to DataFrame
    df = pd.DataFrame(data)

    # Sidebar for filters
    st.sidebar.header("Choose Your Summary Report by Location: ")

    # Filter for Location
    location = st.sidebar.multiselect("Pick the Location", df["LOKASI"].unique())

    # Apply filters if selected
    filtered_df = df.copy()
    if location:
        filtered_df = filtered_df[filtered_df["LOKASI"].isin(location)]

    st.markdown("""
        <div style='background-color: rgba(0, 0, 0, 0.3); padding: 20px; border-radius: 10px;'>
            <h1 style='text-align: center; font-size: 50px; color: white;'>ENERGY USAGE GRAPHIC by LOCATION</h1>
            <p style='text-align: center; font-size: 18px; color: white;'>This graphical report provides an overview of the total energy consumption at various locations, including all MRT stations, workshop areas, administrative buildings, and substation areas. To select the locations to be displayed, users can select the "Select Summary Report by Location" sidebar.</p>
        </div>
        """, unsafe_allow_html=True)

    # Calculate total pemakaian and baseline
    total_pemakaian_2023 = filtered_df['Total Pemakaian 2023'].sum()
    total_pemakaian_2024 = filtered_df['Total Pemakaian 2024'].sum()
    total_baseline_2023 = filtered_df['Total Baseline 2023'].sum()
    # Function to generate styled metric cards
    def metric_card(label, value, background_color):
        st.markdown(f"""
        <div style="
            background-color: {background_color}; 
            padding: 20px; 
            border-radius: 10px; 
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); 
            text-align: center;">
            <h4 style="color: white;">{label}</h4>
            <h2 style="color: white;">{value:,}</h2>
        </div>
        """, unsafe_allow_html=True)

    # Layout for the metrics
    col1, col2, col3 = st.columns([2,2,2])

    # Metric cards with different background colors
    with col1:
        metric_card("Total energy use at the station in 2023 (kWh)", total_pemakaian_2023, "rgba(20, 20, 200, 0.5)")
    with col2:
        metric_card("Total energy use at the station in 2024 (kWh)", total_pemakaian_2024, "rgba(20, 20, 200, 0.5)")
    with col3:
        metric_card("Baseline energy use at station 2023 (kWh)", total_baseline_2023, "rgba(20, 20, 200, 0.5)")

    # Creating the bar chart for energy consumption comparison
    fig = go.Figure()

    # Adding bars for 'Total Pemakaian 2024'
    fig.add_trace(go.Bar(
        x=filtered_df['LOKASI'],
        y=filtered_df['Total Pemakaian 2024'],
        name='Total Pemakaian 2024',
        marker_color='green'
    )) 
    # Adding bars for 'Total Pemakaian 2023'
    fig.add_trace(go.Bar(
        x=filtered_df['LOKASI'],
        y=filtered_df['Total Pemakaian 2023'],
        name='Total Pemakaian 2023',
        marker_color='yellow'
    ))
    # Adding line for 'Total Baseline 2023'
    fig.add_trace(go.Scatter(
        x=filtered_df['LOKASI'],
        y=filtered_df['Total Baseline 2023'],
        name='Total Baseline 2023',
        mode='lines+markers',
        marker_color='orange',
        line=dict(width=8)
    ))

    # Updating layout
    fig.update_layout(
        title="Energy Consumption Comparison 2023 vs 2024 with Baseline",
        xaxis_title="Location",
        yaxis_title="Total Energy (kWh)",
        barmode='group',
        height=600,
        plot_bgcolor='rgba(20, 20, 200, 0.0)',  # Warna latar belakang grafik (transparan)
        paper_bgcolor='rgba(240, 240, 245, 0.1)',
        template="plotly_white"
    )

    # Show the figure using Streamlit
    st.plotly_chart(fig)

    # Download filtered data as CSV
    st.subheader("Download Filtered Data")
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(label="Download CSV", data=csv, file_name="filtered_energy_data.csv", mime="text/csv")

    st.markdown("""
        <div style='background-color: rgba(0, 0, 0, 0.3); padding: 20px; border-radius: 10px;'>
            <h1 style='text-align: center; font-size: 50px; color: white;'>BEST ENERGY EFFICIENCY RANKINGS</h1>
            <p style='text-align: center; font-size: 18px; color: white;'>This graphical report presents information about the station, workshop, and adminsitrative exhibiting the highest efficiency value, expressed as a percentage. This value is derived from the total realization per month in comparison to the baseline per month, and then aggregated to determine the station demonstrating optimal efficiency.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Load the data from 'DATA BASE ENERGI.csv'
    file_path = 'DATA BASE ENERGI.xlsx'
    df = pd.read_excel(file_path)
    
    # Clean up the month data to remove 'NaN' and filter out unwanted months
    df = df[df['BULAN'].notna()]
    
    # Sidebar for filters
    st.sidebar.header("Choose Your Ranking Report by Month : ")
    
    # Filter for Month, including an "All Month" option
    month_options = list(df["BULAN"].unique())
    selected_months = st.sidebar.multiselect(
        "Pick your month", 
        options=month_options, 
        default=None
    )

    # Display "All Month" data if it is selected
    if "All Month" in selected_months:
        filtered_df = df[df['BULAN'] == "All Month"]
        title_months = "All Month"
    elif selected_months:
        filtered_df = df[df['BULAN'].isin(selected_months)]
        title_months = ", ".join(selected_months)
    else:
        filtered_df = df[df['BULAN'] == "All Month"]
        title_months = "All Month"
    
    # Extract required columns for the chart: Location, Efficiency, and Rank
    stations = filtered_df['TEMPAT']
    efficiency = filtered_df['Penghematan']
    rank = filtered_df['RANK']

    # Create a DataFrame for plotting
    plot_df = pd.DataFrame({'TEMPAT': stations, 'Penghematan': efficiency, 'RANK': rank})

    # Sort the data by Efficiency (or by Rank if you prefer)
    plot_df = plot_df.sort_values(by='Penghematan', ascending=False)
    
    # Create a horizontal bar chart using Plotly Express
    fig = px.bar(
        plot_df,
        x='Penghematan',
        y='TEMPAT',
        orientation='h',
        text=plot_df['Penghematan'].apply(lambda x: f"{x:.2f}%"),  # Display percentages with two decimal places
        title=f"Energy Efficiency Ranking - {title_months} 2024",
        color='Penghematan',
        color_continuous_scale=['red', 'orange', 'green', 'blue'],  # Blend of red to blue for negative to positive values
        range_color=(min(plot_df['Penghematan']), max(plot_df['Penghematan']))  # Adjust based on actual data
    )

    # Reverse the order of the y-axis to have the highest at the top
    fig.update_layout(
        title_font_size=22,
        title_x=0.3,
        xaxis_title="Efficiency (%)",
        yaxis=dict(
            showgrid=False,
            title_font=dict(size=20),
            tickfont=dict(size=15),
            categoryorder='total ascending'  # Reverse the y-axis order to display from highest to lowest
        ),
        paper_bgcolor='rgba(240, 240, 245, 0.1)',  # Background similar to previous screenshot
        plot_bgcolor='rgba(20, 20, 200, 0.0)',
        showlegend=False,
        height=600,
        width=800,
        xaxis=dict(showgrid=False, title_font=dict(size=20), tickfont=dict(size=15)),  # Style adjustments for axes 
    )

    # Display the chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)

elif st.session_state['menu_choice'] == 'Report':  
    st.title("Energy Consumption Report")
    st.write("This section will display the detailed report on energy consumption.")
    
    # Function to set a background image from a URL (optional)
    def set_background_image(url):
        page_bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] > .main {{
        background-image: url("{url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        }}
        
        [data-testid="stAppViewContainer"]::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(20, 10, 150, 0.3); /* White overlay with 70% opacity */
        z-index: 1;
        }}

        .main > div {{
        position: relative;
        z-index: 2; /* Ensure content stays above the overlay */
        }}

        [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
        }}
  
        [data-testid="stToolbar"] {{
        right: 2rem;
        }}
        </style>
        """
        st.markdown(page_bg_img, unsafe_allow_html=True)
        
    # Setting one of the Unsplash images as the background
    set_background_image("https://images.unsplash.com/photo-1672023726121-25ba224e82f1?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")

    # Fungsi untuk menambahkan CSS agar background dan highlight lebih menarik
    def apply_custom_style():
        st.markdown(
            """
            <style>
            .custom-box {
                background-color: rgba(0, 110, 250, 0.8); /* Latar belakang biru muda dengan transparansi */
                padding: 15px;
                border-radius: 12px;
                box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.3);
                margin: 10px;
                transition: transform 0.2s;
            }
            .custom-box:hover {
                transform: scale(1.02);
                box-shadow: 6px 6px 20px rgba(0, 0, 0, 0.4);
            }
            .highlight {
                color: #FFD700; /* Warna highlight kuning emas */
                font-weight: bold;
            }
            </style>
            """, unsafe_allow_html=True
        )

    # Memanggil fungsi custom style
    apply_custom_style()

    col1 = st.columns(1)[0]

    with col1:
        st.markdown("""
        <div class="custom-box">
            <h2>Faktor-Faktor Besarnya Penggunaan Energi (Bulan September)</h2>
            <p>Berikut merupakan faktor-faktor penyebab besarnya penggunaan energi (bulan September):</p>
            <ul>
                <li><strong>Lebak Bulus (LBB):</strong> 
                    <ul>
                        <li>Pemasangan lampu penerangan jalan di bawah stasiun</li>
                        <li>Beberapa tenant belum memiliki meteran kWh</li>
                        <li>Pemakaian ruang meeting yang padat pada bulan September</li>
                    </ul>
                </li>
                <li><strong>Fatmawati:</strong> 
                    <ul>
                        <li>Sudah dilakukan optimisasi untuk pengurangan energi hingga 5000 kWh, namun masih ada kenaikan konsumsi</li>
                    </ul>
                </li>
                <li><strong>Cipete Raya:</strong> 
                    <ul>
                        <li>Pemasangan tenant baru pada 23 September 2024</li>
                        <li>Ruang meeting dengan pemakaian yang cukup padat</li>
                    </ul>
                </li>   
                <li><strong>Blok M:</strong> 
                    <ul>
                        <li>Kenaikan ridership sebesar 14%</li>
                        <li>Pemakaian ruang meeting yang padat</li>
                        <li>Penggunaan lift untuk tujuan yang tidak sepenuhnya terkait penumpang</li>
                        <li>Penambahan tenant baru untuk vending machine Azharine</li>
                    </ul>
                </li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Define a three-column layout for the other sections 
    col2, col3 = st.columns([2,1])

    with col2:
        st.markdown("""
        <div class="custom-box">
            <h2>Analisis: Baseline vs. Realisasi</h2>
            <ul>
                <li><span class="highlight">Mengapa ada selisih yang jauh?</span> Lonjakan permintaan yang tidak terduga, penjadwalan yang tidak efisien, perawatan peralatan yang tidak terencana bisa menjadi penyebab deviasi.</li>
                <li><span class="highlight">Apa alasan Realisasi Melebihi Baseline?</span> Bisa disebabkan oleh variasi musiman, perubahan operasional, atau ketidakefisienan peralatan.</li>
            <p>Mengapa realisasi melebihi baseline yang ditetapkan?</p>
            <ul>
                <li><span class="highlight">Peningkatan Permintaan Penumpang</span>: Jumlah penumpang yang lebih tinggi dari perkiraan sering kali menyebabkan peningkatan frekuensi kereta dan penggunaan energi.</li>
                <li><span class="highlight">Operasi Pemeliharaan</span>: Pemeliharaan darurat atau pengujian peralatan di luar jadwal reguler dapat menambah konsumsi energi.</li>
                <li><span class="highlight">Perubahan Musim</span>: Variasi suhu dapat menyebabkan peningkatan penggunaan sistem pemanas atau pendingin.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="custom-box">
            <h2>Temuan Penggunaan Energi yang Berlebih</h2>
            <p>Berdasarkan analisis data, beberapa temuan utama yang diidentifikasi adalah:</p>
            <ul>
                <li><span class="highlight">Waktu Penggunaan Puncak</span>: Waktu-waktu tertentu, seperti jam sibuk pagi dan sore hari, mengalami lonjakan konsumsi energi.</li>
                <li><span class="highlight">Ketidakefisienan Sistem</span>: Sistem lama seperti HVAC dan penerangan mengonsumsi lebih banyak energi dari yang direncanakan.</li>
                <li><span class="highlight">Penggunaan Energi Saat Idle</span>: Penggunaan energi di luar jam operasional menunjukkan adanya peluang untuk meningkatkan prosedur penutupan.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    col4 = st.columns(1)[0]
    with col4:
        st.markdown("""
        <div class="custom-box">
            <h2>Masalah dan Solusi</h2>
            <p>Untuk mengatasi tantangan yang teridentifikasi, beberapa solusi berikut dapat diterapkan:</p>
            <ul>
                <li><span class="highlight">Optimalkan Jadwal Operasional</span>: Penyesuaian jadwal kereta agar lebih sesuai dengan permintaan penumpang dapat mengurangi pemborosan energi.</li>
                <li><span class="highlight">Upgrade Peralatan</span>: Mengganti sistem yang sudah usang dengan alternatif yang lebih efisien energi dapat menurunkan konsumsi secara keseluruhan.</li>
                <li><span class="highlight">Terapkan Protokol Hemat Energi</span>: Menerapkan prosedur operasi standar untuk mematikan sistem yang tidak esensial saat waktu idle dapat membantu.</li>
                <li><span class="highlight">Pemantauan dan Pemeliharaan Prediktif</span>: Menggunakan pemantauan lanjutan untuk memprediksi kegagalan peralatan sebelum terjadi dapat membantu menjaga efisiensi dan keandalan sistem energi.</li>
            </ul>
        </div> 
        """, unsafe_allow_html=True)
          
