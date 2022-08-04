#Library 
import streamlit as st
import os
from PIL import Image

path = os.path.dirname(__file__)

# import modul Image dari Python Imaging Library
img_privasi = path+"/privasi.jpg"
imageprivasi = Image.open(img_privasi)


st.markdown("Cover 🌈")
st.sidebar.markdown(" Pengertian Privasi 🌈")

# Apa yang dimaksud dengan privasi online (Digital)
st.title("Privasi Online (Digital)")
st.image(imageprivasi)
st.write("""
    Privasi merupakan hal penting terkait individu maupun lembaga atau instansi untuk berhadapan dan berinteraksi
    dengan indiviu dan lembaga lain. Privasi itu penting dan mahal sehingga suatu kewajiban untuk menjaga privasi
    dan ditutup rapat, serta tidak boleh setiap orang mengetahuinya. \n
    Pengertian privasi merujuk dari padanan Bahasa Inggris privacy, adalah kemampuan satu atau sekelompok individu
    untuk mempertahankan kehidupan dan urusan personilnya dari publik dan mengontrol arus informasi mengenai diri
    mereka. Di era digital sekarang internet adalah tools penting dalam kehidupan sehari hari. \n
    Berbagai informasi pribadi dikumpulkan dan segala aktivitas yang kita lakukan memiliki jejak digital. Data pribadi
    mencakup identitas data diri, data kesehatan, data pendidikan (formal dan nonformal), data keuangan, dsb.
""")
st.write("""
    Beberapa alasan mengapa data pribadi/ privasi penting untuk dilindungi :
    1. Data adalah aset atau komoditas bernilai tinggi di era big data  dan ekonomi digital.
    2. Data pribadi menyangkut hak asasi dan privasi yang harus dilindungi. Hal ini diatur pada: \n
        a. UU Nomor 12 Tahun 2005 tentang Pengesahan International Covenant on Civil  and Political Rights \n
        b. UU Nomor 36 Tahun 2009 tentang Kesehatan mengatur rahasia kondisi pasien \n
        c. UU Nomor 10 Tahun 1998 tentang Perbankan mengatur data pribadi mengenai nasabah penyimpan dan simpanannya
    """)
