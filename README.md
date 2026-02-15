# Store Assistant AI (SAI)

Store Assistant AI (SAI) adalah proyek R&D untuk membangun chatbot AI modular yang dapat membantu bisnis retail / second-hand dalam menangani customer service, konsultasi, rekomendasi, analitik, dan insight bisnis.

Proyek ini bukan sistem e-commerce penuh.  
SAI dirancang sebagai AI assistant yang dapat diintegrasikan ke website atau WhatsApp.

---

## 🎯 Vision

Membangun AI Store Assistant yang:

- Bisa menjawab seluruh pertanyaan pelanggan
- Membantu proses jual-beli
- Memberikan insight bisnis dari percakapan pelanggan
- Bisa diintegrasikan ke website dan WhatsApp
- Berkembang menjadi SaaS di masa depan

---

## 🧠 Core Concept

SAI menggunakan pendekatan:

- FastAPI (API backend)
- LangChain (LLM orchestration)
- Supabase (database)
- RAG (Retrieval Augmented Generation)
- Structured Query + AI Response Generation

Flow utama:

User → FastAPI → LangChain Agent → Retrieval (Supabase) → LLM → Response

---

# 👤 USER FEATURES

SAI harus mampu menangani:

### 1. Cek Stok
- Menjawab ketersediaan barang
- Memberikan detail harga & kondisi

### 2. Konsultasi Produk
- Rekomendasi berdasarkan kebutuhan
- Rekomendasi berdasarkan budget

### 3. Komplain
- Mencatat komplain pelanggan
- Menyimpan ke database untuk evaluasi

### 4. Rentang Harga Jual (Buyback Estimator)
- Memberikan estimasi harga jika user ingin menjual barang

### 5. Generate Nota
- Membuat invoice sederhana
- Mencatat transaksi

### 6. Rekomendasi Produk
- Berdasarkan histori percakapan
- Berdasarkan stok tersedia

### 7. Menjawab Rentang Harga Barang
- Contoh: “Laptop 5–6 juta dapat apa?”

---

# 🛠 ADMIN FEATURES

### 1. Pencatatan Otomatis Barang Masuk
- Jika membeli barang dari user
- Tercatat sebagai inventory

### 2. Dashboard Analitik
- Total omset
- Total barang masuk / keluar
- Rentang waktu tertentu

### 3. Rangkuman Pertanyaan User
- Ringkasan pertanyaan terbanyak
- Insight produk yang paling sering ditanyakan

### 4. Rekomendasi Pola Tahunan
- Kapan harus stok barang tertentu
- Kapan harga naik / turun
- Berdasarkan histori penjualan

### 5. Intent Analytics
- Persentase user:
  - Tanya stok
  - Konsultasi
  - Komplain
  - Mau jual barang

---

# 🏗 Project Structure

