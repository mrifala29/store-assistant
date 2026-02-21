# Store Assistant AI (SAI)

**Store Assistant AI (SAI)** adalah proyek riset dan pengembangan untuk membangun chatbot AI modular yang membantu bisnis retail—terutama toko second-hand—dalam menangani layanan pelanggan, konsultasi produk, rekomendasi, serta analitik berbasis percakapan.

SAI **bukan** platform e-commerce end-to-end. Sistem ini dirancang sebagai AI assistant yang dapat diintegrasikan ke website maupun WhatsApp untuk meningkatkan efisiensi operasional dan kualitas layanan.

---

## 🎯 Vision

Membangun AI Store Assistant yang mampu:

- Menjawab pertanyaan pelanggan secara otomatis dan akurat  
- Mendukung proses jual-beli melalui percakapan  
- Menghasilkan insight bisnis dari interaksi pelanggan  
- Terintegrasi dengan website dan WhatsApp  
- Berkembang menjadi platform SaaS di masa mendatang  

---

## 🧠 Core Concept

SAI dibangun dengan arsitektur modular berbasis:

- **FastAPI** — backend API  
- **LangChain** — orkestrasi LLM  
- **Supabase** — database & storage  
- **RAG (Retrieval-Augmented Generation)**  
- **Structured Query + AI Response Generation**

### Alur Utama

Pendekatan ini memungkinkan respons yang kontekstual, terstruktur, dan dapat diaudit.

---

# 👤 User Features

SAI dirancang untuk menangani kebutuhan pelanggan berikut:

## 1. Cek Stok
- Menyediakan informasi ketersediaan barang  
- Menampilkan detail harga dan kondisi produk  

## 2. Konsultasi Produk
- Rekomendasi berdasarkan kebutuhan pengguna  
- Rekomendasi berdasarkan rentang anggaran  

## 3. Penanganan Komplain
- Mencatat komplain pelanggan  
- Menyimpan data ke database untuk evaluasi layanan  

## 4. Buyback Estimator
- Memberikan estimasi harga jika pelanggan ingin menjual barang  
- Mendukung proses akuisisi inventory  

## 5. Generate Nota
- Membuat invoice sederhana  
- Mencatat transaksi secara otomatis  

## 6. Rekomendasi Produk
- Berdasarkan histori percakapan  
- Berdasarkan ketersediaan stok  

## 7. Estimasi Berdasarkan Rentang Harga
Contoh: *“Laptop 5–6 juta dapat apa?”*  
SAI akan memberikan opsi produk yang relevan dengan budget pengguna.

---

# 🛠 Admin Features

## 1. Pencatatan Otomatis Barang Masuk
- Mencatat pembelian barang dari pelanggan  
- Otomatis menambahkan ke inventory  

## 2. Dashboard Analitik
- Total omzet  
- Total barang masuk dan keluar  
- Filter berdasarkan rentang waktu  

## 3. Rangkuman Pertanyaan User
- Identifikasi pertanyaan yang paling sering muncul  
- Insight produk yang paling diminati  

## 4. Rekomendasi Pola Tahunan
- Rekomendasi waktu optimal untuk restock  
- Analisis tren kenaikan/penurunan harga  
- Berdasarkan histori penjualan  

## 5. Intent Analytics
Analisis distribusi intent pengguna, seperti:

- Tanya stok  
- Konsultasi produk  
- Komplain  
- Penjualan barang ke toko  

---

## 🚧 Status

Proyek ini masih dalam tahap **aktif pengembangan (R&D)** dan akan terus berkembang seiring validasi kebutuhan bisnis dan umpan balik pengguna.