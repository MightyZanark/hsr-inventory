# HSR Game Inventory
### *Deployment* bisa dilihat di [sini](https://zanark-hsr-inventory.adaptable.app/).

> Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

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
