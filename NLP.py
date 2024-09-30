# NLP
import re
import string

# Teks yang akan diproses
text = """Universitas Pelita Bangsa, yang terletak di Cikarang, Bekasi, adalah salah satu universitas swasta yang terus berkembang pesat di Indonesia! Kampus ini menawarkan berbagai program studi, mulai dari Teknik Informatika, Manajemen, hingga Ilmu Hukum, yang semuanya dirancang untuk membekali mahasiswa dengan keterampilan yang relevan di dunia kerja. Dengan lokasi strategis di kawasan industri (apakah ini bukan keuntungan besar?), Universitas Pelita Bangsa memiliki banyak keunggulan, termasuk akses mudah ke berbagai perusahaan besar untuk keperluan magang dan kerja sama industri! Visi kampus ini adalah mencetak lulusan yang berdaya saing tinggi melalui pengajaran yang berkualitas dan fasilitas modern (wow!), yang didukung oleh dosen-dosen berpengalaman."""

# Fungsi untuk membersihkan dan memproses teks
def tokenize_text(text):
    # Ubah teks menjadi huruf kecil
    text = text.lower()
    # Hapus tanda baca
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Pisahkan teks menjadi kata-kata
    words = text.split()
    return words

# Proses teks dan ambil hasilnya
tokens = tokenize_text(text)

# Tampilkan hasil
print(f"Ada {len(tokens)} kata.")
for i, word in enumerate(tokens, 1):
    print(f"Kata {i}: {word}")
