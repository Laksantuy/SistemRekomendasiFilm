
# 🎥 Sistem Rekomendasi Film 🎥

Sistem rekomendasi film sederhana berbasis Python yang menggunakan algoritma **K-Nearest Neighbors (KNN)** dengan **Manhattan Distance**.  
Proyek ini membantu pengguna mendapatkan rekomendasi 5 film terbaik berdasarkan input genre, rating, dan durasi yang mereka inginkan.

---

## 🚀 Fitur Utama
- Dataset berisi **50 film populer** dari berbagai genre:  
  ✅ Superhero  
  ✅ Animasi  
  ✅ Romance  
  ✅ Horror  

- Rekomendasi film berdasarkan:  
  ✔️ Genre (dengan bobot lebih tinggi)  
  ✔️ Rating film  
  ✔️ Durasi film  

- Normalisasi data menggunakan **MinMaxScaler** untuk hasil yang lebih akurat.  
- Input yang user-friendly dan validasi input secara otomatis.  
- Output rekomendasi top 5 film dalam format yang menarik di terminal.

---

## 🛠️ Teknologi yang Digunakan
- Python  
- Pandas  
- scikit-learn (NearestNeighbors & MinMaxScaler)

---

## 📊 Contoh Input
```
🎬 Selamat datang dalam Sistem Rekomendasi Film! 🎬
Sebutkan film yang sudah kamu tonton: Avengers Endgame
Genre (Superhero=0, Animasi=1, Romance=2, Horror=3): 0
Rating (1-10): 8.5
Durasi (dalam menit): 140
```

---

## 📚 Contoh Output Rekomendasi
```
🌟 Ini adalah TOP 5 rekomendasi film yang harus kamu tonton! 🌟
=============================================

🎥 Rekomendasi #1:
   Judul: The Avengers
   Genre: Superhero
   Rating: 8.0
   Durasi: 143 minutes

🎥 Rekomendasi #2:
   Judul: Thor: Ragnarok
   Genre: Superhero
   Rating: 7.9
   Durasi: 130 minutes

🎥 Rekomendasi #3:
   Judul: Doctor Strange
   Genre: Superhero
   Rating: 7.5
   Durasi: 115 minutes

🎥 Rekomendasi #4:
   Judul: Iron Man
   Genre: Superhero
   Rating: 7.9
   Durasi: 126 minutes

🎥 Rekomendasi #5:
   Judul: Black Panther
   Genre: Superhero
   Rating: 7.3
   Durasi: 134 minutes

=============================================
Selamat Marathon! 🍿🎉
```

---

## 🤝 Kontribusi
Pull request dan masukan selalu terbuka!  
Jika ingin menambahkan genre baru atau meningkatkan model, feel free to contribute.  

---

## 📩 Kontak
📧 Jika ada pertanyaan atau kolaborasi, hubungi saya melalui email: **[laksanaaura@gmail.com]**  

---

## ⭐ Jangan lupa untuk memberi bintang (⭐) jika kamu suka proyek ini!  
