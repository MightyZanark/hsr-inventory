# HSR Game Inventory
- [Tugas 2](#tugas-2)
- [Tugas 3](#tugas-3)
- [Tugas 4](#tugas-4)
- [Tugas 5](#tugas-5)


## Tugas 2

> Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).

1. Pertama saya membuat sebuah virtual environment dengan `python -m venv env` dan menyalakannya. Kemudian, saya membuat file `requirements.txt` yang isinya *dependencies* sebagai berikut dan menginstallnya dengan perintah `pip install -r requirements.txt`.
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```

2. Selanjutnya, saya membuat proyek Django baru dengan nama `game_inventory` melalui perintah `django-admin startproject game_inventory .`, menginisialisasi direktori root sebagai git repository dengan perintah `git init`, dan menambahkan file `.gitignore` yang sesuai dengan yang diberikan pada tutorial.

3. Setelah itu, saya mengedit file `settings.py`, pada variable `ALLOWED_HOST` dan menambahkan `"*"` sebagai elemen di dalam array tersebut.

4. Kemudian, saya membuat app baru bernama `main` melalui perintah `python manage.py startapp main` dan menambahkan aplikasi tersebut ke `settings.py` yang terdapat dalam direktori `game_inventory`, dalam variable yang bernama `INSTALLED_APPS`.

5. Setelah itu, saya membuat direktori `template` dalam direktori app `main` tersebut dan menambahkan file bernama [`main.html`](/main/templates/main.html) yang nantinya berguna untuk menunjukkan nama aplikasi, nama saya, kelas saya, dan juga barang-barang yang sedang ada di inventori saya.

6. Setelah selesai mengkonfigurasi `main.html`, saya membuat function `show_main` di dalam file [`views.py`](/main/views.py) yang terdapat di direktori `main` guna menampilkan file `main.html` dengan context yang diperlukannya. 

7. Agar `main.html` benar tampil saat saya mengakses halaman webnya, saya membuat file `urls.py` di direktori main dan menambahkan potongan *code* berikut.
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main')
]
```
Hal yang serupa saya tambahkan pada file `urls.py` pada direktori `game_inventory`.
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'))
]
```
Saya mengkonfigurasi agar `main.html` dapat tampil ketika page diakses secara langsung, tanpa harus menuju ke *path* tertentu.

8. Setelah itu, saya mencoba menjalankan dan berhasil terlihat `main.html` dengan context yang saya tambahkan pada `views.py`.

![Screnshot yang menunjukkan main.html dengan context saat dijalankan di local](/ss_main_html_with_context.png)

9. Selanjutnya, saya mulai membuat model bernama `Item` dalam file [`models.py`](/main/models.py) yang berada di direktori `main`. Model `Item` tersebut memiliki atribut berupa `name`, `amount`, `description`, dan `category`. `name` berupa sebuah `CharField` dengan panjang maksimal 50 karakter, `amount` berupa sebuah `IntegerField`, `description` berupa sebuah `TextField`, dan `category` berupa sebuah `CharField` yang memiliki 3 opsi pilihan. Selesai membuat model tersebut, saya menjalankan perintah `python manage.py makemigrations && python manage.py migrate` agar database juga ikut terupdate.

10. Setelah selesai membuat model, saya lanjutkan dengan membuat unit testing dalam file [`tests.py`](/main/tests.py) yang mengetes apakah model yang saya telah buat tersebut sudah sesuai yang saya inginkan atau belum. Test pertama, `test_item_have_all_attribute` mengecek apakah atribut yang saya deklarasikan dalam model benar-benar ada dan test ke-2, `test_item_default_category` mengecek apakah jika atribut `category` tidak diberikan saat pembuatan objek, apakah *default value*nya sesuai dengan apa yang telah saya berikan di file `model.py`. Saya juga melakukan `pip install coverage` dan menambahkannya di `requirements.txt`, mengikuti apa yang terdapat dalam ppt agar bisa melihat data hasil melakukan test dengan perintah `python manage.py test`.

11. Terakhir, saya melakukan *deployment* ke [Adaptable](https://adaptable.io) mengikuti langkah-langkah yang telah diberikan pada tutorial, dengan konfigurasi versi Python 3.10 dan `Start Command` dengan perintah `python manage.py migrate && gunicorn game_inventory.wsgi`. *Deployment* dapat dilihat di link [berikut](https://zanark-hsr-inventory.adaptable.app/).

---
> Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.

![Gambar bagan basic HTTP Request hingga HTTP Response](/basic-django.png)

(Gambar diambil dari [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page))

Pada bagan di atas, dapat dilihat bahwa *HTTP Request* yang berasal dari *client* akan pertama dikirim ke file `urls.py` untuk melihat *request* tersebut ingin meminta hal apa. Misalnya jika *HTTP Request* dari *client* ingin pergi ke lokasi `/` atau *root*, file `urls.py` akan melihat *function* apa yang akan dipanggil untuk menerima *request* tersebut sehingga diproses dan mengembalikan *response*. Dalam kasus aplikasi saya, ketika terdapat sebuah *request* ke `/`, maka *function* yang akan dipanggil adalah `show_main`. *Function* yang akan memproses *request* berada di dalam file `views.py`. Dalam *function* tersebut, bisa saja memerlukan data dari `models.py` atau data di *request* ingin kita simpan ke *database* melalui `models.py`. *HTTP Response* yang akan dihasilkan dari *function* yang dipanggil tersebut secara umum akan menggunakan suatu *template* HTML, yang terdapat dalam direktori `templates`. *Template* HTML tersebut pada dasarnya merupakan file HTML biasa, namun melalui Django, kita bisa menggunakan sintaks spesial untuk memasukkan data ke HTML secara dinamis. Contoh penggunaannya dapat dilihat pada file [`main.html`](/main/templates/main.html). Proses pemasukan data ke file HTML dilakukan pada *function* yang dipanggil di `views.py` dan setelah melalui proses tersebut, file HTML tersebut akan dikirimkan kembali kepada *client* yang di awal me*request* halaman tersebut.

---
> Jelaskan mengapa kita menggunakan ***virtual environment***? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan ***virtual environment***?

Kita menggunakan *virtual environment* agar kita dapat mengisolasi *dependencies* yang dibutuhkan untuk aplikasi Django kita dengan *dependencies* lainnya. Kita mengisolasi *dependencies* tersebut karena ada kemungkinan ketika *dependencies* tersebut memiliki versi terbaru dan kita memperbaharui *dependencies* tersebut ke versi terbarunya, akan terjadi konflik atau ada fitur-fitur yang tidak berfungsi seperti yang kita harapkan.

Kita bisa saja membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment* karena pada dasarnya *dependencies* yang dibutuhkan bisa saja kita install secara global di laptop/komputer kita. Namun, akan lebih baik jika kita menggunakan *virtual environment* agar tidak mengganggu *environment* lain yang mungkin kita miliki.

---
> Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

- `MVC` merupakan singkatan dari `Model-View-Controller`. 
    * `Model` merupakan bagian yang mengatur data dan berinteraksi dengan *database*. 
    
    * `View` merupakan bagian yang mengontrol presentasi dari data tersebut, bagaimana data tersebut akan ditampilkan. 
    
    * `Controller` merupakan bagian yang memanipulasi data dengan `Model` dan kemudian meneruskannya ke `View` untuk diproses menjadi tampilan akhir yang akan ditampilkan ke layar pengguna.

- `MVT` merupakan singkatan dari `Model-View-Template`. 
    * `Model` merupakan bagian yang mengontrol akses data dan memberikan data sesuai yang diminta oleh `View`. 
    
    * `View` merupakan bagian yang mengontrol bagaimana data akan ditampilkan ke layar pengguna.
    
    * `Template` merupakan bagian yang mengontrol tampilan dasar aplikasi, yang nantinya akan diisi oleh data-data dari `View`.

- `MVVM` merupakan singkatan dari `Model-View-ViewModel`.
    * `Model` merupakan bagian yang mengatur data dan logika aplikasi.
    
    * `View` merupakan bagian yang mengontrol bagaimana tampilan yang akan pengguna lihat di layar, namun tidak mengolah data yang diterimanya, hanya meletakkan data ke tempat yang telah didefinisikan.
    
    * `ViewModel` merupakan bagian yang menjembatani `Model` dan `View` dan memberikan data yang akan ditampilkan ke pengguna ke `View`.

- Perbedaan antara `MVC`, `MVT`, dan `MVVM`:
    1. `View` pada `MVC` mengontrol secara keseluruhan bagaimana data akan dipresentasikan kepada pengguna, sedangkan pada `MVT`, `Template` merupakan bagian yang bertanggung jawab melakukan tugas tersebut, dan pada `MVVM`, `View` hanya meletakkan data yang diterimanya ke tempat-tempat yang telah dibuatnya, tidak terjadi proses pengolahan data.

    2. `Controller` pada `MVC` mengontrol semua proses manipulasi data dengan `Model` dan meneruskannya ke `View`, sedangkan pada `MVT`, `View` merupakan bagian yang memiliki tugas paling mirip dengan `Controller` namun `View` memproses *HTTP Request* dan mengembalikan *HTTP Response*, dan pada `MVVM`, bagian `ViewModel` merupakan bagian yang mirip dengan `Controller`, hanya saja `ViewModel` lebih berperan sebagai jembatan antara `View` dan `Model` di `MVVM`, tidak mengontrol proses-proses.

---
Ref:
- [Django Project MVT Structure](https://www.geeksforgeeks.org/django-project-mvt-structure/) from `GeeksForGeeks`
- [MVC Framework Introduction](https://www.geeksforgeeks.org/mvc-framework-introduction/) from `GeeksForGeeks`
- [Model-View-ViewModel (MVVM)](https://learn.microsoft.com/en-us/dotnet/architecture/maui/mvvm) from `Miscrosoft`
- [What Is MVVM Architecture?](https://builtin.com/software-engineering-perspectives/mvvm-architecture) from `builtin`
- [MVVM (Model View ViewModel) Architecture Pattern in Android](https://www.geeksforgeeks.org/mvvm-model-view-viewmodel-architecture-pattern-in-android/) from `GeeksForGeeks`
- [Difference between MVC and MVT design patterns](https://www.geeksforgeeks.org/difference-between-mvc-and-mvt-design-patterns/) from `GeeksForGeeks`
- [Model-view-viewmodel](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel) from `Wikipedia`
---

## Tugas 3

> Apa perbedaan antara form `POST` dan form `GET` dalam Django?

Perbedaannya adalah `POST` menggabungkan data dari form dan meng*encode* data tersebut lalu dikirimkan ke server, sedangkan `GET` menggabungkan data dari form menjadi sebuah string dan menggunakannya di dalam URL. `POST` biasanya digunakan untuk *request* yang mengandung data sensitif seperti untuk *login*, atau untuk *request* yang mengubah data di *database*. Di lain sisi, `GET` biasa digunakan untuk *request* seperti pencarian sesuatu di *database*.

---
> Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

Perbedaan utamanya adalah pada XML, data akan dikirim dalam bentuk yang kompleks karena menggunakan struktur *tag* untuk setiap elemen data, sehingga cukup sulit untuk dibentuk dan dikirim. Pada JSON, data yang dikirim berupa sebuah objek JavaScript yang memiliki struktur `key`: `value`, dengan `key` berupa string dan `value` dapat berupa string, array, atau objek lain, sehingga lebih mudah untuk dibentuk dan dikirim. Pada HTML, data yang dikirim bentuknya mirip seperti XML, namun *tag* nya tidak bisa sembarangan dan harus mengikuti ketentuan yang telah ada karena setiap *tag* di HTML memiliki arti semantiknya sendiri, namun karena ketentuan tersebut, pembentukan dan pengiriman data di HTML lebih mudah dibanding XML.

---
> Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

JSON sering digunakan karena struktur JSON jauh lebih simpel dan efisien dibandingkan dengan struktur lain seperti XML. Karena web modern sangat mementingkan efisiensi dan kecepatan respon, tentu saja jika ada cara pertukaran data yang dapat dijalankan dengan cepat dan efisien seperti JSOn, pasti banyak yang ingin menggunakannya. Besarnya data yang mungkin di tukar dalam era web modern ini juga menjadi alasan mengapa JSON sangat sering digunakan, karena JSON tidak memakan terlalu banyak memori jika dibandingkan dengan struktur XML. 

---
> Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).

1. Pertama, saya membuat direktori baru di *root* direktori saya yang bernama `templates`. Di dalam direktori tersebut, saya membuat *file* bernama [`base.html`](/templates/base.html) guna sebagai *template* dasar untuk *file* html lainnya.

2. Setelah itu, saya membuat *file* [`forms.py`](/main/forms.py) sebagai bentuk form dasar untuk model `Item` yang telah saya buat sebelumnya. Isi dari *file* tersebut kurang lebih mirip dengan yang ada di tutorial, hanya berbeda pada atribut `amount` dan atribut tambahan `category`.

3. Selanjutnya saya membuat *template* [`add_item.html`](/main/templates/add_item.html) yang akan digunakan untuk tempat pengisian data `Item` dan merupakan *template* dari *function* `add_item` yang saya tambahkan di `views.py`. *Function* tersebut sama dengan yang ditunjukkan pada tutorial.

4. Selagi saya membuat *function* `add_item` di `views.py`, saya juga mengedit *function* `show_main` agar dapat menampilkan data `Item` yang nantinya dibuat melalui fitur `form` yang telah saya buat sebelumnya. Saya menampilkan `Item` dalam urutan *descending* berdasarkan atribut `amount` dari `Item` tersebut. Saya juga membuat agar terlihat berapa jumlah objek `Item` yang sekarang ada di inventori dan berapa banyak total *slot* inventori yang terpakai.

5. Saya melanjutkan membuat *function* di `views.py` untuk menampilkan data dalam bentuk `XML` dan `JSON`, baik secara menyeluruh maupun secara spesifik berdasarkan `id` yang diminta. Saya kurang lebih hanya mengikuti tutorial untuk bagian ini.

6. Setelah selesai membuat *function-function*, saya lanjutkan dengan melakukan *routing*. Pada bagian ini juga sejujurnya saya hanya mengikuti tutorial dengan perbedaannya hanya terletak pada *route* `add-item`. 

7. Terakhir, saya memodifikasi `main.html` agar dapat menampilkan data-data `Item` dalam bentuk tabel, memberikan info kepada pengguna berapa banyak `Item` yang tersimpan di inventori beserta total *slot* inventori yang terpakai, dan tentunya menambahkan tombol untuk menambahkan data `Item`. Saya juga memodifikasinya agar menggunakan `base.html` yang telah saya buat di awal.

---
> Hasil akses kelima URL di poin 2 menggunakan Postman

HTML Biasa
![Pure HTML](/html.png)

XML
![XML](/xml.png)

XML by ID 1
![XML with query id of 1](/xml_id_1.png)

JSON
![JSON](/json.png)

JSON by ID 2
![JSON with query id of 2](/json_id_2.png)

---

## Tugas 4

> Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?

Django `UserCreationForm` adalah semacam *template* form dari Django yang mampu membuat sebuah objek `User` yang memiliki atribut seperti nama depan, nama belakang, password, email, dan username. Kelebihan dari form ini adalah kita tidak perlu susah-susah membuat form untuk pembuatan objek `User` di aplikasi kita, karena `UserCreationForm` sudah menangani semua itu, dari bentuk form, validasi input, hingga keamanan password. Di lain sisi, kekurangan dari `UserCreationForm` adalah keterbatasan atribut yang bisa dimiliki oleh sebuah objek `User` dan juga keterbatasan bentuk form yang akan tampil di halaman web. 

---
> Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

Autentikasi dalam Django adalah proses validasi apakah pengguna yang ingin masuk ke aplikasi benar-benar pengguna yang dimaksud atau bukan. Sedangkan, otorisasi di Django adalah proses yang menentukan pengguna yang telah terautentikasi tersebut bisa melakukan apa saja di aplikasi ini. Kedua hal tersebut penting karena di era digital ini, banyak orang yang "menyamar" menjadi orang lain untuk kepentingan yang tidak baik. Dengan adanya proses autentikasi dan otorisasi, jika orang ingin menyamar menjadi orang lain, mereka membutuhkan usaha yang lebih.

---
> Apa itu *cookies* dalam konteks aplikasi web, dan bagaimana Django menggunakan *cookies* untuk mengelola data sesi pengguna?

*Cookies* simpelnya adalah suatu file yang menyimpan data yang dibuat oleh aplikasi web yang kita kunjungi yang kemudian akan disimpan di perangkat yang kita gunakan ketika kita mengunjungi aplikasi web tersebut sehingga jika kita mengunjunginya lagi, kita tidak harus memasukkan data yang sudah kita masukkan sebelumnya. Di Django, *cookies* digunakan untuk mengelola data sesi pengguna dengan cara memberikan pengguna yang telah terautentikasi sebuah cookie yang berisi ID dari sesi pengguna tersebut, yang memiliki waktu aktif tertentu atau selama *browser* terbuka.

---
> Apakah penggunaan *cookies* aman secara *default* dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Penggunaan *cookies* secara *default* belum tentu aman karena *cookies* sendiri hanyalah sebuah file yang tersimpan di perangkat yang kita miliki, sehingga orang yang memiliki akses ke perangkat kita bisa saja mencari dan melihat file *cookies* kita. Oleh karena itu, implementasi *cookies* pada aplikasi web yang kita buat harus di implementasikan dengan baik. Namun, meskipun implementasi *cookies* kita baik, masih ada beberapa cara lain orang dapat mencuri *cookies* kita, misalnya dengan XSS (*Cross Site Scripting*), MitM (*Man in the Middle*), CSRF (*Cross Site Request Forgery*), dan lainnya.

---
> Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).

1. Pertama, saya membuat *file* [`register.html`](/main/templates/register.html) dan [`login.html`](/main/templates/login.html) untuk keperluan registrasi dan login pengguna.

2. Setelah *template* untuk halaman registrasi dan login selesai dibuat, saya lanjutkan dengan membuat *function* di `views.py` yang berguna untuk menampilkan *form* registrasi dan login bernama `register_user` dan `login_user`. Namun tentunya jika ada opsi login, maka seharusnya ada opsi logout juga, oleh karena itu saya juga buat *function* `logout_user`.

3. Pada *function* `register_user`, saya menggunakan *form* bawaan dari Django yang bernama `UserCreationForm` untuk membuat objek pengguna di aplikasi saya. Awalnya saya ingin memodifikasi `UserCreationForm` dengan menambah atribut `pbp_class`, namun karena keterbatasan waktu dan adanya tugas lain, saya belum bisa mengimplementasikannya di tugas ini.

4. Pada *function* `login_user`, pengguna diautentikasi menurut `username` dan `password` yang sebelumnya sudah dimasukkan ketika registrasi. Jika `username` dan `password` sesuai, maka pengguna akan berhasil diautentikasi dan akan memiliki *cookie* `last_login` dengan data waktu ia login terakhir kali, dan kemudian membawa pengguna ke halaman utama aplikasi.

5. Pada *function* `logout_user`, pengguna akan di logout dengan *function* bawaan dari Django lalu *cookie* `last_login` nya akan dihapus.

6. Sebelum saya mencoba membuat user, saya juga memodifikasi *function* `show_main` sehingga hanya orang yang terautentikasi bisa melihat halaman utama. Hal ini saya lakukan dengan menggunakan *decorator* yang sudah dibuat oleh Django bernama `login_required`. Selanjutnya saya juga memodifikasi `main.html` agar memiliki tombol logout, nama yang ditampilkan bersesuaian dengan nama pengguna yang terautentikasi, dan menampilkan *cookie* `last_login` pengguna.

7. Setelah itu semua selesai, saya menjalankan server lalu membuat akun yang bernama `Maxwell` dan `user2`. Namun karena data dari tugas sebelumnya masih ada dan tidak memiliki *owner*, kedua akun tersebut akan memperlihatkan data yang sama. Oleh karena itu, saya menghubungkan model `Item` dengan `User` sehingga setiap `Item` hanya dimiliki oleh 1 `User`. Saya melakukan hal tersebut dengan menambahkan atribut `user` di `models.py` pada class `Item` yang merupakan sebuah `ForeignKey` ke model `User` yang merupakan bawaan dari Django. Setelah melakukan perubahan ini, saya membuat migrasi dan membuat data yang sudah ada sebelumnya milik `User` dengan id `1`, yaitu `User` yang pertama kali saya buat.

8. Setelah selesai melakukan migrasi, saya langsung mencoba menjalankan server kembali untuk melihat apakah sudah sesuai atau belum. Ketika saya login dengan akun yang memiliki id `1` (akun dengan nama `Maxwell`), saya melihat data yang ditampilkan sesuai. Namun, ketika saya login dengan akun `user2`, saya melihat bahwa data yang seharusnya menjadi milik `Maxwell` sekarang masih ditampilkan. Saya membuang waktu yang relatif banyak disini dengan melakukan `git restore`, menghapus `db.sqlite3`, dan melakukan migrasi ulang dari tugas sebelumnya hingga tugas ini karena saya pikir saya melewati sebuah step. Ternyata, setelah membaca `views.py` lagi, saya lupa untuk mengubah objek `Item` yang diambil menjadi objek `Item` yang dimiliki oleh `user` yang sedang mengakses halamannya. Saya ubah itu, dan setelah dicoba kembali, hasilnya seperti ekspektasi.

---

## Tugas 5

> Jelaskan manfaat dari setiap *element selector* dan kapan waktu yang tepat untuk menggunakannya.

- *Element Selector*
Manfaat *element selector* adalah memilih semua *element* yang memiliki HTML tag yang sama dan mengubah properti dari semua *element* tersebut. *Selector* ini biasa digunakan ketika kita ingin mengubah properti atau *style* dari sebuah *element* secara menyeluruh di projek kita, tidak hanya satu atau dua.

- *ID Selector*
Manfaat *id selector* adalah memilih suatu *element* yang memiliki *id* yang sesuai pada HTML tagnya seperti yang kita inginkan, sehingga kita bisa dengan spesifik mengubah properti dari *element* yang memiliki *id* tersebut. *Selector* ini biasa digunakan ketika kita hanya ingin mengubah properti atau *style* dari suatu *element* spesifik, yang juga mungkin terdapat di beberapa *file* HTML lain dengan *id* yang sama.

- *Class Selector*
Manfaat *class selector* adalah memilih suatu kelompok *element* yang berada dalam satu *class* yang sama dan mengubah properti atau *style* dari sekelompok *element* itu. *Selector* ini biasa digunakan ketika ada beberapa *element* yang dapat dikelompokkan dalam suatu *class*, sehingga kita dapat mengubah properti atau *style* dari sekelompok *element* tersebut secara bersamaan. *Class selector* juga akan mengubah properti dari *child element* yang terdapat di dalam *parent element* yang memiliki *class* tersebut.

---
> Jelaskan HTML5 Tag yang kamu ketahui.

- *section*
Tag `<section>` merupakan sebuah *semantic* tag yang berfungsi untuk memberi tahu pengguna atau *search engine* bahwa *element-element* yang berada di dalam tag tersebut merepresentasikan sebuah *section* atau bagian tertentu. Misalnya *section* pendahuluan, isi, penutup.

- *footer*
Tag `<footer>` merupakan sebuah *semantic* tag yang menandakan bagian "kaki" dari sebuah halaman web. *Footer* biasa berisi dengan hal seperti *copyright*, *contact information*, *link* untuk kembali ke bagian atas halaman, dan lainnya.

- *header*
Tag `<header>` merupakan sebuah *semantic* tag yang menandakan bagian "kepala" dari sebuah halaman web. *Header* biasa diisi dengan logo atau *icon* dari halaman web tersebut.

- *nav*
Tag `<nav>` merupakan sebuah *semantic* tag yang menandakan bagian navigasi dalam sebuah halaman web. Bagian navigasi tersebut biasa terletak pada bagian paling atas halaman web dan berisi *link-link* yang menuju halaman lain di aplikasi web tersebut.

---
> Jelaskan perbedaan antara *margin* dan *padding*.

Perbedaan antara *margin* dan *padding* adalah *margin* merupakan area kosong dan transparan yang terletak di sekitar sebuah *element* sehingga terdapat jarak antara *element* yang satu dengan *element* yang lain. Sedangkan, *padding* adalah area kosong yang terletak di antara sebuah *element* dengan konten *element* tersebut dan akan mengikuti warna *background* dari konten tersebut. Konten disini dapat berupa teks, gambar, ataupun hal lain yang dapat diletakkan dalam sebuah *element*.

---
> Jelaskan perbedaan antara *framework* CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

Perbedaan *framework* CSS Tailwind dan Bootstrap:
- Tailwind memiliki tingkat pembelajaran yang lebih sulit dibanding Bootstrap karena banyaknya *utility class* yang telah disediakan.
- Tailwind akan memiliki ukuran *file* CSS yang lebih kecil di akhir dibanding Bootstrap karena Tailwind hanya perlu me*load* *utility class*, sedangkan Bootstrap harus me*load* berbagai macam komponen yang telah didefinisikan juga.
- Tailwind memberikan kemampuan *customization* yang lebih luas dibanding Bootstrap, sedangkan Bootstrap memberikan *template* yang bisa digunakan langsung.

Menurut saya, kita sebaiknya menggunakan Bootstrap ketika kita tidak terlalu mementingkan *customization* pada aplikasi web kita, dan juga ketika ukuran *file* aplikasi web kita bukan merupakan masalah. Sebaliknya, menurut saya kita menggunakan Tailwind ketika kita ingin melakukan *customization* pada aplikasi web kita secara lebih detil dan sesuai dengan selera kita, bukan hanya sekedar "terlihat bagus", dan juga ketika kita memiliki keterbatasan ukuran *file* untuk aplikasi web kita.

---
> Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).

1. Pertama, saya menambahkan link *CDN* Bootstrap ke `base.html` sehingga semua *file* HTML lain saya langsung dapat menggunakan *class-class* yang disediakan oleh Bootstrap.

2. Setelah itu, saya melakukan *customization* pada halaman `login` terlebih dahulu karena halaman tersebut adalah halaman pertama yang dikunjungi pengguna. Saya membuat judul `Login` berada di tengah halaman melalui *class* `text-center` dan mengikuti tutorial pada dokumentasi Bootstrap untuk membuat input `Username`, `Password`, dan tombol `Submit` terlihat lebih menarik. Saya juga membuat ketika `Username` atau `Password` yang dimasukkan salah, kalimat yang muncul akan berada di dalam kotak berwarna merah. Selain itu, jika pengguna baru saja berhasil melakukan registrasi, kalimat berhasil tersebut akan terletak dalam sebuah kotak berwarna hijau.

3. Selanjutnya, saya memodifikasi halaman `register`. Saya melakukan hal yang sama untuk judul `Register`, yaitu menaruhnya di tengah halaman, lalu membuat tabel input `Username`, `Password`, dan `Password confirmation` lebih rapi. Untuk tombol `Register` saya juga sesuai kan dengan panjang kotak input.

4. Setelah halaman `login` dan `register`, saya melanjutkan ke halaman `inventory`. Disini saya melakukan hal yang sama untuk judul `HSR Game Inventory`, yaitu meletakkannya di tengah halaman web. Setelah itu, saya juga merapikan tabel untuk *item inventory* dengan memberikan *class* `table` dan `table-striped` pada tabel tersebut. Setelah itu saya mengubah semua tombol agar memiliki warna merah/biru sesuai dengan apa yang dilakukan tombol tersebut. Selain itu, saya juga membuat *item* terakhir pada tabel pasti memiliki warna *background* hitam dan tulisan kuning emas.

5. Halaman terkahir yang saya ubah adalah halaman `add-item`. Kurang lebih yang saya lakukan pada halaman tersebut sama seperti yang saya lakukan terhadap halaman `register`, hanya sekedar merapikan tabel input dan menambahkan warna pada tombol `Add Item`.

---
