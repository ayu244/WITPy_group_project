
import streamlit as st
import os
import time
from PIL import Image


path = os.path.dirname(__file__)

img_carding = path+'/Carding.jpg'
img_hacking = path+'/Hacking.jpg'
img_cracking = path+'/cracking.jpg'
img_phising = path+'/phising.jpg'
img_spamming = path+'/spamming.png'
img_malware = path+'/malware.png'

st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Jenis-jenis Cybercrime ❄️")

st.title("Menjaga Privasi Online")

st.header("Jenis-jenis Cyber Crime")

st.subheader("1. Carding")


image_carding = Image.open(img_carding)

st.image(image_carding, caption='Carding', width=600)

st.write("Merupakan tindakan ilegal yang melakukan aktivitas berbelanja dengan menggunakan nomor dan identitas kartu kredit orang lain yang diperoleh secara ilegal. Carding adalah suatu motif pembobolan (theft) serta kecurangan (fraud) di ruang dunia maya yang dilakukan oleh carder.")
st.write("Contoh asus:")
st.write("Boy William Jadi Saksi Kasus Carding, Dicecar 30 Pertanyaan hingga Akui Terima Endorse")
st.write("Kasus tiket kekiniaan ini dilakukan oleh carder atau pelaku dengan membeli data kartu kredit lewat Facebook senilai Rp 150 ribu - Rp 300 ribu per CC, database ini didapatkan dari kebocoran data perbankan, marketplace dan paling sering pada saat transaksi di kasir. Kemudian pelaku menambahkan mesin skimmer pada saat proses pembayaran di EDC tanpa diketahui pihak lain dan melakukan copy data dan mencetak CC kloning atau secara manual dengan mencatat data nomor, nama dan tanggal berlaku kartu kredit plus 3 digit CVV di belakang kartu. Dengan data yang didapat para carder dapat melakukan transaksi di berbagai marketplace.")
st.write("Solusi:")
st.write("- Perhatikan cara menggesek kartu saat transaksi;")
st.write("- Pilih situs belanja online terpercaya;")
st.write("- Rahasiakan data pribadi atau kartu kredit; dan")
st.write("- Gunakan internet pribadi.")

st.subheader("2. Hacking")

image_hacking = Image.open(img_hacking)

st.image(image_hacking, caption='Hacking', width=600)

st.write("Merupakan kegiatan penerobosan program komputer milik orang lain.")
st.write("Contoh kasus:")
st.write("Kasus cyber crime hacker pernah terjadi di Sleman, Daerah Istimewa Yogyakarta 2019. Kasus tersebut melibatkan hacker berinisial BBA (21) yang ditangkap karena meretas server sebuah perusahaan di San Antonio, Texas, Amerika Serikat. Pelaku melakukan tindak pidana hacking dengan modus ransomware. Tersangka ini menyebarkan atau mengirimkan email ke korban, berisi link atau tautan, di mana ketika korban mengklik link itu, akan menyebabkan server komputer mati. Setelah server komputer sasarannya mati, pelaku kemudian meminta uang tebusan dalam bentuk mata uang cryptocurrency bitcoin sebagai syarat untuk mengembalikan fungsi sistem. Dalam beraksi, BBA bisa memeras hingga 300 bitcoin. Satu bitcoin itu kalau ditukar nilainya sekitar Rp 150 juta. Dalam aksinya, dia mengirimkan tautan email http://ddiam.com/shipping200037315.pdf.exe ke salah satu satu karyawan di perusahaan tersebut. Link tersebut mengarahkan pengguna ke link lain berisikan cryptolocker.")
st.write("Solusi:")
st.write("- Perbaharui selalu perangkat lunak dan aplikasi;")
st.write("- Gunakan alat berbasis cloud; dan")
st.write('- Buat kata sandi biometrik atau kode akses yang rumit.')

st.subheader("3. Cracking")

image_cracking = Image.open(img_cracking)

st.image(image_cracking, caption='Cracking', width=600)

st.write('Merupakan hacking untuk tujuan yang jahat, sebutan ini diberi untuk cracker yaitu hacker bertopi hitam _(black hat hacker)_.')
st.write('Contoh kasus:')
st.write('Dua Warga Indonesia Berhasil Bobol Kartu Kredit Via Online Polda Metro Jaya melalui Kasat Cyber Crime Ajun Komisaris Besar Winston Tommy Watuliu berhasil meringkus dua pelaku kejahatan cyber crime. Kasus mereka yaitu membobol kartu kredit secara online milik perusahaan di luar negeri. Kedua Cracker ini bernama Adi dan Ari mereka berhasil menerobos sistem perbankan perusahaan asing, seperti Capital One USA, Cash Bank USA dan GT Morgan Bank USA kemudian membobol kartu kredit milik perusahaan ternama tersebut. Setelah berhasil kedua pelaku tersebut menggunakan kartu kreditnya untuk membeli tiket pesawat Air Asia lalu tiket tersebut dijual pelaku dengan harga yang sangat murah. Tidak tanggung-tanggung untuk menarik pembeli mereka sengaja memasang iklan seperti di situs weeding.com dan kaskus. Dan hebatnya lagi dari pengakuan kedua cracker tersebut mereka mempelajari teknik bobol credit card ini secara otodidak. Tapi sepandai-pandai tupai melompat akhirnya jatuh juga, begitulah kisah dua cracker tanah air kita, setelah berhasil membobol kartu kredit dari Ricop yaitu perusahaan yang memproduksi anggur di San Francisco mereka berhasil ditangkap oleh Polda Metro Jaya ditempat terpisah, di Jakarta dan Malang. Dari tangan mereka berhasil diamankan barang bukti seperti laptop, dua BlackBerry, modem, komputer, buku tabungan BCA dan daftar perusahaan yang akan menjadi target pembobolan.')
st.write('Solusi')
st.write('- Gunakan Password unik untuk setiap website;')
st.write('- Hindari jaringan wifi publik;')
st.write('- Gunakan VPN;')
st.write('- Ubah informasi login router;')
st.write('- Jangan klik iklan di internet; dan')
st.write('- Kunjungi situs dengan _https_.')

st.subheader('4. Phising')

image_phising = Image.open(img_phising)

st.image(image_phising, caption='Phising', width=600)

st.write('Merupakan kegiatan memancing pemakai komputer di internet agar mau memberikan informasi pribadi pada suatu website yang sudah di deface.')
st.write('Contoh kasus:')
st.write('Para pengguna kredivo menjadi korban phising adalah contoh penyalahgunaan data pribadi. Korban di hubungi oleh para hacker dengan berdalih memberikan promo, bonus, atau hadiah.')
st.write('Solusi:')
st.write('Akses platform terkait apabila Anda dihubungi dari lembaga atau platform digital tertentu yang mencurigakan dan segera lakukan penggantian password.')

st.subheader('5. Spamming')

image_spamming = Image.open(img_spamming)

st.image(image_spamming, caption='Spamming', width=600)

st.write('Merupakan tindakan pengiriman berita atau iklan  melalui surat elektronik (email) yang tidak dikehendaki. Bentuk spam email ini adalah mengirimkan surat elektronik komersial secara massal yang tidak diminta oleh si penerima email. Pengiriman spam email ini bisa dilakukan melalui _jaringan zombie_ jaringan virus yang telah menginfeksi komputer pribadi maupun kantor di seluruh dunia.')
st.write('Solusi:')
st.write('- Jangan membalas email orang yang tidak dikenal;')
st.write('- Jangan memamerkan email pribadi di blog/website/sosial media')
st.write('- Buatlah email lebih dari satu;')
st.write('- Gunakan software anti spam;')
st.write('- Aktifkan fitur anti spam di email anda; dan')
st.write('- Gunakan _at_ saat melampirkan email di website.')

st.subheader('6. Malware')

image_malware = Image.open(img_malware)

st.image(image_malware, caption='Malware', width=600)

st.write('Merupakan program komputer yang mencari kelemahan dari suatu software.')
st.write('Contoh kasus:')
st.write('Contoh kasus serangan malware paling merusak dan mematikan pertama adalah serangan spyware bernama WannaCry pada tahun 2017. Spyware ini menyerang rumah sakit dan banyak pabrik seluruh dunia. Serangan WannaCry juga sangat massif. Dalam empat hari penyebaran serangan WannaCry telah melumpuhkan lebih dari 200 ribu komputer di 150 negara, termasuk perusahaan pesawat yaitu Boeing. Jika ditotal kerugian gara-gara ransomware WannaCry sendiri berkisar antara USD$ 4-8 miliar atau Rp 112,9 miliar. Ada tanda-tanda khusus sebuah komputer telah terinfeksi virus ransomware WannaCry. Tanda yang paling kentara adalah munculnya pop-up window yang berisi pesan bahwa data pemilik komputer telah dienkripsi. Untuk membukanya maka pemilik harus membayar tebusan yang ditentukan oleh peretas. Kasus ini pun menjadi perbincangan masyarakat global. Kala itu Amerika Serikat telah menemukan bukti yang dan menunduh jika Korea Utara menjadi dalang dari malware WannaCry. Di Indonesia kasus serangan WannaCry menyerang 2 rumah sakit yakni Rumah Sakit Dharmais dan Rumah Sakit Harapan Kita. Kedua rumah sakit tersebut diserang  WannaCry pada 12 Mei 2017 yang menyebabkan data pasien dalam jaringan komputer rumah sakit tidak bisa diakses.')
st.write('Solusi:')
st.write('- Pastikan Anda memiliki backup data;')
st.write('- Putusakan koneksi internet;')
st.write('- Jalankan mode safe mode;')
st.write('- Hapus temprary files;')
st.write('- Scan perangkat menggunakan anti malware;')
st.write('- Gunakan windows defender; dan')
st.write('- Hapus program yang tidak dikenal.')