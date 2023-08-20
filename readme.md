# Parallelism dan Multiprocessing di Python

Dua contoh hasil uji coba multiprocessing -- berikut adalah bukti konsep yang saya pelajari dari library `multiprocessing`.

## Hasil

### [Multiprocess_pool.py](./multiprocess_pool.py)

Contoh proses **Pool** dan **mapping** untuk mengkalikan angka dalam list

### [Sequential_numeric.py](./sequential_numeric.py)

Proses menghitung dari 0 hingga 200.000.000 (200 juta) 3 kali berurutan **tanpa parallel processing** berfungsi sebagai patokan

### [Multiprocess_numeric.py](./multiprocess_numeric.py)

Proses menghitung dari 0 hingga 200.000.000 (200 juta) 3 kali proses sekaligus **dengan parallel processing** sebagai bukti dari konsep

## Pengantar

`multiprocessing` adalah package yang mendukung proses menggunakan API yang mirip dengan modul `threading`. `multiprocessing` menawarkan remote dan local, yang secara efektif melebihi _Global Interpreter Lock_ dengan menggunakan subproses daripada thread. Karena itu, modul `multiprocessor` memungkinkan programmer untuk sepenuhnya memanfaatkan beberapa prosesor CPU pada perangkat tertentu. Modul multiproses juga memperkenalkan API yang tidak memiliki analog dalam modul `threading`. Contoh utamanya adalah objek `Pool` yang menawarkan cara mudah untuk paralel eksekusi function di beberapa nilai input, mendistribusikan data input di seluruh proses (data parallelism).

## Python Multiprocessing

Salah satu cara untuk mengimplementasikan sistem parallelism adalah menggunakan module `multiprocessing`. Modul `multiprocessing` memungkinkan kita untuk membuat banyak proses, salah satunya adalah dengan interpreter itu sendiri. Python juga memiliki library built-in `threading`, module `multiprocessing` membuat proses baru, sedangkan `threading` membuat threads baru.
![gambar](https://uploads.sitepoint.com/wp-content/uploads/2022/07/1658988061serial_parallel_diagram.jpg)

### Pool Class

Salah satu contoh class dari `multiprocessing` adalah **Pool**. **Pool** class  dapat digunakan untuk melalukan eksekusi function secara paralel. Class `multiprocessing.Pool()` memunculkan sekumpulan proses yang disebut **workers** dan dapat mengirimkan tugas menggunakan metode `apply/apply_async` dan `map/map_async`.

```python
pool = multiprocessing_Pool()
pool = multiprocessing_Pool(processes=4)
```

## Manfaat dari menggunakan Multiprocessing

Berikut beberapa manfaat dari multiprocessing:

- Penggunaan CPU lebih efektif disaat menjalankan program yang memerlukan CPU yang tinggi.
- Lebih banyak kontrol kepada child komponen daripada threads.
- Lebih mudah untuk diprogram.
