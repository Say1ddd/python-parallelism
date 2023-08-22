import time # import library time

def worker(num):
    awal = time.time()
    for _ in range(200000000): # menghitung 0 ke 200000000, untuk benchmark
        pass
    akhir = time.time()
    print(f"Worker {num} selesai, durasi: {akhir-awal} detik \nmenghitung..")
    return akhir-awal

def start():
    print("menghitung 0 sampai 200000000...")
    durasi = sum(worker(i) for i in range(3))
    return durasi

durasi_final = start()
print(f"Total waktu digunakan: {durasi_final} detik") # print durasi proses dari awal hingga selesai
