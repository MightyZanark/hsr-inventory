# HSR Game Inventory

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

5. Setelah itu, saya membuat direktori `template` dalam direktori app `main` tersebut dan menambahkan file bernama [main.html](/main/templates/main.html) yang nantinya berguna untuk menunjukkan nama aplikasi, nama saya, kelas saya, dan juga barang-barang yang sedang ada di inventori saya.

6. Setelah selesai mengkonfigurasi `main.html`, saya membuat function `show_main` di dalam file [views.py](/main/views.py) yang terdapat di direktori `main` guna menampilkan file `main.html` dengan context yang diperlukannya. 

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

9. Selanjutnya, saya mulai membuat model bernama `Item` dalam file [models.py](/main/models.py) yang berada di direktori `main`. Model `Item` tersebut memiliki atribut berupa `name`, `amount`, `description`, dan `category`. `name` berupa sebuah `CharField` dengan panjang maksimal 50 karakter, `amount` berupa sebuah `IntegerField`, `description` berupa sebuah `TextField`, dan `category` berupa sebuah `CharField` yang memiliki 3 opsi pilihan. Selesai membuat model tersebut, saya menjalankan perintah `python manage.py makemigrations && python manage.py migrate` agar database juga ikut terupdate.

10. 
