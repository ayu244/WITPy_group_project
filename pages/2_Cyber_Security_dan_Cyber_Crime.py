#Library 
import streamlit as st
import os
from PIL import Image

path = os.path.dirname(__file__)

# import modul Image dari Python Imaging Library
img_imagecybersecurity = path+"/imagecybersecurity.png"
imagecybersecurity = Image.open(img_imagecybersecurity)

img_imagecybercrime = path+"/imagecybercrime.jpg"
imagecybercrime = Image.open(img_imagecybercrime)

img_cia = path+"/cia.png"
imagecia = Image.open(img_cia)

# st.markdown("Page 2 🌺")
# st.sidebar.markdown(" Pengertian Cyber Security dan Cyber Crime 🌺")

# Apa Yang di Maksud dengan Cyber Security dan Cyber Crime
st.title("Cyber Security dan Cyber Crime")
with st.container():
    st.header("Cyber Security")    
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(imagecybersecurity)
    with text_column:
        st.write("""
            Menurut Cisco, Cyber Security adalah praktik melindungi sistem, jaringan, dan program dari serangan digital.
            Cyber Security biasanya ditujukan untuk mengakses, mengubah, atau menghancurkan informasi sensitif, memeras
            uang dari pengguna atau mengganggu operasional proses bisnis. Jadi dapat disimpulkan, Cyber Security adalah
            sebuah proses perlindungan program, data, sistem, maupun jaringan dari serangan digital ataupun akses ilegal.
            """)
    st.write("""
        Cyber security atau keamanan siber merupakan tindakan untuk melindungi informasi di dunia maya dari aneka
        serangan. Cyber security makin populer berhubung makin banyaknya penggunaan komputer seperti desktop, laptop,
        martphone, server, dan perangkat IoT (internet of things) serta penggunaan jaringan komputer seperti internet
        dalam kehidupan umat manusia sehari-hari.
        """)

with st.container():
    st.write("""
        Pada Cyber Security ada 3 konsep cyber security, yang di kenal sebagai CIA Triad, yaitu model keamanan
        yang dikembangkan untuk membantu manusia memikirkan berbagai keamanan teknologi informasi. Unsur-unsur
        ini dianggap yang paling penting diseluruh platform, terumata pada Web App. antara lain :
        """)
    tab1, tab2, tab3 = st.tabs(["Confidentiality", "Intergrity", "Availability"])
    st.image(imagecia)
    with tab1:
        st.header("Confidentiality (Kerahasiaan)")
        st.write("""Artinya keamanan cyber berperan dalam merahasiakan ataupun menyimpan informasi data. Sehingga,
        sistem keamanan ini akan melakukan kontrol terhadap setiap akses data tersebut. Tujuannya untuk mencegah
        terjadinya kebocoran atau pencurian data.""")
        st.caption("""Contoh : Hanya karyawan bagian penggajian yang memiliki akses ke database penggajian perusahaan.
        Karyawan bagian luar itu hanya bisa melihat struktur perusahaan yang berisi nama dan jabatan.""")
    with tab2:
        st.header("Intergrity (Integritas)")
        st.write("""Artinya sistem keamanan cyber memungkinkan setiap orang menyerahkan data secara valid, konsisten,
        dan tepercaya.""")
        st.caption("""Contoh : Kita mempunyai bisnis toko online. Kita harus memberikan informasi produk yang jelas
        dan harga yang akurat. Hal ini membuat pelanggan percaya pada integritas toko online.""")
    with tab3:
        st.header("Availability (Ketersediaan)")
        st.write("""Artinya sistem keamanan juga berkaitan dengan tersedianya suatu aplikasi, sistem, ataupun data
        yang merupakan hak konsumen, dan dapat diakses dengan lancar serta mudah tanpa halangan.""")
        st.caption("""Contoh : Pengguna mobile banking harus melakukan transfer mendadak. Dia akan kecewa ketika
        aplikasi mobile banking tersebut tiba-tiba down. Hal tersebut dapat mengurani kepercayaan pengguna
        kepada bank yang bersangkutan.""")


with st.container():
    st.header("Cyber Crime")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(imagecybercrime)
    with text_column:
        st.write("""Pengertian cyber crime atau kejahatan berbasis komputer, adalah kejahatan yang melibatkan komputer
            dan jaringan (network). Komputer mungkin telah digunakan dalam pelaksanaan kejahatan, atau mungkin itu sasarannya.
            """)
    st.write("""Didefinisikan juga sebagai pelanggaran yang dilakukan terhadap perorangan atau sekelompok individu dengan
        motif kriminal untuk secara sengaja menyakiti reputasi korban atau menyebabkan kerugian fisik atau mental atau
        kerugian kepada korban baik secara langsung maupun tidak (jaringan termasuk namun tidak terbatas pada ruang Chat,
        email, notice boards langsung, menggunakan jaringan telekomunikasi modern seperti Internet dan kelompok) dan
        telepon genggam (Bluetooth / SMS / MMS). Cybercrime dapat mengancam seseorang, keamanan negara atau kesehatan
        finansial.
        """)