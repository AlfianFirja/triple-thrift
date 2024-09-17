## Tugas 2
## Alfian Bassam Firjatulah / 2306212695 / A

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

---

## Tugas 3

### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery penting dalam pengimplementasian platform karena hal tersebut dapat memastikan ketersediaan dan kecepatan akses ke data bagi para *user* atau sistem yang memerlukannya. Dengan delivery, platform dapat memberikan respons yang cepat, menjaga konsistensi informasi, dan memungkinkan interoperabilitas antarkomponen sistem. Hal ini juga mendukung keamanan dengan memastikan data dikirimkan secara aman dan terenkripsi.

Selain itu, data delivery juga memungkinkan platform untuk menyesuaikan skala dengan pertumbuhan pengguna dan volume data, serta mendukung pemrosesan data secara *real-time*. Hal ini tentunya akan membantu meningkatkan efisiensi operasional platform, mengoptimalkan kinerja, dan menjaga pengalaman pengguna yang baik.

---

 ### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Berikut adalah keuntungan dan kerugian dari keduannya:
**XML (eXtensible Markup Language)**
Keuntungan:
1. Struktur yang fleksibel
2. Mendukung banyak tipe data
3. Dapat diparsing dengan mudah
4. Terdapat skema untuk memvalidasi struktur data
Kerugian:
1. Ukuran file yang lebih besar
2. Kinerja lebih lambat karena strukturnya yangkompleks
3. Verbosity dalam skala besar
**JSON (JavaScript Object Notation)**
Keuntungan:
1. Ringkas dan lebih cepat
2. Mendukung struktur data seperti objek, array, dan nilai primitif
3. Integrasi dengan JavaScript
Kerugian:
1. Tidak ada skema formal untuk memvalidasi struktur data
2. Kurang fleksibel dengan data yang  kompleks
3. Tidak mendukung komen

JSON lebih populerdaripada XML karena lebih sederhana, cepat, dan efisien, serta lebih mudan diintegrasikan dengan aplikasi web modern yang banyak meggunakan JavaScript. JSON juga cocok untuk API modern dan transfer data dalam aplikasi berbasis jaringan, yang menjadikannya pilihan default dalam banyak kasus

 ### 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method `is_Valid()` padaform Django berfungsi untuk memvalidasi data yang diinput oleh user. Method ini akan mengembalikan nilai `True` jika data yang diinput user valid dan `False` jika data tidak valid. Hal ini memungkinkan developers untuk memastikan ke-valid-an data yang diinput user sebelum disimpan ke database.

Method `is_valid` diperlukan untuk memvalidasi form secara otomatis tanpa harus menulis kode validasi manual, hal ini juga berguna untuk keamanan aplikasi karena Django akan membantu melindungi aplikasi dari input tak valid atau berbahaya, dan juga dapat membantu mengelola error dengan mudah.

 ### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Kita membutuhkan `csrf_token` untuk melindungi aplikasi kita dari CSRF (Cross-Site Request Forgery). CSRF adalah jenis serangan di mana seorang penyerang menggunakan data pengguna yang telah diautentifikasi untuk menjalankan aksi yang tidak diinginkan, seperti mengubah data atau melakukan transaksi tanpa sepengetahuan pengguna.

Jika kita tidak menggunakan `csrf_token` tentunya web kita tidak terlindungi dari serangan CSRF dan memungkinkan terjadinya kebocoran dan perubahan data tanpa sepengetahuan pengguna.

Penyerang dapat memanfaatkan ketiadaan `csrf_token` ini untuk mengirim permintaan bahaya, seperti memasukkan link penipuan, dan penyerang juga bisa menggunakan sesi aktif pengguna untuk melakukan operasi berbahaya tanpa harus mengetahui kredensial login pengguna.

 ### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
 1. Membuat file `base.html` yang berisikan template dasar yang dapat digunakan untuk kerangka dari halaman web lainnya dalam proyek. (jangan lupa sesuaikan direktori acuan pada `settings.py`)
 2. Ubah primary key dari integer menjadi UUID untuk menerapkan *best practice* dari sisi keamanan aplikasi.
 tambahkan:
 ```python
 import uuid
 ```
 ```python
 ...
 id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
 ...
 ```
 Setelahnya jangan lupa lakukan migrasi. (Lakukan migrasi setiap ada perubahan pada `models.py`)
 3. Membuat `forms.py` untuk membuat struktur form yang dapat menerima input dari user.
 4. Pada `views.py` buat fungsi baru dengan nama `create_product_entry` untuk menerima parameter `request` dan menyimpannya pada database
 5. update `show_main` pada `views.py` agar dapat menampilakn seluruh data pada database dengan potongan kode berikut:
 ```python
 def show_main(request):
    mood_entries = MoodEntry.objects.all()
    ...
 ```
 6. Tambahkan path url ke dalam variabel `urlpatterns` pada `urls.py` agar dapat mengakses fungsi yang telah di-import.
 7. Buat berkas html baru untuk membuat tampilan page untuk menambahkan data (menerima input) dan menambahkan `csrf_token` sebagai security seperti yang telah dijelaskan tadi.
 8. Buka `views.py` dan tambahkan fungsi `show_xml`, `show_json`, `show_xml_by_id`, `show_json_by_id` yang berfungsi untuk menampilkan data dengan format XML dan JSON
 9. Jangan lupa tambahin path URL tiap fungsi pada nomer 8

 ### 6. Screenshot Postman

 ![XML Alfian Tugas 3](/postmanXML.png)

 ![JSON Alfian Tugas 3](/postmanJSON.png)