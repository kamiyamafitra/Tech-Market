import streamlit as st

# Inisialisasi session state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Fungsi untuk navigasi
def switch_page(page_name):
    st.session_state.page = page_name

# Sidebar atau navigasi
st.sidebar.title("Menu")
if st.sidebar.button("Home", use_container_width=True):
    switch_page("Home")
if st.sidebar.button("Motherboard 😃", use_container_width=True):
    switch_page("Motherboard")
if st.sidebar.button("CPU 😎", use_container_width=True):
    switch_page("CPU")
if st.sidebar.button("GPU 💀", use_container_width=True):
    switch_page("GPU")
if st.sidebar.button("SSD 🧐", use_container_width=True):
    switch_page("SSD")
if st.sidebar.button("RAM 🙂", use_container_width=True):
    switch_page("RAM")
if st.sidebar.button("PSU ⚡", use_container_width=True):
    switch_page("PSU")
if st.sidebar.button("Casing 🤔", use_container_width=True):
    switch_page("Casing")


# Menampilkan konten berdasarkan halaman
if st.session_state.page == "Home":
    st.title("Selamat datang di Merapi")
    st.subheader("(Mending Rakit PC)")
    st.write("**Solusi Lengkap untuk Merakit dan Meng-upgrade PC Impian Anda, Tanpa Ribet.**")
    st.write("Salah satu alasan utama mengapa merakit PC adalah pilihan terbaik untuk jangka panjang adalah kemudahannya untuk di-upgrade sesuai kebutuhan di masa depan.")
    st.write("Dengan merakit PC, Anda dapat memilih komponen berkualitas yang sesuai dengan kebutuhan saat ini, seperti motherboard dengan dukungan prosesor dan RAM terbaru. Ketika kebutuhan meningkat, seperti untuk gaming, pekerjaan kreatif, atau tugas berat lainnya, Anda cukup mengganti atau menambahkan komponen tertentu tanpa harus membeli PC baru secara keseluruhan. Hal ini tidak hanya menghemat biaya, tetapi juga memastikan performa PC Anda selalu optimal seiring perkembangan teknologi.")
    st.subheader("Gunakan menu dibagian kiri untuk Menjelajahi lebih banyak produk lainnya.")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Cpu")
        st.image("Zaki/kumpulan gambar/53bc3a1d-cf61-41d7-91f4-2124dbde60d9.jpg", caption="Intel core i9 14900K Box")
    
    with col2:
        st.header("Gpu")
        st.image("Zaki/kumpulan gambar/d909e419-85d0-476f-995d-4e2476f310c8.jpg", caption="MSI GeForce RTX 4090 GAMING X TRIO 24GB GDDR6X")

    with col3:
        st.header("Casing")
        st.image("Zaki/kumpulan gambar/b70fc2df-20f4-4626-ad91-1de714210895.jpg", caption="TECWARE FLATLINE TG MK2")
    




elif st.session_state.page == "Motherboard":
    st.title("Motherboard")
    st.write("Motherboard adalah komponen utama dalam sebuah PC yang berfungsi sebagai papan sirkuit utama tempat semua komponen lain saling terhubung dan berkomunikasi. Bisa dibilang, motherboard adalah tulang\
             punggung dari sebuah komputer karena tanpa itu, komponen lain seperti prosesor, RAM, kartu grafis, dan penyimpanan tidak dapat berfungsi bersama.")
    
    col4, col5, col6, col7 = st.columns(4)
    with col4:
        st.subheader("Mobo 1")
        st.image("zaki/kumpulan gambar/13757756_509be07d-f324-4df7-832e-e3b0d0009bcd_600_600.jpg", caption="ASROCK B550M PRO4")
        with st.popover("Press"):
            st.markdown("**Rp. 1.548.000**")
            st.markdown("Supports 3rd Gen AMD AM4 Ryzen™ / Future AMD Ryzen™\
                        Processors 8 Power Phase Design, Digi Power\
                        Supports DDR4 4733+ (OC)\
                        1 PCIe 4.0 x16, 1 PCIe 3.0 x16, 1 PCIe 3.0 x1, 1 M.2 Key E for WiFi\
                        Graphics Output Options: HDMI, DisplayPort, D-Sub\
                        AMD CrossFireX™\
                        7.1 CH HD Audio (Realtek ALC1200 Audio Codec), Nahimic Audio\
                        6 SATA3, 1 Hyper M.2 (PCIe Gen4 x4), 1 M.2 (PCIe Gen3 x2 & SATA3)\
                        2 USB 3.2 Gen2 (Rear Type A+C), 8 USB 3.2 Gen1 (4 Front, 4 Rear)\
                        Realtek Gigabit LAN")
            st.button("Order now")
            col4 = 1548000 # Harganya
    
    with col5:
        st.subheader("Mobo 2")
        st.image("zaki/kumpulan gambar/20221111162833.jpg", caption="SROCK MOTHERBOARD B560M HDV M.2 R2.0 (INTEL)")
        with st.popover("Press"):
            st.markdown("**Rp. 1.250.000**")
            st.markdown("Supports 10th Gen Intel® Core™ Processors and 11th Gen Intel® Core™ Processors (LGA1200)\
                        6 Power Phase design\
                        Supports Intel® Turbo Boost Max 3.0 Technology\
                        Intel® B560\
                        2 x DDR4 DIMM Slots\
                        10th Gen Intel® Core™ Processors support DDR4 non-ECC, un-buffered memory up to 4600+(OC)*\
                        Supports ECC UDIMM memory modules (operate in non-ECC mode)\
                        Max. capacity of system memory: 64GB**\
                        Supports Intel® Extreme Memory Profile (XMP) 2.0\
                        7.1 CH HD Audio (Realtek ALC897 Audio Codec)\
                        Giga PHY Intel® I219V\
                        11th Gen Intel® Core™ Processors -1 x PCI Express 4.0 x16 Slot* 10th Gen Intel® Core™ Processors - 1 x PCI Express 3.0 x16 Slot* - 2 x PCI Express 3.0 x1 Slots\
                        4 x SATA3 6.0 Gb/s Connectors, support Intel® Rapid Storage Technology 18, NCQ, AHCI and Hot Plug\
                        1 x Hyper M.2 Socket (M2_1), supports M Key type 2260/2280 M.2 PCI Express module up to Gen4x4 (64 Gb/s) (Socket M2_1 works with 11th Gen Intel® Core™ processors only)*\
                        1 x Ultra M.2 Socket (M2_2), supports M Key type 2260/2280 M.2 SATA3 6.0 Gb/s module and M.2 PCI Express module up to Gen3 x4 (32 Gb/s)*\
                        Micro ATX Form Factor: 9.6-in x 7.8-in, 24.4 cm x 19.8 cm ")
            st.button("Order Now")




elif st.session_state.page == "CPU":
    st.title("CPU")
    st.write("Ini adalah halaman informasi CPU.")




elif st.session_state.page == "GPU":
    st.title("GPU")
    st.write("ini adalah halaman informasi GPU")




elif st.session_state.page == "SSD":
    st.title("SSD")
    st.write("ini adalah halaman informasi SSD")




elif st.session_state.page == "RAM":
    st.title("RAM")
    st.write("ini adalah halaman informasi RAM")




elif st.session_state.page == "PSU":
    st.title("PSU")
    st.write("ini adalah halaman informasi PSU")




elif st.session_state.page == "Casing":
    st.title("Casing")
    st.write("ini adalah halaman informasi Casing")