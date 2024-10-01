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

 ### 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
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
 XML
 ![XML Alfian Tugas 3](/postmanXML.png)

 JSON
 ![JSON Alfian Tugas 3](/postmanJSON.png)

 XML_by_ID
![JSON Alfian Tugas 3](/postmanXML_by_ID.png)

 JSON_by_ID
 ![JSON Alfian Tugas 3](/postmanJSON_by_ID.png)

---

## Tugas 4

---

### 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()

`HttpResponseRedirect()` dan `redirect()` adalah dua cara untuk mengalihkan pengguna ke URL lain dalam Django, tetapi mereka memiliki beberapa perbedaan penting:

#### **HttpResponseRedirect()**
- **Deskripsi**: merupakan cara untuk memberitahu browser agar berpindah ke URL baru, sehingga berguna dalam berbagai skenario pengalihan dalam aplikasi web.
- **Penggunaan**: harus memberikan URL sebagai argumen ke `HttpResponseRedirect()`.
- **Contoh**:
    ```python
    from django.http import HttpResponseRedirect

    def my_view(request):
        ...
        return HttpResponseRedirect('/some-url/')
    ```

#### **redirect()**
- **Deskripsi**: memiliki tujuan sama seperti `HttpResponseRedirect()`, namun fungsi ini dapat menerima berbagai jenis argumen, seperti URL string, nama view, atau objek model, dan secara otomatis menangani pembuatan objek HttpResponseRedirect untuk developer.
- **Penggunaan**: Anda dapat memberikan URL sebagai string, nama view sebagai string, atau objek model. Jika Anda memberikan nama view, Django akan menghasilkan URL secara otomatis menggunakan `reverse()`.
- **Contoh**:
    ```python
    from django.shortcuts import redirect

    def my_view(request):
        ...
        return redirect('some_view_name')  # Nama view yang didefinisikan dalam urls.py
    ```
  
#### Perbedaan Utama
- **Fleksibilitas**: `redirect()` lebih fleksibel karena mendukung pengalihan berdasarkan nama view, sedangkan `HttpResponseRedirect()` hanya menggunakan URL.
- **Kemudahan**: `redirect()` lebih mudah digunakan, terutama saat bekerja dengan nama view dan ingin menghindari hardcoding URL.
---

### 2. Jelaskan cara kerja penghubungan model Product dengan User!
Dalam model `Product`, kita menggunakan `ForeignKey` untuk membuat relasi dengan model `User`. `ForeignKey` ini artinya hubungan *one-to-many*. Dengan begitu, setiap produk bisa memiliki satu pemilik (`User`), tetapi satu user bisa memiliki banyak produk.

Saat kita membuat produk baru, kita mengaitkan produk tersebut dengan pengguna yang sedang login. Jadi, kita menyimpan informasi siapa pemilik produk tersebut di dalam model `Product`.

Ketika pengguna membuat produk, kita mengambil informasi pengguna yang sedang login dan menyimpannya sebagai pemilik produk tersebut. Saat kita ingin menampilkan produk milik pengguna tertentu, kita bisa mengambil semua produk yang terkait dengan pengguna itu.

---

### 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
1. **Authentication (Autentikasi)**:
   - **Pengertian**: Proses memverifikasi identitas pengguna. 
   - **Tujuan**: Untuk memastikan bahwa pengguna adalah siapa yang mereka klaim, misalnya melalui login dengan username dan password.
   - **Contoh**: Saat Anda memasukkan username dan password untuk masuk ke akun, sistem memeriksa apakah informasi itu benar dan cocok dengan data di database.

2. **Authorization (Otorisasi)**:
   - **Pengertian**: Proses menentukan hak akses pengguna. 
   - **Tujuan**: Untuk menentukan apa yang boleh dilakukan oleh pengguna berdasarkan hak akses mereka setelah mereka berhasil diautentikasi.
   - **Contoh**: Setelah Anda login, Anda mungkin bisa melihat halaman profil Anda, tetapi tidak bisa mengakses halaman admin jika Anda bukan admin.

#### Impementasi pada Django

#### 1. **Autentikasi di Django**:
   - Django menyediakan sistem autentikasi bawaan yang sangat mudah digunakan. Sistem ini mengelola proses login, logout, dan pemeriksaan apakah pengguna sudah terautentikasi.
   - Django menggunakan **middleware** untuk memeriksa apakah pengguna telah login di setiap permintaan (request) yang dikirimkan ke server.
   - Ketika pengguna login, Django menyimpan informasi autentikasi dalam sesi pengguna dengan menggunakan cookie yang aman.
   
   - **Contoh login**:
     ```python
     from django.contrib.auth import authenticate, login
     
     def user_login(request):
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(request, username=username, password=password)
         if user is not None:
             login(request, user)  # Pengguna berhasil login
         else:
             # Invalid login
     ```
   
   - **Fungsi utama**:
     - `authenticate()`: Memeriksa apakah username dan password cocok dengan yang ada di database.
     - `login()`: Menyimpan informasi autentikasi dalam sesi, sehingga pengguna dianggap sudah login.
     - `logout()`: Menghapus informasi autentikasi dari sesi, mengeluarkan pengguna.

#### 2. **Otorisasi di Django**:
   - Setelah pengguna berhasil login, Django menentukan akses pengguna berdasarkan hak atau **permission** yang mereka miliki.
   - Django menggunakan model **Group** dan **Permission** untuk menentukan hak akses bagi pengguna. Anda dapat membuat berbagai kelompok (misalnya, *Admin*, *Editor*, *User*) dan memberikan hak akses tertentu untuk masing-masing kelompok.
   - Django juga menyediakan **@permission_required** dan **@user_passes_test** decorator untuk melindungi view atau URL tertentu agar hanya pengguna dengan hak akses tertentu yang bisa mengaksesnya.

   - **Contoh otorisasi berdasarkan peran pengguna**:
     ```python
     from django.contrib.auth.decorators import login_required, permission_required

     @login_required
     @permission_required('app_name.can_view_data', raise_exception=True)
     def view_data(request):
         # Logika untuk pengguna dengan izin
         return render(request, 'data.html')
     ```

   - **Fungsi utama**:
     - `@login_required`: Memastikan bahwa hanya pengguna yang telah login dapat mengakses view tertentu.
     - `@permission_required`: Memeriksa apakah pengguna memiliki izin tertentu sebelum mengakses view. Jika tidak, akan muncul error atau bisa diarahkan ke halaman khusus.

### Ringkasan:
- **Authentication**: Proses memverifikasi siapa pengguna (misalnya, melalui login).
- **Authorization**: Proses menentukan apa yang boleh dilakukan oleh pengguna setelah login.
- **Di Django**, autentikasi dilakukan menggunakan sistem bawaan melalui login/logout, dan otorisasi dilakukan dengan peran atau izin menggunakan permission dan decorator seperti `@login_required`.
---

### 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
#### Bagaimana Django Mengingat Pengguna yang Telah Login?

Django mengingat pengguna yang telah login menggunakan **cookies** dan **session**.

1. **Cookies**:
   - Ketika pengguna login, Django mengirimkan sebuah **cookie** ke browser pengguna. Cookie ini biasanya berisi **session ID** yang unik.
   - Session ID ini adalah pengenal unik yang disimpan di sisi klien (browser) dan berfungsi sebagai "kunci" untuk mengakses data yang disimpan di server tentang pengguna tersebut.

2. **Session**:
   - Django menggunakan **session** untuk menyimpan informasi tentang pengguna di sisi server. Informasi ini termasuk apakah pengguna telah login dan detail terkait pengguna lainnya.
   - Setiap kali pengguna melakukan permintaan ke server setelah login, session ID yang tersimpan di cookie akan dikirim kembali ke server.
   - Django kemudian mencocokkan session ID ini dengan data di database server untuk mengetahui apakah pengguna tersebut telah login. Jika cocok, Django akan menganggap bahwa pengguna tersebut masih terautentikasi dan mengingat siapa dia.

3. **Proses Kerja Login dan Session**:
   - Setelah pengguna login, Django menggunakan fungsi `login(request, user)` untuk menyimpan pengguna dalam session.
   - Django kemudian mengirimkan cookie ke browser pengguna, yang berisi session ID tersebut.
   - Pada setiap request berikutnya, browser mengirimkan cookie ini kembali ke server. Django membaca session ID dan menggunakan data session yang tersimpan untuk mengenali pengguna.

4. **Contoh Penggunaan Cookies dan Session di Django**:
   - Saat pengguna login, Django membuat sebuah session, seperti berikut:
     ```python
     from django.contrib.auth import login

     def my_view(request):
         # Mengautentikasi pengguna
         user = authenticate(username='myusername', password='mypassword')
         if user is not None:
             # Login dan menyimpan pengguna ke session
             login(request, user)
     ```

#### Kegunaan Lain dari Cookies

Selain digunakan untuk mengingat pengguna yang login, cookies memiliki berbagai kegunaan lain dalam pengembangan web:

1. **Menyimpan Preferensi Pengguna**:
   - Cookies sering digunakan untuk menyimpan preferensi pengguna, seperti bahasa yang dipilih, tema tampilan, atau pengaturan lainnya.
   
2. **Pelacakan dan Analitik**:
   - Cookies juga digunakan oleh banyak situs web untuk melacak aktivitas pengguna dan menganalisis data penggunaan. Contohnya, Google Analytics menggunakan cookies untuk melacak kunjungan pengguna di situs web.

3. **Session Shopping Cart**:
   - Dalam aplikasi e-commerce, cookies bisa digunakan untuk menyimpan informasi tentang produk yang ditambahkan ke keranjang belanja sebelum pengguna login atau tanpa login sama sekali.

4. **Targeted Advertising**:
   - Cookies sering digunakan oleh pengiklan untuk menampilkan iklan yang relevan berdasarkan perilaku pengguna di internet. Cookies ini dikenal sebagai **third-party cookies** karena dibuat oleh layanan pihak ketiga di luar situs yang sedang dikunjungi pengguna.

#### Apakah Semua Cookies Aman Digunakan?

Tidak semua cookies aman secara default, dan ada risiko keamanan yang perlu diperhatikan:

1. **Cookies Aman (Secure Cookies)**:
   - **Cookies yang aman** adalah cookies yang ditandai dengan flag `Secure`. Ini memastikan bahwa cookie hanya dikirim melalui koneksi **HTTPS**, yang terenkripsi, sehingga mencegah pencurian data melalui jaringan yang tidak aman.
   - Django memungkinkan Anda untuk menetapkan cookie sebagai "secure" dengan mengonfigurasi `SESSION_COOKIE_SECURE = True` dalam pengaturan Django.

2. **HttpOnly Cookies**:
   - Cookies dengan flag **HttpOnly** tidak bisa diakses oleh JavaScript di browser. Ini memberikan perlindungan terhadap serangan **Cross-Site Scripting (XSS)**, di mana penyerang mencoba mencuri cookie pengguna.
   - Django memungkinkan Anda menetapkan flag ini dengan mengonfigurasi `SESSION_COOKIE_HTTPONLY = True`.

3. **Third-Party Cookies**:
   - **Third-party cookies** adalah cookies yang tidak dibuat oleh situs yang sedang dikunjungi, melainkan oleh layanan pihak ketiga (seperti pengiklan atau pelacak). Cookies ini sering digunakan untuk pelacakan iklan atau analitik.
   - Third-party cookies lebih berisiko terhadap privasi pengguna, karena digunakan untuk melacak aktivitas di berbagai situs web.
   
4. **Session Hijacking**:
   - Jika session ID (yang disimpan di dalam cookie) dicuri, penyerang bisa melakukan **session hijacking** (pembajakan sesi) dan berpura-pura menjadi pengguna yang sah. Untuk mencegah hal ini, Django memiliki fitur keamanan seperti penggunaan HTTPS, secure cookies, dan sesi berbatas waktu.

5. **Cross-Site Request Forgery (CSRF)**:
   - Cookies rentan terhadap serangan **CSRF**, di mana penyerang mencoba membuat pengguna melakukan tindakan yang tidak diinginkan di situs web tanpa sepengetahuan mereka.
   - Django menangani ini dengan memberikan token CSRF untuk setiap permintaan POST, yang memverifikasi bahwa permintaan datang dari pengguna yang sah.

### Ringkasan
- Django mengingat pengguna yang telah login dengan menggunakan **cookies** yang menyimpan session ID, dan server menyimpan data session untuk setiap pengguna.
- Cookies memiliki berbagai kegunaan, seperti menyimpan preferensi pengguna, analitik, atau mengelola keranjang belanja.
- **Tidak semua cookies aman** secara default. Cookies harus dilindungi dengan menggunakan fitur keamanan seperti **Secure** dan **HttpOnly**. Selain itu, penting untuk menghindari third-party cookies yang berisiko bagi privasi dan rentan terhadap serangan seperti **session hijacking** atau **CSRF**.
---

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist

#### a. **Fungsi Registrasi, Login, dan Logout**
**Registrasi:** Membuat fitur registrasi dengan memanfaatka form bawaan dari django yaitu `UserCreationForm`. Form ini menyediakan fields seperti **Username, Password1, Password2**, sehingga tidak perlu membuat form dari awal. Lalu jangan lupa buat file html untuk membuat page nya.

**Login dan Logout:** Membuat fitur login dan logut dengan memanfaatkan fungsi bawaan yaitu `authentucate`, `login`, dan `logout`.

Yang perlu di import pada `views.py`:
```python
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
```

#### b. **Membuat Dua Akun Pengguna dengan Dummy Data**
Registrasikan terlebih dahulu akun-akun yang ingin dibuat, lalu login satu-satu dan tambahkan product-product nya.

#### c. **Menghubungkan Model `Product` dengan `User`**
menggunakan `ForeignKey` untuk membuat relasi dengan model `User`. `ForeignKey` ini artinya hubungan *one-to-many*. Dengan begitu, setiap produk bisa memiliki satu pemilik (`User`), tetapi satu user bisa memiliki banyak produk.

#### d. **Menampilkan Detail Pengguna yang Login dan Menggunakan Cookies**
**Menampilkan Username:** Setelah pengguna login, tampilkan informasi pengguna yang sedang login (seperti username) di halaman utama. Anda bisa mengakses objek pengguna dari `request.user` untuk menampilkan detailnya.

**Menampilkan Last Login:** Simpan informasi waktu login terakhir pengguna menggunakan cookies atau session. Saat pengguna berhasil login, simpan waktu login terakhir ke dalam session atau cookies dan tampilkan informasi ini di halaman utama.

---

## Tugas 5

---

