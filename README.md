### 1. Implementasi Checklist secara Step-by-Step
#### 1.a Membuat proyek Django baru
Langkah awal adalah membuat direktori utama untuk proyek. Kemudian buat virtual environment, dan jalankan perintah berikut untuk memulai proyek:

```bash
django-admin startproject triplr-thrift
```

Ini akan menghasilkan beberapa file dan direktori untuk proyek tersebut.

#### 1.b Membuat aplikasi dengan nama `main`
Pada terminal di direktori utama, jalankan perintah berikut untuk membuat aplikasi baru dengan nama `main`:

```bash
python manage.py startapp main
```

#### 1.c Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`
Buka file `urls.py` di direktori aplikasi, dan definisikan pola URL untuk `view` yang diinginkan. Contoh routing:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_main, name='show_main'),
]
```

#### 1.d Membuat model pada aplikasi `main` dengan nama `Product`
Buka file `models.py` di direktori aplikasi, dan buat model `Product` dengan atribut sebagai berikut:

```python
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    address = models.TextField()
```

#### 1.e Membuat fungsi pada `views.py`
Buka file `views.py`, lalu buat fungsi untuk mengembalikan data ke template HTML:

```python
from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Rak Sepatu Stainless Steel 5 Susun',
        'price': 35000,
        'description': 'Rak sepatu stainless steel 5 susun, minus tingkat ke 3 patah jadi sisa 4 susun, harga beli 99000',
        'address': 'Jl. Masjid Al-Farouq (Kos Pondok Ananda)',
    }
    return render(request, "main.html", context)
```

#### 1.f Membuat routing pada `urls.py` aplikasi `main`
Buka file `urls.py` pada direktori aplikasi, lalu tambahkan path URL untuk memetakan fungsi di `views.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_main, name='show_main'),
]
```

#### 1.g Melakukan deployment ke PWS
Untuk melakukan deployment ke PWS (PythonAnywhere atau platform lain):
1. Buat repository di PWS.
2. Push project yang sudah dikerjakan ke repository tersebut.

---

### 2. Bagan Request Client ke Web Aplikasi Django

Berikut adalah bagan yang menjelaskan alur request dan respon dari client ke aplikasi Django:

![Bagan Request Client](/Bagan.png)

**Penjelasan Alur:**
1. **Client** mengirim request HTTP (misal: `GET /`).
2. **urls.py** memetakan URL request ke fungsi yang ada di `views.py`.
3. **views.py** mengambil data dari **models.py** jika dibutuhkan (misal: `Product`).
4. **views.py** kemudian mengirimkan data tersebut ke berkas **HTML** untuk dirender.
5. **Berkas HTML** dikirim kembali sebagai respon kepada client dalam bentuk halaman web.

---

### 3. Fungsi Git dalam Pengembangan Perangkat Lunak
Git memiliki beberapa fungsi utama, di antaranya:
- **Kontrol Versi**: Melacak perubahan kode dan memungkinkan pengembang mengembalikan versi sebelumnya.
- **Kolaborasi Tim**: Mendukung pengembang untuk bekerja bersama pada proyek yang sama tanpa konflik.
- **Penyelesaian Konflik**: Membantu mendeteksi dan menyelesaikan konflik penggabungan kode.
- **Backup dan Recovery**: Setiap repositori Git berfungsi sebagai pencadangan otomatis.
- **Manajemen Fitur**: Dengan fitur branching, memungkinkan pengembangan fitur baru tanpa mengganggu kode utama.
- **Integrasi Layanan Hosting**: Mendukung kolaborasi global melalui platform seperti GitHub atau GitLab.
- **Audit Perubahan**: Commit dengan pesan membantu dokumentasi perubahan kode.
- **Dukungan CI/CD**: Mendukung otomatisasi pengujian dan penerapan setiap perubahan kode.

---

### 4. Mengapa Framework Django Cocok untuk Pembelajaran?
Beberapa alasan mengapa Django sering dijadikan framework untuk belajar pengembangan perangkat lunak adalah:
1. **Mudah Dipahami**: Struktur jelas dan mendukung banyak fitur siap pakai.
2. **Dokumentasi Lengkap**: Memiliki dokumentasi yang sangat baik untuk belajar mandiri.
3. **Pola MVT**: Django menggunakan pola Model-View-Template yang memberikan wawasan tentang arsitektur perangkat lunak.
4. **Skalabilitas**: Django digunakan oleh banyak perusahaan besar, memberikan wawasan tentang proyek berskala besar.

---

### 5. Mengapa Model pada Django Disebut ORM?
Model pada Django disebut sebagai **ORM (Object-Relational Mapping)** karena memungkinkan pengembang berinteraksi dengan database melalui objek-objek Python. ORM membuat pengembangan lebih mudah karena operasi CRUD (Create, Read, Update, Delete) dapat dilakukan menggunakan objek Python tanpa harus menulis query SQL secara manual.