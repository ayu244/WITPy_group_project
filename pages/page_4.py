
import streamlit as st

import os
from PIL import Image

path = os.path.dirname(__file__)

img_hindaricc = path+'/hindaricc.jpg'

st.markdown("# Page 4 🎉")
st.sidebar.markdown("# Page 4 🎉")

st.title('Privasi dalam Sosial Media')

st.header('Tips dan Trik Menjaga Privasi Online')

image_hindaricc = Image.open(img_hindaricc)

st.image(image_hindaricc, caption='Tips dan trik menghindari Cyber Crime')


st.write('Terdapat beberapa tips dan trik yang boleh digunakan untuk menjaga privasi online, diantaranya:')
st.write('1. Jangan gunakan _software_ bajakan;')
st.write('2. Pasang perangkat lunak keamanan yang _up to date_;')
st.write('3. Menggunakan _data encryption_;')
st.write('4. Hapus _temporary file_;')
st.write('5. Scan perangkat menggunakan anti malware;')
st.write('6. Rajin mengganti kata sandi dan gunakan kata sandi yang kuat;')
st.write('7. Backup data-data secara rutin;')
st.write('8. Jangan sembarangan memberi informasi terkait informasi pribadi kepada siapa pun;')
st.write('9. Hindari menggunakan jaringan WIFI asing di tempat umum; dan')
st.write('10. baikan lampiran surat elektronik dan URL yang terindikasi mencurigakan.')